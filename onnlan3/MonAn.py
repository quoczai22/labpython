from abc import ABC, abstractmethod
from datetime import datetime


# =================================================================
# 1. INTERFACE: ITroGia (Hỗ trợ chương trình trợ giá / khuyến mãi)
# =================================================================
class ITroGia(ABC):
    """Interface định nghĩa phương thức tính trợ giá/khuyến mãi cho món ăn."""
    @abstractmethod
    def tinhTroGia(self):
        """Trả về tổng số tiền trợ giá cho món ăn (VND)."""
        pass


# =================================================================
# 2. LỚP TRỪU TƯỢNG: MonAn (Abstract Class)
# =================================================================
class MonAn(ABC):
    # Biến static / class attribute: Thuế VAT áp dụng chung là 5%
    VAT = 0.05

    def __init__(self, ma_mon="TD0001", ten_mon="Cơm tấm sườn bì", ngay_che_bien=None, gia_ban=20000, so_phan=50):
        """
        Khởi tạo món ăn:
        - Mặc định: mã 'TD0001', tên 'Cơm tấm sườn bì', ngày hiện tại, giá 20000, số phần 50.
        - Khởi tạo đầy đủ tham số khi truyền vào giá trị cụ thể.
        """
        self._ma_mon = ""
        self._ten_mon = ten_mon
        self._ngay_che_bien = ngay_che_bien if ngay_che_bien is not None else datetime.now()
        self._gia_ban = 0
        self._so_phan = max(0, so_phan)

        # Sử dụng setter để áp dụng ràng buộc dữ liệu
        self.ma_mon = ma_mon
        self.gia_ban = gia_ban

    # ----------------- PROPERTIES (GETTER & SETTER) -----------------
    @property
    def ma_mon(self):
        return self._ma_mon

    @ma_mon.setter
    def ma_mon(self, value):
        # Yêu cầu: Bắt buộc dài 6 ký tự, bắt đầu bằng "TD", 4 ký tự còn lại là chữ số
        val_str = str(value).strip().upper()
        if len(val_str) == 6 and val_str.startswith("TD") and val_str[2:].isdigit():
            self._ma_mon = val_str
            return True
        else:
            print(f"[Lỗi] Mã món '{value}' không hợp lệ! Mã phải có 6 ký tự, bắt đầu bằng 'TD' và 4 chữ số (VD: TD0001).")
            # Gán giá trị hợp lệ mặc định nếu bị sai
            if not self._ma_mon:
                self._ma_mon = "TD0001"
            return False

    @property
    def gia_ban(self):
        return self._gia_ban

    @gia_ban.setter
    def gia_ban(self, value):
        # Yêu cầu: Giá bán phải là số dương (> 0)
        try:
            val_num = float(value)
            if val_num > 0:
                self._gia_ban = val_num
                return True
            else:
                print(f"[Lỗi] Giá bán {value} không hợp lệ! Giá bán phải là số dương (> 0).")
                if self._gia_ban <= 0:
                    self._gia_ban = 20000
                return False
        except (ValueError, TypeError):
            print(f"[Lỗi] Giá bán '{value}' phải là số hợp lệ!")
            return False

    @property
    def ten_mon(self):
        return self._ten_mon

    @ten_mon.setter
    def ten_mon(self, value):
        if str(value).strip():
            self._ten_mon = str(value).strip()
            return True
        print("[Lỗi] Tên món không được để trống!")
        return False

    @property
    def so_phan(self):
        return self._so_phan

    @so_phan.setter
    def so_phan(self, value):
        try:
            val_int = int(value)
            if val_int >= 0:
                self._so_phan = val_int
                return True
            print("[Lỗi] Số phần phải >= 0!")
            return False
        except ValueError:
            print("[Lỗi] Số phần phải là số nguyên!")
            return False

    @property
    def ngay_che_bien(self):
        return self._ngay_che_bien

    @ngay_che_bien.setter
    def ngay_che_bien(self, value):
        if isinstance(value, datetime):
            self._ngay_che_bien = value
        elif isinstance(value, str):
            for fmt in ("%d/%m/%Y", "%Y-%m-%d", "%d-%m-%Y"):
                try:
                    self._ngay_che_bien = datetime.strptime(value.strip(), fmt)
                    return True
                except ValueError:
                    pass
            print("[Lỗi] Định dạng ngày không hợp lệ! Dùng định dạng dd/mm/yyyy.")
            return False
        return True

    # Getter / Setter kiểu hàm truyền thống theo phong cách cũ
    def get_ma_mon(self):
        return self._ma_mon

    def set_ma_mon(self, ma):
        self.ma_mon = ma

    def get_gia_ban(self):
        return self._gia_ban

    def set_gia_ban(self, gia):
        self.gia_ban = gia

    # ----------------- PHƯƠNG THỨC XỬ LÝ NGHIỆP VỤ -----------------
    def GiamGia(self):
        """
        Giảm giá:
        - Số phần > 100: giảm 10%
        - Số phần > 50: giảm 5%
        - Còn lại: không giảm
        """
        tong_tien_goc = self._so_phan * self._gia_ban
        if self._so_phan > 100:
            return tong_tien_goc * 0.10
        elif self._so_phan > 50:
            return tong_tien_goc * 0.05
        return 0.0

    @abstractmethod
    def PhuThu(self):
        """Phương thức trừu tượng: tính tiền phụ thu theo từng loại món ăn."""
        pass

    def ThanhTien(self):
        """Thành tiền = số phần * giá bán - Giảm giá + phụ thu"""
        return (self._so_phan * self._gia_ban) - self.GiamGia() + self.PhuThu()

    def tinhThueVAT(self):
        """Thuế VAT = Thành tiền * VAT (5%)"""
        return self.ThanhTien() * MonAn.VAT

    def tinhChietKhau(self):
        """Phương thức chiết khấu / trợ giá (mặc định kiểm tra qua interface ITroGia)."""
        if isinstance(self, ITroGia):
            return self.tinhTroGia()
        return 0.0

    # ----------------- NHẬP / XUẤT THÔNG TIN -----------------
    def nhap(self):
        """Nhập thông tin cơ bản của món ăn từ bàn phím."""
        while True:
            ma = input("Nhập mã món ăn (bắt đầu 'TD' + 4 chữ số, VD: TD0001): ").strip()
            if self.ma_mon_setter_check(ma):
                self._ma_mon = ma.upper()
                break

        while True:
            ten = input("Nhập tên món ăn: ").strip()
            if ten:
                self._ten_mon = ten
                break
            print("Tên món không được để trống!")

        while True:
            ngay_str = input("Nhập ngày chế biến (dd/mm/yyyy, bấm Enter để lấy ngày hiện tại): ").strip()
            if not ngay_str:
                self._ngay_che_bien = datetime.now()
                break
            try:
                self._ngay_che_bien = datetime.strptime(ngay_str, "%d/%m/%Y")
                break
            except ValueError:
                print("Ngày không hợp lệ! Vui lòng nhập đúng định dạng dd/mm/yyyy.")

        while True:
            try:
                gia = float(input("Nhập đơn giá bán (> 0): "))
                if gia > 0:
                    self._gia_ban = gia
                    break
                print("Giá bán phải lớn hơn 0!")
            except ValueError:
                print("Giá bán phải là số hợp lệ!")

        while True:
            try:
                sp = int(input("Nhập số phần (>= 0): "))
                if sp >= 0:
                    self._so_phan = sp
                    break
                print("Số phần phải lớn hơn hoặc bằng 0!")
            except ValueError:
                print("Số phần phải là số nguyên!")

    def ma_mon_setter_check(self, val_str):
        val_str = str(val_str).strip().upper()
        if len(val_str) == 6 and val_str.startswith("TD") and val_str[2:].isdigit():
            return True
        print("Mã món không hợp lệ! Bắt buộc 6 ký tự, bắt đầu 'TD' kèm 4 chữ số.")
        return False

    def Xuat(self):
        """Xuất thông tin món ăn (virtual method)."""
        ngay_str = self._ngay_che_bien.strftime("%d/%m/%Y") if self._ngay_che_bien else ""
        tro_gia = self.tinhChietKhau()
        tro_gia_str = f", Trợ giá: -{tro_gia:,.0f} VND" if tro_gia > 0 else ""
        print(f"Mã món: {self._ma_mon} | Tên: {self._ten_mon} | Ngày CB: {ngay_str} | "
              f"Đơn giá: {self._gia_ban:,.0f} VND | Số phần: {self._so_phan} | "
              f"Giảm giá: {self.GiamGia():,.0f} VND | Phụ thu: {self.PhuThu():,.0f} VND | "
              f"Thành tiền: {self.ThanhTien():,.0f} VND | Thuế VAT (5%): {self.tinhThueVAT():,.0f} VND{tro_gia_str}")


