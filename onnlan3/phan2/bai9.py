import math

class Fraction:
    def __init__(self, tu_so=0, mau_so=1):
        self.tu_so=tu_so
        self.mau_so=mau_so
        self.__tu_so=tu_so
        if mau_so==0:
            print("Mau so khong the bang 0. He thong tu dong dat mau so la 1")
            self.__mau_so=1
        else:
            self.__mau_so=mau_so

#get

    def get_tu_so(self):
        return self.__tu_so

    def get_mau_so(self):
        return self.__mau_so

#set

    def set_tu_so(self, tu_so):
        self.__tu_so=tu_so
        return True

    def set_mau_so(self, mau_so):
        if mau_so==0:
            print("Mau so khong the bang 0! Khong cap nhat.")
            return False
        self.__mau_so=mau_so
        return True

    def __gcd(self, a, b):
        a, b = abs(a), abs(b)
        while b!=0:
            a, b = b, a % b
        return a

    def simplify(self):
        if self.__mau_so<0:
            self.__tu_so=-self.__tu_so
            self.__mau_so=-self.__mau_so
        if self.__tu_so==0:
            self.__mau_so=1
            return self

        ucln=self.__gcd(self.__tu_so, self.__mau_so)
        self.__tu_so//=ucln
        self.__mau_so//=ucln
        return self

    def add(self, other):
        tu_moi=self.__tu_so*other.get_mau_so()+self.__mau_so*other.get_tu_so()
        mau_moi=self.__mau_so*other.get_mau_so()
        res=Fraction(tu_moi, mau_moi)
        res.simplify()
        return res

    def multiply(self, other):
        tu_moi=self.__tu_so*other.get_tu_so()
        mau_moi=self.__mau_so*other.get_mau_so()
        res=Fraction(tu_moi, mau_moi)
        res.simplify()
        return res

    def inputInfo(self):
        while True:
            try:
                tu=int(input("Hay nhap tu so: "))
                self.set_tu_so(tu)
                break
            except ValueError:
                print("Tu so phai la so nguyen!")

        while True:
            try:
                mau=int(input("Hay nhap mau so: "))
                if self.set_mau_so(mau):
                    break
            except ValueError:
                print("Mau so phai la so nguyen hop le!")

    def display(self):
        if self.__tu_so==0:
            print("0")
        elif self.__mau_so==1:
            print(f"{self.__tu_so}")
        else:
            print(f"{self.__tu_so}/{self.__mau_so}")


def main():
    print("--- KHOI TAO PHAN SO f1 (3/6) VA f2 (-2/-4) ---")
    f1=Fraction(3, 6)
    f2=Fraction(-2, -4)

    print("Phan so f1 ban dau: ", end="")
    f1.display()
    print("Phan so f2 ban dau: ", end="")
    f2.display()

    print("\n--- TOI GIAN PHAN SO (simplify) ---")
    f1.simplify()
    f2.simplify()
    print("Phan so f1 sau khi toi gian: ", end="")
    f1.display()
    print("Phan so f2 sau khi toi gian: ", end="")
    f2.display()

    print("\n--- TINH TONG VA TICH ---")
    f_tong=f1.add(f2)
    print("Tong f1 + f2 = ", end="")
    f_tong.display()

    f_tich=f1.multiply(f2)
    print("Tich f1 * f2 = ", end="")
    f_tich.display()

    print("\n--- KIEM TRA DONG GOI: THU DOI MAU SO BANG 0 ---")
    f1.set_mau_so(0)
    print("Mau so cua f1 hien tai:", f1.get_mau_so())

    print("\n--- KIEM TRA GOI PHUONG THUC PRIVATE __gcd ---")
    try:
        f1.__gcd(10, 5)
    except AttributeError:
        print("Goi f1.__gcd() that bai: Phuong thuc private khong the truy cap tu ben ngoai lop.")


if __name__=="__main__":
    main()
