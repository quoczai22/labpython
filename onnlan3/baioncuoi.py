# =================================================================
# 1. LỚP CHA: VeXemPhim (ĐÃ VIẾT SẴN HOÀN CHỈNH)
# =================================================================
class VeXemPhim:
    def __init__(self, ma_ve="", ten_phim="", gia_goc=0.0):
        self.ma_ve = ma_ve
        self.ten_phim = ten_phim
        self.gia_goc = gia_goc

    def nhap(self):
        self.ma_ve = input("Hay nhap ma ve: ")
        self.ten_phim = input("Hay nhap ten phim: ")
        while True:
            try:
                gia = float(input("Hay nhap gia ve goc: "))
                if gia > 0:
                    self.gia_goc = gia
                    break
                print("Gia ve goc phai lon hon 0!")
            except ValueError:
                print("Gia ve phai la so hop le!")

    def tinh_gia_ve(self):
        return self.gia_goc

    def hien_thi(self):
        print(f"[Ve Thuong] Ma ve: {self.ma_ve}, Phim: {self.ten_phim}, "
              f"Gia goc: {self.gia_goc:,.0f} VND, Gia thanh toan: {self.tinh_gia_ve():,.0f} VND")


# =================================================================
# 2. CÁC LỚP CON (KẾ THỪA VÀ GHI ĐÈ ĐA HÌNH)
# =================================================================

# --- Lớp 1: VeHocSinhSinhVien (Kế thừa từ VeXemPhim) ---
class VeHocSinhSinhVien(VeXemPhim):
    def __init__(self):
        super().__init__()
        self.ngay_thu = ""

    def nhap(self):
        super().nhap()
        self.ngay_thu = input("Hay nhap ngay thu / ma the: ")

    def tinh_gia_ve(self):
        # HSSV duoc giam 20% gia goc
        return self.gia_goc * 0.8

    def hien_thi(self):
        print(f"[Ve HSSV] Ma ve: {self.ma_ve}, Phim: {self.ten_phim}, Gia goc: {self.gia_goc:,.0f} VND, "
              f"Ghi chu: {self.ngay_thu}, Gia thanh toan (Giam 20%): {self.tinh_gia_ve():,.0f} VND")


# --- Lớp 2: VeVIP (Kế thừa từ VeXemPhim) ---
class VeVIP(VeXemPhim):
    def __init__(self):
        super().__init__()
        self.loai_cho_ngoi = ""

    def nhap(self):
        super().nhap()
        self.loai_cho_ngoi = input("Hay nhap loai cho ngoi (Vi du: phong VIP): ")

    def tinh_gia_ve(self):
        if self.loai_cho_ngoi.strip().lower() == "phong vip":
            return self.gia_goc * 1.5
        return self.gia_goc * 1.2

    def hien_thi(self):
        print(f"[Ve VIP] Ma ve: {self.ma_ve}, Phim: {self.ten_phim}, Gia goc: {self.gia_goc:,.0f} VND, "
              f"Loai cho ngoi: {self.loai_cho_ngoi}, Gia thanh toan: {self.tinh_gia_ve():,.0f} VND")


# =================================================================
# 3. CHƯƠNG TRÌNH CHÍNH (main)
# =================================================================
def main():
    ds_ve = []
    
    # 1. Ve thuong
    v1 = VeXemPhim("VT01", "Doraemon", 80000)
    ds_ve.append(v1)

    # 2. Ve HSSV
    v2 = VeHocSinhSinhVien()
    v2.ma_ve = "SV01"
    v2.ten_phim = "Tham Tu Conan"
    v2.gia_goc = 80000
    v2.ngay_thu = "The SV: 2021001"
    ds_ve.append(v2)

    # 3. Ve VIP
    v3 = VeVIP()
    v3.ma_ve = "VIP01"
    v3.ten_phim = "Avatar 3"
    v3.gia_goc = 100000
    v3.loai_cho_ngoi = "phong VIP"
    ds_ve.append(v3)

    print("================ DANH SACH VE XEM PHIM ================")
    # Duyet da hinh
    for ve in ds_ve:
        ve.hien_thi()

    # Tinh tong doanh thu
    tong_doanh_thu = sum(ve.tinh_gia_ve() for ve in ds_ve)
    print("="*55)
    print(f"=> TONG DOANH THU BAN VE: {tong_doanh_thu:,.0f} VND")
    print("="*55)


if __name__ == "__main__":
    main()
