class DongVat:
    def __init__(self, ten="", tuoi=0, can_nang=0.0):
        self.ten=ten
        self.tuoi=tuoi
        self.can_nang=can_nang

    def nhap(self):
        self.ten=input("Hay nhap ten dong vat: ")
        while True:
            try:
                t=int(input("Hay nhap tuoi: "))
                if t>=0:
                    self.tuoi=t
                    break
                print("Tuoi phai lon hon hoac bang 0!")
            except ValueError:
                print("Tuoi phai la so nguyen!")

        while True:
            try:
                cn=float(input("Hay nhap can nang (kg): "))
                if cn>=0:
                    self.can_nang=cn
                    break
                print("Can nang phai lon hon hoac bang 0!")
            except ValueError:
                print("Can nang phai la so hop le!")

    def keu(self):
        return "Dong vat phat ra tieng keu"

    def di_chuyen(self):
        return "Dong vat dang di chuyen"

    def an(self):
        return "Dong vat dang an"

    def hien_thi(self):
        print(f"Ten: {self.ten}, Tuoi: {self.tuoi}, Can nang: {self.can_nang:.1f} kg | "
              f"Tieng keu: '{self.keu()}' | Di chuyen: '{self.di_chuyen()}' | Thuc an: '{self.an()}'")


class Cho(DongVat):
    def keu(self):
        return "Gâu gâu"

    def di_chuyen(self):
        return "Chạy bằng bốn chân"

    def an(self):
        return "Ăn thịt và thức ăn dành cho chó"

    def hien_thi(self):
        print(f"[Chó] Ten: {self.ten}, Tuoi: {self.tuoi}, Can nang: {self.can_nang:.1f} kg | "
              f"Tieng keu: '{self.keu()}' | Di chuyen: '{self.di_chuyen()}' | Thuc an: '{self.an()}'")


class Meo(DongVat):
    def keu(self):
        return "Meo meo"

    def di_chuyen(self):
        return "Đi bằng bốn chân"

    def an(self):
        return "Ăn cá và thức ăn dành cho mèo"

    def hien_thi(self):
        print(f"[Mèo] Ten: {self.ten}, Tuoi: {self.tuoi}, Can nang: {self.can_nang:.1f} kg | "
              f"Tieng keu: '{self.keu()}' | Di chuyen: '{self.di_chuyen()}' | Thuc an: '{self.an()}'")


class Chim(DongVat):
    def keu(self):
        return "Chíp chíp"

    def di_chuyen(self):
        return "Bay bằng cánh"

    def an(self):
        return "Ăn hạt và côn trùng"

    def hien_thi(self):
        print(f"[Chim] Ten: {self.ten}, Tuoi: {self.tuoi}, Can nang: {self.can_nang:.1f} kg | "
              f"Tieng keu: '{self.keu()}' | Di chuyen: '{self.di_chuyen()}' | Thuc an: '{self.an()}'")


def main():
    # Tao it nhat 6 dong vat thuoc nhieu loai khac nhau
    ds_dong_vat=[
        Cho("Golden Retriever", 3, 28.5),
        Cho("Poodle", 2, 6.0),
        Meo("Mèo Mướp", 1, 3.5),
        Meo("Mèo Ba Tư", 4, 5.2),
        Chim("Chim Sẻ", 1, 0.1),
        Chim("Vẹt Lory", 2, 0.4)
    ]

    print("================ DANH SACH DONG VAT ================")
    # Duyet danh sach va goi chung cac phuong thuc
    for dv in ds_dong_vat:
        dv.hien_thi()

    # Tim dong vat co can nang lon nhat
    dv_max_nang=max(ds_dong_vat, key=lambda dv: dv.can_nang)
    print(f"\n=> Dong vat co can nang lon nhat: {dv_max_nang.ten} ({type(dv_max_nang).__name__}) voi can nang: {dv_max_nang.can_nang:.1f} kg")

    # Dem so luong dong vat cua tung loai
    dem_loai={}
    for dv in ds_dong_vat:
        ten_loai=type(dv).__name__
        dem_loai[ten_loai]=dem_loai.get(ten_loai, 0)+1

    print("\n--- THONG KE SO LUONG THEO LOAI ---")
    for loai, sl in dem_loai.items():
        print(f"- Loai {loai}: {sl} con")

    # Minh hoa tinh da hinh
    print("\n--- MINH HOA TINH DA HINH (keu(), di_chuyen(), an()) ---")
    for dv in ds_dong_vat:
        print(f"{dv.ten:<18} -> Tieng keu: {dv.keu():<10} | Di chuyen: {dv.di_chuyen():<20} | An: {dv.an()}")


if __name__=="__main__":
    main()
