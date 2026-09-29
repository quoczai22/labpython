class Customer:
    def __init__(self, ma_kh="", ho_ten="", loai_kh="Thuong", tong_tien=0):
        self.__ma_kh=ma_kh
        self.__ho_ten=ho_ten
        self.__loai_kh=loai_kh
        self.__tong_tien=tong_tien if tong_tien>=0 else 0

    KhachHang = None # Will assign below

    def get_ma_kh(self):
        return self.__ma_kh

    def set_ma_kh(self, ma_kh):
        if ma_kh.strip():
            self.__ma_kh=ma_kh
            return True
        else:
            print("Ma khach hang khong duoc de trong")
            return False

    def get_ho_ten(self):
        return self.__ho_ten

    def set_ho_ten(self, ho_ten):
        if ho_ten.strip():
            self.__ho_ten=ho_ten
            return True
        else:
            print("Ban phai nhap ho ten")
            return False

    def get_loai_kh(self):
        return self.__loai_kh

    def set_loai_kh(self, loai_kh):
        valid=["thuong", "bac", "vang", "vip"]
        if loai_kh.strip().lower() in valid:
            self.__loai_kh=loai_kh.strip().title() if loai_kh.strip().lower()!="vip" else "VIP"
            return True
        else:
            print("Loai khach hang phai la: Thuong, Bac, Vang, hoac VIP")
            return False

    def get_tong_tien(self):
        return self.__tong_tien
    
    def set_tong_tien(self, tong_tien):
        if tong_tien<0:
            print("Tong tien phai lon hon hoac bang 0!")
            return False
        else:
            self.__tong_tien=tong_tien
            return True

    def discount_rate(self):
        loai=self.__loai_kh.strip().lower()
        if loai=="thuong":
            return 0.0
        elif loai=="bac":
            return 0.05
        elif loai=="vang":
            return 0.10
        elif loai=="vip":
            return 0.15
        return 0.0

    def discount_amount(self):
        return self.__tong_tien*self.discount_rate()

    # alias cho code cu
    discount_ammount = discount_amount

    def payment(self):
        return self.__tong_tien-self.discount_amount()

    def input(self):
        while True:
            ma=input("Hay nhap ma khach hang: ")
            if self.set_ma_kh(ma):
                break
        while True:
            ht=input("Hay nhap ho ten khach hang: ")
            if self.set_ho_ten(ht):
                break
        while True:
            loai=input("Hay nhap loai khach hang (Thuong/Bac/Vang/VIP): ")
            if self.set_loai_kh(loai):
                break
        while True:
            try:
                tt=float(input("Hay nhap tong tien ban dau: "))
                if self.set_tong_tien(tt):
                    break
            except ValueError:
                print("Tong tien phai la so hop le!")

    def display(self):
        print(f"Ma khach hang: {self.__ma_kh}")
        print(f"Ho ten: {self.__ho_ten}")
        print(f"Loai khach hang: {self.__loai_kh}")
        print(f"Tong tien ban dau: {self.get_tong_tien()}")
        print(f"Ty le giam gia: {int(self.discount_rate()*100)}%")
        print(f"So tien duoc giam: {self.discount_amount()}")
        print(f"So tien phai thanh toan: {self.payment()}")

KhachHang = Customer

def main():
    kh1=Customer()
    kh1.input()
    print("\n--- Thong tin khach hang ---")
    kh1.display()

    print("\n--- Kiem tra getter / setter ---")
    print("Tong tien hien tai (getter):", kh1.get_tong_tien())
    kh1.set_tong_tien(kh1.get_tong_tien()+500000)
    print("Tong tien sau khi tang 500k (setter):", kh1.get_tong_tien())
    print("So tien thanh toan moi:", kh1.payment())

    print("\n--- Thu truy cap thuoc tinh private tu ben ngoai ---")
    try:
        print("Truy cap __tong_tien:", kh1.__tong_tien)
    except AttributeError:
        print("Truy cap __tong_tien that bai: Khong the truy cap truc tiep thuoc tinh private tu ben ngoai.")

if __name__=="__main__":
    main()