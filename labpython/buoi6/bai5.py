class TaiKhoan:
    def __init__(self, so_tai_khoan="", chu_tai_khoan="", so_du=0.0):
        self.so_tai_khoan=so_tai_khoan
        self.chu_tai_khoan=chu_tai_khoan
        self.so_du=so_du if so_du>=0 else 0.0

    def nap_tien(self, so_tien):
        if so_tien<=0:
            print("So tien nap phai lon hon 0!")
            return False
        self.so_du+=so_tien
        print(f"[{self.so_tai_khoan}] Nap thanh cong {so_tien:,.0f} VND. So du hien tai: {self.so_du:,.0f} VND")
        return True

    def rut_tien(self, so_tien):
        if so_tien<=0:
            print("So tien rut phai lon hon 0!")
            return False
        if so_tien>self.so_du:
            print(f"[{self.so_tai_khoan}] Khong the rut! So du khong du (So du: {self.so_du:,.0f} VND)")
            return False
        self.so_du-=so_tien
        print(f"[{self.so_tai_khoan}] Rut thanh cong {so_tien:,.0f} VND. So du con lai: {self.so_du:,.0f} VND")
        return True

    def chuyen_tien(self, tai_khoan_nhan, so_tien):
        if so_tien<=0:
            print("So tien chuyen phai lon hon 0!")
            return False
        if so_tien>self.so_du:
            print(f"[{self.so_tai_khoan}] Khong the chuyen! So du khong du (So du: {self.so_du:,.0f} VND)")
            return False
        self.so_du-=so_tien
        tai_khoan_nhan.so_du+=so_tien
        print(f"[{self.so_tai_khoan}] Chuyen thanh cong {so_tien:,.0f} VND sang [{tai_khoan_nhan.so_tai_khoan}]. So du con lai: {self.so_du:,.0f} VND")
        return True

    def kiem_tra_so_du(self):
        return self.so_du

    def tinh_lai(self):
        return 0.0

    def hien_thi(self):
        print(f"STK: {self.so_tai_khoan}, Chu TK: {self.chu_tai_khoan}, So du: {self.so_du:,.0f} VND")


class TaiKhoanTietKiem(TaiKhoan):
    def __init__(self, so_tai_khoan="", chu_tai_khoan="", so_du=0.0, lai_suat=0.06):
        super().__init__(so_tai_khoan, chu_tai_khoan, so_du)
        self.lai_suat=lai_suat

    def tinh_lai(self):
        return self.so_du*self.lai_suat

    def cong_lai(self):
        tien_lai=self.tinh_lai()
        self.so_du+=tien_lai
        print(f"[{self.so_tai_khoan}] Da cong tien lai: {tien_lai:,.0f} VND. So du moi: {self.so_du:,.0f} VND")

    def hien_thi(self):
        print(f"[TK Tiet Kiem] STK: {self.so_tai_khoan}, Chu TK: {self.chu_tai_khoan}, "
              f"So du: {self.so_du:,.0f} VND, Lai suat: {self.lai_suat*100:.1f}%, Lai du kien: {self.tinh_lai():,.0f} VND")


class TaiKhoanThanhToan(TaiKhoan):
    def __init__(self, so_tai_khoan="", chu_tai_khoan="", so_du=0.0, phi_giao_dich=5000.0):
        super().__init__(so_tai_khoan, chu_tai_khoan, so_du)
        self.phi_giao_dich=phi_giao_dich

    def rut_tien(self, so_tien):
        if so_tien<=0:
            print("So tien rut phai lon hon 0!")
            return False
        tong_tru=so_tien+self.phi_giao_dich
        if tong_tru>self.so_du:
            print(f"[{self.so_tai_khoan}] Khong the rut! So du khong du chi tra {so_tien:,.0f} + phi {self.phi_giao_dich:,.0f} VND")
            return False
        self.so_du-=tong_tru
        print(f"[{self.so_tai_khoan}] Rut {so_tien:,.0f} VND (Phi: {self.phi_giao_dich:,.0f} VND). So du con lai: {self.so_du:,.0f} VND")
        return True

    def chuyen_tien(self, tai_khoan_nhan, so_tien):
        if so_tien<=0:
            print("So tien chuyen phai lon hon 0!")
            return False
        tong_tru=so_tien+self.phi_giao_dich
        if tong_tru>self.so_du:
            print(f"[{self.so_tai_khoan}] Khong the chuyen! So du khong du chi tra {so_tien:,.0f} + phi {self.phi_giao_dich:,.0f} VND")
            return False
        self.so_du-=tong_tru
        tai_khoan_nhan.so_du+=so_tien
        print(f"[{self.so_tai_khoan}] Chuyen {so_tien:,.0f} VND den [{tai_khoan_nhan.so_tai_khoan}] (Phi: {self.phi_giao_dich:,.0f} VND). So du con lai: {self.so_du:,.0f} VND")
        return True

    def hien_thi(self):
        print(f"[TK Thanh Toan] STK: {self.so_tai_khoan}, Chu TK: {self.chu_tai_khoan}, "
              f"So du: {self.so_du:,.0f} VND, Phi GD: {self.phi_giao_dich:,.0f} VND")


def main():
    # Tao nhieu tai khoan thuoc hai loai khac nhau
    tk_tk1=TaiKhoanTietKiem("TK01", "Nguyen Van An", 50000000, 0.06)
    tk_tk2=TaiKhoanTietKiem("TK02", "Tran Thi Mai", 100000000, 0.07)
    tk_tt1=TaiKhoanThanhToan("TT01", "Le Van Long", 15000000, 5000)
    tk_tt2=TaiKhoanThanhToan("TT02", "Pham Hoang Yen", 8000000, 3000)

    ds_tk=[tk_tk1, tk_tk2, tk_tt1, tk_tt2]

    print("================ DANH SACH TAI KHOAN BAN DAU ================")
    for tk in ds_tk:
        tk.hien_thi()

    print("\n================ THUC HIEN CAC GIAO DICH ================")
    print("\n1. Nap tien:")
    tk_tt1.nap_tien(5000000)

    print("\n2. Rut tien:")
    tk_tt1.rut_tien(2000000)
    tk_tk1.rut_tien(10000000)

    print("\n3. Chuyen tien (co phi giao dich tren TK thanh toan):")
    tk_tt1.chuyen_tien(tk_tt2, 3000000)

    print("\n4. Tinh lai va cong lai cho tai khoan tiet kiem:")
    for tk in ds_tk:
        if isinstance(tk, TaiKhoanTietKiem):
            print(f"Tien lai cua {tk.chu_tai_khoan}: {tk.tinh_lai():,.0f} VND")
            tk.cong_lai()

    print("\n================ THONG TIN TAI KHOAN SAU GIAO DICH ================")
    for tk in ds_tk:
        tk.hien_thi()

    # Tim tai khoan co so du lon nhat
    tk_max_sodu=max(ds_tk, key=lambda tk: tk.kiem_tra_so_du())
    print(f"\n=> Tai khoan co so du lon nhat: {tk_max_sodu.chu_tai_khoan} ({tk_max_sodu.so_tai_khoan}) voi so du: {tk_max_sodu.kiem_tra_so_du():,.0f} VND")


if __name__=="__main__":
    main()
