class HoaDonDien:
    def __init__(self, ma_kh="", ho_ten="", so_kwh=0.0):
        self.ma_kh=ma_kh
        self.ho_ten=ho_ten
        self.so_kwh=so_kwh

    def nhap(self):
        self.ma_kh=input("Hay nhap ma khach hang: ")
        self.ho_ten=input("Hay nhap ho ten khach hang: ")
        while True:
            try:
                kwh=float(input("Hay nhap so dien tieu thu (kWh): "))
                if kwh>=0:
                    self.so_kwh=kwh
                    break
                print("So dien tieu thu phai lon hon hoac bang 0!")
            except ValueError:
                print("So dien phai la so hop le!")

    def tinh_tien_dien(self):
        return 0.0

    def tinh_thue(self):
        # VAT 10%
        return self.tinh_tien_dien()*0.10

    def tinh_tong_tien(self):
        return self.tinh_tien_dien()+self.tinh_thue()

    def hien_thi(self):
        print(f"Ma KH: {self.ma_kh}, Ho ten: {self.ho_ten}, So kWh: {self.so_kwh:.1f}, "
              f"Tien dien: {self.tinh_tien_dien():,.0f} VND, VAT: {self.tinh_thue():,.0f} VND, "
              f"Tong tien: {self.tinh_tong_tien():,.0f} VND")


class HoaDonHoGiaDinh(HoaDonDien):
    def __init__(self, ma_kh="", ho_ten="", so_kwh=0.0):
        super().__init__(ma_kh, ho_ten, so_kwh)

    def tinh_tien_dien(self):
        kwh=self.so_kwh
        if kwh<=50:
            return kwh*1800
        elif kwh<=100:
            return 50*1800+(kwh-50)*2000
        else:
            return 50*1800+50*2000+(kwh-100)*2500

    def hien_thi(self):
        print(f"[Ho Gia Dinh] Ma KH: {self.ma_kh}, Ho ten: {self.ho_ten}, So kWh: {self.so_kwh:.1f}, "
              f"Tien dien: {self.tinh_tien_dien():,.0f} VND, VAT: {self.tinh_thue():,.0f} VND, "
              f"Tong tien: {self.tinh_tong_tien():,.0f} VND")


class HoaDonKinhDoanh(HoaDonDien):
    def __init__(self, ma_kh="", ho_ten="", so_kwh=0.0):
        super().__init__(ma_kh, ho_ten, so_kwh)

    def tinh_tien_dien(self):
        return self.so_kwh*3000

    def hien_thi(self):
        print(f"[Kinh Doanh]  Ma KH: {self.ma_kh}, Ho ten: {self.ho_ten}, So kWh: {self.so_kwh:.1f}, "
              f"Tien dien: {self.tinh_tien_dien():,.0f} VND, VAT: {self.tinh_thue():,.0f} VND, "
              f"Tong tien: {self.tinh_tong_tien():,.0f} VND")


def main():
    # Tao it nhat 4 hoa don gom ca ho gia dinh va kinh doanh
    ds_hd=[
        HoaDonHoGiaDinh("GD01", "Nguyen Van An", 45),
        HoaDonHoGiaDinh("GD02", "Tran Thi Mai", 85),
        HoaDonHoGiaDinh("GD03", "Le Hoang Phuc", 180),
        HoaDonKinhDoanh("KD01", "Cong ty TNHH Song Lam", 450),
        HoaDonKinhDoanh("KD02", "Nha hang Bien Dong", 1200)
    ]

    print("================ DANH SACH HOA DON TIEN DIEN ================")
    # Duyet danh sach va hien thi day du cac cot
    for hd in ds_hd:
        hd.hien_thi()

    # Tinh tong doanh thu tien dien cua tat ca khach hang
    tong_doanh_thu=sum(hd.tinh_tong_tien() for hd in ds_hd)
    print(f"\n=> Tong doanh thu tien dien (da gom VAT): {tong_doanh_thu:,.0f} VND")

    # Tim khach hang co tong tien thanh toan cao nhat
    hd_max=max(ds_hd, key=lambda hd: hd.tinh_tong_tien())
    print(f"=> Khach hang co tong tien thanh toan cao nhat: {hd_max.ho_ten} ({hd_max.ma_kh}) voi tong tien: {hd_max.tinh_tong_tien():,.0f} VND")

    # Minh hoa tinh da hinh thong qua phuong thuc tinh_tien_dien()
    print("\n--- MINH HOA TINH DA HINH QUA tinh_tien_dien() ---")
    for hd in ds_hd:
        print(f"{hd.ma_kh:<6} | {hd.ho_ten:<26} | {type(hd).__name__:<16} | So kWh: {hd.so_kwh:>6.1f} | Tien dien: {hd.tinh_tien_dien():>10,.0f} VND")


if __name__=="__main__":
    main()
