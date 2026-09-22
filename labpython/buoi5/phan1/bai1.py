import math

class Circle:
    def __init__(self):
        self.radius=0
        
    def inputInfo(self):
        self.radius=float(input("Hay nhap ban kinh hinh tron: "))
        if self.radius<=0:
            print("Ban kinh phai lon hon 0")
            return False
        return True
        
    def perimeter(self):
        return 2*math.pi*self.radius
        
    def area(self):
        return math.pi*(self.radius**2)
        
    def display(self):
        print(f"Ban kinh la: {self.radius}, Chu vi la: {self.perimeter()}, Dien tich la: {self.area()}")

def main():
    c1=Circle()
    if c1.inputInfo():
        c1.display()

if __name__=="__main__":
    main()
