from datetime import datetime

class NguoiLaoDong:
    def __init__(self, ma_ns="", ho_ten="", nam_sinh=0, luong_co_ban=0.0):
        self.ma_ns=ma_ns
        self.ho_ten=ho_ten
        self.nam_sinh=nam_sinh
        self.luong_co_ban=luong_co_ban

    def nhap(self):
        self.ma_ns=input("Hay nhap ma nhan su: ")
        self.ho_ten=input("Hay nhap ho ten: ")
        nam_hien_tai=datetime.now().year
        while True:
            try:
                ns=int(input(f"Hay nhap nam sinh (1900 - {nam_hien_tai}): "))
                if 1900<=ns<=nam_hien_tai:
                    self.nam_sinh=ns
                    break
                print("Nam sinh khong hop le!")
            except ValueError:
                print("Nam sinh phai la so nguyen!")

        while True:
            try:
                lcb=float(input("Hay nhap luong co ban: "))
                if lcb>=0:
                    self.luong_co_ban=lcb
                    break
                print("Luong co ban phai lon hon hoac bang 0!")
            except ValueError:
                print("Luong co ban phai la so hop le!")

    def tinh_tuoi(self):
        return datetime.now().year-self.nam_sinh

    def tinh_thu_nhap(self):
        return self.luong_co_ban

    def tinh_thue(self):
        tn=self.tinh_thu_nhap()
        if tn>=15000000:
            return tn*0.05
        return 0.0

    def tinh_thuc_lanh(self):
        return self.tinh_thu_nhap()-self.tinh_thue()

    def hien_thi(self):
        print(f"Ma NS: {self.ma_ns}, Ho ten: {self.ho_ten}, Tuoi: {self.tinh_tuoi()}, "
              f"Thu nhap: {self.tinh_thu_nhap():,.0f} VND, Thue: {self.tinh_thue():,.0f} VND, "
              f"Thuc lanh: {self.tinh_thuc_lanh():,.0f} VND")


class GiaoVien(NguoiLaoDong):
    def __init__(self, ma_ns="", ho_ten="", nam_sinh=0, luong_co_ban=0.0, so_tiet_day=0):
        super().__init__(ma_ns, ho_ten, nam_sinh, luong_co_ban)
        self.so_tiet_day=so_tiet_day

    def nhap(self):
        super().nhap()
        while True:
            try:
                tiet=int(input("Hay nhap so tiet day: "))
                if tiet>=0:
                    self.so_tiet_day=tiet
                    break
                print("So tiet day phai lon hon hoac bang 0!")
            except ValueError:
                print("So tiet day phai la so nguyen!")

    def tinh_tien_day(self):
        return self.so_tiet_day*100000

    def tinh_thu_nhap(self):
        return self.luong_co_ban+self.tinh_tien_day()

    def hien_thi(self):
        print(f"[Giao Vien] Ma NS: {self.ma_ns}, Ho ten: {self.ho_ten}, Tuoi: {self.tinh_tuoi()}, "
              f"Luong CB: {self.luong_co_ban:,.0f}, So tiet: {self.so_tiet_day}, Tien day: {self.tinh_tien_day():,.0f}, "
              f"Thu nhap: {self.tinh_thu_nhap():,.0f}, Thue: {self.tinh_thue():,.0f}, Thuc lanh: {self.tinh_thuc_lanh():,.0f}")


class NhanVienHanhChinh(NguoiLaoDong):
    def __init__(self, ma_ns="", ho_ten="", nam_sinh=0, luong_co_ban=0.0, so_ngay_cong=0):
        super().__init__(ma_ns, ho_ten, nam_sinh, luong_co_ban)
        self.so_ngay_cong=so_ngay_cong

    def nhap(self):
        super().nhap()
        while True:
            try:
                cong=int(input("Hay nhap so ngay cong: "))
                if cong>=0:
                    self.so_ngay_cong=cong
                    break
                print("So ngay cong phai lon hon hoac bang 0!")
            except ValueError:
                print("So ngay cong phai la so nguyen!")

    def tinh_tien_cong(self):
        return self.so_ngay_cong*150000

    def tinh_thu_nhap(self):
        return self.luong_co_ban+self.tinh_tien_cong()

    def hien_thi(self):
        print(f"[NV Hanh Chinh] Ma NS: {self.ma_ns}, Ho ten: {self.ho_ten}, Tuoi: {self.tinh_tuoi()}, "
              f"Luong CB: {self.luong_co_ban:,.0f}, So ngay cong: {self.so_ngay_cong}, Tien cong: {self.tinh_tien_cong():,.0f}, "
              f"Thu nhap: {self.tinh_thu_nhap():,.0f}, Thue: {self.tinh_thue():,.0f}, Thuc lanh: {self.tinh_thuc_lanh():,.0f}")


def main():
    # Tao danh sach gom ca giao vien va nhan vien hanh chinh
    ds_ns=[
        GiaoVien("GV01", "Tran Minh Tuan", 1985, 9000000, 70),
        GiaoVien("GV02", "Nguyen Thi Hanh", 1990, 8500000, 50),
        GiaoVien("GV03", "Vu Hoang Giang", 1982, 10000000, 85),
        NhanVienHanhChinh("HC01", "Pham Van Dong", 1993, 6000000, 24),
        NhanVienHanhChinh("HC02", "Le Thi Bich", 1996, 5500000, 26)
    ]

    print("================ DANH SACH NHAN SU TRUONG HOC ================")
    for ns in ds_ns:
        ns.hien_thi()

    # Tinh tong so tien nha truong phai chi tra
    tong_chi_tra=sum(ns.tinh_thu_nhap() for ns in ds_ns)
    tong_thuc_lanh=sum(ns.tinh_thuc_lanh() for ns in ds_ns)
    print(f"\n=> Tong thu nhap nha truong chi tra: {tong_chi_tra:,.0f} VND")
    print(f"=> Tong thuc lanh chuyen cho nhan su: {tong_thuc_lanh:,.0f} VND")

    # Tim nguoi co thu nhap cao nhat
    ns_max_tn=max(ds_ns, key=lambda ns: ns.tinh_thu_nhap())
    print(f"=> Nguoi co thu nhap cao nhat: {ns_max_tn.ho_ten} ({ns_max_tn.ma_ns}) voi thu nhap: {ns_max_tn.tinh_thu_nhap():,.0f} VND")

    # Dem so giao vien va so nhan vien hanh chinh
    so_gv=sum(1 for ns in ds_ns if isinstance(ns, GiaoVien))
    so_hc=sum(1 for ns in ds_ns if isinstance(ns, NhanVienHanhChinh))
    print(f"=> So luong giao vien: {so_gv}")
    print(f"=> So luong nhan vien hanh chinh: {so_hc}")

    # Minh hoa tinh da hinh
    print("\n--- MINH HOA TINH DA HINH QUA tinh_thu_nhap() ---")
    for ns in ds_ns:
        print(f"{ns.ma_ns:<6} | {ns.ho_ten:<18} | {type(ns).__name__:<18} | Thu nhap: {ns.tinh_thu_nhap():>12,.0f} VND")


if __name__=="__main__":
    main()
