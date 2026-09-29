class Student:
    def __init__(self):
        self.student_id=""
        self.full_name=""
        self.age=0
        self.gpa=0
        
    def inputInfo(self):
        self.student_id=input("Hay nhap ma sinh vien: ")
        if not self.student_id:
            print("Ma sinh vien khong duoc de trong")
            return False
        
        self.full_name=input("Hay nhap ten sinh vien: ") 
        if not self.full_name:
            print("Ten sinh vien khong duoc de trong")
            return False
        
        self.age=int(input("Hay nhap tuoi cua sinh vien: "))
        if self.age<18:
            print("Phai nhap tuoi lon hon 18")
            return False
        
        self.gpa=float(input("Hay nhap gpa cua sinh vien nay: "))
        if not (0 <= self.gpa <= 10):
            print("Diem trung binh phai tu 0 den 10")
            return False
        return True
        
    def display(self):
        print(f"Ma sinh vien la: {self.student_id}, Ten sinh vien la: {self.full_name}, Tuoi la: {self.age}, Gpa la: {self.gpa}")
        self.is_scholarship()
        
    def is_scholarship(self):
        if self.gpa>=8.0:
            print("Du dieu kien nhan hoc bong")
        else:
            print("Khong du dieu kien nhan hoc bong")

def main():
    sv1=Student()
    if sv1.inputInfo():
        sv1.display()

if __name__=="__main__":
    main()
            
        
    