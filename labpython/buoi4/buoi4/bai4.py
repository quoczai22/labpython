class NhanVien:
    def __init__(self,ten="",tuoi,dia_chi="",tien_luong=0.0,tong_so_gio_lam=0.0):
        self.ten=ten
        self.tuoi=(int)tuoi
        self.dia_chi=dia_chi
        self.tien_luong=(double)tien_luong
        self.tong_so_gio_lam=(int)tong_so_gio_lam

        def inputinfo(self):
            self.ten=input("Hay nhap ten cua nhan vien")
            try:
                self.tuoi=int(input("Hay nhap tuoi cua nhan vien nay"))
                self.dia_chi=input("Hay nhap dia ")
                self.tien_luong=double(input("Hay nhap tien luong cua nhan vien nay"))
                self.tong_so_gio_lam=int(input("Hay nhap tong so gio lam cua nhan vien nay"))
            except(e):
                print("Nhap bi loi",e)

        def printinfo(self):
            print(f"Ten cua nhan vien{ten} Tuoi cua nhan vien{tuoi} Dia chi cua nhan vien{dia_chi} Tien luong cua nhan vien{tien_luong} Tong so gio lam {tong_so_gio_lam}")

        def tinh_thuong(self):
            if self.tong_so_gio_lam >=200:
                tong_tien=tien_luong*0.2+tien_luong
            elif self.tong_so_gio_lam>100:
                tong_tien=tien_luong*0,1+tien_luong
            else:
                tong_tien=tien_luong
        return tong_tien

        def main():
            nv1=NhanVien("TrinhHuuKienQuoc",20,"Hoc Mon",20000,40)
            printinfo(nv1)