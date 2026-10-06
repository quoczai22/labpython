from abc import ABC, abstractmethod


# =================================================================
# 1. INTERFACE: IHoTroGia (Chính sách hỗ trợ giá giao hàng)
# =================================================================
class IHoTroGia(ABC):
    """
    Interface định nghĩa chính sách hỗ trợ giá cho hóa đơn vận chuyển.
    Áp dụng cho Hóa đơn giao thực phẩm và Hóa đơn giao hàng hóa.
    Đơn vị tính: Nghìn đồng.
    """
    @abstractmethod
    def tinhHoTroGia(self):
        """Trả về số tiền hỗ trợ giá (nghìn đồng)."""
        pass


# =================================================================
# 2. LỚP TRỪU TƯỢNG: HoaDonVanChuyen (Abstract Class)
# =================================================================
class HoaDonVanChuyen(ABC):
    # Thuộc tính static: Phí sử dụng ứng dụng áp dụng chung cho tất cả hóa đơn là 10 (nghìn đồng)
    PhiSDUD = 10.0

    def __init__(self, maHD="HD001", tenKH="Nguyễn Cửu Đàm", khoangCach=10.0, giaCuoc=5.0):
        """
        Khởi tạo hóa đơn vận chuyển:
        - Mặc định: mã "HD001", tên "Nguyễn Cửu Đàm", khoảng cách 10 km, giá cước 5 nghìn đồng.
        - Khởi tạo đầy đủ tham số khi truyền vào giá trị cụ thể.
        """
        self._maHD = ""
        self._tenKH = str(tenKH).strip() if tenKH else "Nguyễn Cửu Đàm"
        self._khoangCach = 10.0
        self._giaCuoc = 5.0

        # Áp dụng validation qua properties
        self.maHD = maHD
        self.khoangCach = khoangCach
        self.giaCuoc = giaCuoc

    # ----------------- PROPERTIES (GETTER & SETTER) -----------------
    @property
    def maHD(self):
        return self._maHD

    @maHD.setter
    def maHD(self, value):
        # Yêu cầu: Chiều dài 5 ký tự, bắt đầu bằng "HD", 3 ký tự còn lại là các chữ số
        val_str = str(value).strip().upper()
        if len(val_str) == 5 and val_str.startswith("HD") and val_str[2:].isdigit():
            self._maHD = val_str
            return True
        else:
            print(f"[Cảnh báo] Mã hóa đơn '{value}' không hợp lệ! Bắt buộc 5 ký tự: bắt đầu bằng 'HD' và 3 chữ số (VD: HD001).")
            if not self._maHD:
                self._maHD = "HD001"
            return False

    @property
    def khoangCach(self):
        return self._khoangCach

    @khoangCach.setter
    def khoangCach(self, value):
        # Yêu cầu: Khoảng cách phải > 0, ngược lại thông báo lỗi
        try:
            val_num = float(value)
            if val_num > 0:
                self._khoangCach = val_num
                return True
            else:
                print(f"[Lỗi] Khoảng cách {value} không hợp lệ! Khoảng cách phải lớn hơn 0 (> 0 km).")
                return False
        except (ValueError, TypeError):
            print(f"[Lỗi] Khoảng cách '{value}' phải là số hợp lệ!")
            return False

    @property
    def giaCuoc(self):
        return self._giaCuoc

    @giaCuoc.setter
    def giaCuoc(self, value):
        try:
            val_num = float(value)
            if val_num > 0:
                self._giaCuoc = val_num
                return True
            print(f"[Cảnh báo] Giá cước {value} phải lớn hơn 0!")
            return False
        except (ValueError, TypeError):
            print(f"[Cảnh báo] Giá cước '{value}' phải là số hợp lệ!")
            return False

    @property
    def tenKH(self):
        return self._tenKH

    @tenKH.setter
    def tenKH(self, value):
        if str(value).strip():
            self._tenKH = str(value).strip()

    # ----------------- PHƯƠNG THỨC NGHIỆP VỤ -----------------
    def PhiVanChuyen(self):
        """Phí vận chuyển = khoảng cách * giá cước."""
        return self._khoangCach * self._giaCuoc

    @abstractmethod
    def ChiPhi(self):
        """Phương thức trừu tượng: chi phí phát sinh của từng loại hóa đơn vận chuyển."""
        pass

    def ThanhTien(self):
        """Thành tiền = Phí vận chuyển + Phí sử dụng ứng dụng + Chi phí."""
        return self.PhiVanChuyen() + HoaDonVanChuyen.PhiSDUD + self.ChiPhi()

    # ----------------- NHẬP / XUẤT THÔNG TIN -----------------
    def nhap(self):
        """Nhập thông tin hóa đơn vận chuyển."""
        while True:
            ma = input("Nhập mã hóa đơn (dài 5 ký tự, bắt đầu 'HD' + 3 số, VD: HD001): ").strip().upper()
            if len(ma) == 5 and ma.startswith("HD") and ma[2:].isdigit():
                self._maHD = ma
                break
            print("Mã hóa đơn không hợp lệ! Vui lòng nhập lại.")

        while True:
            ten = input("Nhập tên khách hàng: ").strip()
            if ten:
                self._tenKH = ten
                break
            print("Tên khách hàng không được để trống!")

        while True:
            try:
                kc = float(input("Nhập khoảng cách di chuyển (km, > 0): "))
                if kc > 0:
                    self._khoangCach = kc
                    break
                print("Khoảng cách phải lớn hơn 0!")
            except ValueError:
                print("Khoảng cách phải là số thực hợp lệ!")

        while True:
            try:
                gc = float(input("Nhập giá cước (nghìn đồng/km, > 0): "))
                if gc > 0:
                    self._giaCuoc = gc
                    break
                print("Giá cước phải lớn hơn 0!")
            except ValueError:
                print("Giá cước phải là số hợp lệ!")

    def Xuat(self):
        """Phương thức xuất thông tin virtual."""
        ho_tro_str = ""
        if isinstance(self, IHoTroGia):
            ho_tro_str = f" | Hỗ trợ giá: -{self.tinhHoTroGia():.1f}k"

        print(f"Mã HD: {self._maHD} | KH: {self._tenKH:<16} | Cự ly: {self._khoangCach:>4.1f} km | "
              f"Giá cước: {self._giaCuoc:>4.1f}k/km | Phí VC: {self.PhiVanChuyen():>6.1f}k | "
              f"Phí SDUD: {HoaDonVanChuyen.PhiSDUD:>4.1f}k | Chi phí phát sinh: {self.ChiPhi():>6.1f}k | "
              f"Thành tiền: {self.ThanhTien():>6.1f}k VND{ho_tro_str}")


