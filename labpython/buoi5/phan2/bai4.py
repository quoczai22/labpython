class IntegerList:
    def __init__(self):
        self.numbers=[]

    def add_number(self, number):
        self.numbers.append(number)
        print("Da them so vao danh sach")

    def remove_number(self, number):
        if number in self.numbers:
            self.numbers.remove(number)
            print("Da xoa so khoi danh sach")
        else:
            print("So khong ton tai trong danh sach")

    def search_number(self, number):
        if number in self.numbers:
            print(f"So {number} co trong danh sach")
        else:
            print(f"So {number} khong co trong danh sach")

    def sum_numbers(self):
        return sum(self.numbers)

    def maximum(self):
        if not self.numbers:
            print("Danh sach rong")
            return None
        return max(self.numbers)

    def minimum(self):
        if not self.numbers:
            print("Danh sach rong")
            return None
        return min(self.numbers)

    def input(self):
        n=int(input("Hay nhap so luong phan tu: "))
        for i in range(n):
            x=int(input(f"Hay nhap so thu {i+1}: "))
            self.add_number(x)

    def display(self):
        if not self.numbers:
            print("Danh sach rong")
        else:
            print(f"Danh sach so nguyen: {self.numbers}")

def main():
    ds=IntegerList()
    ds.input()
    ds.display()

    print("Tong cac so trong danh sach la: ", ds.sum_numbers())
    print("So lon nhat la: ", ds.maximum())
    print("So nho nhat la: ", ds.minimum())

    so_tim=int(input("Hay nhap so can tim: "))
    ds.search_number(so_tim)

    so_xoa=int(input("Hay nhap so can xoa: "))
    ds.remove_number(so_xoa)
    ds.display()

if __name__=="__main__":
    main()
