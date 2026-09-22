class Course:
    def __init__(self):
        self.course_id=""
        self.course_name=""
        self.max_students=0
        self.students=[]

    def input(self):
        self.course_id=input("Hay nhap ma khoa hoc: ")
        self.course_name=input("Hay nhap ten khoa hoc: ")
        self.max_students=int(input("Hay nhap so luong hoc vien toi da: "))

    def is_full(self):
        return len(self.students)>=self.max_students

    def register_student(self, student_name):
        if self.is_full():
            print("Khoa hoc da day hoc vien")
            return False
        if student_name in self.students:
            print("Hoc vien da dang ky roi")
            return False
        self.students.append(student_name)
        print("Dang ky hoc vien thanh cong")
        return True

    def cancel_registration(self, student_name):
        if student_name in self.students:
            self.students.remove(student_name)
            print("Huy dang ky thanh cong")
            return True
        print("Khong tim thay hoc vien trong danh sach")
        return False

    def display(self):
        print(f"Ma: {self.course_id}, Ten khoa: {self.course_name}, Si so: {len(self.students)}/{self.max_students}, Danh sach: {self.students}")


class CourseManager:
    def __init__(self):
        self.courses=[]

    def add_course(self, course):
        for c in self.courses:
            if c.course_id==course.course_id:
                print("Ma khoa hoc da ton tai")
                return False
        self.courses.append(course)
        print("Them khoa hoc thanh cong")
        return True

    def find_course(self, course_id):
        for c in self.courses:
            if c.course_id==course_id:
                return c
        print("Khong tim thay khoa hoc")
        return None

    def register_student(self, course_id, student_name):
        c=self.find_course(course_id)
        if c:
            c.register_student(student_name)

    def cancel_registration(self, course_id, student_name):
        c=self.find_course(course_id)
        if c:
            c.cancel_registration(student_name)

    def statistics(self):
        print("Thong ke so luong hoc vien tung khoa:")
        for c in self.courses:
            c.display()

def main():
    manager=CourseManager()

    n=int(input("Hay nhap so luong khoa hoc can tao: "))
    for i in range(n):
        c=Course()
        c.input()
        manager.add_course(c)

    ma_kh=input("Hay nhap ma khoa hoc can dang ky: ")
    ten_hv=input("Hay nhap ten hoc vien can dang ky: ")
    manager.register_student(ma_kh, ten_hv)

    manager.statistics()

    ma_huy=input("Hay nhap ma khoa hoc can huy dang ky: ")
    ten_huy=input("Hay nhap ten hoc vien can huy: ")
    manager.cancel_registration(ma_huy, ten_huy)

    manager.statistics()

if __name__=="__main__":
    main()
