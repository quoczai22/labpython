from abc import ABC, abstractmethod
from datetime import datetime


# =================================================================
# 1. INTERFACE: ITroGia (Chương trình trợ giá in ấn cho tài liệu)
# =================================================================
class ITroGia(ABC):
    """
    Interface định nghĩa phương thức trợ giá in ấn.
    Áp dụng cho Sách giáo khoa và Sách thiếu nhi.
    """
    @abstractmethod
    def tinhTroGia(self):
        """Trả về tổng số tiền được trợ giá in ấn (VND)."""
        pass


# =================================================================
# 2. LỚP TRỪU TƯỢNG: TaiLieu (Abstract Class)
# =================================================================
class TaiLieu(ABC):
    # Thuộc tính static: Tỉ lệ chiết khấu chung là 10% (0.10)
    tiLeChietKhau = 0.10

    def __init__(self, maTaiLieu="TL0001", tenTaiLieu="Lập trình HĐT",
                 tacGia="Ông Văn Thông", ngayXB=None, giaBia=30000, soBanIn=1000):
        """
        Khởi tạo tài liệu:
        - Mặc định: mã "TL0001", tên "Lập trình HĐT", tác giả "Ông Văn Thông",
          ngày hiện tại, giá bìa 30000, số bản in 1000.
        - Khởi tạo đầy đủ tham số khi truyền vào giá trị cụ thể.
        """
        self._maTaiLieu = ""
        self._tenTaiLieu = str(tenTaiLieu).strip() if tenTaiLieu else "Lập trình HĐT"
        self._tacGia = str(tacGia).strip() if tacGia else "Ông Văn Thông"
        self._ngayXB = ngayXB if ngayXB is not None else datetime.now()
        self._giaBia = 0
        self._soBanIn = max(0, soBanIn)

        # Sử dụng setter để đảm bảo tính hợp lệ của dữ liệu
        self.maTaiLieu = maTaiLieu
        self.giaBia = giaBia

    # ----------------- PROPERTIES (GETTER & SETTER) -----------------
    @property
    def maTaiLieu(self):
        return self._maTaiLieu

    @maTaiLieu.setter
    def maTaiLieu(self, value):
        # Yêu cầu: Chiều dài 6 ký tự, bắt đầu bằng "TL", 4 ký tự còn lại là chữ số
        val_str = str(value).strip().upper()
        if len(val_str) == 6 and val_str.startswith("TL") and val_str[2:].isdigit():
            self._maTaiLieu = val_str
            return True
        else:
            print(f"[Cảnh báo] Mã tài liệu '{value}' không hợp lệ! Phải có 6 ký tự, bắt đầu bằng 'TL' và 4 chữ số (VD: TL0001).")
            if not self._maTaiLieu:
                self._maTaiLieu = "TL0001"
            return False

    @property
    def giaBia(self):
        return self._giaBia

    @giaBia.setter
    def giaBia(self, value):
        # Yêu cầu: Giá bìa phải là số dương (> 0)
        try:
            val_num = float(value)
            if val_num > 0:
                self._giaBia = int(val_num)
                return True
            else:
                print(f"[Cảnh báo] Giá bìa {value} không hợp lệ! Phải là số dương (> 0).")
                if self._giaBia <= 0:
                    self._giaBia = 30000
                return False
        except (ValueError, TypeError):
            print(f"[Cảnh báo] Giá bìa '{value}' phải là số hợp lệ!")
            return False

    @property
    def tenTaiLieu(self):
        return self._tenTaiLieu

    @tenTaiLieu.setter
    def tenTaiLieu(self, value):
        if str(value).strip():
            self._tenTaiLieu = str(value).strip()

    @property
    def tacGia(self):
        return self._tacGia

    @tacGia.setter
    def tacGia(self, value):
        if str(value).strip():
            self._tacGia = str(value).strip()

    @property
    def soBanIn(self):
        return self._soBanIn

    @soBanIn.setter
    def soBanIn(self, value):
        try:
            val_int = int(value)
            if val_int >= 0:
                self._soBanIn = val_int
                return True
            print("[Cảnh báo] Số bản in phải >= 0!")
            return False
        except ValueError:
            print("[Cảnh báo] Số bản in phải là số nguyên!")
            return False

    @property
    def ngayXB(self):
        return self._ngayXB

    @ngayXB.setter
    def ngayXB(self, value):
        if isinstance(value, datetime):
            self._ngayXB = value
        elif isinstance(value, str):
            for fmt in ("%d/%m/%Y", "%Y-%m-%d", "%d-%m-%Y"):
                try:
                    self._ngayXB = datetime.strptime(value.strip(), fmt)
                    return True
                except ValueError:
                    pass
            print("[Cảnh báo] Định dạng ngày xuất bản không hợp lệ! Vui lòng dùng dd/mm/yyyy.")
            return False
        return True

    # ----------------- PHƯƠNG THỨC XỬ LÝ NGHIỆP VỤ -----------------
    def GiamGia1(self):
        """
        Giảm giá 1: Giảm giá theo số lượng bản in.
        - Số bản in từ 1000 bản trở lên: giảm 20% tổng giá bìa.
        - Dưới 1000 bản: 0.
        """
        tong_gia_bia = self._soBanIn * self._giaBia
        if self._soBanIn >= 1000:
            return 0.20 * tong_gia_bia
        return 0.0

    @abstractmethod
    def GiamGia2(self):
        """Phương thức trừu tượng: giảm giá theo từng loại tài liệu cụ thể."""
        pass

    def GiamGia(self):
        """Tổng giảm giá = Giảm giá 1 + Giảm giá 2."""
        return self.GiamGia1() + self.GiamGia2()

    def ThanhTien(self):
        """Thành tiền = Số lượng bản in * Giá bìa - Giảm giá."""
        tong_tien = self._soBanIn * self._giaBia
        return max(0.0, tong_tien - self.GiamGia())

    def tinhChietKhau(self):
        """Chiết khấu = Thành tiền * Tỉ lệ chiết khấu (10%)."""
        return self.ThanhTien() * TaiLieu.tiLeChietKhau

    # ----------------- NHẬP / XUẤT THÔNG TIN -----------------
    def nhap(self):
        """Nhập thông tin cơ bản của tài liệu."""
        while True:
            ma = input("Nhập mã tài liệu (dài 6 ký tự, bắt đầu 'TL' + 4 số, VD: TL0001): ").strip()
            val_str = ma.upper()
            if len(val_str) == 6 and val_str.startswith("TL") and val_str[2:].isdigit():
                self._maTaiLieu = val_str
                break
            print("Mã không hợp lệ! Vui lòng nhập lại.")

        while True:
            ten = input("Nhập tên tài liệu: ").strip()
            if ten:
                self._tenTaiLieu = ten
                break
            print("Tên tài liệu không được để trống!")

        while True:
            tg = input("Nhập tác giả: ").strip()
            if tg:
                self._tacGia = tg
                break
            print("Tác giả không được để trống!")

        while True:
            ngay_str = input("Nhập ngày xuất bản (dd/mm/yyyy, Enter để lấy ngày hiện tại): ").strip()
            if not ngay_str:
                self._ngayXB = datetime.now()
                break
            try:
                self._ngayXB = datetime.strptime(ngay_str, "%d/%m/%Y")
                break
            except ValueError:
                print("Ngày không hợp lệ! Định dạng: dd/mm/yyyy.")

        while True:
            try:
                gia = float(input("Nhập giá bìa (> 0): "))
                if gia > 0:
                    self._giaBia = int(gia)
                    break
                print("Giá bìa phải lớn hơn 0!")
            except ValueError:
                print("Giá bìa phải là số hợp lệ!")

        while True:
            try:
                sb = int(input("Nhập số lượng bản in (>= 0): "))
                if sb >= 0:
                    self._soBanIn = sb
                    break
                print("Số lượng bản in phải >= 0!")
            except ValueError:
                print("Số bản in phải là số nguyên!")

    def Xuat(self):
        """Xuất thông tin tài liệu (virtual method)."""
        ngay_str = self._ngayXB.strftime("%d/%m/%Y") if self._ngayXB else ""
        tro_gia_str = ""
        if isinstance(self, ITroGia):
            tro_gia_str = f" | Trợ giá in: {self.tinhTroGia():,.0f} VND"

        print(f"Mã: {self._maTaiLieu} | Tên: {self._tenTaiLieu} | Tác giả: {self._tacGia} | "
              f"Ngày XB: {ngay_str} | Giá bìa: {self._giaBia:,.0f} VND | Bản in: {self._soBanIn:,} | "
              f"Giảm giá: {self.GiamGia():,.0f} VND | Thành tiền: {self.ThanhTien():,.0f} VND | "
              f"Chiết khấu (10%): {self.tinhChietKhau():,.0f} VND{tro_gia_str}")


