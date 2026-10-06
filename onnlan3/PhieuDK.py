from abc import ABC, abstractmethod
from datetime import datetime


# =================================================================
# 1. INTERFACE: IChiPhiUuDai (Chính sách ưu đãi học trực tuyến)
# =================================================================
class IChiPhiUuDai(ABC):
    """
    Interface định nghĩa chính sách chi phí ưu đãi cho người học trực tuyến.
    Chỉ áp dụng cho: Học viên mới và Học viên dài hạn.
    Đơn vị tính: USD.
    """
    @abstractmethod
    def UuDai(self):
        """Trả về mức chi phí ưu đãi trực tuyến (USD)."""
        pass


# =================================================================
# 2. LỚP TRỪU TƯỢNG: PhieuDK (Abstract Class)
# =================================================================
class PhieuDK(ABC):
    # Thuộc tính static: Tỉ giá chuyển đổi chung áp dụng là 23,400 VND / 1 USD
    TiGia = 23400

    def __init__(self, maPDK="P00001", maKhoaHoc="KH0100", tenKhoaHoc="Lập trình HĐT",
                 tenNH="Lê Văn Tỉnh", ngayDK=None, hocPhi=120.0, soTiet=45):
        """
        Khởi tạo phiếu đăng ký khóa học:
        - Mặc định: mã phiếu "P00001", người học "Lê Văn Tỉnh", mã KH "KH0100",
          tên KH "Lập trình HĐT", số tiết 45, học phí 120 USD, ngày hiện tại.
        - Khởi tạo đầy đủ tham số khi truyền vào giá trị cụ thể.
        """
        self._maPDK = str(maPDK).strip() if maPDK else "P00001"
        self._maKhoaHoc = "KH0100"
        self._tenKhoaHoc = str(tenKhoaHoc).strip() if tenKhoaHoc else "Lập trình HĐT"
        self._tenNH = str(tenNH).strip() if tenNH else "Lê Văn Tỉnh"
        self._ngayDK = ngayDK if ngayDK is not None else datetime.now()
        self._hocPhi = max(0.0, float(hocPhi))
        self._soTiet = 45

        # Áp dụng ràng buộc qua setter
        self.MAKHOAHOC = maKhoaHoc
        self.SOTIET = soTiet

    # ----------------- PROPERTIES (GETTER & SETTER) -----------------
    @property
    def MAKHOAHOC(self):
        return self._maKhoaHoc

    @MAKHOAHOC.setter
    def MAKHOAHOC(self, value):
        # Yêu cầu: Chiều dài 6 ký tự, bắt đầu bằng "KH", 4 ký tự còn lại là chữ số
        val_str = str(value).strip().upper()
        if len(val_str) == 6 and val_str.startswith("KH") and val_str[2:].isdigit():
            self._maKhoaHoc = val_str
            return True
        else:
            print(f"[Cảnh báo] Mã khóa học '{value}' không hợp lệ! Phải có 6 ký tự, bắt đầu bằng 'KH' và 4 chữ số (VD: KH0100).")
            if not self._maKhoaHoc:
                self._maKhoaHoc = "KH0000"
            return False

    @property
    def SOTIET(self):
        return self._soTiet

    @SOTIET.setter
    def SOTIET(self, value):
        # Yêu cầu: Số tiết phải là số dương (> 0)
        try:
            val_int = int(value)
            if val_int > 0:
                self._soTiet = val_int
                return True
            else:
                print(f"[Cảnh báo] Số tiết ({value}) phải là số dương (> 0)!")
                if self._soTiet <= 0:
                    self._soTiet = 0
                return False
        except (ValueError, TypeError):
            print(f"[Cảnh báo] Số tiết '{value}' phải là số nguyên!")
            return False

    @property
    def maPDK(self):
        return self._maPDK

    @maPDK.setter
    def maPDK(self, value):
        if str(value).strip():
            self._maPDK = str(value).strip()

    @property
    def tenKhoaHoc(self):
        return self._tenKhoaHoc

    @tenKhoaHoc.setter
    def tenKhoaHoc(self, value):
        if str(value).strip():
            self._tenKhoaHoc = str(value).strip()

    @property
    def tenNH(self):
        return self._tenNH

    @tenNH.setter
    def tenNH(self, value):
        if str(value).strip():
            self._tenNH = str(value).strip()

    @property
    def ngayDK(self):
        return self._ngayDK

    @ngayDK.setter
    def ngayDK(self, value):
        if isinstance(value, datetime):
            self._ngayDK = value
        elif isinstance(value, str):
            for fmt in ("%d/%m/%Y", "%Y-%m-%d", "%d-%m-%Y"):
                try:
                    self._ngayDK = datetime.strptime(value.strip(), fmt)
                    return True
                except ValueError:
                    pass
            print("[Cảnh báo] Định dạng ngày đăng ký không hợp lệ! Dùng dd/mm/yyyy.")
            return False
        return True

    @property
    def hocPhi(self):
        return self._hocPhi

    @hocPhi.setter
    def hocPhi(self, value):
        try:
            val_num = float(value)
            if val_num >= 0:
                self._hocPhi = val_num
                return True
            print("[Cảnh báo] Học phí phải >= 0 USD!")
            return False
        except (ValueError, TypeError):
            print("[Cảnh báo] Học phí không hợp lệ!")
            return False

    # ----------------- PHƯƠNG THỨC NGHIỆP VỤ -----------------
    def GiamGia1(self):
        """
        Giảm giá 1: Giảm giá cho các phiếu đăng ký sớm:
        - Đăng ký trước tháng 4 (tháng 1, 2, 3): giảm 5% học phí.
        - Đăng ký trước tháng 6 (tháng 4, 5): giảm 3% học phí.
        - Còn lại: không giảm (0 USD).
        """
        thang = self._ngayDK.month
        if thang < 4:
            return 0.05 * self._hocPhi
        elif thang < 6:
            return 0.03 * self._hocPhi
        return 0.0

    @abstractmethod
    def GiamGia2(self):
        """Phương thức trừu tượng: giảm giá theo từng đối tượng học viên."""
        pass

    def GiamGia(self):
        """Tổng giảm giá = Giảm giá 1 + Giảm giá 2."""
        return self.GiamGia1() + self.GiamGia2()

    def ThanhTien(self):
        """Thành tiền (USD) = Học phí - Giảm giá."""
        return max(0.0, self._hocPhi - self.GiamGia())

    def ThanhTienVND(self):
        """Thành tiền VNĐ = Thành tiền * Tỉ giá (23400)."""
        return self.ThanhTien() * PhieuDK.TiGia

    # ----------------- NHẬP / XUẤT THÔNG TIN -----------------
    def nhap(self):
        """Nhập thông tin phiếu đăng ký."""
        self._maPDK = input("Nhập mã phiếu đăng ký (VD: P00001): ").strip()
        while True:
            mkh = input("Nhập mã khóa học (dài 6 ký tự, bắt đầu 'KH' + 4 số, VD: KH0100): ").strip().upper()
            if len(mkh) == 6 and mkh.startswith("KH") and mkh[2:].isdigit():
                self._maKhoaHoc = mkh
                break
            print("Mã khóa học không hợp lệ! Vui lòng nhập lại.")

        self._tenKhoaHoc = input("Nhập tên khóa học: ").strip()
        self._tenNH = input("Nhập tên người học: ").strip()

        while True:
            ngay_str = input("Nhập ngày đăng ký (dd/mm/yyyy, Enter để lấy ngày hiện tại): ").strip()
            if not ngay_str:
                self._ngayDK = datetime.now()
                break
            try:
                self._ngayDK = datetime.strptime(ngay_str, "%d/%m/%Y")
                break
            except ValueError:
                print("Ngày không hợp lệ! Định dạng: dd/mm/yyyy.")

        while True:
            try:
                hp = float(input("Nhập học phí (USD, > 0): "))
                if hp > 0:
                    self._hocPhi = hp
                    break
                print("Học phí phải > 0!")
            except ValueError:
                print("Học phí phải là số hợp lệ!")

        while True:
            try:
                st = int(input("Nhập số tiết học (> 0): "))
                if st > 0:
                    self._soTiet = st
                    break
                print("Số tiết phải > 0!")
            except ValueError:
                print("Số tiết phải là số nguyên!")

    def Xuat(self):
        """Phương thức xuất thông tin virtual."""
        ngay_str = self._ngayDK.strftime("%d/%m/%Y") if self._ngayDK else ""
        uu_dai_str = ""
        if isinstance(self, IChiPhiUuDai):
            uu_dai_str = f" | Ưu đãi online: -{self.UuDai():.1f} USD"

        print(f"Mã phiếu: {self._maPDK} | Khóa học: {self._tenKhoaHoc} ({self._maKhoaHoc}) | "
              f"Học viên: {self._tenNH:<16} | Ngày ĐK: {ngay_str} | Số tiết: {self._soTiet:>2} | "
              f"Học phí: {self._hocPhi:>6.1f} $ | Giảm giá: {self.GiamGia():>5.1f} $ | "
              f"Thành tiền: {self.ThanhTien():>6.1f} $ ({self.ThanhTienVND():>12,.0f} VND){uu_dai_str}")


