class Student:
    def __init__(self):
        self.ma_sv=""
        self.nganh_hoc=""
        self.khoa=""
        self.nam_nhap_hoc=0
        self.diem_gk=0
        self.diem_ck=0
        self.diem_kt=0

    def input(self):
        while True:
            self.ma_sv=input("Hay nhap ma sinh vien (5 ky tu: 2 chu dau, 3 so sau): ").strip().upper()
            if len(self.ma_sv)==5 and self.ma_sv[:2].isalpha() and self.ma_sv[2:].isdigit():
                break
            print("Ma sinh vien khong hop le, xin moi nhap lai!")

        self.nganh_hoc=input("Hay nhap nganh hoc: ")
        self.khoa=input("Hay nhap khoa hoc: ")
        self.nam_nhap_hoc=int(input("Hay nhap nam nhap hoc: "))
        self.diem_gk=float(input("Hay nhap diem giua ky: "))
        self.diem_ck=float(input("Hay nhap diem cuoi ky: "))
        self.diem_kt=float(input("Hay nhap diem kiem tra: "))

    def average_score(self):
        return (self.diem_gk+self.diem_ck+self.diem_kt)/3

    def academic_rank(self):
        dtb=self.average_score()
        if dtb>=8.0:
            return "Gioi"
        elif dtb>=6.5:
            return "Kha"
        elif dtb>=5.0:
            return "Trung binh"
        else:
            return "Yeu"

    def display(self):
        print(f"Ma SV: {self.ma_sv}, Nganh: {self.nganh_hoc}, Khoa: {self.khoa}, Nam: {self.nam_nhap_hoc}")
        print(f"Diem GK: {self.diem_gk}, Diem CK: {self.diem_ck}, Diem KT: {self.diem_kt}")
        print(f"Diem trung binh: {round(self.average_score(), 2)}, Xep loai: {self.academic_rank()}")

def main():
    sv=Student()
    sv.input()
    sv.display()

if __name__=="__main__":
    main()