# =================================================================
# 3. CÁC LỚP CON (KẾ THỪA VÀ CÀI ĐẶT ĐA HÌNH)
# =================================================================

# ----------------- Lớp 1: Sách Giáo Khoa -----------------
class SachGiaoKhoa(TaiLieu, ITroGia):
    """
    Sách giáo khoa có thêm thuộc tính bậc học:
    - Bậc học: "Tiểu học", "THCS", "THPT"
    - Giảm giá 2: Tiểu học giảm 15%, THCS giảm 10%, THPT giảm 5% của tổng giá bìa.
    - Trợ giá in (ITroGia): Tiểu học và THCS trợ giá 1000 đồng/bản in, THPT không trợ giá (0 đồng).
    """
    def __init__(self, maTaiLieu="TL0001", tenTaiLieu="Toán Lớp 1", tacGia="Bộ GD&ĐT",
                 ngayXB=None, giaBia=25000, soBanIn=1500, bacHoc="Tiểu học"):
        super().__init__(maTaiLieu, tenTaiLieu, tacGia, ngayXB, giaBia, soBanIn)
        self.bacHoc = bacHoc

    @property
    def bacHoc(self):
        return self._bacHoc

    @bacHoc.setter
    def bacHoc(self, value):
        val = str(value).strip().lower()
        if "tiểu học" in val or "tieu hoc" in val:
            self._bacHoc = "Tiểu học"
        elif "thcs" in val or "cấp 2" in val or "cap 2" in val:
            self._bacHoc = "THCS"
        elif "thpt" in val or "cấp 3" in val or "cap 3" in val:
            self._bacHoc = "THPT"
        else:
            self._bacHoc = "Tiểu học"

    def GiamGia2(self):
        tong_gia_bia = self._soBanIn * self._giaBia
        if self._bacHoc == "Tiểu học":
            return 0.15 * tong_gia_bia
        elif self._bacHoc == "THCS":
            return 0.10 * tong_gia_bia
        elif self._bacHoc == "THPT":
            return 0.05 * tong_gia_bia
        return 0.0

    def tinhTroGia(self):
        # Trợ giá 1000 đ/bản in cho Tiểu học và THCS
        if self._bacHoc in ["Tiểu học", "THCS"]:
            return 1000 * self._soBanIn
        return 0.0

    def nhap(self):
        super().nhap()
        while True:
            bh = input("Nhập bậc học (1: Tiểu học, 2: THCS, 3: THPT): ").strip()
            if bh in ["1", "Tiểu học", "tieu hoc"]:
                self.bacHoc = "Tiểu học"
                break
            elif bh in ["2", "THCS", "thcs"]:
                self.bacHoc = "THCS"
                break
            elif bh in ["3", "THPT", "thpt"]:
                self.bacHoc = "THPT"
                break
            print("Lựa chọn không hợp lệ! Vui lòng chọn 1, 2 hoặc 3.")

    def Xuat(self):
        print(f"[SGK] ", end="")
        super().Xuat()
        print(f"      -> Bậc học: {self._bacHoc} | Mức trợ giá in ấn: {self.tinhTroGia():,.0f} VND")