# =================================================================
# 3. CÁC LỚP CON (KẾ THỪA VÀ CÀI ĐẶT ĐA HÌNH)
# =================================================================

# ----------------- Lớp 1: Học Viên Mới -----------------
class HocVienMoi(PhieuDK, IChiPhiUuDai):
    """
    Học viên mới:
    - Thuộc tính: namSinh (năm sinh).
    - Giảm giá 2: Nếu lớn hơn 22 tuổi (năm hiện tại - namSinh > 22) -> không được giảm (0 USD),
      ngược lại được giảm 10 USD.
    - Ưu đãi online (IChiPhiUuDai): Khóa học có số tiết >= 45 được hỗ trợ 10 USD, còn lại 8 USD.
    """
    def __init__(self, maPDK="P00001", maKhoaHoc="KH0100", tenKhoaHoc="Lập trình HĐT",
                 tenNH="Lê Văn Tỉnh", ngayDK=None, hocPhi=120.0, soTiet=45, namSinh=2004):
        super().__init__(maPDK, maKhoaHoc, tenKhoaHoc, tenNH, ngayDK, hocPhi, soTiet)
        self.namSinh = namSinh

    @property
    def namSinh(self):
        return self._namSinh

    @namSinh.setter
    def namSinh(self, value):
        try:
            self._namSinh = int(value)
        except (ValueError, TypeError):
            self._namSinh = 2004

    def GiamGia2(self):
        nam_hien_tai = datetime.now().year
        tuoi = nam_hien_tai - self._namSinh
        if tuoi > 22:
            return 0.0
        return 10.0

    def UuDai(self):
        if self._soTiet >= 45:
            return 10.0
        return 8.0

    def nhap(self):
        super().nhap()
        while True:
            try:
                ns = int(input("Nhập năm sinh học viên: "))
                if 1950 <= ns <= datetime.now().year:
                    self.namSinh = ns
                    break
                print("Năm sinh không hợp lệ!")
            except ValueError:
                print("Năm sinh phải là số nguyên!")

    def Xuat(self):
        print(f"[HV MỚI]      ", end="")
        super().Xuat()
        tuoi = datetime.now().year - self._namSinh
        print(f"               -> Năm sinh: {self._namSinh} (Tuổi: {tuoi}) | Ưu đãi học online: {self.UuDai():.1f} USD")


