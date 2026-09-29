import math

class QuadraticEquation:
    def __init__(self, a=1.0, b=0.0, c=0.0):
        if a==0:
            raise ValueError("He so 'a' phai khac 0 de tao thanh phuong trinh bac hai!")
        self.__a=float(a)
        self.__b=float(b)
        self.__c=float(c)

    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def get_c(self):
        return self.__c

    def get_discriminant(self):
        # Delta = b^2 - 4ac
        return (self.__b**2)-(4*self.__a*self.__c)

    def solve(self):
        delta=self.get_discriminant()
        if delta>0:
            x1=(-self.__b+math.sqrt(delta))/(2*self.__a)
            x2=(-self.__b-math.sqrt(delta))/(2*self.__a)
            return [x1, x2]
        elif delta==0:
            x0=-self.__b/(2*self.__a)
            return [x0]
        else:
            return [] # vo nghiem thuc

    def display(self):
        print(f"Phuong trinh: {self.__a}x² + ({self.__b})x + ({self.__c}) = 0")
        delta=self.get_discriminant()
        print(f"  Discriminant (Delta): {delta:.4f}")
        roots=self.solve()
        if len(roots)==2:
            print(f"  Phuong trinh co 2 nghiem phan biet: x1 = {roots[0]:.4f}, x2 = {roots[1]:.4f}")
        elif len(roots)==1:
            print(f"  Phuong trinh co nghiem kep: x0 = {roots[0]:.4f}")
        else:
            print("  Phuong trinh vo nghiem thuc.")


def main():
    print("--- TEST PHUONG TRINH CO 2 NGHIEM (x² - 5x + 6 = 0) ---")
    eq1=QuadraticEquation(1, -5, 6)
    eq1.display()

    print("\n--- TEST PHUONG TRINH CO NGHIEM KEP (x² - 4x + 4 = 0) ---")
    eq2=QuadraticEquation(1, -4, 4)
    eq2.display()

    print("\n--- TEST PHUONG TRINH VO NGHIEM (x² + 2x + 5 = 0) ---")
    eq3=QuadraticEquation(1, 2, 5)
    eq3.display()

    print("\n--- TEST RANG BUOC a != 0 ---")
    try:
        eq_error=QuadraticEquation(0, 2, 3)
    except ValueError as e:
        print("Bat duoc ngoai le thanh cong:", e)


if __name__=="__main__":
    main()