# =================================================================
# 3. CÁC LỚP CON (KẾ THỪA VÀ CÀI ĐẶT ĐA HÌNH)
# =================================================================

# ----------------- Lớp 1: Gà Rán -----------------
class GaRan(MonAn):
    def __init__(self, ma_mon="TD0001", ten_mon="Gà rán giòn", ngay_che_bien=None,
                 gia_ban=35000, so_phan=1, cay=False, phan="cánh"):
        super().__init__(ma_mon, ten_mon, ngay_che_bien, gia_ban, so_phan)
        self.cay = cay          # True (có cay) / False (không cay)
        self.phan = phan        # "cánh" hoặc "đùi"

    def PhuThu(self):
        """
        - Gà rán phần cánh cay: phụ thu thêm 1000/phần.
        - Gà rán phần đùi cay: phụ thu thêm 500/phần.
        - Không cay hoặc phần khác: phụ thu 0.
        """
        if self.cay:
            phan_chuan = self.phan.strip().lower()
            if phan_chuan in ["cánh", "canh"]:
                return 1000 * self._so_phan
            elif phan_chuan in ["đùi", "dui"]:
                return 500 * self._so_phan
        return 0.0

    def nhap(self):
        super().nhap()
        # Nhập thuộc tính cay
        while True:
            c = input("Có cay không? (1: Có / 0: Không): ").strip()
            if c in ["1", "co", "có", "true", "y"]:
                self.cay = True
                break
            elif c in ["0", "khong", "không", "false", "n"]:
                self.cay = False
                break
            print("Vui lòng chọn 1 (Có) hoặc 0 (Không)!")

        # Nhập phần (đùi / cánh)
        while True:
            p = input("Chọn phần gà (1: Cánh / 2: Đùi): ").strip().lower()
            if p in ["1", "canh", "cánh"]:
                self.phan = "cánh"
                break
            elif p in ["2", "dui", "đùi"]:
                self.phan = "đùi"
                break
            print("Vui lòng chọn 1 (Cánh) hoặc 2 (Đùi)!")

    def Xuat(self):
        cay_str = "Có cay" if self.cay else "Không cay"
        print(f"[GÀ RÁN] ", end="")
        super().Xuat()
        print(f"       -> Chi tiết: Phần: {self.phan.capitalize()} | Vị: {cay_str}")


