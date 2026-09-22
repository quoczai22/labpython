import math

class Point:
    def __init__(self, x=0, y=0):
        self.__x=x
        self.__y=y

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x=x

    def get_y(self):
        return self.__y

    def set_y(self, y):
        self.__y=y

    def input(self):
        x=float(input("Hay nhap hoanh do x: "))
        self.set_x(x)
        y=float(input("Hay nhap tung do y: "))
        self.set_y(y)

    def display(self):
        print(f"Toa do diem: ({self.get_x()}, {self.get_y()})")

    def distance_to_origin(self):
        return math.sqrt(self.__x**2 + self.__y**2)

    def distance_to(self, other):
        return math.sqrt((self.__x - other.get_x())**2 + (self.__y - other.get_y())**2)

def main():
    p1=Point()
    p1.input()
    p1.display()

    p2=Point()
    p2.input()
    p2.display()

    print("Khoang cach tu p1 den goc toa do la: ", p1.distance_to_origin())
    print("Khoang cach tu p2 den goc toa do la: ", p2.distance_to_origin())
    print("Khoang cach giua p1 va p2 la: ", p1.distance_to(p2))

    p1.set_x(10)
    print("Hoanh do p1 sau khi set lai la: ", p1.get_x())

    try:
        print(p1.__x)
    except AttributeError:
        print("Khong the truy cap truc tiep thuoc tinh private __x")

if __name__=="__main__":
    main()
