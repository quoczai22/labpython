class SanPham:
    def __init__(self, ma_sp="", ten_sp="", don_gia=0.0):
        self.ma_sp=ma_sp
        self.ten_sp=ten_sp
        self.don_gia=don_gia

    def nhap(self):
        self.ma_sp=input("Hay nhap ma san pham: ")
        self.ten_sp=input("Hay nhap ten san pham: ")
        while True:
            try:
                dg=float(input("Hay nhap don gia: "))
                if dg>0:
                    self.don_gia=dg
                    break
                print("Don gia phai lon hon 0!")
            except ValueError:
                print("Don gia phai la so hop le!")

    def tinh_gia_ban(self):
        return self.don_gia

    def tinh_thue(self):
        return self.don_gia*0.1

    def hien_thi(self):
        print(f"Ma SP: {self.ma_sp}, Ten: {self.ten_sp}, Don gia: {self.don_gia:,.0f} VND, Gia ban: {self.tinh_gia_ban():,.0f} VND")


class ThucPham(SanPham):
    def __init__(self, ma_sp="", ten_sp="", don_gia=0.0, so_ngay_con_han=0):
        super().__init__(ma_sp, ten_sp, don_gia)
        self.so_ngay_con_han=so_ngay_con_han

    def nhap(self):
        super().nhap()
        while True:
            try:
                han=int(input("Hay nhap so ngay con han: "))
                if han>=0:
                    self.so_ngay_con_han=han
                    break
                print("So ngay con han phai lon hon hoac bang 0!")
            except ValueError:
                print("So ngay con han phai la so nguyen!")

    def kiem_tra_sap_het_han(self):
        return self.so_ngay_con_han<=3

    def tinh_muc_giam(self):
        return 0.10 if self.kiem_tra_sap_het_han() else 0.0

    def tinh_gia_ban(self):
        if self.kiem_tra_sap_het_han():
            return self.don_gia*0.90
        return self.don_gia

    def hien_thi(self):
        canh_bao=" (SAP HET HAN - Giam 10%)" if self.kiem_tra_sap_het_han() else ""
        print(f"[Thuc Pham] Ma SP: {self.ma_sp}, Ten: {self.ten_sp}, Don gia: {self.don_gia:,.0f} VND, "
              f"Con lai: {self.so_ngay_con_han} ngay, Gia ban: {self.tinh_gia_ban():,.0f} VND{canh_bao}")


class DienTu(SanPham):
    def __init__(self, ma_sp="", ten_sp="", don_gia=0.0, thoi_gian_bao_hanh=0):
        super().__init__(ma_sp, ten_sp, don_gia)
        self.thoi_gian_bao_hanh=thoi_gian_bao_hanh

    def nhap(self):
        super().nhap()
        while True:
            try:
                bh=int(input("Hay nhap thoi gian bao hanh (thang): "))
                if bh>=0:
                    self.thoi_gian_bao_hanh=bh
                    break
                print("Thoi gian bao hanh phai lon hon hoac bang 0!")
            except ValueError:
                print("Thoi gian bao hanh phai la so nguyen!")

    def tinh_gia_ban(self):
        # Phi bao hanh 10%
        return self.don_gia+self.don_gia*0.10

    def hien_thi(self):
        print(f"[Dien Tu] Ma SP: {self.ma_sp}, Ten: {self.ten_sp}, Don gia: {self.don_gia:,.0f} VND, "
              f"Bao hanh: {self.thoi_gian_bao_hanh} thang, Gia ban (+10% BH): {self.tinh_gia_ban():,.0f} VND")


class QuanAo(SanPham):
    def __init__(self, ma_sp="", ten_sp="", don_gia=0.0, loai_khach_hang="Thuong"):
        super().__init__(ma_sp, ten_sp, don_gia)
        self.loai_khach_hang=loai_khach_hang

    def nhap(self):
        super().nhap()
        loai=input("Hay nhap loai khach hang (VIP/Thuong): ").strip()
        self.loai_khach_hang="VIP" if loai.upper()=="VIP" else "Thuong"

    def tinh_gia_ban(self):
        if self.loai_khach_hang.upper()=="VIP":
            return self.don_gia*0.85
        return self.don_gia

    def hien_thi(self):
        giam=" (VIP - Giam 15%)" if self.loai_khach_hang.upper()=="VIP" else ""
        print(f"[Quan Ao] Ma SP: {self.ma_sp}, Ten: {self.ten_sp}, Don gia: {self.don_gia:,.0f} VND, "
              f"Loai KH: {self.loai_khach_hang}, Gia ban: {self.tinh_gia_ban():,.0f} VND{giam}")


def main():
    # Tao danh sach gom nhieu loai san pham
    ds_sp=[
        ThucPham("TP01", "Sua tuoi Vinamilk", 35000, 2),
        ThucPham("TP02", "Banh mi sandwich", 25000, 7),
        DienTu("DT01", "Tai nghe Bluetooth", 500000, 12),
        DienTu("DT02", "Chuot khong day", 300000, 24),
        QuanAo("QA01", "Ao so mi nam", 400000, "VIP"),
        QuanAo("QA02", "Quan jean nu", 450000, "Thuong")
    ]

    print("================ DANH SACH SAN PHAM ================")
    for sp in ds_sp:
        sp.hien_thi()

    # Tinh tong gia tri cua tat ca san pham (gia ban thuc te)
    tong_gia_tri=sum(sp.tinh_gia_ban() for sp in ds_sp)
    print(f"\n=> Tong gia tri tat ca san pham (theo gia ban): {tong_gia_tri:,.0f} VND")

    # Tim san pham co gia ban cao nhat
    sp_max_gia=max(ds_sp, key=lambda sp: sp.tinh_gia_ban())
    print(f"=> San pham co gia ban cao nhat: {sp_max_gia.ten_sp} ({sp_max_gia.ma_sp}) voi gia ban: {sp_max_gia.tinh_gia_ban():,.0f} VND")

    # Liet ke cac thuc pham sap het han
    print("\n--- DANH SACH THUC PHAM SAP HET HAN (<= 3 NGAY) ---")
    tp_sap_het_han=[sp for sp in ds_sp if isinstance(sp, ThucPham) and sp.kiem_tra_sap_het_han()]
    if tp_sap_het_han:
        for tp in tp_sap_het_han:
            print(f"- {tp.ten_sp} ({tp.ma_sp}): Con lai {tp.so_ngay_con_han} ngay -> Gia ban uu dai: {tp.tinh_gia_ban():,.0f} VND")
    else:
        print("Khong co thuc pham nao sap het han.")

    # Minh hoa tinh da hinh
    print("\n--- MINH HOA TINH DA HINH QUA tinh_gia_ban() ---")
    for sp in ds_sp:
        print(f"{sp.ma_sp:<6} | {sp.ten_sp:<22} | Don gia: {sp.don_gia:>8,.0f} | Gia ban: {sp.tinh_gia_ban():>8,.0f} VND")


if __name__=="__main__":
    main()
