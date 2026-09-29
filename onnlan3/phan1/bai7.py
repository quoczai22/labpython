import math
class Fraction:
    def __init__(self, numerator=0, denominator=1):
        self.numerator=numerator
        self.denominator=denominator

    def input_fraction(self):
        self.numerator=int(input("Hay nhap tu so: "))
        while True:
            try:
                self.denominator=int(input("Hay nhap mau so: "))
                if self.denominator==0:
                    print("Mau so khong duoc bang 0. Xin moi ban nhap lai!")
                else:
                    break
            except ValueError:
                print("Mau so phai la mot so nguyen. Xin moi ban nhap lai!")

    def simplify(self):
        gcd=math.gcd(self.numerator,self.denominator)
        num=self.numerator//gcd
        den=self.denominator//gcd
        if den<0:
            num=-num
            den=-den
        return num,den

    def value(self):
        return self.numerator/self.denominator

    def display(self):
        num,den=self.simplify()
        if den==1:
            print(f"Gia tri cua phan so la: {self.value()}, Hien thi theo dang phan so la: {num}")
        else:
            print(f"Gia tri cua phan so la: {self.value()}, Hien thi theo dang phan so la: {num}/{den}")

def main():
    ps1=Fraction()
    ps1.input_fraction()
    ps1.display()

if __name__=="__main__":
    main()



        
        