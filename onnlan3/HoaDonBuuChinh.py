from abc import ABC, abstractmethod
from datetime import datetime


# =================================================================
# 1. INTERFACE: IPhiDamBaoHangHoa (Phí bảo đảm an toàn hàng hóa)
# =================================================================
class IPhiDamBaoHangHoa(ABC):
    """
    Interface định nghĩa phương thức tính phí bảo đảm hàng hóa.
    Áp dụng cho Chuyển phát nhanh 2h và Chuyển phát nhanh 24h.
    """
    @abstractmethod
    def phi(self):
        """Trả về tiền phí bảo đảm hàng hóa (VND)."""
        pass


# =================================================================
# 2. LỚP TRỪU TƯỢNG: HoaDon (Abstract Class)
# =================================================================
class HoaDon(ABC):
    def __init__(self, maVanDon="KG04001", tenNguoiGui="Nguyen Van A", tenNguoiNhan="Nguyen Van C",
                 diaChi="TPHCM", ngayGui=None, tuyen="Noi Tinh", soKg=0.35):
        """
        Khởi tạo hóa đơn bưu chính:
        - Mặc định: maVanDon="KG04001", tenNguoiGui="Nguyen Van A", tenNguoiNhan="Nguyen Van C",
          diaChi="TPHCM", ngayGui=19/05/2025, tuyen="Noi Tinh", soKg=0.35.
        - Khởi tạo đầy đủ tham số khi truyền vào giá trị cụ thể.
        """
        self._maVanDon = "KG00000"
        self._tenNguoiGui = str(tenNguoiGui).strip() if tenNguoiGui else "Nguyen Van A"
        self._tenNguoiNhan = str(tenNguoiNhan).strip() if tenNguoiNhan else "Nguyen Van C"
        self._diaChi = str(diaChi).strip() if diaChi else "TPHCM"
        self._ngayGui = ngayGui if ngayGui is not None else datetime(2025, 5, 19)
        self._tuyen = "Noi Tinh"
        self._soKg = 0.0

        # Ràng buộc qua property
        self.MAVANDON = maVanDon
        self.tuyen = tuyen
        self.SOKG = soKg

    # ----------------- PROPERTIES (GETTER & SETTER) -----------------
    @property
    def MAVANDON(self):
        return self._maVanDon

    @MAVANDON.setter
    def MAVANDON(self, value):
        val_str = str(value).strip().upper()
        # Yêu cầu: Dài 7 ký tự, bắt đầu bằng "LG" (hoặc KG theo mặc định), các ký tự còn lại là số
        if len(val_str) == 7 and (val_str.startswith("LG") or val_str.startswith("KG")) and val_str[2:].isdigit():
            self._maVanDon = val_str
            return True
        else:
            self._maVanDon = "KG00000"
            return False

    @property
    def SOKG(self):
        return self._soKg

    @SOKG.setter
    def SOKG(self, value):
        try:
            val_num = float(value)
            if val_num >= 0:
                self._soKg = val_num
                return True
            self._soKg = 0.0
            return False
        except (ValueError, TypeError):
            self._soKg = 0.0
            return False

    @property
    def tuyen(self):
        return self._tuyen

    @tuyen.setter
    def tuyen(self, value):
        val_str = str(value).strip().title()
        if "noi" in val_str.lower() or "nội" in val_str.lower():
            self._tuyen = "Noi Tinh"
        else:
            self._tuyen = "Lien Tinh"

    @property
    def tenNguoiGui(self):
        return self._tenNguoiGui

    @property
    def tenNguoiNhan(self):
        return self._tenNguoiNhan

    @property
    def diaChi(self):
        return self._diaChi

    @property
    def ngayGui(self):
        return self._ngayGui

    # ----------------- PHƯƠNG THỨC NGHIỆP VỤ -----------------
    @abstractmethod
    def TienCuoc(self):
        """Phương thức trừu tượng tính tiền cước gửi hàng."""
        pass

    def TinhChiPhiTT(self):
        """
        Tổng chi phí thanh toán = Tiền cước + Phụ phí tuyến đường
        - Tuyến Nội tỉnh: 22,000 VND
        - Tuyến Liên tỉnh: 33,000 VND
        """
        phu_phi = 22000 if self._tuyen.lower() == "noi tinh" else 33000
        return self.TienCuoc() + phu_phi

    def xuat(self):
        """Phương thức xuất thông tin virtual."""
        ngay_str = self._ngayGui.strftime("%d/%m/%Y") if self._ngayGui else ""
        phi_db_str = ""
        if isinstance(self, IPhiDamBaoHangHoa):
            phi_db_str = f" | Phí đảm bảo: {self.phi():,.0f} VND"

        print(f"Mã VĐ: {self._maVanDon} | Người gửi: {self._tenNguoiGui:<14} | Người nhận: {self._tenNguoiNhan:<14} | "
              f"Địa chỉ: {self._diaChi:<10} | Ngày: {ngay_str} | Tuyến: {self._tuyen:<9} | Khối lượng: {self._soKg:>5.2f} kg | "
              f"Tiền cước: {self.TienCuoc():>8,.0f} VND | Chi phí TT: {self.TinhChiPhiTT():>8,.0f} VND{phi_db_str}")


