class Student:
    def __init__(self):
        self.student_id=""
        self.name=""
        self.gpa=0

    def inputInfo(self):
        self.student_id=input("Hay nhap ma sinh vien: ")
        self.name=input("Hay nhap ho ten sinh vien: ")
        self.gpa=float(input("Hay nhap gpa cua sinh vien: "))

    def compare_gpa(self, other_student):
        if self.gpa>other_student.gpa:
            print(f"Sinh vien {self.name} co gpa cao hon {other_student.name}")
        elif self.gpa<other_student.gpa:
            print(f"Sinh vien {other_student.name} co gpa cao hon {self.name}")
        else:
            print(f"Hai sinh vien co gpa bang nhau")

    def __eq__(self, other):
        return (self.student_id==other.student_id and self.name==other.name and self.gpa==other.gpa)

    def display(self):
        print(f"Ma sinh vien: {self.student_id}, Ten: {self.name}, GPA: {self.gpa}")

def main():
    s1=Student()
    s1.inputInfo()
    s1.display()

    s2=Student()
    s2.inputInfo()
    s2.display()

    s1.compare_gpa(s2)

    print("student1 is student2: ", s1 is s2)
    print("student1 == student2: ", s1 == s2)

if __name__=="__main__":
    main()