# ----------------- Lớp 2: Cơm Sườn (Kế thừa MonAn & ITroGia) -----------------
class ComSuon(MonAn, ITroGia):
    def __init__(self, ma_mon="TD0001", ten_mon="Cơm tấm sườn bì", ngay_che_bien=None,
                 gia_ban=20000, so_phan=50, mon_an_them="bì"):
        super().__init__(ma_mon, ten_mon, ngay_che_bien, gia_ban, so_phan)
        self.mon_an_them = mon_an_them   # "bì", "trứng", "chả", hoặc "không"

    def PhuThu(self):
        """
        Phụ thu:
        - Bì: 2000 đồng/phần
        - Trứng: 5000 đồng/phần
        - Chả: 5500 đồng/phần
        """
        mon_them = self.mon_an_them.strip().lower()
        if mon_them in ["bì", "bi"]:
            return 2000 * self._so_phan
        elif mon_them in ["trứng", "trung"]:
            return 5000 * self._so_phan
        elif mon_them in ["chả", "cha"]:
            return 5500 * self._so_phan
        return 0.0

    def tinhTroGia(self):
        """Khuyến mãi: Cơm sườn được trợ giá 1000 đồng/phần đối với tất cả món cơm sườn."""
        return 1000 * self._so_phan

    def tinhChietKhau(self):
        return self.tinhTroGia()

    def nhap(self):
        super().nhap()
        while True:
            print("Chọn món ăn thêm: 1: Bì (+2,000đ) | 2: Trứng (+5,000đ) | 3: Chả (+5,500đ) | 0: Không thêm")
            chon = input("Lựa chọn (0-3): ").strip()
            if chon == "1":
                self.mon_an_them = "bì"
                break
            elif chon == "2":
                self.mon_an_them = "trứng"
                break
            elif chon == "3":
                self.mon_an_them = "chả"
                break
            elif chon == "0":
                self.mon_an_them = "không"
                break
            print("Lựa chọn không hợp lệ, vui lòng chọn lại!")

    def Xuat(self):
        print(f"[CƠM SƯỜN] ", end="")
        super().Xuat()
        print(f"         -> Món thêm: {self.mon_an_them.capitalize()} | Trợ giá khuyến mãi: {self.tinhTroGia():,.0f} VND")