# =================================================================
# 3. CÁC LỚP CON (KẾ THỪA VÀ CÀI ĐẶT ĐA HÌNH)
# =================================================================

# ----------------- Lớp 1: Chuyển Phát Thường -----------------
class ChuyenPhatThuong(HoaDon):
    """
    Chuyển phát thường:
    - Thuộc tính bổ sung: soLanGui (số lần khách hàng đã gửi).
    - Tiền cước:
      * Nếu soKg <= 5 kg: TienCuoc = soKg * 8000
      * Ngược lại (> 5 kg): TienCuoc = 40000 + (soKg - 5) * 10000
      * Ưu đãi: Nếu soLanGui > 20 và TienCuoc > 50000 thì khống chế tối đa TienCuoc = 50000.
    """
    def __init__(self, maVanDon="KG04001", tenNguoiGui="Nguyen Van A", tenNguoiNhan="Nguyen Van C",
                 diaChi="TPHCM", ngayGui=None, tuyen="Noi Tinh", soKg=0.35, soLanGui=1):
        super().__init__(maVanDon, tenNguoiGui, tenNguoiNhan, diaChi, ngayGui, tuyen, soKg)
        self.soLanGui = max(0, int(soLanGui))

    def TienCuoc(self):
        if self._soKg <= 5.0:
            tc = self._soKg * 8000.0
        else:
            tc = 40000.0 + (self._soKg - 5.0) * 10000.0

        if self.soLanGui > 20 and tc > 50000.0:
            return 50000.0
        return tc

    def xuat(self):
        print(f"[CP THƯỜNG]   ", end="")
        super().xuat()
        print(f"               -> Số lần gửi của khách: {self.soLanGui}")


# ----------------- Lớp 2: Chuyển Nhanh 2h -----------------
class ChuyenNhanh2h(HoaDon, IPhiDamBaoHangHoa):
    """
    Chuyển nhanh 2 giờ:
    - Thuộc tính bổ sung: khoangCach (khoảng cách vận chuyển, km).
    - Tiền cước:
      * Nếu khoangCach < 4 km: TienCuoc = 23000
      * Ngược lại (>= 4 km): TienCuoc = 23000 + (khoangCach - 4) * 4000
    - Phí đảm bảo hàng hóa (IPhiDamBaoHangHoa): phi() = 0.15 * TienCuoc()
    """
    def __init__(self, maVanDon="LG01001", tenNguoiGui="Nguyen Van A", tenNguoiNhan="Nguyen Van C",
                 diaChi="TPHCM", ngayGui=None, tuyen="Noi Tinh", soKg=0.35, khoangCach=5.0):
        super().__init__(maVanDon, tenNguoiGui, tenNguoiNhan, diaChi, ngayGui, tuyen, soKg)
        self.khoangCach = max(0.0, float(khoangCach))

    def TienCuoc(self):
        if self.khoangCach < 4.0:
            return 23000.0
        return 23000.0 + (self.khoangCach - 4.0) * 4000.0

    def phi(self):
        return 0.15 * self.TienCuoc()

    def xuat(self):
        print(f"[CN 2H]       ", end="")
        super().xuat()
        print(f"               -> Khoảng cách giao: {self.khoangCach:.1f} km | Phí đảm bảo (15%): {self.phi():,.0f} VND")


