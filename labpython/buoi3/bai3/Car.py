class Car:
    def __init__(self, tenxe, mausac, loaixe, nguyenlieu):
        self.tenxe = tenxe
        self.mausac = mausac
        self.loaixe = loaixe
        self.nguyenlieu = nguyenlieu

    def showInfo(self):
        print("Ten xe la:", self.tenxe)
        print("Mau sac la:", self.mausac)
        print("Loai xe la:", self.loaixe)
        print("Nguyen lieu la:", self.nguyenlieu)

    def xeDien(self):
        self.loaixe = "Xe dien"
        self.nguyenlieu = "Dien"

    def xeXang(self):
        self.loaixe = "Xe xang"
        self.nguyenlieu = "Xang"

    def xeDau(self):
        self.loaixe = "Xe dau"
        self.nguyenlieu = "Dau"

def main():
    Toyota=Car("Toyota","xanh","","")
    Toyota.xeDau()
    Toyota.showInfo()
    print("Ten xe la: ",getattr(Toyota,"tenxe"))
    setattr(Toyota,"mausac","do")
    print("Mau xe la",getattr(Toyota,"mausac"))
    hasKey=hasattr(Toyota,"key")
    print("Co key: ",hasKey)
if __name__=="__main__":
    main()