# ----------------- Lớp 2: Tài Liệu Tham Khảo -----------------
class TaiLieuThamKhao(TaiLieu):
    """
    Tài liệu tham khảo có thêm thuộc tính chuyên ngành:
    - Chuyên ngành: "Văn học", "Nghệ thuật", "Kỹ thuật"
    - Giảm giá 2: Văn học giảm 7%, Nghệ thuật giảm 5%, Kỹ thuật giảm 3% của tổng giá bìa.
    - Không thuộc chương trình trợ giá in ấn.
    """
    def __init__(self, maTaiLieu="TL0001", tenTaiLieu="Lịch sử Văn học", tacGia="Nhiều tác giả",
                 ngayXB=None, giaBia=40000, soBanIn=500, chuyenNganh="Văn học"):
        super().__init__(maTaiLieu, tenTaiLieu, tacGia, ngayXB, giaBia, soBanIn)
        self.chuyenNganh = chuyenNganh

    @property
    def chuyenNganh(self):
        return self._chuyenNganh

    @chuyenNganh.setter
    def chuyenNganh(self, value):
        val = str(value).strip().lower()
        if "văn học" in val or "van hoc" in val:
            self._chuyenNganh = "Văn học"
        elif "nghệ thuật" in val or "nghe thuat" in val:
            self._chuyenNganh = "Nghệ thuật"
        elif "kỹ thuật" in val or "ky thuat" in val:
            self._chuyenNganh = "Kỹ thuật"
        else:
            self._chuyenNganh = "Văn học"

    def GiamGia2(self):
        tong_gia_bia = self._soBanIn * self._giaBia
        if self._chuyenNganh == "Văn học":
            return 0.07 * tong_gia_bia
        elif self._chuyenNganh == "Nghệ thuật":
            return 0.05 * tong_gia_bia
        elif self._chuyenNganh == "Kỹ thuật":
            return 0.03 * tong_gia_bia
        return 0.0

    def nhap(self):
        super().nhap()
        while True:
            cn = input("Nhập chuyên ngành (1: Văn học, 2: Nghệ thuật, 3: Kỹ thuật): ").strip()
            if cn in ["1", "Văn học", "van hoc"]:
                self.chuyenNganh = "Văn học"
                break
            elif cn in ["2", "Nghệ thuật", "nghe thuat"]:
                self.chuyenNganh = "Nghệ thuật"
                break
            elif cn in ["3", "Kỹ thuật", "ky thuat"]:
                self.chuyenNganh = "Kỹ thuật"
                break
            print("Lựa chọn không hợp lệ! Vui lòng chọn 1, 2 hoặc 3.")

    def Xuat(self):
        print(f"[THAM KHẢO] ", end="")
        super().Xuat()
        print(f"            -> Chuyên ngành: {self._chuyenNganh}")