# ----------------- Lớp 3: Chuyển Nhanh 24h -----------------
class ChuyenNhanh24h(HoaDon, IPhiDamBaoHangHoa):
    """
    Chuyển nhanh 24 giờ:
    - Thuộc tính bổ sung: kichThuoc (tổng kích thước kiện hàng, cm).
    - Tiền cước:
      * Phụ phí vượt khổ (vk): kichThuoc < 50 cm ? 0 : (kichThuoc - 50) * 1000
      * TienCuoc = 20000 + soKg * 2000 + vk
    - Phí đảm bảo hàng hóa (IPhiDamBaoHangHoa): phi() = 0.10 * TienCuoc()
    """
    def __init__(self, maVanDon="LG02002", tenNguoiGui="Nguyen Van A", tenNguoiNhan="Nguyen Van C",
                 diaChi="TPHCM", ngayGui=None, tuyen="Noi Tinh", soKg=0.35, kichThuoc=60.0):
        super().__init__(maVanDon, tenNguoiGui, tenNguoiNhan, diaChi, ngayGui, tuyen, soKg)
        self.kichThuoc = max(0.0, float(kichThuoc))

    def TienCuoc(self):
        vk = 0.0 if self.kichThuoc < 50.0 else (self.kichThuoc - 50.0) * 1000.0
        return 20000.0 + self._soKg * 2000.0 + vk

    def phi(self):
        return 0.10 * self.TienCuoc()

    def xuat(self):
        print(f"[CN 24H]      ", end="")
        super().xuat()
        print(f"               -> Kích thước kiện: {self.kichThuoc:.1f} cm | Phí đảm bảo (10%): {self.phi():,.0f} VND")


