class Student:
    def __init__(self):
        self.student_id=""
        self.name=""
        self.grades={}

    def input(self):
        self.student_id=input("Hay nhap ma sinh vien: ")
        self.name=input("Hay nhap ten sinh vien: ")
        so_mon=int(input("Hay nhap so luong mon hoc: "))
        for i in range(so_mon):
            ten_mon=input("Hay nhap ten mon: ")
            diem=float(input("Hay nhap diem: "))
            self.grades[ten_mon]=diem

    def gpa(self):
        if not self.grades:
            return 0
        return sum(self.grades.values())/len(self.grades)

    def is_scholarship(self):
        return self.gpa()>=8.0 and all(d>=5.0 for d in self.grades.values())

    def display(self):
        hb="Co hoc bong" if self.is_scholarship() else "Khong"
        print(f"Ma SV: {self.student_id}, Ten: {self.name}, Diem: {self.grades}, GPA: {round(self.gpa(), 2)}, Hoc bong: {hb}")


class ClassManager:
    def __init__(self):
        self.students=[]

    def add_student(self, s):
        for sv in self.students:
            if sv.student_id==s.student_id:
                print("Ma sinh vien da ton tai")
                return False
        self.students.append(s)
        print("Them sinh vien thanh cong")
        return True

    def sort_by_gpa(self):
        self.students.sort(key=lambda s: s.gpa(), reverse=True)
        print("Da sap xep sinh vien theo GPA giam dan")

    def scholarship_students(self):
        print("Danh sach sinh vien du dieu kien hoc bong:")
        for s in self.students:
            if s.is_scholarship():
                s.display()

    def display_all(self):
        for s in self.students:
            s.display()

def main():
    cm=ClassManager()

    n=int(input("Hay nhap so luong sinh vien trong lop: "))
    for i in range(n):
        sv=Student()
        sv.input()
        cm.add_student(sv)

    print("Danh sach lop hoc:")
    cm.display_all()

    cm.sort_by_gpa()
    cm.display_all()

    cm.scholarship_students()

if __name__=="__main__":
    main()