# ----------------- Lớp 3: Sách Thiếu Nhi -----------------
class SachThieuNhi(TaiLieu, ITroGia):
    """
    Sách thiếu nhi:
    - Giảm giá 2: Tất cả tài liệu loại này được giảm 10% tổng giá bìa.
    - Trợ giá in (ITroGia): Tất cả các sách đều được trợ giá 2000 đồng cho một bản in.
    """
    def __init__(self, maTaiLieu="TL0001", tenTaiLieu="Truyện Cổ Tích Cây Tre Trăm Đốt",
                 tacGia="Dân gian", ngayXB=None, giaBia=20000, soBanIn=2000):
        super().__init__(maTaiLieu, tenTaiLieu, tacGia, ngayXB, giaBia, soBanIn)

    def GiamGia2(self):
        tong_gia_bia = self._soBanIn * self._giaBia
        return 0.10 * tong_gia_bia

    def tinhTroGia(self):
        # Trợ giá 2000 đ/bản in cho tất cả sách thiếu nhi
        return 2000 * self._soBanIn

    def Xuat(self):
        print(f"[THIẾU NHI] ", end="")
        super().Xuat()
        print(f"            -> Đối tượng: Thiếu nhi | Trợ giá in ấn: {self.tinhTroGia():,.0f} VND")


