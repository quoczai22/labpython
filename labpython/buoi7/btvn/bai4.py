import datetime


class GiaoDich:
    def __init__(self, ma="", ngay_gd=None, don_gia=0.0, so_luong=0):
        self.__ma = ma
        self.__ngay_gd = ngay_gd if ngay_gd is not None else datetime.date.today()
        self.__don_gia = don_gia
        self.__so_luong = so_luong

    def get_ma(self):
        return self.__ma

    def set_ma(self, ma):
        ma = str(ma).strip()
        if ma == "":
            print("Loi: Ma giao dich khong duoc de trong!")
            return False
        self.__ma = ma
        return True

    def get_ngay_gd(self):
        return self.__ngay_gd

    def set_ngay_gd(self, ngay):
        # Chap nhan datetime.date hoac chuoi dd/mm/yyyy
        if isinstance(ngay, str):
            try:
                ngay = datetime.datetime.strptime(ngay.strip(), "%d/%m/%Y").date()
            except ValueError:
                print("Loi: Dinh dang ngay khong hop le (can nhap theo dd/mm/yyyy)!")
                return False

        if isinstance(ngay, datetime.date):
            if ngay > datetime.date.today():
                print("Loi: Ngay khong duoc lon hon ngay hom nay!")
                return False
            self.__ngay_gd = ngay
            return True
        else:
            print("Loi: Kieu ngay thang khong hop le!")
            return False

    def get_don_gia(self):
        return self.__don_gia

    def set_don_gia(self, don_gia):
        try:
            don_gia = float(don_gia)
            if don_gia < 0:
                print("Loi: Don gia khong duoc nho hon 0!")
                return False
            self.__don_gia = don_gia
            return True
        except ValueError:
            print("Loi: Don gia phai la so!")
            return False

    def get_so_luong(self):
        return self.__so_luong

    def set_so_luong(self, so_luong):
        try:
            so_luong = int(so_luong)
            if so_luong <= 0:
                print("Loi: So luong phai lon hon 0!")
                return False
            self.__so_luong = so_luong
            return True
        except ValueError:
            print("Loi: So luong phai la so nguyen hop le!")
            return False

    def thanh_tien(self):
        return self.__so_luong * self.__don_gia

    def get_ngay_gd_str(self):
        if isinstance(self.__ngay_gd, datetime.date):
            return self.__ngay_gd.strftime("%d/%m/%Y")
        return str(self.__ngay_gd)

    def xuat(self):
        print(f"{self.get_ma()} - {self.get_ngay_gd_str()} - So luong: {self.get_so_luong()} - Don gia: {self.get_don_gia():.0f} - Thanh tien: {self.thanh_tien():.0f}")


class GiaoDichVang(GiaoDich):
    LOAI_VANG_HOP_LE = ["18k", "24k", "9999"]

    def __init__(self, ma="", ngay_gd=None, don_gia=0.0, so_luong=0, loai_vang=""):
        super().__init__(ma, ngay_gd, don_gia, so_luong)
        self.__loai_vang = loai_vang

    def get_loai_vang(self):
        return self.__loai_vang

    def set_loai_vang(self, loai_vang):
        loai_vang = str(loai_vang).strip().lower()
        if loai_vang not in [v.lower() for v in self.LOAI_VANG_HOP_LE]:
            print(f"Loi: Loai vang khong hop le! Chi chap nhan: {', '.join(self.LOAI_VANG_HOP_LE)}")
            return False
        self.__loai_vang = loai_vang
        return True

    def thanh_tien(self):
        # Thanh tien = so luong * don gia
        return self.get_so_luong() * self.get_don_gia()

    def xuat(self):
        # Format theo mau de bai: gd001 - 13/03/2017 - 18k - 10 - 2350000 - Thành tiền = 23500000
        print(f"{self.get_ma()} - {self.get_ngay_gd_str()} - {self.get_loai_vang()} - {self.get_so_luong()} - {self.get_don_gia():.0f} - Thành tiền = {self.thanh_tien():.0f}")


class GiaoDichTienTe(GiaoDich):
    LOAI_TIEN_HOP_LE = ["USD", "EUR", "AUD"]

    def __init__(self, ma="", ngay_gd=None, don_gia=0.0, so_luong=0, loai_tien_te="", loai_gd="mua"):
        super().__init__(ma, ngay_gd, don_gia, so_luong)
        self.__loai_tien_te = loai_tien_te
        self.__loai_gd = loai_gd  # "mua" hoac "ban"

    def get_loai_tien_te(self):
        return self.__loai_tien_te

    def set_loai_tien_te(self, loai_tien_te):
        loai_tien_te = str(loai_tien_te).strip().upper()
        if loai_tien_te not in self.LOAI_TIEN_HOP_LE:
            print(f"Loi: Loai tien te khong hop le! Chi chap nhan: {', '.join(self.LOAI_TIEN_HOP_LE)}")
            return False
        self.__loai_tien_te = loai_tien_te
        return True

    def get_loai_gd(self):
        return self.__loai_gd

    def set_loai_gd(self, loai_gd):
        loai_gd = str(loai_gd).strip().lower()
        if loai_gd in ["1", "mua"]:
            self.__loai_gd = "mua"
            return True
        elif loai_gd in ["0", "ban", "bán"]:
            self.__loai_gd = "bán"
            return True
        else:
            print("Loi: Loai giao dich chi chap nhan 1 (mua) hoac 0 (ban)!")
            return False

    def thanh_tien(self):
        # Mua: thanh tien = so luong * ty gia
        # Ban: thanh tien = (so luong * ty gia) * 1.05
        if self.__loai_gd == "mua":
            return self.get_so_luong() * self.get_don_gia()
        else:
            return (self.get_so_luong() * self.get_don_gia()) * 1.05

    def xuat(self):
        # Format theo mau de bai: GD mua: gd002 - 14/03/2017 - USD - 100 - 23000 - Thành tiền = 2300000
        print(f"GD {self.get_loai_gd()}: {self.get_ma()} - {self.get_ngay_gd_str()} - {self.get_loai_tien_te()} - {self.get_so_luong()} - {self.get_don_gia():.0f} - Thành tiền = {self.thanh_tien():.0f}")


