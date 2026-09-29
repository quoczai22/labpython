import math

class Hinh:
    def tinh_dien_tich(self):
        return 0

    def tinh_chu_vi(self):
        return 0

    def hien_thi(self):
        print(f"Hinh hoc - Dien tich: {self.tinh_dien_tich():.2f}, Chu vi: {self.tinh_chu_vi():.2f}")


class HinhChuNhat(Hinh):
    def __init__(self, chieu_dai=0.0, chieu_rong=0.0):
        self.chieu_dai=chieu_dai
        self.chieu_rong=chieu_rong

    def nhap(self):
        while True:
            try:
                dai=float(input("Hay nhap chieu dai: "))
                rong=float(input("Hay nhap chieu rong: "))
                if dai>0 and rong>0:
                    self.chieu_dai=dai
                    self.chieu_rong=rong
                    break
                print("Chieu dai va chieu rong phai lon hon 0!")
            except ValueError:
                print("Du lieu nhap vao phai la so hop le!")

    def tinh_dien_tich(self):
        return self.chieu_dai*self.chieu_rong

    def tinh_chu_vi(self):
        return (self.chieu_dai+self.chieu_rong)*2

    def hien_thi(self):
        print(f"[Hinh Chu Nhat] Dai: {self.chieu_dai}, Rong: {self.chieu_rong}, "
              f"Chu vi: {self.tinh_chu_vi():.2f}, Dien tich: {self.tinh_dien_tich():.2f}")


class HinhTron(Hinh):
    def __init__(self, ban_kinh=0.0):
        self.ban_kinh=ban_kinh

    def nhap(self):
        while True:
            try:
                r=float(input("Hay nhap ban kinh: "))
                if r>0:
                    self.ban_kinh=r
                    break
                print("Ban kinh phai lon hon 0!")
            except ValueError:
                print("Ban kinh phai la so hop le!")

    def tinh_dien_tich(self):
        return math.pi*(self.ban_kinh**2)

    def tinh_chu_vi(self):
        return 2*math.pi*self.ban_kinh

    def hien_thi(self):
        print(f"[Hinh Tron] Ban kinh: {self.ban_kinh}, "
              f"Chu vi: {self.tinh_chu_vi():.2f}, Dien tich: {self.tinh_dien_tich():.2f}")


class HinhTamGiac(Hinh):
    def __init__(self, a=0.0, b=0.0, c=0.0):
        self.a=a
        self.b=b
        self.c=c

    def kiem_tra_hop_le(self):
        return (self.a>0 and self.b>0 and self.c>0 and
                self.a+self.b>self.c and
                self.a+self.c>self.b and
                self.b+self.c>self.a)

    def nhap(self):
        while True:
            try:
                a=float(input("Hay nhap canh a: "))
                b=float(input("Hay nhap canh b: "))
                c=float(input("Hay nhap canh c: "))
                self.a, self.b, self.c = a, b, c
                if self.kiem_tra_hop_le():
                    break
                print("Ba canh phai lon hon 0 va tong 2 canh bat ky phai lon hon canh con lai!")
            except ValueError:
                print("Du lieu nhap vao phai la so hop le!")

    def tinh_chu_vi(self):
        if not self.kiem_tra_hop_le():
            return 0
        return self.a+self.b+self.c

    def tinh_dien_tich(self):
        if not self.kiem_tra_hop_le():
            return 0
        p=self.tinh_chu_vi()/2
        return math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))

    def hien_thi(self):
        print(f"[Hinh Tam Giac] Ba canh: ({self.a}, {self.b}, {self.c}), "
              f"Chu vi: {self.tinh_chu_vi():.2f}, Dien tich: {self.tinh_dien_tich():.2f}")


def main():
    # Tao danh sach gom nhieu loai hinh hoc khac nhau
    ds_hinh=[
        HinhChuNhat(5, 8),
        HinhTron(4),
        HinhTamGiac(3, 4, 5),
        HinhChuNhat(6, 6),
        HinhTron(5.5),
        HinhTamGiac(6, 8, 10)
    ]

    print("================ DANH SACH CAC HINH HOC ================")
    # Duyet danh sach va goi chung cac phuong thuc
    for hinh in ds_hinh:
        hinh.hien_thi()

    # Tim hinh co dien tich lon nhat
    hinh_max_dt=max(ds_hinh, key=lambda h: h.tinh_dien_tich())
    print("\n--- HINH CO DIEN TICH LON NHAT ---")
    hinh_max_dt.hien_thi()
    print(f"=> Dien tich lon nhat: {hinh_max_dt.tinh_dien_tich():.2f}")

    # Minh hoa tinh da hinh
    print("\n--- MINH HOA DA HINH: TINH CHU VI VA DIEN TICH ---")
    for h in ds_hinh:
        print(f"{type(h).__name__:<15} | Chu vi: {h.tinh_chu_vi():>8.2f} | Dien tich: {h.tinh_dien_tich():>8.2f}")


if __name__=="__main__":
    main()
