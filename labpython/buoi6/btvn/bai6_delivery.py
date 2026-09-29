class DonHang:
    def __init__(self, ma_don="", ten_khach_hang="", khoang_cach=0.0, khoi_luong=0.0):
        self.ma_don=ma_don
        self.ten_khach_hang=ten_khach_hang
        self.khoang_cach=khoang_cach
        self.khoi_luong=khoi_luong

    def nhap(self):
        self.ma_don=input("Hay nhap ma don hang: ")
        self.ten_khach_hang=input("Hay nhap ten khach hang: ")
        while True:
            try:
                kc=float(input("Hay nhap khoang cach (km > 0): "))
                if kc>0:
                    self.khoang_cach=kc
                    break
                print("Khoang cach phai lon hon 0!")
            except ValueError:
                print("Khoang cach phai la so hop le!")

        while True:
            try:
                kl=float(input("Hay nhap khoi luong (kg > 0): "))
                if kl>0:
                    self.khoi_luong=kl
                    break
                print("Khoi luong phai lon hon 0!")
            except ValueError:
                print("Khoi luong phai la so hop le!")

    def tinh_phi_giao_hang(self):
        return 0.0

    def tinh_phu_phi(self):
        return 0.0

    def tinh_tong_tien(self):
        return self.tinh_phi_giao_hang()+self.tinh_phu_phi()

    def hien_thi(self):
        print(f"Ma don: {self.ma_don}, Khach: {self.ten_khach_hang}, KC: {self.khoang_cach:.1f} km, "
              f"KL: {self.khoi_luong:.1f} kg, Phi GH: {self.tinh_phi_giao_hang():,.0f} VND, "
              f"Phu phi: {self.tinh_phu_phi():,.0f} VND, Tong tien: {self.tinh_tong_tien():,.0f} VND")


class GiaoHangTieuChuan(DonHang):
    def tinh_phi_giao_hang(self):
        # Khoang cach * 5.000 + Khoi luong * 2.000
        return self.khoang_cach*5000+self.khoi_luong*2000

    def tinh_phu_phi(self):
        return 0.0

    def hien_thi(self):
        print(f"[Tieu Chuan] Ma: {self.ma_don}, KH: {self.ten_khach_hang}, KC: {self.khoang_cach:>4.1f} km, "
              f"KL: {self.khoi_luong:>4.1f} kg, Phi: {self.tinh_phi_giao_hang():>9,.0f}, "
              f"Phu phi: {self.tinh_phu_phi():>7,.0f}, Tong: {self.tinh_tong_tien():>10,.0f} VND")


class GiaoHangNhanh(DonHang):
    def tinh_phi_giao_hang(self):
        # Khoang cach * 8.000 + Khoi luong * 3.000
        return self.khoang_cach*8000+self.khoi_luong*3000

    def tinh_phu_phi(self):
        # Phu phi giao nhanh bang 10% phi giao hang
        return self.tinh_phi_giao_hang()*0.10

    def hien_thi(self):
        print(f"[Nhanh]      Ma: {self.ma_don}, KH: {self.ten_khach_hang}, KC: {self.khoang_cach:>4.1f} km, "
              f"KL: {self.khoi_luong:>4.1f} kg, Phi: {self.tinh_phi_giao_hang():>9,.0f}, "
              f"Phu phi: {self.tinh_phu_phi():>7,.0f}, Tong: {self.tinh_tong_tien():>10,.0f} VND")


class GiaoHangHoaToc(DonHang):
    def tinh_phi_giao_hang(self):
        # Khoang cach * 12.000 + Khoi luong * 4.000
        return self.khoang_cach*12000+self.khoi_luong*4000

    def tinh_phu_phi(self):
        # Phu phi hoa toc bang 20% phi giao hang
        return self.tinh_phi_giao_hang()*0.20

    def hien_thi(self):
        print(f"[Hoa Toc]    Ma: {self.ma_don}, KH: {self.ten_khach_hang}, KC: {self.khoang_cach:>4.1f} km, "
              f"KL: {self.khoi_luong:>4.1f} kg, Phi: {self.tinh_phi_giao_hang():>9,.0f}, "
              f"Phu phi: {self.tinh_phu_phi():>7,.0f}, Tong: {self.tinh_tong_tien():>10,.0f} VND")


def main():
    # Tao it nhat 6 don hang thuoc nhieu loai dich vu khac nhau
    ds_dh=[
        GiaoHangTieuChuan("DH01", "Nguyen Van An", 12.0, 5.0),
        GiaoHangTieuChuan("DH02", "Tran Thi Mai", 25.0, 10.0),
        GiaoHangNhanh("DH03", "Le Hoang Nam", 8.5, 3.0),
        GiaoHangNhanh("DH04", "Pham Thi Dung", 30.0, 6.0),
        GiaoHangHoaToc("DH05", "Vo Van Truong", 15.0, 2.5),
        GiaoHangHoaToc("DH06", "Dang My Linh", 22.5, 8.0)
    ]

    print("================ DANH SACH DON HANG GIAO NHAN ================")
    # Duyet danh sach va hien thi
    for dh in ds_dh:
        dh.hien_thi()

    # Tinh tong doanh thu giao hang cua cong ty
    tong_doanh_thu=sum(dh.tinh_tong_tien() for dh in ds_dh)
    print(f"\n=> Tong doanh thu giao hang cua cong ty: {tong_doanh_thu:,.0f} VND")

    # Tim don hang co tong tien lon nhat
    dh_max=max(ds_dh, key=lambda dh: dh.tinh_tong_tien())
    print(f"=> Don hang co tong tien lon nhat: {dh_max.ma_don} ({dh_max.ten_khach_hang}) voi tong tien: {dh_max.tinh_tong_tien():,.0f} VND")

    # Dem so don hang cua tung loai dich vu
    dem_loai={}
    for dh in ds_dh:
        loai=type(dh).__name__
        dem_loai[loai]=dem_loai.get(loai, 0)+1

    print("\n--- THONG KE SO DON HANG THEO LOAI DICH VU ---")
    for loai, sl in dem_loai.items():
        print(f"- {loai}: {sl} don hang")

    # Liet ke cac don hang co khoang cach giao tren 20 km
    print("\n--- DANH SACH DON HANG CO KHOANG CACH > 20 KM ---")
    dh_tren_20km=[dh for dh in ds_dh if dh.khoang_cach>20]
    for dh in dh_tren_20km:
        print(f"- Ma: {dh.ma_don}, Khach: {dh.ten_khach_hang}, Khoang cach: {dh.khoang_cach:.1f} km, Tong tien: {dh.tinh_tong_tien():,.0f} VND")

    # Minh hoa tinh da hinh
    print("\n--- MINH HOA TINH DA HINH (tinh_phi_giao_hang() & tinh_phu_phi()) ---")
    for dh in ds_dh:
        print(f"{dh.ma_don:<6} | {type(dh).__name__:<18} | Phi GH: {dh.tinh_phi_giao_hang():>9,.0f} VND | Phu phi: {dh.tinh_phu_phi():>8,.0f} VND")


if __name__=="__main__":
    main()
