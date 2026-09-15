class NhanVien:
    def __init__(self):
        self.ten=""
        self.tuoi=0
        self.dia_chi=""
        self.tien_luong=0
        self.tong_gio_lam=0

    def inputInfo(self):
        self.ten=input("Hay nhap ho va ten cua ban: ")
        self.tuoi=int(input("Hay nhap vao tuoi cua ban:"))
        self.dia_chi=input("Hay nhap dia chi cua ban: ")
        self.tien_luong=float(input("Hay nhap vao tien luong: "))
        self.tong_gio_lam=int(input("Hay nhap vao tong gio lam: "))

    def outputInfo(self):
        print(f"Ten la: {self.ten}, Tuoi la: {self.tuoi}, Dia chi là: {self.dia_chi}, Tien luong la: {self.tien_luong}, Tong gio lam la: {self.tong_gio_lam}, Tien thuong la: {self.tinhThuong()}")

    def tinhThuong(self):
        thuong = 0.0
        if self.tong_gio_lam >= 200:
            thuong = self.tien_luong * 0.2
        elif self.tong_gio_lam >= 100:
            thuong = self.tien_luong * 0.1
        else:
            thuong = 0.0
        return thuong

def main():
    nv1=NhanVien()
    nv1.inputInfo()
    nv1.outputInfo()

if __name__=="__main__":
    main()

