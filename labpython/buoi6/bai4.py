from datetime import datetime

class PhuongTien:
    def __init__(self, ma_pt="", hang_sx="", nam_sx=0):
        self.ma_pt=ma_pt
        self.hang_sx=hang_sx
        self.nam_sx=nam_sx

    def nhap(self):
        self.ma_pt=input("Hay nhap ma phuong tien: ")
        self.hang_sx=input("Hay nhap hang san xuat: ")
        nam_hien_tai=datetime.now().year
        while True:
            try:
                nam=int(input(f"Hay nhap nam san xuat (<= {nam_hien_tai}): "))
                if 1900<=nam<=nam_hien_tai:
                    self.nam_sx=nam
                    break
                print(f"Nam san xuat khong hop le (phai tu 1900 den {nam_hien_tai})!")
            except ValueError:
                print("Nam san xuat phai la so nguyen!")

    def tinh_tuoi_xe(self):
        nam_hien_tai=datetime.now().year
        return max(0, nam_hien_tai-self.nam_sx)

    def tinh_chi_phi(self):
        return 0

    def hien_thi(self):
        print(f"Ma PT: {self.ma_pt}, Hang SX: {self.hang_sx}, Nam SX: {self.nam_sx}, "
              f"Tuoi xe: {self.tinh_tuoi_xe()} nam, Chi phi: {self.tinh_chi_phi():,.0f} VND")


class XeMay(PhuongTien):
    def __init__(self, ma_pt="", hang_sx="", nam_sx=0, so_km=0.0):
        super().__init__(ma_pt, hang_sx, nam_sx)
        self.so_km=so_km

    def nhap(self):
        super().nhap()
        while True:
            try:
                km=float(input("Hay nhap so km da di: "))
                if km>=0:
                    self.so_km=km
                    break
                print("So km phai lon hon hoac bang 0!")
            except ValueError:
                print("So km phai la so hop le!")

    def tinh_chi_phi(self):
        return self.so_km*1000

    def hien_thi(self):
        print(f"[Xe May] Ma PT: {self.ma_pt}, Hang: {self.hang_sx}, Nam SX: {self.nam_sx}, "
              f"Tuoi xe: {self.tinh_tuoi_xe()} nam, So km: {self.so_km:,.1f}, Chi phi: {self.tinh_chi_phi():,.0f} VND")


class OTo(PhuongTien):
    def __init__(self, ma_pt="", hang_sx="", nam_sx=0, so_km=0.0):
        super().__init__(ma_pt, hang_sx, nam_sx)
        self.so_km=so_km

    def nhap(self):
        super().nhap()
        while True:
            try:
                km=float(input("Hay nhap so km da di: "))
                if km>=0:
                    self.so_km=km
                    break
                print("So km phai lon hon hoac bang 0!")
            except ValueError:
                print("So km phai la so hop le!")

    def tinh_chi_phi(self):
        return self.so_km*3000

    def hien_thi(self):
        print(f"[O To] Ma PT: {self.ma_pt}, Hang: {self.hang_sx}, Nam SX: {self.nam_sx}, "
              f"Tuoi xe: {self.tinh_tuoi_xe()} nam, So km: {self.so_km:,.1f}, Chi phi: {self.tinh_chi_phi():,.0f} VND")


class XeTai(PhuongTien):
    def __init__(self, ma_pt="", hang_sx="", nam_sx=0, so_km=0.0, trong_tai=0.0):
        super().__init__(ma_pt, hang_sx, nam_sx)
        self.so_km=so_km
        self.trong_tai=trong_tai

    def nhap(self):
        super().nhap()
        while True:
            try:
                km=float(input("Hay nhap so km da di: "))
                if km>=0:
                    self.so_km=km
                    break
                print("So km phai lon hon hoac bang 0!")
            except ValueError:
                print("So km phai la so hop le!")

        while True:
            try:
                tt=float(input("Hay nhap trong tai (tan): "))
                if tt>=0:
                    self.trong_tai=tt
                    break
                print("Trong tai phai lon hon hoac bang 0!")
            except ValueError:
                print("Trong tai phai la so hop le!")

    def tinh_chi_phi(self):
        return self.so_km*4000+self.trong_tai*500000

    def kiem_tra_qua_tai(self):
        return self.trong_tai>10

    def hien_thi(self):
        canh_bao=" (QUA TAI > 10 tan!)" if self.kiem_tra_qua_tai() else ""
        print(f"[Xe Tai] Ma PT: {self.ma_pt}, Hang: {self.hang_sx}, Nam SX: {self.nam_sx}, "
              f"Tuoi xe: {self.tinh_tuoi_xe()} nam, Trong tai: {self.trong_tai} tan, "
              f"So km: {self.so_km:,.1f}, Chi phi: {self.tinh_chi_phi():,.0f} VND{canh_bao}")


def main():
    # Tao danh sach nhieu phuong tien thuoc cac loai khac nhau
    ds_pt=[
        XeMay("XM01", "Honda", 2021, 15000),
        XeMay("XM02", "Yamaha", 2018, 32000),
        OTo("OT01", "Toyota", 2020, 45000),
        OTo("OT02", "Hyundai", 2022, 20000),
        XeTai("XT01", "Hino", 2017, 60000, 8.5),
        XeTai("XT02", "Isuzu", 2019, 80000, 15.0)
    ]

    print("================ DANH SACH PHUONG TIEN GIAO THONG ================")
    for pt in ds_pt:
        pt.hien_thi()

    # Tinh tong chi phi van hanh cua tat ca phuong tien
    tong_chi_phi=sum(pt.tinh_chi_phi() for pt in ds_pt)
    print(f"\n=> Tong chi phi van hanh cua tat ca phuong tien: {tong_chi_phi:,.0f} VND")

    # Tim phuong tien co chi phi van hanh cao nhat
    pt_max_cp=max(ds_pt, key=lambda pt: pt.tinh_chi_phi())
    print(f"=> Phuong tien co chi phi van hanh cao nhat: {pt_max_cp.ma_pt} ({type(pt_max_cp).__name__}) voi chi phi: {pt_max_cp.tinh_chi_phi():,.0f} VND")

    # Liet ke cac xe tai bi xac dinh la qua tai (> 10 tan)
    print("\n--- DANH SACH XE TAI BI QUA TAI (> 10 TAN) ---")
    xe_tai_qua_tai=[pt for pt in ds_pt if isinstance(pt, XeTai) and pt.kiem_tra_qua_tai()]
    if xe_tai_qua_tai:
        for xt in xe_tai_qua_tai:
            print(f"- Ma: {xt.ma_pt}, Hang: {xt.hang_sx}, Trong tai: {xt.trong_tai} tan, Chi phi: {xt.tinh_chi_phi():,.0f} VND")
    else:
        print("Khong co xe tai nao bi qua tai.")

    # Minh hoa tinh da hinh
    print("\n--- MINH HOA TINH DA HINH QUA tinh_chi_phi() ---")
    for pt in ds_pt:
        print(f"{pt.ma_pt:<6} | {type(pt).__name__:<10} | Tuoi xe: {pt.tinh_tuoi_xe():>2} nam | Chi phi: {pt.tinh_chi_phi():>12,.0f} VND")


if __name__=="__main__":
    main()
