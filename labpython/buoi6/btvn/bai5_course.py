class KhoaHoc:
    def __init__(self, ma_khoa_hoc="", ten_khoa_hoc="", so_hoc_vien=0, hoc_phi=0.0):
        self.ma_khoa_hoc=ma_khoa_hoc
        self.ten_khoa_hoc=ten_khoa_hoc
        self.so_hoc_vien=so_hoc_vien
        self.hoc_phi=hoc_phi

    def nhap(self):
        self.ma_khoa_hoc=input("Hay nhap ma khoa hoc: ")
        self.ten_khoa_hoc=input("Hay nhap ten khoa hoc: ")
        while True:
            try:
                shv=int(input("Hay nhap so hoc vien (> 0): "))
                if shv>0:
                    self.so_hoc_vien=shv
                    break
                print("So hoc vien phai lon hon 0!")
            except ValueError:
                print("So hoc vien phai la so nguyen!")

        while True:
            try:
                hp=float(input("Hay nhap hoc phi mot hoc vien: "))
                if hp>=0:
                    self.hoc_phi=hp
                    break
                print("Hoc phi khong duoc am!")
            except ValueError:
                print("Hoc phi phai la so hop le!")

    def tinh_doanh_thu(self):
        return self.so_hoc_vien*self.hoc_phi

    def tinh_chi_phi(self):
        return 0.0

    def tinh_loi_nhuan(self):
        return self.tinh_doanh_thu()-self.tinh_chi_phi()

    def hien_thi(self):
        print(f"Ma KH: {self.ma_khoa_hoc}, Ten KH: {self.ten_khoa_hoc}, Hoc vien: {self.so_hoc_vien}, "
              f"Doanh thu: {self.tinh_doanh_thu():,.0f} VND, Chi phi: {self.tinh_chi_phi():,.0f} VND, "
              f"Loi nhuan: {self.tinh_loi_nhuan():,.0f} VND")


class KhoaHocTrucTiep(KhoaHoc):
    def __init__(self, ma_khoa_hoc="", ten_khoa_hoc="", so_hoc_vien=0, hoc_phi=0.0, so_buoi_hoc=0):
        super().__init__(ma_khoa_hoc, ten_khoa_hoc, so_hoc_vien, hoc_phi)
        self.so_buoi_hoc=so_buoi_hoc

    def nhap(self):
        super().nhap()
        while True:
            try:
                buoi=int(input("Hay nhap so buoi hoc: "))
                if buoi>=0:
                    self.so_buoi_hoc=buoi
                    break
                print("So buoi hoc phai lon hon hoac bang 0!")
            except ValueError:
                print("So buoi hoc phai la so nguyen!")

    def tinh_chi_phi(self):
        # Chi phi = So buoi hoc * 1.500.000
        return self.so_buoi_hoc*1500000

    def hien_thi(self):
        print(f"[Truc Tiep]  Ma: {self.ma_khoa_hoc}, Ten: {self.ten_khoa_hoc}, HV: {self.so_hoc_vien}, "
              f"So buoi: {self.so_buoi_hoc}, Doanh thu: {self.tinh_doanh_thu():,.0f}, "
              f"Chi phi: {self.tinh_chi_phi():,.0f}, Loi nhuan: {self.tinh_loi_nhuan():,.0f} VND")


class KhoaHocTrucTuyen(KhoaHoc):
    def __init__(self, ma_khoa_hoc="", ten_khoa_hoc="", so_hoc_vien=0, hoc_phi=0.0, phi_he_thong=0.0):
        super().__init__(ma_khoa_hoc, ten_khoa_hoc, so_hoc_vien, hoc_phi)
        self.phi_he_thong=phi_he_thong

    def nhap(self):
        super().nhap()
        while True:
            try:
                phi=float(input("Hay nhap phi he thong: "))
                if phi>=0:
                    self.phi_he_thong=phi
                    break
                print("Phi he thong phai lon hon hoac bang 0!")
            except ValueError:
                print("Phi he thong phai la so hop le!")

    def tinh_chi_phi(self):
        # Chi phi = Phi he thong + 5% doanh thu
        return self.phi_he_thong+0.05*self.tinh_doanh_thu()

    def hien_thi(self):
        print(f"[Truc Tuyen] Ma: {self.ma_khoa_hoc}, Ten: {self.ten_khoa_hoc}, HV: {self.so_hoc_vien}, "
              f"Phi HT: {self.phi_he_thong:,.0f}, Doanh thu: {self.tinh_doanh_thu():,.0f}, "
              f"Chi phi: {self.tinh_chi_phi():,.0f}, Loi nhuan: {self.tinh_loi_nhuan():,.0f} VND")


