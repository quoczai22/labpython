class PhuongTrinhBacNhat:
    def __init__(self):
        self.a=0
        self.b=0

    def get_a(self):
        return self.__a

    def set_a(self,a):
        self.__a=a

    def get_b(self):
        return self.__b

    def set_b(self,b):
        self.__b=b

    def nhap(self):
        a=float(input("Hay nhap so a: "))
        self.set_a(a)
        b=float(input("Hay nhap so b: "))
        self.set_b(b)

    def tinh_ptr(self):
        if self.__a==0:
            if self.__b==0:
                return "Phuong trinh co vo so nghiem"
            else:
                return "Phuong trinh vo nghiem"
        else:
            x=-self.__b/self.__a
            return x
        
    def xuat(self):
        print(f"ket qua cua phuong trinh bac nhat la {self.tinh_ptr()}")

def main():
    pt1=PhuongTrinhBacNhat()
    pt1.nhap()
    pt1.xuat()

if __name__=="__main__":
    main()



