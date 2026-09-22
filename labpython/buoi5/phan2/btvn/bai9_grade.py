class SubjectResult:
    def __init__(self):
        self.subject_id=""
        self.subject_name=""
        self.attendance=0
        self.midterm=0
        self.final=0

    def input(self):
        self.subject_id=input("Hay nhap ma mon hoc: ")
        self.subject_name=input("Hay nhap ten mon hoc: ")
        self.attendance=float(input("Hay nhap diem chuyen can: "))
        self.midterm=float(input("Hay nhap diem giua ky: "))
        self.final=float(input("Hay nhap diem cuoi ky: "))

    def calc_final_score(self):
        return self.attendance*0.1 + self.midterm*0.3 + self.final*0.6

    def is_passed(self):
        return self.calc_final_score()>=4.0

    def display(self):
        kq="Dat" if self.is_passed() else "Khong dat"
        print(f"Ma mon: {self.subject_id}, Ten: {self.subject_name}, Chuyen can: {self.attendance}, Giua ky: {self.midterm}, Cuoi ky: {self.final}, Tong ket: {round(self.calc_final_score(), 2)}, Ket qua: {kq}")


class GradeManager:
    def __init__(self):
        self.results=[]

    def add_result(self, res):
        for r in self.results:
            if r.subject_id==res.subject_id:
                print("Mon hoc da ton tai")
                return False
        self.results.append(res)
        print("Them diem mon hoc thanh cong")
        return True

    def display_results(self):
        for r in self.results:
            r.display()

    def average_score(self):
        if not self.results:
            return 0
        return sum(r.calc_final_score() for r in self.results)/len(self.results)

    def failed_subjects(self):
        print("Danh sach mon khong dat:")
        for r in self.results:
            if not r.is_passed():
                r.display()

    def sort_by_score(self):
        self.results.sort(key=lambda r: r.calc_final_score(), reverse=True)
        print("Da sap xep cac mon theo diem tong ket giam dan")

def main():
    gm=GradeManager()

    n=int(input("Hay nhap so luong mon hoc: "))
    for i in range(n):
        res=SubjectResult()
        res.input()
        gm.add_result(res)

    print("Bang diem tat ca cac mon:")
    gm.display_results()

    print("Diem trung binh cac mon la: ", round(gm.average_score(), 2))

    gm.failed_subjects()

    gm.sort_by_score()
    gm.display_results()

if __name__=="__main__":
    main()
