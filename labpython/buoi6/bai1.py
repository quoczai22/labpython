class NhanVien:
    def __init__(self, ma_nv="", ho_ten="", luong_co_ban=0):
        self.ma_nv=ma_nv
        self.ho_ten=ho_ten
        self.luong_co_ban=luong_co_ban

    def nhap(self):
        self.ma_nv=input("Hay nhap ma nhan vien: ")
        self.ho_ten=input("Hay nhap ho ten nhan vien: ")
        while True:
            try:
                luong=float(input("Hay nhap luong co ban: "))
                if luong>=0:
                    self.luong_co_ban=luong
                    break
                print("Luong co ban phai lon hon hoac bang 0!")
            except ValueError:
                print("Luong co ban phai la so hop le!")

    def tinh_luong(self):
        return self.luong_co_ban

    def tinh_thue(self):
        luong=self.tinh_luong()
        if luong>=15000000:
            return luong*0.05
        return 0

    def tinh_thuc_lanh(self):
        return self.tinh_luong()-self.tinh_thue()

    def hien_thi(self):
        print(f"Ma NV: {self.ma_nv}, Ho ten: {self.ho_ten}, Luong co ban: {self.luong_co_ban:,.0f} VND, "
              f"Luong: {self.tinh_luong():,.0f} VND, Thue: {self.tinh_thue():,.0f} VND, "
              f"Thuc lanh: {self.tinh_thuc_lanh():,.0f} VND")


class NhanVienVanPhong(NhanVien):
    def __init__(self, ma_nv="", ho_ten="", luong_co_ban=0, so_ngay_lam=0):
        super().__init__(ma_nv, ho_ten, luong_co_ban)
        self.so_ngay_lam=so_ngay_lam

    def nhap(self):
        super().nhap()
        while True:
            try:
                ngay=int(input("Hay nhap so ngay lam viec: "))
                if ngay>=0:
                    self.so_ngay_lam=ngay
                    break
                print("So ngay lam viec phai lon hon hoac bang 0!")
            except ValueError:
                print("So ngay lam viec phai la so nguyen hop le!")

    def tinh_luong(self):
        return self.luong_co_ban+self.so_ngay_lam*200000

    def hien_thi(self):
        print(f"[NV Van Phong] Ma NV: {self.ma_nv}, Ho ten: {self.ho_ten}, Luong CB: {self.luong_co_ban:,.0f}, "
              f"So ngay lam: {self.so_ngay_lam}, Luong: {self.tinh_luong():,.0f}, "
              f"Thue: {self.tinh_thue():,.0f}, Thuc lanh: {self.tinh_thuc_lanh():,.0f}")


class NhanVienKinhDoanh(NhanVien):
    def __init__(self, ma_nv="", ho_ten="", luong_co_ban=0, doanh_so=0):
        super().__init__(ma_nv, ho_ten, luong_co_ban)
        self.doanh_so=doanh_so

    def nhap(self):
        super().nhap()
        while True:
            try:
                ds=float(input("Hay nhap doanh so ban hang: "))
                if ds>=0:
                    self.doanh_so=ds
                    break
                print("Doanh so ban hang phai lon hon hoac bang 0!")
            except ValueError:
                print("Doanh so phai la so hop le!")

    def tinh_hoa_hong(self):
        return self.doanh_so*0.05

    def tinh_luong(self):
        return self.luong_co_ban+self.tinh_hoa_hong()

    def hien_thi(self):
        print(f"[NV Kinh Doanh] Ma NV: {self.ma_nv}, Ho ten: {self.ho_ten}, Luong CB: {self.luong_co_ban:,.0f}, "
              f"Doanh so: {self.doanh_so:,.0f}, Hoa hong: {self.tinh_hoa_hong():,.0f}, "
              f"Luong: {self.tinh_luong():,.0f}, Thue: {self.tinh_thue():,.0f}, Thuc lanh: {self.tinh_thuc_lanh():,.0f}")


def main():
    # Tao it nhat 2 nhan vien van phong va 2 nhan vien kinh doanh
    ds_nv=[
        NhanVienVanPhong("VP01", "Nguyen Van An", 6000000, 24),
        NhanVienVanPhong("VP02", "Tran Thi Binh", 7000000, 26),
        NhanVienKinhDoanh("KD01", "Le Van Cuong", 5000000, 150000000),
        NhanVienKinhDoanh("KD02", "Pham Thi Dung", 5500000, 220000000)
    ]

    print("================ DANH SACH NHAN VIEN ================")
    for nv in ds_nv:
        nv.hien_thi()

    # Tinh tong tien luong cong ty phai chi tra
    tong_luong=sum(nv.tinh_luong() for nv in ds_nv)
    print(f"\n=> Tong tien luong cong ty phai chi tra: {tong_luong:,.0f} VND")

    # Tim nhan vien co tien luong cao nhat
    nv_max_luong=max(ds_nv, key=lambda nv: nv.tinh_luong())
    print(f"=> Nhan vien co tien luong cao nhat la: {nv_max_luong.ho_ten} voi muc luong: {nv_max_luong.tinh_luong():,.0f} VND")

    # Minh hoa tinh da hinh
    print("\n--- MINH HOA TINH DA HINH QUA tinh_luong() ---")
    for nv in ds_nv:
        print(f"Nhan vien: {nv.ho_ten} ({type(nv).__name__}) -> Luong: {nv.tinh_luong():,.0f} VND")


if __name__=="__main__":
    main()