# =================================================================
# 4. CHƯƠNG TRÌNH CHÍNH (main - MINH HỌA VÀ ĐA HÌNH)
# =================================================================
def main():
    print("================================================================================")
    print("     CHƯƠNG TRÌNH QUẢN LÝ XUẤT BẢN TÀI LIỆU NHÀ XUẤT BẢN (MÃ ĐỀ: 03 - ĐỀ 02)")
    print("================================================================================")

    # 1. Minh họa khởi tạo mặc định theo Yêu cầu 3a
    print("\n--- 1. Kiểm tra khởi tạo mặc định (Default Constructor) ---")
    tl_mac_dinh = SachGiaoKhoa()
    tl_mac_dinh.Xuat()

    # 2. Khởi tạo danh sách các tài liệu cụ thể
    ds_tai_lieu = [
        # SGK Tiểu học: số bản in 2000 (>= 1000: giảm 20% + tiểu học 15% = giảm 35%), trợ giá 1000/bản
        SachGiaoKhoa(maTaiLieu="TL0002", tenTaiLieu="Tiếng Việt 1 - Tập 1", tacGia="Nguyễn Minh Thuyết",
                     giaBia=28000, soBanIn=2000, bacHoc="Tiểu học"),

        # SGK THCS: số bản in 1200 (>= 1000: giảm 20% + THCS 10% = giảm 30%), trợ giá 1000/bản
        SachGiaoKhoa(maTaiLieu="TL0003", tenTaiLieu="Toán 8 - Cánh Diều", tacGia="Đỗ Đức Thái",
                     giaBia=32000, soBanIn=1200, bacHoc="THCS"),

        # SGK THPT: số bản in 800 (< 1000: giảm 0% + THPT 5% = giảm 5%), không trợ giá
        SachGiaoKhoa(maTaiLieu="TL0004", tenTaiLieu="Vật Lý 11 - Kết Nối", tacGia="Vũ Văn Hùng",
                     giaBia=35000, soBanIn=800, bacHoc="THPT"),

        # Tham khảo Văn học: số bản in 600 (< 1000: giảm 0% + Văn học 7% = giảm 7%)
        TaiLieuThamKhao(maTaiLieu="TL0005", tenTaiLieu="Tuyển tập Thơ Việt Nam Hiện Đại", tacGia="Mã Giang Lân",
                        giaBia=65000, soBanIn=600, chuyenNganh="Văn học"),

        # Tham khảo Kỹ thuật: số bản in 1500 (>= 1000: giảm 20% + Kỹ thuật 3% = giảm 23%)
        TaiLieuThamKhao(maTaiLieu="TL0006", tenTaiLieu="Giáo trình Trí Tuệ Nhân Tạo", tacGia="Nguyễn Thanh Thủy",
                        giaBia=85000, soBanIn=1500, chuyenNganh="Kỹ thuật"),

        # Sách thiếu nhi: số bản in 3000 (>= 1000: giảm 20% + thiếu nhi 10% = giảm 30%), trợ giá 2000/bản
        SachThieuNhi(maTaiLieu="TL0007", tenTaiLieu="Dế Mèn Phiêu Lưu Ký", tacGia="Tô Hoài",
                     giaBia=45000, soBanIn=3000),

        # Sách thiếu nhi: số bản in 500 (< 1000: giảm 0% + thiếu nhi 10% = giảm 10%), trợ giá 2000/bản
        SachThieuNhi(maTaiLieu="TL0008", tenTaiLieu="Truyện Cổ Andersen", tacGia="Hans Christian Andersen",
                     giaBia=50000, soBanIn=500)
    ]

    print("\n========================= DANH SÁCH TÀI LIỆU XUẤT BẢN =========================")
    for i, tl in enumerate(ds_tai_lieu, start=1):
        print(f"\n[{i}]", end=" ")
        tl.Xuat()

    # Tính toán thống kê
    tong_thanh_tien = sum(tl.ThanhTien() for tl in ds_tai_lieu)
    tong_chiet_khau = sum(tl.tinhChietKhau() for tl in ds_tai_lieu)
    tong_tro_gia = sum(tl.tinhTroGia() for tl in ds_tai_lieu if isinstance(tl, ITroGia))

    print("\n=========================== THỐNG KÊ DOANH THU ===========================")
    print(f"-> Tổng Thành tiền các tài liệu              : {tong_thanh_tien:>18,.0f} VND")
    print(f"-> Tổng Chiết khấu (10% của Thành tiền)      : {tong_chiet_khau:>18,.0f} VND")
    print(f"-> Tổng Trợ giá in ấn (Interface ITroGia)    : {tong_tro_gia:>18,.0f} VND")
    print(f"--------------------------------------------------------------------------")
    print(f"=> DOANH THU THỰC TẾ (Sau chiết khấu & trợ giá): {tong_thanh_tien - tong_chiet_khau - tong_tro_gia:>15,.0f} VND")
    print("==========================================================================")

    # Tìm tài liệu có thành tiền lớn nhất
    tl_max = max(ds_tai_lieu, key=lambda x: x.ThanhTien())
    print(f"\n=> Tài liệu có Thành tiền cao nhất: {tl_max.tenTaiLieu} ({tl_max.maTaiLieu}) với {tl_max.ThanhTien():,.0f} VND")

    # Danh sách các tài liệu được hỗ trợ trợ giá in ấn
    print("\n--- DANH SÁCH TÀI LIỆU ĐƯỢC TRỢ GIÁ IN ẤN (IMPLEMENT ITroGia) ---")
    for tl in ds_tai_lieu:
        if isinstance(tl, ITroGia) and tl.tinhTroGia() > 0:
            print(f"- {tl.tenTaiLieu} ({tl.maTaiLieu}): Trợ giá {tl.tinhTroGia():,.0f} VND")


if __name__ == "__main__":
    main()