# =================================================================
# 3. CÁC LỚP CON (KẾ THỪA VÀ CÀI ĐẶT ĐA HÌNH)
# =================================================================

# ----------------- Lớp 1: Hóa Đơn Chở Người -----------------
class HoaDonChoNguoi(HoaDonVanChuyen):
    """
    Hóa đơn chở người:
    - Thuộc tính bổ sung: loại xe vận chuyển (scooter, xe máy, ô tô, ...).
    - Chi phí: Nếu loại xe là scooter thì Chi phí = 2 * khoảng cách, ngược lại không phát sinh (0).
    - Không có chính sách hỗ trợ giá.
    """
    def __init__(self, maHD="HD001", tenKH="Nguyễn Cửu Đàm", khoangCach=10.0, giaCuoc=5.0, loaiXe="scooter"):
        super().__init__(maHD, tenKH, khoangCach, giaCuoc)
        self.loaiXe = loaiXe

    @property
    def loaiXe(self):
        return self._loaiXe

    @loaiXe.setter
    def loaiXe(self, value):
        self._loaiXe = str(value).strip().lower() if value else "scooter"

    def ChiPhi(self):
        # Nếu loại xe là scooter: Chi phí = 2 * khoảng cách
        if "scooter" in self._loaiXe:
            return 2.0 * self._khoangCach
        return 0.0

    def nhap(self):
        super().nhap()
        lx = input("Nhập loại xe vận chuyển (scooter / xe máy / ô tô): ").strip()
        self.loaiXe = lx if lx else "scooter"

    def Xuat(self):
        print(f"[CHỞ NGƯỜI]   ", end="")
        super().Xuat()
        print(f"               -> Loại phương tiện: {self._loaiXe.title()}")