# =================================================================
# 4. CHƯƠNG TRÌNH CHÍNH (main - MINH HỌA VÀ ĐA HÌNH)
# =================================================================
def main():
    print("==========================================================================================")
    print("        CHƯƠNG TRÌNH QUẢN LÝ HÓA ĐƠN BƯU CHÍNH CHUYỂN PHÁT (GIAI DE HDT - DE 01)")
    print("==========================================================================================")

    # 1. Khởi tạo mặc định
    print("\n--- 1. Kiểm tra khởi tạo mặc định (Default Constructor) ---")
    hd_mac_dinh = ChuyenPhatThuong()
    hd_mac_dinh.xuat()

    # 2. Khởi tạo danh sách hóa đơn vận đơn
    ds_van_don = [
        # CP Thường: soKg 3kg (<= 5kg: 3 * 8000 = 24k), soLanGui = 5, nội tỉnh (+ 22k)
        ChuyenPhatThuong(maVanDon="LG00101", tenNguoiGui="Lê Văn Hùng", tenNguoiNhan="Trần Thị Mai",
                         diaChi="Hà Nội", ngayGui=datetime(2025, 5, 20), tuyen="Lien Tinh", soKg=3.0, soLanGui=5),

        # CP Thường: soKg 8kg (> 5kg: 40k + 3*10k = 70k), khách VIP gửi > 20 lần (giới hạn 50k), nội tỉnh (+ 22k)
        ChuyenPhatThuong(maVanDon="LG00102", tenNguoiGui="Vũ Tuấn Kiệt", tenNguoiNhan="Ngô Gia Bảo",
                         diaChi="TPHCM", ngayGui=datetime(2025, 5, 21), tuyen="Noi Tinh", soKg=8.0, soLanGui=25),

        # CN 2h: khoảng cách 3.5 km (< 4km: 23k), phí đảm bảo 15% (3.45k), nội tỉnh (+ 22k)
        ChuyenNhanh2h(maVanDon="LG00201", tenNguoiGui="Phạm Lan Anh", tenNguoiNhan="Đỗ Nhật Nam",
                      diaChi="Đà Nẵng", ngayGui=datetime(2025, 5, 22), tuyen="Noi Tinh", soKg=1.2, khoangCach=3.5),

        # CN 2h: khoảng cách 7.0 km (>= 4km: 23k + 3*4k = 35k), phí đảm bảo 15% (5.25k), liên tỉnh (+ 33k)
        ChuyenNhanh2h(maVanDon="LG00202", tenNguoiGui="Bùi Đình Chiểu", tenNguoiNhan="Nguyễn Thúy Kiều",
                      diaChi="Cần Thơ", ngayGui=datetime(2025, 5, 22), tuyen="Lien Tinh", soKg=2.5, khoangCach=7.0),

        # CN 24h: nặng 4kg, kích thước 45 cm (< 50cm: vk = 0 -> 20k + 4*2k = 28k), phí đảm bảo 10% (2.8k)
        ChuyenNhanh24h(maVanDon="LG00301", tenNguoiGui="Hoàng Đức Thịnh", tenNguoiNhan="Lý Hải My",
                       diaChi="Hải Phòng", ngayGui=datetime(2025, 5, 23), tuyen="Lien Tinh", soKg=4.0, kichThuoc=45.0),

        # CN 24h: nặng 6kg, kích thước 65 cm (vk = 15*1000 = 15k -> 20k + 12k + 15k = 47k), phí đảm bảo 10% (4.7k)
        ChuyenNhanh24h(maVanDon="LG00302", tenNguoiGui="Đặng Khắc Toàn", tenNguoiNhan="Trịnh Xuân Thanh",
                       diaChi="TPHCM", ngayGui=datetime(2025, 5, 23), tuyen="Noi Tinh", soKg=6.0, kichThuoc=65.0)
    ]

    print("\n============================== DANH SÁCH VẬN ĐƠN BƯU CHÍNH ==============================")
    for i, vd in enumerate(ds_van_don, start=1):
        print(f"\n[{i}]", end=" ")
        vd.xuat()

    # Thống kê tổng hợp
    tong_chi_phi_tt = sum(vd.TinhChiPhiTT() for vd in ds_van_don)
    tong_phi_dam_bao = sum(vd.phi() for vd in ds_van_don if isinstance(vd, IPhiDamBaoHangHoa))
    tong_doanh_thu = tong_chi_phi_tt + tong_phi_dam_bao

    print("\n================================== TỔNG KẾT DOANH THU ==================================")
    print(f"-> Tổng Chi phí thanh toán cước & tuyến      : {tong_chi_phi_tt:>15,.0f} VND")
    print(f"-> Tổng Phí đảm bảo hàng hóa (Interface)    : {tong_phi_dam_bao:>15,.0f} VND")
    print(f"----------------------------------------------------------------------------------------")
    print(f"=> TỔNG DOANH THU TOÀN BỘ VẬN ĐƠN           : {tong_doanh_thu:>15,.0f} VND")
    print("========================================================================================")

    # Đơn hàng có chi phí thanh toán cao nhất
    vd_max = max(ds_van_don, key=lambda x: x.TinhChiPhiTT())
    print(f"\n=> Vận đơn có cước phí cao nhất: {vd_max.MAVANDON} (Người gửi: {vd_max.tenNguoiGui}) với {vd_max.TinhChiPhiTT():,.0f} VND")

    # Danh sách đơn hàng có phí đảm bảo
    print("\n--- DANH SÁCH ĐƠN HÀNG THU PHÍ ĐẢM BẢO AN TOÀN (IMPLEMENT IPhiDamBaoHangHoa) ---")
    for vd in ds_van_don:
        if isinstance(vd, IPhiDamBaoHangHoa):
            print(f"- {vd.MAVANDON} ({vd.tenNguoiGui} -> {vd.tenNguoiNhan}): Phí đảm bảo {vd.phi():,.0f} VND")


if __name__ == "__main__":
    main()