# ----------------- Lớp 2: Học Viên Dài Hạn -----------------
class HocVienDaiHan(PhieuDK, IChiPhiUuDai):
    """
    Học viên dài hạn:
    - Thuộc tính: SLKH (số lượng khóa học đã đăng ký trước đây).
    - Giảm giá 2:
      * SLKH <= 5: giảm 5% học phí
      * SLKH từ 6 đến 10: giảm 10% học phí
      * SLKH > 10: giảm 15% học phí
    - Ưu đãi online (IChiPhiUuDai): Tất cả phiếu đăng ký đều được hỗ trợ 15 USD.
    """
    def __init__(self, maPDK="P00001", maKhoaHoc="KH0100", tenKhoaHoc="Lập trình HĐT",
                 tenNH="Lê Văn Tỉnh", ngayDK=None, hocPhi=120.0, soTiet=45, SLKH=4):
        super().__init__(maPDK, maKhoaHoc, tenKhoaHoc, tenNH, ngayDK, hocPhi, soTiet)
        self.SLKH = SLKH

    @property
    def SLKH(self):
        return self._SLKH

    @SLKH.setter
    def SLKH(self, value):
        try:
            self._SLKH = max(0, int(value))
        except (ValueError, TypeError):
            self._SLKH = 0

    def GiamGia2(self):
        if self._SLKH <= 5:
            return 0.05 * self._hocPhi
        elif 6 <= self._SLKH <= 10:
            return 0.10 * self._hocPhi
        else:
            return 0.15 * self._hocPhi

    def UuDai(self):
        return 15.0

    def nhap(self):
        super().nhap()
        while True:
            try:
                sl = int(input("Nhập số lượng khóa học đã từng đăng ký: "))
                if sl >= 0:
                    self.SLKH = sl
                    break
                print("Số lượng khóa học phải >= 0!")
            except ValueError:
                print("Số lượng khóa học phải là số nguyên!")

    def Xuat(self):
        print(f"[HV DÀI HẠN]  ", end="")
        super().Xuat()
        print(f"               -> Đã học: {self._SLKH} khóa | Ưu đãi học online: {self.UuDai():.1f} USD")


