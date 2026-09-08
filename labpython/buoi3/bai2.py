class Person:
    def __init__(self,hoten,ngaysinh):
        self.hoten=hoten
        self.ngaysinh=ngaysinh
    
    def hienthithongtin(self):
        print("Ho ten: ",self.hoten)
        print("Ho ten: ",self.ngaysinh)

def main():
    Quoc=Person("Trinh Huu Kien Quoc",17042006)
    Quoc.hienthithongtin()

if __name__=="__main__":
    main()
