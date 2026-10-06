# PHÂN TÍCH CHI TIẾT BÀI 4 - LAB 7 BTVN
## ĐỀ TÀI: HỆ THỐNG QUẢN LÝ GIAO DỊCH (VÀNG & TIỀN TỆ)

Tài liệu phân tích cấu trúc mã nguồn file [`bai4.py`](file:///d:/python/ontapkiemtra/labpython/buoi7/btvn/bai4.py) phục vụ ôn tập kiểm tra OOP.

---

## 1. SƠ ĐỒ CẤU TRÚC LỚP (CLASS ARCHITECTURE)

```
                     ┌─────────────────────────────────────────┐
                     │          class GiaoDich (Lớp Cha)       │
                     ├─────────────────────────────────────────┤
                     │ - __ma: str                             │
                     │ - __ngay_gd: datetime.date              │
                     │ - __don_gia: float                      │
                     │ - __so_luong: int                       │
                     ├─────────────────────────────────────────┤
                     │ + get_*() / set_*() (Validation)        │
                     │ + thanh_tien()                          │
                     │ + xuat()                                │
                     └────────────────────┬────────────────────┘
                                          │ Kế thừa
                 ┌────────────────────────┴────────────────────────┐
                 │                                                 │
┌─────────────────────────────────┐               ┌─────────────────────────────────┐
│     class GiaoDichVang          │               │      class GiaoDichTienTe       │
├─────────────────────────────────┤               ├─────────────────────────────────┤
│ - __loai_vang: str              │               │ - __loai_tien_te: str           │
│   (18k, 24k, 9999)              │               │   (USD, EUR, AUD)               │
│                                 │               │ - __loai_gd: str (mua / ban)    │
├─────────────────────────────────┤               ├─────────────────────────────────┤
│ + thanh_tien()                  │               │ + thanh_tien()                  │
│   = so_luong * don_gia          │               │   = Mua: SL * ĐG                │
│ + xuat()                        │               │   = Bán: (SL * ĐG) * 1.05       │
│                                 │               │ + xuat()                        │
└─────────────────────────────────┘               └─────────────────────────────────┘
                                ▲                                   ▲
                                └─────────────────┬─────────────────┘
                                                  │ Lưu vào danh_sach
                                ┌─────────────────┴─────────────────┐
                                │       class QuanLyGiaoDich        │
                                ├───────────────────────────────────┤
                                │ - danh_sach: list                 │
                                ├───────────────────────────────────┤
                                │ + them_giao_dich(gd)              │
                                │ + xuat_danh_sach()                │
                                │ + tong_so_luong_vang()            │
                                │ + tong_so_luong_tien_te()         │
                                │ + thong_ke()                      │
                                └───────────────────────────────────┘
```

---

## 2. PHÂN TÍCH TỪNG THÀNH PHẦN

### A. Lớp Cha: `GiaoDich` (Dòng 4 - 84)
Đóng vai trò chứa các thuộc tính và hành vi chung nhất của mọi giao dịch.

1. **Thuộc tính Private (`__`)**:
   - `self.__ma`: Mã định danh giao dịch.
   - `self.__ngay_gd`: Ngày diễn ra giao dịch (kiểu `datetime.date`).
   - `self.__don_gia`: Giá trên một đơn vị.
   - `self.__so_luong`: Số lượng giao dịch.

2. **Các Setter kiểm tra tính hợp lệ (Validation)**:
   - `set_ma(ma)`: Không cho phép chuỗi rỗng (`if not ma: return False`).
   - `set_ngay_gd(ngay)`:
     - Cho phép truyền chuỗi định dạng `"dd/mm/yyyy"` rồi chuyển thành `datetime.date`.
     - Kiểm tra ngày **không được lớn hơn hôm nay**: `if ngay > datetime.date.today(): return False`.
   - `set_don_gia(don_gia)`: Dùng `try ... float(don_gia) ... except ValueError`, bắt buộc `don_gia >= 0`.
   - `set_so_luong(so_luong)`: Dùng `try ... int(so_luong) ... except ValueError`, bắt buộc `so_luong > 0`.

3. **Phương thức cơ bản**:
   - `thanh_tien()`: Mặc định tính `so_luong * don_gia`.
   - `get_ngay_gd_str()`: Định dạng ngày thành `"dd/mm/yyyy"` bằng `.strftime("%d/%m/%Y")`.

---

### B. Lớp Con 1: `GiaoDichVang` (Dòng 86 - 111)
Đại diện cho giao dịch mua bán vàng, kế thừa từ `GiaoDich`.

1. **Khởi tạo và Kế thừa (`super()`)**:
   ```python
   def __init__(self, ma="", ngay_gd=None, don_gia=0.0, so_luong=0, loai_vang=""):
       super().__init__(ma, ngay_gd, don_gia, so_luong)  # Gọi hàm tạo lớp cha
       self.__loai_vang = loai_vang                      # Thuộc tính riêng
   ```

2. **Kiểm tra danh sách hợp lệ (Whitelist)**:
   - Biến lớp: `LOAI_VANG_HOP_LE = ["18k", "24k", "9999"]`
   - Trong `set_loai_vang`: Kiểm tra nếu `loai_vang.lower()` không nằm trong danh sách thì báo lỗi.

3. **Công thức tính tiền (Ghi đè - Override)**:
   - `thanh_tien()` = `self.get_so_luong() * self.get_don_gia()`

---

### C. Lớp Con 2: `GiaoDichTienTe` (Dòng 113 - 158)
Đại diện cho giao dịch ngoại tệ, kế thừa từ `GiaoDich`.

1. **Thuộc tính riêng**:
   - `__loai_tien_te`: `"USD"`, `"EUR"`, `"AUD"` (kiểm tra theo `LOAI_TIEN_HOP_LE`).
   - `__loai_gd`: `"mua"` hoặc `"bán"`.
     - `set_loai_gd`: Cho phép nhập số `"1"` / chữ `"mua"` hoặc `"0"` / `"bán"`.

2. **Công thức tính tiền đặc thù**:
   - Nếu mua: `Thành tiền = Số lượng * Tỷ giá`
   - Nếu bán: `Thành tiền = (Số lượng * Tỷ giá) * 1.05` (có thêm 5% chênh lệch/phí)
   ```python
   def thanh_tien(self):
       if self.__loai_gd == "mua":
           return self.get_so_luong() * self.get_don_gia()
       else:
           return (self.get_so_luong() * self.get_don_gia()) * 1.05
   ```

---

### D. Lớp Quản Lý: `QuanLyGiaoDich` (Dòng 160 - 201)
Chịu trách nhiệm quản lý danh sách tập hợp các giao dịch.

1. **Lưu trữ đa hình (Polymorphism)**:
   - Thuộc tính `self.danh_sach = []` chứa lẫn lộn cả `GiaoDichVang` và `GiaoDichTienTe`.

2. **Kỹ thuật lọc đối tượng bằng `isinstance`**:
   - Tính tổng số lượng vàng:
     ```python
     sum(gd.get_so_luong() for gd in self.danh_sach if isinstance(gd, GiaoDichVang))
     ```
   - Tính tổng số lượng tiền tệ:
     ```python
     sum(gd.get_so_luong() for gd in self.danh_sach if isinstance(gd, GiaoDichTienTe))
     ```
   - Tính tổng tiền của từng loại tương tự với `gd.thanh_tien()`.

---

### E. Hàm Nhập Liệu & Điều Khiển: `nhap_giao_dich` & `main` (Dòng 203 - 302)
1. Sử dụng kỹ thuật **Validate nhiều tầng bằng vòng lặp `while True`**:
   - Nhập mã GD -> đúng mới thoát lặp.
   - Nhập ngày -> đúng định dạng và `<=` hôm nay mới thoát lặp.
   - Nhập số lượng -> `> 0` mới thoát lặp.
   - Chọn loại: Nhập `1` -> tạo `GiaoDichVang`; Nhập `2` -> tạo `GiaoDichTienTe`.
2. Sau khi nhập thành công, gọi `ql.them_giao_dich(gd)`.
3. Hỏi người dùng muốn tiếp tục (`1`) hay dừng lại (`0`).

---

## 3. TỔNG HỢP CÁC KỸ THUẬT OOP CẦN NHỚ TRONG BÀI NÀY

| Kỹ thuật OOP | Thể hiện trong bài 4 | Ý nghĩa / Cách viết |
| :--- | :--- | :--- |
| **Encapsulation (Đóng gói)** | `self.__ma`, `self.__don_gia`, ... | Dùng 2 gạch dưới `__` giấu dữ liệu; giao tiếp qua `get_()` và `set_()`. |
| **Inheritance (Kế thừa)** | `class GiaoDichVang(GiaoDich):` | Kế thừa thuộc tính và phương thức từ lớp cha; dùng `super().__init__(...)`. |
| **Polymorphism (Đa hình)** | `gd.thanh_tien()`, `gd.xuat()` | Cùng 1 hàm `thanh_tien()` nhưng Vàng tính khác, Tiền tệ tính khác tuỳ vào đối tượng thực tế. |
| **Object Type Checking** | `isinstance(gd, GiaoDichVang)` | Kiểm tra đối tượng `gd` thuộc lớp cụ thể nào để thống kê phân loại. |
| **String Formatting** | `f"{self.get_don_gia():.0f}"` | In số thực không lấy phần thập phân (`:.0f`) hoặc định dạng tiền tệ có dấu phẩy (`:,.0f`). |

---

## 4. CHECKLIST BƯỚC LÀM NHANH NẾU GẶP ĐỀ TƯƠNG TỰ KHI THI

- [ ] **Bước 1**: Viết lớp cha chung trước (`GiaoDich`), viết đủ `__init__`, các cặp `get/set` kèm điều kiện `if ... return False / True`.
- [ ] **Bước 2**: Viết hàm xử lý ngày `strptime` và kiểm tra `<=` ngày hôm nay.
- [ ] **Bước 3**: Tạo các lớp con, nhớ dùng `super().__init__(...)` và thêm thuộc tính riêng.
- [ ] **Bước 4**: Ghi đè (override) hàm tính tiền `thanh_tien()` theo đúng công thức đề bài của từng lớp con.
- [ ] **Bước 5**: Tạo lớp danh sách quản lý, dùng `self.danh_sach.append(obj)` và dùng `isinstance(x, Lop)` để tính tổng/thống kê.
- [ ] **Bước 6**: Viết hàm `main()` có vòng lặp nhập dữ liệu và menu lựa chọn.
