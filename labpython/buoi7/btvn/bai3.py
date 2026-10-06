class SinhVien:
    def __init__(self, ma="", ten=""):
        self.__ma = ma
        self.__ten = ten

    def get_ma(self):
        return self.__ma

    def set_ma(self, ma):
        ma = ma.strip()
        if ma == "":
            print("Loi: Ma sinh vien khong duoc de trong!")
            return False
        self.__ma = ma
        return True

    def get_ten(self):
        return self.__ten

    def set_ten(self, ten):
        ten = ten.strip()
        if ten == "":
            print("Loi: Ten sinh vien khong duoc de trong!")
            return False
        self.__ten = ten
        return True

    def nhap(self):
        while True:
            ma = input("Nhap ma sinh vien: ")
            if self.set_ma(ma):
                break

        while True:
            ten = input("Nhap ho va ten sinh vien: ")
            if self.set_ten(ten):
                break

    def xuat(self):
        print(f"Ma SV: {self.__ma:<10} | Ho va ten: {self.__ten}")


class DanhSachSinhVien:
    def __init__(self):
        self.danh_sach = []

    def tim_sinh_vien(self, ma):
        for sv in self.danh_sach:
            if sv.get_ma().lower() == ma.strip().lower():
                return sv
        return None

    def them_sinh_vien(self, sinh_vien):
        if self.tim_sinh_vien(sinh_vien.get_ma()) is not None:
            print(f"Loi: Ma sinh vien '{sinh_vien.get_ma()}' da ton tai!")
            return False
        self.danh_sach.append(sinh_vien)
        print("Them sinh vien thanh cong!")
        return True

    def xoa_sinh_vien(self, ma):
        sv = self.tim_sinh_vien(ma)
        if sv:
            self.danh_sach.remove(sv)
            return True
        return False

    def sua_sinh_vien(self, ma):
        sv = self.tim_sinh_vien(ma)
        if not sv:
            return False
        print(f"Thong tin hien tai: Ma SV: {sv.get_ma()} - Ten SV: {sv.get_ten()}")
        while True:
            ten_moi = input("Nhap ho va ten moi: ")
            if sv.set_ten(ten_moi):
                break
        return True

    def xuat_danh_sach(self):
        if not self.danh_sach:
            print("Danh sach sinh vien dang trong!")
            return
        print("\n" + "=" * 40)
        print(f"{'STT':<5} {'Ma SV':<12} {'Ho va ten'}")
        print("-" * 40)
        for i, sv in enumerate(self.danh_sach, start=1):
            print(f"{i:<5} {sv.get_ma():<12} {sv.get_ten()}")
        print("=" * 40 + "\n")


def main():
    ds = DanhSachSinhVien()
    while True:
        print("\n--- CHUONG TRINH QUAN LY SINH VIEN ---")
        print("1. Them sinh vien")
        print("2. Xoa sinh vien")
        print("3. Sua sinh vien")
        print("4. Xem danh sach sinh vien")
        print("5. Thoat")
        choice = input("Chon chuc nang (1-5): ").strip()

        if choice == "1":
            sv = SinhVien()
            while True:
                ma = input("Nhap ma sinh vien: ").strip()
                if not ma:
                    print("Loi: Ma sinh vien khong duoc de trong!")
                    continue
                if ds.tim_sinh_vien(ma):
                    print(f"Loi: Ma sinh vien '{ma}' da ton tai trong danh sach! Vui long nhap ma khac.")
                    continue
                sv.set_ma(ma)
                break

            while True:
                ten = input("Nhap ho va ten sinh vien: ").strip()
                if sv.set_ten(ten):
                    break

            ds.them_sinh_vien(sv)

        elif choice == "2":
            ma = input("Nhap ma sinh vien can xoa: ").strip()
            if ds.xoa_sinh_vien(ma):
                print("Xoa sinh vien thanh cong!")
            else:
                print("Khong tim thay sinh vien voi ma vua nhap!")

        elif choice == "3":
            ma = input("Nhap ma sinh vien can sua: ").strip()
            if ds.sua_sinh_vien(ma):
                print("Sua thong tin sinh vien thanh cong!")
            else:
                print("Khong tim thay sinh vien voi ma vua nhap!")

        elif choice == "4":
            ds.xuat_danh_sach()

        elif choice == "5":
            print("Cam on ban da su dung chuong trinh. Tam biet!")
            break

        else:
            print("Lua chon khong hop le! Vui long chon tu 1 den 5.")


if __name__ == "__main__":
    main()