# ----------------- Lớp 3: Học Viên Con Giáo Viên -----------------
class HocVienConGiaoVien(PhieuDK):
    """
    Học viên là con của giáo viên:
    - Thuộc tính: thamNien (thâm niên công tác của ba/mẹ tính theo năm).
    - Giảm giá 2:
      * Thâm niên < 10 năm: giảm 40% học phí
      * Thâm niên >= 10 năm: giảm 50% học phí
    - Không áp dụng chính sách ưu đãi trực tuyến.
    """
    def __init__(self, maPDK="P00001", maKhoaHoc="KH0100", tenKhoaHoc="Lập trình HĐT",
                 tenNH="Lê Văn Tỉnh", ngayDK=None, hocPhi=120.0, soTiet=45, thamNien=8):
        super().__init__(maPDK, maKhoaHoc, tenKhoaHoc, tenNH, ngayDK, hocPhi, soTiet)
        self.thamNien = thamNien

    @property
    def thamNien(self):
        return self._thamNien

    @thamNien.setter
    def thamNien(self, value):
        try:
            self._thamNien = max(0, int(value))
        except (ValueError, TypeError):
            self._thamNien = 0

    def GiamGia2(self):
        if self._thamNien < 10:
            return 0.40 * self._hocPhi
        return 0.50 * self._hocPhi

    def nhap(self):
        super().nhap()
        while True:
            try:
                tn = int(input("Nhập thâm niên công tác của cha/mẹ (năm): "))
                if tn >= 0:
                    self.thamNien = tn
                    break
                print("Thâm niên phải >= 0!")
            except ValueError:
                print("Thâm niên phải là số nguyên!")

    def Xuat(self):
        print(f"[CON GIÁO VIÊN]", end="")
        super().Xuat()
        print(f"               -> Thâm niên giảng dạy của phụ huynh: {self._thamNien} năm")


