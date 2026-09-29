class Student:
    def __init__(self, student_id="", name="", gpa=0.0):
        self.student_id=student_id
        self.name=name
        self.gpa=gpa

    def display(self):
        print(f"[{self.student_id}] {self.name:<20} | GPA: {self.gpa:.2f}")


class Course:
    def __init__(self, course_code="", course_name="", max_students=30, min_gpa=5.0):
        self.course_code=course_code
        self.course_name=course_name
        self.max_students=max_students
        self.min_gpa=min_gpa
        self.registered_students=[] # danh sach doi tuong Student

    def is_full(self):
        return len(self.registered_students)>=self.max_students

    def display_class_list(self):
        print(f"\n--- DANH SACH LOP HOC PHAN: [{self.course_code}] {self.course_name} ---")
        print(f"Si so hien tai: {len(self.registered_students)}/{self.max_students} | GPA yeu cau toi thieu: {self.min_gpa:.1f}")
        if not self.registered_students:
            print("Chua co sinh vien nao dang ky.")
        else:
            for idx, sv in enumerate(self.registered_students, 1):
                print(f"  {idx}. [{sv.student_id}] {sv.name} - GPA: {sv.gpa:.2f}")


class CourseRegistration:
    def __init__(self):
        self.courses=[]

    def add_course(self, course):
        self.courses.append(course)

    def register_course(self, student, course):
        if course.is_full():
            print(f"Dang ky that bai: Hoc phan {course.course_name} da day si so!")
            return False
        if student.gpa<course.min_gpa:
            print(f"Dang ky that bai: Sinh vien {student.name} co GPA {student.gpa:.2f} khong dat yeu cau dau vao (>= {course.min_gpa:.1f}) cua mon {course.course_name}!")
            return False
        for sv in course.registered_students:
            if sv.student_id==student.student_id:
                print(f"Sinh vien {student.name} da dang ky mon nay roi!")
                return False
        course.registered_students.append(student)
        print(f"Dang ky thanh cong: {student.name} -> Hoc phan {course.course_name}.")
        return True


def main():
    reg=CourseRegistration()
    c1=Course("CS101", "Lap trinh Python", max_students=2, min_gpa=5.0)
    c2=Course("AI201", "Hoc May Nang Cao", max_students=30, min_gpa=7.5)
    reg.add_course(c1)
    reg.add_course(c2)

    sv1=Student("SV01", "Nguyen Van An", 8.2)
    sv2=Student("SV02", "Tran Thi Binh", 7.0)
    sv3=Student("SV03", "Le Hoang Cuong", 4.5)
    sv4=Student("SV04", "Pham Thi Dung", 8.5)

    print("--- THUC HIEN DANG KY HOC PHAN ---")
    reg.register_course(sv1, c1)
    reg.register_course(sv2, c1)
    reg.register_course(sv4, c1) # Thu dang ky khi lop CS101 da day

    reg.register_course(sv2, c2) # Thu dang ky mon AI201 (GPA 7.0 < 7.5)
    reg.register_course(sv1, c2) # Dat GPA (8.2 >= 7.5)

    c1.display_class_list()
    c2.display_class_list()


if __name__=="__main__":
    main()
