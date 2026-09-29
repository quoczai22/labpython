class Employee:
    def __init__(self, employee_id="", full_name="", base_salary=0, working_days=0):
        self.employee_id=employee_id
        self.full_name=full_name
        self.base_salary=base_salary
        self.working_days=working_days
        
    def inputInfo(self):
        self.employee_id=input("Hay nhap ma nhan vien: ")
        self.full_name=input("Hay nhap ten nhan vien: ") 
        self.base_salary=float(input("Hay nhap luong nhan vien: "))
        self.working_days=int(input("Hay nhap so ngay lam cong: "))
        
    def display(self):
        print(f"Ma nhan vien la: {self.employee_id}, Ten nhan vien la: {self.full_name}, Luong co ban la: {self.base_salary}, So ngay lam la: {self.working_days}, Luong thuc nhan la: {self.calculate_salary()}")
        
    def calculate_salary(self):
        luong_thuc_nhan=self.base_salary*self.working_days/26
        return luong_thuc_nhan

NhanVien = Employee
    
def main():
    nv1=Employee()
    nv1.inputInfo()
    nv1.display()
    
if __name__=="__main__":
    main()