# ----------------- Lớp 2: Hóa Đơn Giao Thực Phẩm -----------------
class HoaDonGiaoThucPham(HoaDonVanChuyen, IHoTroGia):
    """
    Hóa đơn giao thực phẩm:
    - Thuộc tính:
      * loaiThucPham: nhận 1 trong 3 giá trị:
        "thực phẩm đông lạnh", "thực phẩm giữ nóng", "thực phẩm khô".
      * soLuong: số lượng hàng cần giao (nguyên dương).
    - Chi phí = số lượng * phí bảo quản:
      * "thực phẩm đông lạnh": 2 nghìn đồng
      * "thực phẩm giữ nóng": 3 nghìn đồng
      * "thực phẩm khô": 0 nghìn đồng (miễn phí)
    - Hỗ trợ giá (IHoTroGia):
      * Đông lạnh và số lượng > 5: hỗ trợ 5 nghìn đồng
      * Giữ nóng và số lượng > 5: hỗ trợ 10 nghìn đồng
      * Còn lại: 0
    """
    def __init__(self, maHD="HD001", tenKH="Nguyễn Cửu Đàm", khoangCach=10.0, giaCuoc=5.0,
                 loaiThucPham="thực phẩm đông lạnh", soLuong=6):
        super().__init__(maHD, tenKH, khoangCach, giaCuoc)
        self.loaiThucPham = loaiThucPham
        self.soLuong = soLuong

    @property
    def loaiThucPham(self):
        return self._loaiThucPham

    @loaiThucPham.setter
    def loaiThucPham(self, value):
        val = str(value).strip().lower()
        if "đông lạnh" in val or "dong lanh" in val:
            self._loaiThucPham = "thực phẩm đông lạnh"
        elif "giữ nóng" in val or "giu nong" in val or "nóng" in val:
            self._loaiThucPham = "thực phẩm giữ nóng"
        elif "khô" in val or "kho" in val:
            self._loaiThucPham = "thực phẩm khô"
        else:
            self._loaiThucPham = "thực phẩm khô"

    @property
    def soLuong(self):
        return self._soLuong

    @soLuong.setter
    def soLuong(self, value):
        try:
            val_int = int(value)
            self._soLuong = max(0, val_int)
        except (ValueError, TypeError):
            self._soLuong = 0

    def phiBaoQuan(self):
        """Phí bảo quản theo từng loại thực phẩm."""
        if self._loaiThucPham == "thực phẩm đông lạnh":
            return 2.0
        elif self._loaiThucPham == "thực phẩm giữ nóng":
            return 3.0
        return 0.0

    def ChiPhi(self):
        return self._soLuong * self.phiBaoQuan()

    def tinhHoTroGia(self):
        """
        Nếu mặt hàng đông lạnh và số lượng > 5 thì hỗ trợ 5k.
        Nếu mặt hàng giữ nóng và số lượng > 5 thì hỗ trợ 10k.
        Còn lại không hỗ trợ.
        """
        if self._loaiThucPham == "thực phẩm đông lạnh" and self._soLuong > 5:
            return 5.0
        elif self._loaiThucPham == "thực phẩm giữ nóng" and self._soLuong > 5:
            return 10.0
        return 0.0

    def nhap(self):
        super().nhap()
        while True:
            tp = input("Chọn loại thực phẩm (1: đông lạnh, 2: giữ nóng, 3: khô): ").strip()
            if tp in ["1", "đông lạnh", "dong lanh"]:
                self.loaiThucPham = "thực phẩm đông lạnh"
                break
            elif tp in ["2", "giữ nóng", "giu nong"]:
                self.loaiThucPham = "thực phẩm giữ nóng"
                break
            elif tp in ["3", "khô", "kho"]:
                self.loaiThucPham = "thực phẩm khô"
                break
            print("Lựa chọn không hợp lệ!")

        while True:
            try:
                sl = int(input("Nhập số lượng thực phẩm (>= 0): "))
                if sl >= 0:
                    self.soLuong = sl
                    break
                print("Số lượng phải >= 0!")
            except ValueError:
                print("Số lượng phải là số nguyên!")

    def Xuat(self):
        print(f"[THỰC PHẨM]   ", end="")
        super().Xuat()
        print(f"               -> Loại TP: {self._loaiThucPham} | Số lượng: {self._soLuong} | Phí BQ: {self.phiBaoQuan():.1f}k/món")


