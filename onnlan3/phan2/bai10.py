class ElectronicProduct:
    def __init__(self, ma_sp="", ten_sp="", hang_sx="", gia_nhap=0.0, phan_tram_lai=0.1, thang_bao_hanh=12):
        self.ma_sp=ma_sp
        self.ten_sp=ten_sp
        self.hang_sx=hang_sx
        self.gia_nhap=gia_nhap
        self.phan_tram_lai=phan_tram_lai
        self.thang_bao_hanh=thang_bao_hanh

        self.__ma_sp=ma_sp
        self.__ten_sp=ten_sp
        self._hang_sx=hang_sx
        self.__gia_nhap=gia_nhap if gia_nhap>0 else 1.0
        self.__phan_tram_lai=phan_tram_lai if 0.05<=phan_tram_lai<=0.5 else 0.1
        self.__thang_bao_hanh=thang_bao_hanh if thang_bao_hanh>=0 else 12

#get

    def get_ma_sp(self):
        return self.__ma_sp

    def get_ten_sp(self):
        return self.__ten_sp

    def get_hang_sx(self):
        return self._hang_sx

    @property
    def gia_nhap(self):
        return self.__gia_nhap

    @property
    def phan_tram_lai(self):
        return self.__phan_tram_lai

    @property
    def thang_bao_hanh(self):
        return self.__thang_bao_hanh

#set

    def set_ma_sp(self, ma_sp):
        if ma_sp.strip()!="":
            self.__ma_sp=ma_sp
            return True
        print("Ma san pham khong duoc de trong!")
        return False

    def set_ten_sp(self, ten_sp):
        if ten_sp.strip()!="":
            self.__ten_sp=ten_sp
            return True
        print("Ten san pham khong duoc de trong!")
        return False

    def set_hang_sx(self, hang_sx):
        if hang_sx.strip()!="":
            self._hang_sx=hang_sx
            return True
        print("Hang san xuat khong duoc de trong!")
        return False

    @gia_nhap.setter
    def gia_nhap(self, value):
        if value>0:
            self.__gia_nhap=value
            return True
        else:
            print("Gia nhap phai lon hon 0!")
            return False

    @phan_tram_lai.setter
    def phan_tram_lai(self, value):
        if 0.05<=value<=0.5:
            self.__phan_tram_lai=value
            return True
        else:
            print("Phan tram loi nhuan phai nam trong khoang tu 0.05 (5%) den 0.5 (50%)!")
            return False

    @thang_bao_hanh.setter
    def thang_bao_hanh(self, value):
        if value>=0:
            self.__thang_bao_hanh=value
            return True
        else:
            print("Thoi gian bao hanh phai lon hon hoac bang 0!")
            return False

    # Setter thong thuong de tuong thich phong cach cu
    def set_gia_nhap(self, value):
        if value>0:
            self.__gia_nhap=value
            return True
        print("Gia nhap phai lon hon 0!")
        return False

    def calculate_selling_price(self):
        return self.__gia_nhap*(1+self.__phan_tram_lai)

    def check_warranty(self, months_used):
        if months_used<0:
            print("So thang su dung phai >= 0!")
            return False
        return months_used<=self.__thang_bao_hanh

    def inputInfo(self):
        while True:
            ma=input("Hay nhap ma san pham: ")
            if self.set_ma_sp(ma):
                break

        while True:
            ten=input("Hay nhap ten san pham: ")
            if self.set_ten_sp(ten):
                break

        while True:
            hang=input("Hay nhap hang san xuat: ")
            if self.set_hang_sx(hang):
                break

        while True:
            try:
                gn=float(input("Hay nhap gia nhap (> 0): "))
                if self.set_gia_nhap(gn):
                    break
            except ValueError:
                print("Gia nhap phai la so hop le!")

        while True:
            try:
                pt=float(input("Hay nhap phan tram lai (0.05 - 0.5): "))
                if 0.05<=pt<=0.5:
                    self.phan_tram_lai=pt
                    break
                print("Phan tram loi nhuan phai tu 0.05 den 0.5!")
            except ValueError:
                print("Phan tram lai phai la so hop le!")

        while True:
            try:
                bh=int(input("Hay nhap so thang bao hanh: "))
                if bh>=0:
                    self.thang_bao_hanh=bh
                    break
                print("So thang bao hanh phai >= 0!")
            except ValueError:
                print("Thang bao hanh phai la so nguyen!")

    def display(self):
        print(f"Ma SP: {self.__ma_sp}, Ten SP: {self.__ten_sp}, Hang SX: {self._hang_sx}, "
              f"Gia nhap: {self.__gia_nhap:,.0f} VND, Ty le lai: {self.__phan_tram_lai*100:.1f}%, "
              f"Gia ban de xuat: {self.calculate_selling_price():,.0f} VND, Bao hanh: {self.__thang_bao_hanh} thang")


def main():
    print("--- TAO DOI TUONG ElectronicProduct (Tivi Samsung) ---")
    sp=ElectronicProduct("TV01", "Smart Tivi Samsung 55 inch", "Samsung", 15000000, 0.15, 24)
    sp.display()

    print("\n--- THAY DOI GIA NHAP QUA PROPERTY SETTER (len 16.000.000 VND) ---")
    sp.gia_nhap=16000000
    print(f"Gia nhap moi: {sp.gia_nhap:,.0f} VND")
    print(f"Gia ban le moi sau khi tang gia nhap: {sp.calculate_selling_price():,.0f} VND")

    print("\n--- KIEM TRA HAN BAO HANH (check_warranty) ---")
    so_thang_test=18
    con_han=sp.check_warranty(so_thang_test)
    print(f"Khach hang da dung {so_thang_test} thang: {'Con han bao hanh mien phi' if con_han else 'Het han bao hanh'}")

    so_thang_test2=30
    con_han2=sp.check_warranty(so_thang_test2)
    print(f"Khach hang da dung {so_thang_test2} thang: {'Con han bao hanh mien phi' if con_han2 else 'Het han bao hanh'}")

    print("\n--- TRUY CAP BIEN PROTECTED _hang_sx ---")
    print("Truy cap _hang_sx (protected):", sp._hang_sx, "-> Quy uoc protected co the truy cap nhung khong khuyen khich.")

    print("\n--- TRUY CAP BIEN PRIVATE __gia_nhap ---")
    try:
        print("Truy cap sp.__gia_nhap:", sp.__gia_nhap)
    except AttributeError:
        print("Truy cap sp.__gia_nhap that bai: Bien private da bi Name Mangling an di.")
        print("Lach luat truy cap qua _ElectronicProduct__gia_nhap:", sp._ElectronicProduct__gia_nhap)


if __name__=="__main__":
    main()