# ----------------- Lớp 3: Mì Cay (Kế thừa MonAn & ITroGia) -----------------
class MiCay(MonAn, ITroGia):
    def __init__(self, ma_mon="TD0001", ten_mon="Mì cay hải sản", ngay_che_bien=None,
                 gia_ban=45000, so_phan=1, cap_do=2):
        super().__init__(ma_mon, ten_mon, ngay_che_bien, gia_ban, so_phan)
        self.cap_do = cap_do if 0 <= cap_do <= 5 else 0

    def PhuThu(self):
        """
        Phụ thu cấp độ mì cay:
        - Cấp độ 1: 2000 đồng/phần
        - Cấp độ 2: 2500 đồng/phần
        - Cấp độ 3, 4: 4000 đồng/phần
        - Cấp độ 0, 5: 0 đồng
        """
        if self.cap_do == 1:
            return 2000 * self._so_phan
        elif self.cap_do == 2:
            return 2500 * self._so_phan
        elif self.cap_do in [3, 4]:
            return 4000 * self._so_phan
        return 0.0

    def tinhTroGia(self):
        """Khuyến mãi: Mì cay tất cả các cấp độ đều được trợ giá 1500 đồng/phần."""
        return 1500 * self._so_phan

    def tinhChietKhau(self):
        return self.tinhTroGia()

    def nhap(self):
        super().nhap()
        while True:
            try:
                cd = int(input("Nhập cấp độ mì cay (từ 0 đến 5): "))
                if 0 <= cd <= 5:
                    self.cap_do = cd
                    break
                print("Cấp độ mì cay chỉ từ 0 đến 5!")
            except ValueError:
                print("Cấp độ phải là số nguyên!")

    def Xuat(self):
        print(f"[MÌ CAY] ", end="")
        super().Xuat()
        print(f"       -> Cấp độ cay: Cấp {self.cap_do} | Trợ giá khuyến mãi: {self.tinhTroGia():,.0f} VND")


