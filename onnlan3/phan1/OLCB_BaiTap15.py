class StudentGrades:
    def __init__(self, student_id="", name="", math=0.0, literature=0.0, english=0.0):
        self.student_id=student_id
        self.name=name
        self.grades={'Math': math, 'Literature': literature, 'English': english}

    def calculate_average(self):
        # Cong thuc: (Toan x 2 + Van x 2 + Anh x 1) / 5
        return (self.grades['Math']*2 + self.grades['Literature']*2 + self.grades['English']*1) / 5.0

    def display(self):
        dtb=self.calculate_average()
        print(f"[{self.student_id}] {self.name:<20} | Toan: {self.grades['Math']:>4.1f} | Van: {self.grades['Literature']:>4.1f} | Anh: {self.grades['English']:>4.1f} | DTB: {dtb:>5.2f}")


class GradeBook:
    def __init__(self):
        self.students=[]

    def add_student(self, student):
        self.students.append(student)

    def find_top_student(self):
        if not self.students:
            return None
        return max(self.students, key=lambda s: s.calculate_average())

    def display_report_card(self):
        print("\n" + "="*65)
        print(f"{'BANG TONG KET DIEM LOP HOC':^65}")
        print("="*65)
        # Sap xep theo DTB giam dan
        sorted_students=sorted(self.students, key=lambda s: s.calculate_average(), reverse=True)
        for idx, s in enumerate(sorted_students, 1):
            print(f"{idx:<3}. ", end="")
            s.display()
        print("="*65)
        top=self.find_top_student()
        if top:
            print(f"=> THU KHOA LOP: {top.name} ({top.student_id}) voi DTB: {top.calculate_average():.2f}")


def main():
    gb=GradeBook()
    gb.add_student(StudentGrades("HS01", "Tran Quoc Kien", 9.0, 8.5, 9.5))
    gb.add_student(StudentGrades("HS02", "Le Thi Mai", 8.0, 9.0, 8.0))
    gb.add_student(StudentGrades("HS03", "Nguyen Hoang Nam", 7.0, 6.5, 8.5))
    gb.add_student(StudentGrades("HS04", "Pham Minh Tuan", 9.5, 9.0, 9.0))

    gb.display_report_card()


if __name__=="__main__":
    main()
