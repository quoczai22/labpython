class PhuongTrinhBacHai:
    def __init__(self):
        self.a=0
        self.b=0
        self.c=0

    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def get_c(self):
        return self.__c

    def set_a(self,a):
        if a is not float:
            print("Loi nhap so a!")
            return

        self.__a=a

    def set_b(self,b):
        if b is not float:
            print("Loi nhap so b!")
            return

        self.__b=b

    def set__c(self,c):
        if c is not float:
            print("Loi nhap so c!")
            return

        self.__c=c

    def tinh_ptr(self):
        if self.__a==0:
            if self.__b==0:
                return "Phuong trinh co vo so nghiem"
            else:
                return "Phuong trinh vo nghiem"
        else:
            delta=self.__b**2-4*self.__a*self.__c
            if delta<0:
                return "Phuong trinh vo nghiem"
            elif delta==0:
                x=-self.__b/(2*self.__a)
                return f"Phuong trinh co nghiem kep x1=x2={x}"
            else:
                x1=(-self.__b+delta**0.5)/(2*self.__a)
                x2=(-self.__b-delta**0.5)/(2*self.__a)
                return f"Phuong trinh co 2 nghiem phan biet x1={x1}, x2={x2}"

def main():
    pt2=PhuongTrinhBacHai()
    pt2.nhap()
    pt2.tinh_ptr()

if __name__=="__main__":
    main()

    
        