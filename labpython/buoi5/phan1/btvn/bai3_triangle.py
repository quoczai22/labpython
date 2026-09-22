import math

class Triangle:
    def __init__(self):
        self.a=0
        self.b=0
        self.c=0

    def inputInfo(self):
        self.a=float(input("Hay nhap canh a: "))
        self.b=float(input("Hay nhap canh b: "))
        self.c=float(input("Hay nhap canh c: "))
        if not self.is_valid():
            print("Ba canh khong tao thanh tam giac")
            return False
        return True

    def is_valid(self):
        return (self.a>0 and self.b>0 and self.c>0 and
                self.a+self.b>self.c and
                self.a+self.c>self.b and
                self.b+self.c>self.a)

    def perimeter(self):
        return self.a+self.b+self.c

    def area(self):
        p=self.perimeter()/2
        return math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))

    def triangle_type(self):
        a, b, c = sorted([self.a, self.b, self.c])
        is_vuong = math.isclose(a**2 + b**2, c**2, rel_tol=1e-5)
        if self.a==self.b==self.c:
            return "Tam giac deu"
        elif self.a==self.b or self.b==self.c or self.a==self.c:
            if is_vuong:
                return "Tam giac vuong can"
            return "Tam giac can"
        elif is_vuong:
            return "Tam giac vuong"
        return "Tam giac thuong"

    def display(self):
        print(f"Canh a: {self.a}, Canh b: {self.b}, Canh c: {self.c}, Loai tam giac: {self.triangle_type()}, Chu vi: {self.perimeter()}, Dien tich: {self.area()}")

def main():
    tg=Triangle()
    if tg.inputInfo():
        tg.display()

if __name__=="__main__":
    main()
