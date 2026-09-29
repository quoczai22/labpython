class Employee:
    def __init__(self, employee_id="", name="", position="Nhan vien", salary_coefficient=1.0, base_salary=2000000.0):
        self.employee_id=employee_id
        self.name=name
        self.position=position
        self.salary_coefficient=salary_coefficient
        self.base_salary=base_salary

    def calculate_income(self):
        return self.salary_coefficient*self.base_salary

    def display(self):
        print(f"[{self.employee_id}] {self.name} - Chuc vu: {self.position}, "
              f"He so: {self.salary_coefficient:.2f}, Thu nhap: {self.calculate_income():,.0f} VND")


class Manager(Employee):
    def __init__(self, employee_id="", name="", position="Truong phong", salary_coefficient=1.5, base_salary=2000000.0, allowance=3000000.0):
        super().__init__(employee_id, name, position, salary_coefficient, base_salary)
        self.allowance=allowance
        self.sub_employees=[] # danh sach nhan vien cap duoi truc thuoc

    def add_sub_employee(self, emp):
        if emp not in self.sub_employees:
            self.sub_employees.append(emp)
            return True
        return False

    def calculate_income(self):
        # Thu nhap = He so luong * Luong co so + Phu cap trach nhiem
        return super().calculate_income()+self.allowance

    def display(self):
        print(f"[Quan ly - {self.employee_id}] {self.name} - Chuc vu: {self.position}, "
              f"He so: {self.salary_coefficient:.2f}, Phu cap: {self.allowance:,.0f} VND, Thu nhap: {self.calculate_income():,.0f} VND")
        if self.sub_employees:
            print(f"  * Danh sach {len(self.sub_employees)} nhan vien truc thuoc:")
            for sub in self.sub_employees:
                print(f"    - [{sub.employee_id}] {sub.name} ({sub.position})")


class CompanyManager:
    def __init__(self):
        self.members=[]

    def add_member(self, member):
        for m in self.members:
            if m.employee_id==member.employee_id:
                print(f"Ma nhan vien {member.employee_id} da ton tai!")
                return False
        self.members.append(member)
        return True

    def get_total_payroll(self):
        return sum(m.calculate_income() for m in self.members)

    def display_organization_tree(self):
        print("="*60)
        print(f"{'SO DO TO CHUC PHAN CAP DOANH NGHIEP':^60}")
        print("="*60)
        
        # Danh sach nhan vien da duoc gan cho quan ly
        assigned_subs=set()
        managers=[m for m in self.members if isinstance(m, Manager)]
        
        for mgr in managers:
            print(f"\n[+] QUAN LY: {mgr.name} ({mgr.position}) - Ma: {mgr.employee_id}")
            print(f"    He so: {mgr.salary_coefficient:.2f} | Phu cap: {mgr.allowance:,.0f} VND | Thu nhap: {mgr.calculate_income():,.0f} VND")
            if mgr.sub_employees:
                print("    |-- Cac nhan vien truc thuoc:")
                for sub in mgr.sub_employees:
                    assigned_subs.add(sub.employee_id)
                    print(f"        |--> [{sub.employee_id}] {sub.name:<18} | Chuc vu: {sub.position:<12} | Thu nhap: {sub.calculate_income():>10,.0f} VND")
            else:
                print("    |-- (Chua co nhan vien cap duoi truc thuoc)")

        # Cac nhan vien doc lap (chua gan cho quan ly nao)
        independent_emps=[m for m in self.members if not isinstance(m, Manager) and m.employee_id not in assigned_subs]
        if independent_emps:
            print(f"\n[+] NHAN SU KHAC (Doc lap / Ban giam doc):")
            for emp in independent_emps:
                print(f"    |--> [{emp.employee_id}] {emp.name:<18} | Chuc vu: {emp.position:<12} | Thu nhap: {emp.calculate_income():>10,.0f} VND")

        print("="*60)
        print(f"TONG QUY LUONG CONG TY: {self.get_total_payroll():>34,.0f} VND")
        print("="*60)


def main():
    cong_ty=CompanyManager()

    # Khoi tao cac nhan vien
    nv1=Employee("NV01", "Nguyen Van An", "Lap trinh vien", 2.5)
    nv2=Employee("NV02", "Tran Thi Binh", "Tester", 2.0)
    nv3=Employee("NV03", "Le Hoang Cuong", "DevOps", 2.8)
    nv4=Employee("NV04", "Pham Thi Dung", "Designer", 2.2)

    # Khoi tao quan ly phong ban
    tp_kt=Manager("TP01", "Vu Hoang Giang", "Truong phong Ky thuat", 3.5, 2000000, 5000000)
    tp_kt.add_sub_employee(nv1)
    tp_kt.add_sub_employee(nv2)
    tp_kt.add_sub_employee(nv3)

    tp_tk=Manager("TP02", "Hoang Mai Lan", "Truong phong Thiet ke", 3.0, 2000000, 4000000)
    tp_tk.add_sub_employee(nv4)

    # Them vao he thong cong ty
    cong_ty.add_member(tp_kt)
    cong_ty.add_member(nv1)
    cong_ty.add_member(nv2)
    cong_ty.add_member(nv3)
    cong_ty.add_member(tp_tk)
    cong_ty.add_member(nv4)

    # Hien thi so do to chuc va tong quy luong
    cong_ty.display_organization_tree()


if __name__=="__main__":
    main()
