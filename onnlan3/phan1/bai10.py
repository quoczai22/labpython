import math

class Point2D:
    def __init__(self, x=0.0, y=0.0):
        self.x=x
        self.y=y

    def inputInfo(self):
        while True:
            try:
                self.x=float(input("Hay nhap hoanh do x: "))
                self.y=float(input("Hay nhap tung do y: "))
                break
            except ValueError:
                print("Toa do phai la so hop le!")

    def distance_to(self, other):
        return math.sqrt((self.x-other.x)**2+(self.y-other.y)**2)

    def display(self):
        print(f"({self.x}, {self.y})")


def main():
    print("--- NHAP DIEM THU NHAT (p1) ---")
    p1=Point2D()
    p1.inputInfo()

    print("\n--- NHAP DIEM THU HAI (p2) ---")
    p2=Point2D()
    p2.inputInfo()

    print("\nToa do diem p1: ", end="")
    p1.display()
    print("Toa do diem p2: ", end="")
    p2.display()

    kc=p1.distance_to(p2)
    print(f"=> Khoang cach giua p1 va p2: {kc:.4f}")


if __name__=="__main__":
    main()
