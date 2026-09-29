class Rectangle:
    def __init__(self):
        self.length=0
        self.width=0
        
    def inputInfo(self):
        self.length=float(input("Hay nhap chieu dai: "))
        self.width=float(input("Hay nhap chieu rong: "))
        if self.length<=0 or self.width<=0:
            print("Chieu dai va chieu rong phai lon hon 0")
            return False
        return True
        
    def perimeter(self):
        return (self.length+self.width)*2
        
    def area(self):
        return self.length*self.width
        
    def is_square(self):
        if self.length==self.width:
            return "La hinh vuong"
        return "Khong phai hinh vuong"
        
    def display(self):
        print(f"Chieu dai: {self.length}, Chieu rong: {self.width}, Chu vi: {self.perimeter()}, Dien tich: {self.area()}, Ket luan: {self.is_square()}")

def main():
    hcn1=Rectangle()
    if hcn1.inputInfo():
        hcn1.display()

    hcn2=Rectangle()
    if hcn2.inputInfo():
        hcn2.display()

if __name__=="__main__":
    main()
