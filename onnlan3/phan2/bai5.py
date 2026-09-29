class Employee:
    def __init__(self):
        self.__employee_id=""
        self.__full_name=""
        self.__department=""
        self.__base_salary=0
        self.__working_hours=0

    def get_employee_id(self):
        return self.__employee_id

    def get_department(self):
        return self.__department

    def set_base_salary(self, base_salary):
        if base_salary>=0:
            self.__base_salary=base_salary
        else:
            print("Luong co ban phai lon hon bang 0")

    def bonus(self):
        if self.__working_hours>160:
            return (self.__working_hours-160)*100000
        return 0

    def income(self):
        return self.__base_salary+self.bonus()

    def inputInfo(self):
        self.__employee_id=input("Hay nhap ma nhan vien: ")
        self.__full_name=input("Hay nhap ten nhan vien: ")
        self.__department=input("Hay nhap phong ban: ")
        self.__base_salary=float(input("Hay nhap luong co ban: "))
        self.__working_hours=float(input("Hay nhap so gio lam: "))

    def display(self):
        print(f"Ma nv: {self.__employee_id}, Ten nv: {self.__full_name}, Phong ban: {self.__department}, Luong co ban: {self.__base_salary}, Gio lam: {self.__working_hours}, Thu nhap: {self.income()}")


class EmployeeManager:
    def __init__(self):
        self.employees=[]

    def add_employee(self, emp):
        for e in self.employees:
            if e.get_employee_id()==emp.get_employee_id():
                print("Ma nhan vien da ton tai khong the them")
                return False
        self.employees.append(emp)
        print("Them nhan vien thanh cong")
        return True

    def find_employee(self, emp_id):
        for e in self.employees:
            if e.get_employee_id()==emp_id:
                return e
        print("Khong tim thay nhan vien")
        return None

    def update_salary(self, emp_id, new_salary):
        emp=self.find_employee(emp_id)
        if emp:
            emp.set_base_salary(new_salary)
            print("Cap nhat luong thanh cong")

    def delete_employee(self, emp_id):
        emp=self.find_employee(emp_id)
        if emp:
            self.employees.remove(emp)
            print("Xoa nhan vien thanh cong")

    def sort_by_income(self):
        self.employees.sort(key=lambda e: e.income(), reverse=True)
        print("Da sap xep nhan vien giam dan theo thu nhap")

    def department_statistics(self):
        stats={}
        for e in self.employees:
            pb=e.get_department()
            stats[pb]=stats.get(pb, 0)+1
        for pb, count in stats.items():
            print(f"Phong ban: {pb}, So luong: {count}")

    def display_all(self):
        for e in self.employees:
            e.display()

def main():
    ql=EmployeeManager()
    
    nv1=Employee()
    nv1.inputInfo()
    ql.add_employee(nv1)

    nv2=Employee()
    nv2.inputInfo()
    ql.add_employee(nv2)

    ql.display_all()

    ma_tim=input("Hay nhap ma nv can tim: ")
    tim=ql.find_employee(ma_tim)
    if tim:
        tim.display()

    ma_sua=input("Hay nhap ma nv can sua luong: ")
    luong_moi=float(input("Hay nhap luong moi: "))
    ql.update_salary(ma_sua, luong_moi)

    ma_xoa=input("Hay nhap ma nv can xoa: ")
    ql.delete_employee(ma_xoa)

    ql.sort_by_income()
    ql.display_all()

    ql.department_statistics()

if __name__=="__main__":
    main()
