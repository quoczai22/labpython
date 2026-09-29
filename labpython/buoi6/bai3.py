class SinhVien:
    def __init__(self, ma_sv="", ho_ten="", diem_tb=0.0):
        self.ma_sv=ma_sv
        self.ho_ten=ho_ten
        self.diem_tb=diem_tb

    def nhap(self):
        self.ma_sv=input("Hay nhap ma sinh vien: ")
        self.ho_ten=input("Hay nhap ho ten sinh vien: ")
        while True:
            try:
                dtb=float(input("Hay nhap diem trung binh (0 - 10): "))
                if 0<=dtb<=10:
                    self.diem_tb=dtb
                    break
                print("Diem trung binh phai trong khoang 0 den 10!")
            except ValueError:
                print("Diem phai la so hop le!")

    def xep_loai(self):
        if self.diem_tb>=8.0:
            return "Gioi"
        elif self.diem_tb>=6.5:
            return "Kha"
        elif self.diem_tb>=5.0:
            return "Trung binh"
        return "Yeu"

    def kiem_tra_dat(self):
        return self.diem_tb>=5.0

    def hien_thi(self):
        trang_thai="Dat" if self.kiem_tra_dat() else "Khong dat"
        print(f"Ma SV: {self.ma_sv}, Ho ten: {self.ho_ten}, DTB: {self.diem_tb:.2f}, "
              f"Xep loai: {self.xep_loai()}, Ket qua: {trang_thai}")


class SinhVienCNTT(SinhVien):
    def __init__(self, ma_sv="", ho_ten="", diem_tb=0.0, diem_lap_trinh=0.0):
        super().__init__(ma_sv, ho_ten, diem_tb)
        self.diem_lap_trinh=diem_lap_trinh

    def nhap(self):
        super().nhap()
        while True:
            try:
                dlt=float(input("Hay nhap diem lap trinh (0 - 10): "))
                if 0<=dlt<=10:
                    self.diem_lap_trinh=dlt
                    break
                print("Diem lap trinh phai trong khoang 0 den 10!")
            except ValueError:
                print("Diem phai la so hop le!")

    def kiem_tra_chuyen_nganh(self):
        return self.diem_lap_trinh>=8.0

    def xep_loai(self):
        if self.diem_tb>=8.0 and self.diem_lap_trinh>=8.0:
            return "Gioi chuyen nganh"
        return super().xep_loai()

    def hien_thi(self):
        trang_thai="Dat" if self.kiem_tra_dat() else "Khong dat"
        print(f"[SV CNTT] Ma SV: {self.ma_sv}, Ho ten: {self.ho_ten}, DTB: {self.diem_tb:.2f}, "
              f"Diem lap trinh: {self.diem_lap_trinh:.2f}, Xep loai: {self.xep_loai()}, Ket qua: {trang_thai}")


class SinhVienNgonNgu(SinhVien):
    def __init__(self, ma_sv="", ho_ten="", diem_tb=0.0, diem_ngoai_ngu=0.0):
        super().__init__(ma_sv, ho_ten, diem_tb)
        self.diem_ngoai_ngu=diem_ngoai_ngu

    def nhap(self):
        super().nhap()
        while True:
            try:
                dnn=float(input("Hay nhap diem ngoai ngu (0 - 10): "))
                if 0<=dnn<=10:
                    self.diem_ngoai_ngu=dnn
                    break
                print("Diem ngoai ngu phai trong khoang 0 den 10!")
            except ValueError:
                print("Diem phai la so hop le!")

    def xep_loai(self):
        if self.diem_tb>=8.0 and self.diem_ngoai_ngu>=8.0:
            return "Gioi chuyen nganh"
        return super().xep_loai()

    def hien_thi(self):
        trang_thai="Dat" if self.kiem_tra_dat() else "Khong dat"
        print(f"[SV Ngon Ngu] Ma SV: {self.ma_sv}, Ho ten: {self.ho_ten}, DTB: {self.diem_tb:.2f}, "
              f"Diem ngoai ngu: {self.diem_ngoai_ngu:.2f}, Xep loai: {self.xep_loai()}, Ket qua: {trang_thai}")


def main():
    # Tao it nhat 4 sinh vien thuoc 2 chuyen nganh khac nhau
    ds_sv=[
        SinhVienCNTT("IT01", "Tran Quoc Kien", 8.5, 9.0),
        SinhVienCNTT("IT02", "Le Hoang Nam", 8.2, 7.5),
        SinhVienCNTT("IT03", "Nguyen Van Hai", 4.5, 4.0),
        SinhVienNgonNgu("NN01", "Pham My Linh", 8.8, 8.5),
        SinhVienNgonNgu("NN02", "Vo Thi Huong", 7.0, 8.0),
        SinhVienNgonNgu("NN03", "Hoang Van Dat", 4.0, 5.0)
    ]

    print("================ DANH SACH SINH VIEN ================")
    for sv in ds_sv:
        sv.hien_thi()

    # Dem so sinh vien dat va khong dat
    so_dat=sum(1 for sv in ds_sv if sv.kiem_tra_dat())
    so_khong_dat=len(ds_sv)-so_dat
    print(f"\n=> So sinh vien Dat: {so_dat}")
    print(f"=> So sinh vien Khong dat: {so_khong_dat}")

    # Tim sinh vien co diem trung binh cao nhat
    sv_max_dtb=max(ds_sv, key=lambda sv: sv.diem_tb)
    print(f"\n=> Sinh vien co DTB cao nhat: {sv_max_dtb.ho_ten} ({sv_max_dtb.ma_sv}) voi DTB: {sv_max_dtb.diem_tb:.2f}")

    # Minh hoa tinh da hinh thong qua phuong thuc xep_loai()
    print("\n--- MINH HOA TINH DA HINH QUA xep_loai() ---")
    for sv in ds_sv:
        print(f"{sv.ho_ten:<18} ({type(sv).__name__:<15}) -> DTB: {sv.diem_tb:.2f} | Xep loai: {sv.xep_loai()}")


if __name__=="__main__":
    main()