class KhoaHocVIP(KhoaHoc):
    def __init__(self, ma_khoa_hoc="", ten_khoa_hoc="", so_hoc_vien=0, hoc_phi=0.0, so_buoi_hoc=0, chi_phi_ho_tro=0.0):
        super().__init__(ma_khoa_hoc, ten_khoa_hoc, so_hoc_vien, hoc_phi)
        self.so_buoi_hoc=so_buoi_hoc
        self.chi_phi_ho_tro=chi_phi_ho_tro

    def nhap(self):
        super().nhap()
        while True:
            try:
                buoi=int(input("Hay nhap so buoi hoc: "))
                if buoi>=0:
                    self.so_buoi_hoc=buoi
                    break
                print("So buoi hoc phai lon hon hoac bang 0!")
            except ValueError:
                print("So buoi hoc phai la so nguyen!")

        while True:
            try:
                cp=float(input("Hay nhap chi phi ho tro: "))
                if cp>=0:
                    self.chi_phi_ho_tro=cp
                    break
                print("Chi phi ho tro phai lon hon hoac bang 0!")
            except ValueError:
                print("Chi phi ho tro phai la so hop le!")

    def tinh_chi_phi(self):
        # Chi phi = So buoi hoc * 2.000.000 + Chi phi ho tro
        return self.so_buoi_hoc*2000000+self.chi_phi_ho_tro

    def hien_thi(self):
        print(f"[VIP]        Ma: {self.ma_khoa_hoc}, Ten: {self.ten_khoa_hoc}, HV: {self.so_hoc_vien}, "
              f"So buoi: {self.so_buoi_hoc}, CP ho tro: {self.chi_phi_ho_tro:,.0f}, "
              f"Doanh thu: {self.tinh_doanh_thu():,.0f}, Chi phi: {self.tinh_chi_phi():,.0f}, "
              f"Loi nhuan: {self.tinh_loi_nhuan():,.0f} VND")


def main():
    # Tao it nhat 5 khoa hoc thuoc nhieu loai khac nhau
    ds_kh=[
        KhoaHocTrucTiep("KH01", "Python Co ban", 25, 2000000, 12),
        KhoaHocTrucTiep("KH02", "Lap trinh Web Django", 18, 3500000, 16),
        KhoaHocTrucTuyen("KH03", "Data Science voi Python", 40, 1500000, 5000000),
        KhoaHocTrucTuyen("KH04", "Machine Learning Foundation", 30, 2500000, 6000000),
        KhoaHocVIP("KH05", "1-on-1 AI Masterclass", 5, 12000000, 10, 5000000)
    ]

    print("================ DANH SACH KHOA HOC ================")
    for kh in ds_kh:
        kh.hien_thi()

    # Tinh tong doanh thu cua trung tam
    tong_dt=sum(kh.tinh_doanh_thu() for kh in ds_kh)
    print(f"\n=> Tong doanh thu cua trung tam: {tong_dt:,.0f} VND")

    # Tim khoa hoc co loi nhuan cao nhat
    kh_max_ln=max(ds_kh, key=lambda kh: kh.tinh_loi_nhuan())
    print(f"=> Khoa hoc co loi nhuan cao nhat: {kh_max_ln.ten_khoa_hoc} ({kh_max_ln.ma_khoa_hoc}) voi loi nhuan: {kh_max_ln.tinh_loi_nhuan():,.0f} VND")

    # Liet ke cac khoa hoc co loi nhuan lon hon 10.000.000 dong
    print("\n--- DANH SACH KHOA HOC CO LOI NHUAN > 10.000.000 VND ---")
    kh_tren_10m=[kh for kh in ds_kh if kh.tinh_loi_nhuan()>10000000]
    for kh in kh_tren_10m:
        print(f"- {kh.ten_khoa_hoc} ({kh.ma_khoa_hoc}): Loi nhuan = {kh.tinh_loi_nhuan():,.0f} VND")

    # Minh hoa tinh da hinh thong qua phuong thuc tinh_chi_phi()
    print("\n--- MINH HOA TINH DA HINH QUA tinh_chi_phi() ---")
    for kh in ds_kh:
        print(f"{kh.ma_khoa_hoc:<6} | {kh.ten_khoa_hoc:<30} | {type(kh).__name__:<18} | Chi phi: {kh.tinh_chi_phi():>12,.0f} VND")


if __name__=="__main__":
    main()
