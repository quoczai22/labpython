class Date:
    def __init__(self):
        self.day=1
        self.month=1
        self.year=2000

    def is_leap_year(self):
        return (self.year%4==0 and self.year%100!=0) or (self.year%400==0)

    def days_in_month(self):
        if self.month in (1, 3, 5, 7, 8, 10, 12):
            return 31
        elif self.month in (4, 6, 9, 11):
            return 30
        elif self.month==2:
            if self.is_leap_year():
                return 29
            return 28
        return 0

    def is_valid_date(self):
        if self.year<1 or self.month<1 or self.month>12:
            return False
        return 1<=self.day<=self.days_in_month()

    def inputInfo(self):
        self.day=int(input("Hay nhap ngay: "))
        self.month=int(input("Hay nhap thang: "))
        self.year=int(input("Hay nhap nam: "))
        if not self.is_valid_date():
            print("Ngay khong hop le")
            return False
        return True

    def display(self):
        print(f"Ngay thang nam: {self.day:02d}/{self.month:02d}/{self.year:04d}")

def main():
    d=Date()
    if d.inputInfo():
        d.display()
        print("Nam nhuan: ", d.is_leap_year())
        print("So ngay trong thang: ", d.days_in_month())

if __name__=="__main__":
    main()