# ----------------- Lớp 3: Hóa Đơn Giao Hàng Hóa -----------------
class HoaDonGiaoHangHoa(HoaDonVanChuyen, IHoTroGia):
    """
    Hóa đơn giao hàng hóa:
    - Thuộc tính:
      * hinhThucGiao: nhận 1 trong 3 giá trị "tiêu chuẩn", "giao nhanh 4h", "giao nhanh 24h".
      * khoiLuong: khối lượng hàng (kg).
    - Chi phí = chi phí theo hình thức giao hàng + chi phí phát sinh theo khối lượng:
      * Chi phí hình thức:
        - "tiêu chuẩn": miễn phí (0)
        - "giao nhanh 4h": 50% Phí vận chuyển
        - "giao nhanh 24h": 20% Phí vận chuyển
      * Chi phí phát sinh theo khối lượng:
        - Khối lượng < 1kg: miễn phí (0)
        - Khối lượng >= 1kg: (khối lượng - 1) * 5 (nghìn đồng)
    - Hỗ trợ giá (IHoTroGia): Hỗ trợ 10% của Phí vận chuyển cho tất cả đơn hàng.
    """
    def __init__(self, maHD="HD001", tenKH="Nguyễn Cửu Đàm", khoangCach=10.0, giaCuoc=5.0,
                 hinhThucGiao="tiêu chuẩn", khoiLuong=2.5):
        super().__init__(maHD, tenKH, khoangCach, giaCuoc)
        self.hinhThucGiao = hinhThucGiao
        self.khoiLuong = khoiLuong

    @property
    def hinhThucGiao(self):
        return self._hinhThucGiao

    @hinhThucGiao.setter
    def hinhThucGiao(self, value):
        val = str(value).strip().lower()
        if "4h" in val or "bốn giờ" in val:
            self._hinhThucGiao = "giao nhanh 4h"
        elif "24h" in val or "hai tư giờ" in val or "một ngày" in val:
            self._hinhThucGiao = "giao nhanh 24h"
        else:
            self._hinhThucGiao = "tiêu chuẩn"

    @property
    def khoiLuong(self):
        return self._khoiLuong

    @khoiLuong.setter
    def khoiLuong(self, value):
        try:
            val_num = float(value)
            self._khoiLuong = max(0.0, val_num)
        except (ValueError, TypeError):
            self._khoiLuong = 0.0

    def chiPhiHinhThuc(self):
        pvc = self.PhiVanChuyen()
        if self._hinhThucGiao == "giao nhanh 4h":
            return 0.50 * pvc
        elif self._hinhThucGiao == "giao nhanh 24h":
            return 0.20 * pvc
        return 0.0

    def chiPhiKhoiLuong(self):
        if self._khoiLuong < 1.0:
            return 0.0
        return (self._khoiLuong - 1.0) * 5.0

    def ChiPhi(self):
        return self.chiPhiHinhThuc() + self.chiPhiKhoiLuong()

    def tinhHoTroGia(self):
        # Hỗ trợ 10% của Phí vận chuyển cho tất cả đơn hàng
        return 0.10 * self.PhiVanChuyen()

    def nhap(self):
        super().nhap()
        while True:
            ht = input("Chọn hình thức giao (1: tiêu chuẩn, 2: giao nhanh 4h, 3: giao nhanh 24h): ").strip()
            if ht in ["1", "tiêu chuẩn", "tieu chuan"]:
                self.hinhThucGiao = "tiêu chuẩn"
                break
            elif ht in ["2", "4h", "giao nhanh 4h"]:
                self.hinhThucGiao = "giao nhanh 4h"
                break
            elif ht in ["3", "24h", "giao nhanh 24h"]:
                self.hinhThucGiao = "giao nhanh 24h"
                break
            print("Lựa chọn không hợp lệ!")

        while True:
            try:
                kl = float(input("Nhập khối lượng hàng hóa (kg, >= 0): "))
                if kl >= 0:
                    self.khoiLuong = kl
                    break
                print("Khối lượng phải >= 0!")
            except ValueError:
                print("Khối lượng phải là số thực!")

    def Xuat(self):
        print(f"[HÀNG HÓA]    ", end="")
        super().Xuat()
        print(f"               -> Hình thức: {self._hinhThucGiao.title()} | Khối lượng: {self._khoiLuong:.2f} kg (Phí KL: {self.chiPhiKhoiLuong():.1f}k)")