class QuanLyGiaoDich:
    def __init__(self):
        self.danh_sach = []

    def them_giao_dich(self, gd):
        self.danh_sach.append(gd)

    def xuat_danh_sach(self):
        if not self.danh_sach:
            print("\nDanh sach giao dich dang trong!")
            return

        print("\n" + "=" * 70)
        print("DANH SACH TAT CA GIAO DICH")
        print("=" * 70)
        for i, gd in enumerate(self.danh_sach, start=1):
            print(f"[{i}] ", end="")
            gd.xuat()
        print("=" * 70)

    def tong_so_luong_vang(self):
        return sum(gd.get_so_luong() for gd in self.danh_sach if isinstance(gd, GiaoDichVang))

    def tong_so_luong_tien_te(self):
        return sum(gd.get_so_luong() for gd in self.danh_sach if isinstance(gd, GiaoDichTienTe))

    def tong_thanh_tien_vang(self):
        return sum(gd.thanh_tien() for gd in self.danh_sach if isinstance(gd, GiaoDichVang))

    def tong_thanh_tien_tien_te(self):
        return sum(gd.thanh_tien() for gd in self.danh_sach if isinstance(gd, GiaoDichTienTe))

    def thong_ke(self):
        print("\n" + "=" * 50)
        print("THONG KE GIAO DICH")
        print("=" * 50)
        print(f"- Tong so luong giao dich Vang:     {self.tong_so_luong_vang()}")
        print(f"- Tong so luong giao dich Tien te:  {self.tong_so_luong_tien_te()}")
        print(f"- Tong thanh tien giao dich Vang:    {self.tong_thanh_tien_vang():,.0f} VND")
        print(f"- Tong thanh tien giao dich Tien te: {self.tong_thanh_tien_tien_te():,.0f} VND")
        print("=" * 50)


def nhap_giao_dich(ql):
    print("Quản lý giao dịch:")
    while True:
        # 1. Nhap ma GD
        while True:
            ma = input("Nhập mã GD:      ").strip()
            if ma == "":
                print("Loi: Ma GD khong duoc rong!")
                continue
            break

        # 2. Nhap ngay GD
        while True:
            ngay_str = input("Nhập ngày GD:    ").strip()
            try:
                ngay_gd = datetime.datetime.strptime(ngay_str, "%d/%m/%Y").date()
                if ngay_gd > datetime.date.today():
                    print("Ngay khong duoc lon hon ngay hom nay!")
                    continue
                break
            except ValueError:
                print("Dinh dang ngay khong dung! Vui long nhap dd/mm/yyyy (vi du: 13/03/2017)")

        # 3. Nhap so luong
        while True:
            try:
                so_luong = int(input("Nhập số lượng:   ").strip())
                if so_luong <= 0:
                    print("So luong phai lon hon 0!")
                    continue
                break
            except ValueError:
                print("So luong phai la so nguyen hop le!")

        # 4. Chon loai giao dich
        while True:
            loai_gd_input = input("Chọn loại giao dịch: 1: Vàng, 2: Tiền Tệ:    ").strip()
            if loai_gd_input in ["1", "2"]:
                break
            print("Vui long chon 1 hoac 2!")

        # Xu ly theo loai giao dich
        if loai_gd_input == "1":
            gd = GiaoDichVang(ma=ma, ngay_gd=ngay_gd, so_luong=so_luong)
            # Nhap loai vang
            while True:
                loai_vang = input("Chọn loại: 18k / 24k / 9999:    ").strip()
                if gd.set_loai_vang(loai_vang):
                    break
            # Nhap don gia
            while True:
                don_gia_str = input("Nhập đơn giá:    ").strip()
                if gd.set_don_gia(don_gia_str):
                    break

            # In thong tin giao dich vua nhap
            gd.xuat()
            print(f"Tổng số lượng: {gd.get_so_luong()}")
            print(f"Tổng số tiền: {gd.thanh_tien():.0f}")
            ql.them_giao_dich(gd)

        else:
            gd = GiaoDichTienTe(ma=ma, ngay_gd=ngay_gd, so_luong=so_luong)
            # Nhap loai tien te
            while True:
                loai_tien = input("Chọn loại: USD / EUR / AUD:     ").strip()
                if gd.set_loai_tien_te(loai_tien):
                    break
            # Nhap ty gia
            while True:
                ty_gia_str = input("Nhập tỷ giá:     ").strip()
                if gd.set_don_gia(ty_gia_str):
                    break
            # Nhap mua hay ban
            while True:
                mua_ban = input("Bạn mua hay bán? 1: mua, 0: bán:    ").strip()
                if gd.set_loai_gd(mua_ban):
                    break

            # In thong tin giao dich vua nhap
            gd.xuat()
            print(f"Tổng số lượng: {gd.get_so_luong()}")
            print(f"Tổng số tiền: {gd.thanh_tien():.0f}")
            ql.them_giao_dich(gd)

        # Hoi tiep tuc
        tiep_tuc = input("Bạn muốn tiếp tục giao dịch? 1: Có, 0: Không    ").strip()
        if tiep_tuc != "1":
            break


def main():
    ql = QuanLyGiaoDich()
    nhap_giao_dich(ql)
    ql.xuat_danh_sach()
    ql.thong_ke()


if __name__ == "__main__":
    main()