# =================================================================
# 4. CHƯƠNG TRÌNH CHÍNH (main - MINH HỌA VÀ ĐA HÌNH)
# =================================================================
def main():
    print("========================================================================")
    print("     CHƯƠNG TRÌNH QUẢN LÝ MÓN ĂN CỬA HÀNG THỨC ĂN NHANH (MÃ ĐỀ: 03)")
    print("========================================================================")

    # 1. Minh họa khởi tạo mặc định theo Yêu cầu 3a
    print("\n--- 1. Kiểm tra khởi tạo mặc định (Default Constructor) ---")
    mon_mac_dinh = ComSuon()
    mon_mac_dinh.Xuat()

    # 2. Khởi tạo danh sách các món ăn cụ thể để minh họa đa hình
    ds_mon_an = [
        # Gà rán cánh cay (phụ thu 1000/phần)
        GaRan(ma_mon="TD0002", ten_mon="Gà rán sốt cay", gia_ban=35000, so_phan=60, cay=True, phan="cánh"),
        # Gà rán đùi không cay (phụ thu 0)
        GaRan(ma_mon="TD0003", ten_mon="Gà rán truyền thống", gia_ban=32000, so_phan=30, cay=False, phan="đùi"),
        # Cơm sườn chả (phụ thu 5500/phần, trợ giá 1000/phần, > 100 phần được giảm 10%)
        ComSuon(ma_mon="TD0004", ten_mon="Cơm sườn chả trứng", gia_ban=45000, so_phan=120, mon_an_them="chả"),
        # Cơm sườn bì (phụ thu 2000/phần, trợ giá 1000/phần)
        ComSuon(ma_mon="TD0005", ten_mon="Cơm sườn bì chả", gia_ban=40000, so_phan=40, mon_an_them="bì"),
        # Mì cay cấp độ 3 (phụ thu 4000/phần, trợ giá 1500/phần, > 50 phần được giảm 5%)
        MiCay(ma_mon="TD0006", ten_mon="Mì cay kim chi bò", gia_ban=50000, so_phan=80, cap_do=3),
        # Mì cay cấp độ 1 (phụ thu 2000/phần, trợ giá 1500/phần)
        MiCay(ma_mon="TD0007", ten_mon="Mì cay hải sản", gia_ban=48000, so_phan=20, cap_do=1),
    ]

    print("\n======================= DANH SÁCH MÓN ĂN HIỆN CÓ =======================")
    # Duyệt danh sách thể hiện tính Đa hình (Polymorphism)
    for i, mon in enumerate(ds_mon_an, start=1):
        print(f"\n[{i}]", end=" ")
        mon.Xuat()

    # Tính toán tổng hợp
    tong_thanh_tien = sum(mon.ThanhTien() for mon in ds_mon_an)
    tong_vat = sum(mon.tinhThueVAT() for mon in ds_mon_an)
    tong_tro_gia = sum(mon.tinhChietKhau() for mon in ds_mon_an)
    tong_doanh_thu_thuc = (tong_thanh_tien + tong_vat) - tong_tro_gia

    print("\n========================== THỐNG KÊ DOANH THU ==========================")
    print(f"-> Tổng Thành tiền (chưa VAT, chưa trừ trợ giá) : {tong_thanh_tien:>15,.0f} VND")
    print(f"-> Tổng Thuế VAT (5%)                            : {tong_vat:>15,.0f} VND")
    print(f"-> Tổng Trợ giá khuyến mãi (Interface ITroGia)  : {tong_tro_gia:>15,.0f} VND")
    print(f"------------------------------------------------------------------------")
    print(f"=> TỔNG TIỀN THANH TOÁN THỰC TẾ               : {tong_doanh_thu_thuc:>15,.0f} VND")
    print("========================================================================")

    # Tìm món ăn có thành tiền lớn nhất
    mon_max = max(ds_mon_an, key=lambda m: m.ThanhTien())
    print(f"\n=> Món ăn có Thành tiền cao nhất: {mon_max.ten_mon} ({mon_max.ma_mon}) với {mon_max.ThanhTien():,.0f} VND")

    # Kiểm tra các món thuộc chương trình trợ giá (sử dụng Interface ITroGia)
    print("\n--- DANH SÁCH MÓN HƯỞNG TRỢ GIÁ (IMPLEMENT ITroGia) ---")
    for mon in ds_mon_an:
        if isinstance(mon, ITroGia):
            print(f"- {mon.ten_mon} ({mon.ma_mon}): Trợ giá {mon.tinhTroGia():,.0f} VND")


if __name__ == "__main__":
    main()