# =================================================================
# 4. CHƯƠNG TRÌNH CHÍNH (main - MINH HỌA VÀ ĐA HÌNH)
# =================================================================
def main():
    print("==========================================================================================")
    print("        CHƯƠNG TRÌNH QUẢN LÝ HÓA ĐƠN VẬN CHUYỂN GIAO HÀNG (MÃ ĐỀ: 01 - ĐỀ 03)")
    print("==========================================================================================")

    # 1. Minh họa khởi tạo mặc định theo Yêu cầu 4
    print("\n--- 1. Kiểm tra khởi tạo mặc định (Default Constructor) ---")
    hd_mac_dinh = HoaDonChoNguoi()
    hd_mac_dinh.Xuat()

    # 2. Khởi tạo danh sách hóa đơn cụ thể để minh họa đa hình
    ds_hoa_don = [
        # Hóa đơn chở người bằng scooter (chi phí = 2 * khoảng cách = 2 * 8 = 16k)
        HoaDonChoNguoi(maHD="HD002", tenKH="Trần Thị Lan", khoangCach=8.0, giaCuoc=6.0, loaiXe="scooter"),

        # Hóa đơn chở người bằng xe thông thường (chi phí = 0)
        HoaDonChoNguoi(maHD="HD003", tenKH="Phạm Minh Tuấn", khoangCach=15.0, giaCuoc=5.0, loaiXe="xe số"),

        # Hóa đơn giao thực phẩm đông lạnh, số lượng 8 (> 5: hỗ trợ 5k, phí BQ: 8 * 2 = 16k)
        HoaDonGiaoThucPham(maHD="HD004", tenKH="Lê Hoàng Yến", khoangCach=6.0, giaCuoc=5.0,
                           loaiThucPham="thực phẩm đông lạnh", soLuong=8),

        # Hóa đơn giao thực phẩm giữ nóng, số lượng 10 (> 5: hỗ trợ 10k, phí BQ: 10 * 3 = 30k)
        HoaDonGiaoThucPham(maHD="HD005", tenKH="Ngô Bảo Châu", khoangCach=5.0, giaCuoc=6.0,
                           loaiThucPham="thực phẩm giữ nóng", soLuong=10),

        # Hóa đơn giao thực phẩm khô, số lượng 4 (phí BQ: 0, hỗ trợ 0)
        HoaDonGiaoThucPham(maHD="HD006", tenKH="Vũ Đức Đam", khoangCach=12.0, giaCuoc=4.5,
                           loaiThucPham="thực phẩm khô", soLuong=4),

        # Hóa đơn giao hàng nhanh 4h, nặng 3.5 kg (phí HT: 50% PVC = 25k, phí KL: (3.5 - 1)*5 = 12.5k, hỗ trợ: 10% PVC = 5k)
        HoaDonGiaoHangHoa(maHD="HD007", tenKH="Đặng Thu Hà", khoangCach=10.0, giaCuoc=5.0,
                          hinhThucGiao="giao nhanh 4h", khoiLuong=3.5),

        # Hóa đơn giao hàng nhanh 24h, nặng 0.8 kg (< 1kg: phí KL = 0, phí HT: 20% PVC = 8k, hỗ trợ 10% PVC = 4k)
        HoaDonGiaoHangHoa(maHD="HD008", tenKH="Hoàng Quốc Việt", khoangCach=8.0, giaCuoc=5.0,
                          hinhThucGiao="giao nhanh 24h", khoiLuong=0.8),

        # Hóa đơn giao hàng tiêu chuẩn, nặng 5.0 kg (phí HT: 0, phí KL: (5-1)*5 = 20k, hỗ trợ 10% PVC = 4k)
        HoaDonGiaoHangHoa(maHD="HD009", tenKH="Bùi Văn Cường", khoangCach=8.0, giaCuoc=5.0,
                          hinhThucGiao="tiêu chuẩn", khoiLuong=5.0)
    ]

    print("\n============================== DANH SÁCH CÁC HÓA ĐƠN ==============================")
    for i, hd in enumerate(ds_hoa_don, start=1):
        print(f"\n[{i}]", end=" ")
        hd.Xuat()

    # Thống kê tổng hợp
    tong_thanh_tien = sum(hd.ThanhTien() for hd in ds_hoa_don)
    tong_ho_tro = sum(hd.tinhHoTroGia() for hd in ds_hoa_don if isinstance(hd, IHoTroGia))
    tong_thuc_thu = tong_thanh_tien - tong_ho_tro

    print("\n================================== TỔNG KẾT DOANH THU ==================================")
    print(f"-> Tổng Thành tiền (theo quy định hóa đơn)      : {tong_thanh_tien:>10.1f} nghìn VND")
    print(f"-> Tổng Chi phí công ty hỗ trợ giá (Interface) : {tong_ho_tro:>10.1f} nghìn VND")
    print(f"----------------------------------------------------------------------------------------")
    print(f"=> DOANH THU THỰC THU TỪ KHÁCH HÀNG            : {tong_thuc_thu:>10.1f} nghìn VND ({tong_thuc_thu * 1000:,.0f} VND)")
    print("========================================================================================")

    # Hóa đơn có cước phí thanh toán cao nhất
    hd_max = max(ds_hoa_don, key=lambda x: x.ThanhTien())
    print(f"\n=> Hóa đơn có Thành tiền cao nhất: {hd_max.maHD} của KH '{hd_max.tenKH}' với {hd_max.ThanhTien():.1f}k VND")

    # Danh sách đơn hàng nhận hỗ trợ giá
    print("\n--- DANH SÁCH ĐƠN HÀNG ĐƯỢC ÁP DỤNG CHÍNH SÁCH HỖ TRỢ GIÁ ---")
    for hd in ds_hoa_don:
        if isinstance(hd, IHoTroGia) and hd.tinhHoTroGia() > 0:
            print(f"- {hd.maHD} ({hd.tenKH}): Hỗ trợ {hd.tinhHoTroGia():.1f}k VND")


if __name__ == "__main__":
    main()