# =================================================================
# 4. CHƯƠNG TRÌNH CHÍNH (main - MINH HỌA VÀ ĐA HÌNH)
# =================================================================
def main():
    print("==========================================================================================")
    print("      CHƯƠNG TRÌNH QUẢN LÝ PHIẾU ĐĂNG KÝ KHÓA HỌC ONLINE (MÃ ĐỀ: 03 - ĐỀ 04)")
    print("==========================================================================================")

    # 1. Minh họa khởi tạo mặc định theo Yêu cầu 3a
    print("\n--- 1. Kiểm tra khởi tạo mặc định (Default Constructor) ---")
    pdk_mac_dinh = HocVienMoi()
    pdk_mac_dinh.Xuat()

    # 2. Khởi tạo danh sách các phiếu đăng ký cụ thể
    # Lưu ý: ngày đăng ký kiểm tra chính sách giảm giá sớm (trước tháng 4: 5%, trước tháng 6: 3%)
    ds_phieu = [
        # HV Mới: Đăng ký tháng 2 (trước tháng 4: giảm 5%), sinh 2005 (tuổi <= 22: giảm thêm 10$), số tiết 60 (>= 45: ưu đãi 10$)
        HocVienMoi(maPDK="P00002", maKhoaHoc="KH0201", tenKhoaHoc="Lập trình Python Nâng Cao",
                   tenNH="Trần Quốc Bảo", ngayDK=datetime(2026, 2, 15), hocPhi=150.0, soTiet=60, namSinh=2005),

        # HV Mới: Đăng ký tháng 5 (trước tháng 6: giảm 3%), sinh 1998 (tuổi > 22: giảm 0$), số tiết 30 (< 45: ưu đãi 8$)
        HocVienMoi(maPDK="P00003", maKhoaHoc="KH0302", tenKhoaHoc="Nhập môn Machine Learning",
                   tenNH="Võ Hoàng Nam", ngayDK=datetime(2026, 5, 20), hocPhi=200.0, soTiet=30, namSinh=1998),

        # HV Dài Hạn: Đăng ký tháng 3 (trước tháng 4: giảm 5%), đã học 4 khóa (SLKH <= 5: giảm 5%), ưu đãi 15$
        HocVienDaiHan(maPDK="P00004", maKhoaHoc="KH0405", tenKhoaHoc="Deep Learning Chuyên Sâu",
                      tenNH="Nguyễn Hải Đăng", ngayDK=datetime(2026, 3, 10), hocPhi=250.0, soTiet=50, SLKH=4),

        # HV Dài Hạn: Đăng ký tháng 8 (không giảm sớm), đã học 8 khóa (SLKH 6-10: giảm 10%), ưu đãi 15$
        HocVienDaiHan(maPDK="P00005", maKhoaHoc="KH0506", tenKhoaHoc="Xử Lý Ngôn Ngữ Tự Nhiên",
                      tenNH="Đặng Bích Ngọc", ngayDK=datetime(2026, 8, 25), hocPhi=180.0, soTiet=45, SLKH=8),

        # HV Dài Hạn: Đăng ký tháng 4 (trước tháng 6: giảm 3%), đã học 12 khóa (> 10: giảm 15%), ưu đãi 15$
        HocVienDaiHan(maPDK="P00006", maKhoaHoc="KH0607", tenKhoaHoc="Cloud Computing & DevOps",
                      tenNH="Lý Minh Tâm", ngayDK=datetime(2026, 4, 12), hocPhi=300.0, soTiet=60, SLKH=12),

        # HV Con Giáo Viên: Đăng ký tháng 1 (trước tháng 4: giảm 5%), phụ huynh thâm niên 6 năm (< 10: giảm 40%)
        HocVienConGiaoVien(maPDK="P00007", maKhoaHoc="KH0708", tenKhoaHoc="Thiết Kế Hệ Thống Lớn",
                           tenNH="Phạm Quỳnh Anh", ngayDK=datetime(2026, 1, 18), hocPhi=220.0, soTiet=45, thamNien=6),

        # HV Con Giáo Viên: Đăng ký tháng 9 (không giảm sớm), phụ huynh thâm niên 15 năm (>= 10: giảm 50%)
        HocVienConGiaoVien(maPDK="P00008", maKhoaHoc="KH0809", tenKhoaHoc="Cơ Sở Dữ Liệu Phân Tán",
                           tenNH="Hoàng Đức Vĩnh", ngayDK=datetime(2026, 9, 5), hocPhi=240.0, soTiet=40, thamNien=15)
    ]

    print("\n============================== DANH SÁCH PHIẾU ĐĂNG KÝ ==============================")
    for i, pdk in enumerate(ds_phieu, start=1):
        print(f"\n[{i}]", end=" ")
        pdk.Xuat()

    # Thống kê tổng hợp
    tong_thanh_tien_usd = sum(pdk.ThanhTien() for pdk in ds_phieu)
    tong_thanh_tien_vnd = sum(pdk.ThanhTienVND() for pdk in ds_phieu)
    tong_uu_dai_usd = sum(pdk.UuDai() for pdk in ds_phieu if isinstance(pdk, IChiPhiUuDai))
    tong_uu_dai_vnd = tong_uu_dai_usd * PhieuDK.TiGia
    tong_thuc_thu_vnd = tong_thanh_tien_vnd - tong_uu_dai_vnd

    print("\n================================== TỔNG KẾT TÀI CHÍNH ==================================")
    print(f"-> Tổng Học phí thực tế (Thành tiền USD)          : {tong_thanh_tien_usd:>10.1f} USD")
    print(f"-> Quy đổi sang VNĐ (Tỉ giá 23,400)              : {tong_thanh_tien_vnd:>14,.0f} VND")
    print(f"-> Tổng Ưu đãi học trực tuyến (Interface)         : {tong_uu_dai_usd:>10.1f} USD ({tong_uu_dai_vnd:,.0f} VND)")
    print(f"----------------------------------------------------------------------------------------")
    print(f"=> TỔNG HỌC PHÍ THỰC THU (Sau trừ ưu đãi online) : {tong_thuc_thu_vnd:>14,.0f} VND")
    print("========================================================================================")

    # Khóa học có thành tiền cao nhất
    pdk_max = max(ds_phieu, key=lambda x: x.ThanhTien())
    print(f"\n=> Phiếu có học phí cao nhất: {pdk_max.maPDK} - Khóa '{pdk_max.tenKhoaHoc}' của HV '{pdk_max.tenNH}' với {pdk_max.ThanhTien():.1f} USD ({pdk_max.ThanhTienVND():,.0f} VND)")

    # Danh sách học viên hưởng ưu đãi trực tuyến
    print("\n--- DANH SÁCH HỌC VIÊN ĐƯỢC HƯỞNG ƯU ĐÃI TRỰC TUYẾN (IMPLEMENT IChiPhiUuDai) ---")
    for pdk in ds_phieu:
        if isinstance(pdk, IChiPhiUuDai):
            print(f"- {pdk.tenNH} ({pdk.maPDK}): Ưu đãi {pdk.UuDai():.1f} USD ({pdk.UuDai() * PhieuDK.TiGia:,.0f} VND)")


if __name__ == "__main__":
    main()
