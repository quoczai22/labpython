class Person:
    def __init__(self):
        self.full_name=""
        self.age=0

    def inputInfo(self):
        self.full_name=input("Hay nhap ho ten: ")
        self.age=int(input("Hay nhap tuoi: "))

    def display(self):
        print(f"Ho ten: {self.full_name}, Tuoi: {self.age}")

def main():
    p=Person()
    p.inputInfo()
    p.display()

    print("Kiem tra thuoc tinh address co chua: ", hasattr(p, "address"))

    setattr(p, "address", "TP.HCM")
    print("Address sau khi gan la: ", getattr(p, "address"))

    print("Cac thuoc tinh hien tai: ", p.__dict__)

    delattr(p, "address")
    print("Cac thuoc tinh sau khi xoa address: ", p.__dict__)

    print("Ten lop: ", p.__class__.__name__)
    print("Danh sach thuoc tinh va phuong thuc: ", dir(p))

if __name__=="__main__":
    main()
