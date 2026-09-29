class Clock:
    def __init__(self):
        self.hour=0
        self.minute=0
        self.second=0

    def is_valid(self):
        return (0<=self.hour<=23 and 0<=self.minute<=59 and 0<=self.second<=59)

    def input(self):
        while True:
            self.hour=int(input("Hay nhap gio: "))
            self.minute=int(input("Hay nhap phut: "))
            self.second=int(input("Hay nhap giay: "))
            if self.is_valid():
                break
            else:
                print("Thoi gian khong hop le, xin moi nhap lai!")

    def display(self):
        print(f"Thoi gian la: {self.hour:02d}:{self.minute:02d}:{self.second:02d}")

def main():
    clk=Clock()
    clk.input()
    clk.display()

if __name__=="__main__":
    main()
