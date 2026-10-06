# PHÂN TÍCH CHI TIẾT BÀI 5 - LAB 7
## ĐỀ TÀI: QUẢN LÝ SINH VIÊN VỚI CLASS ATTRIBUTE & CLASSMETHOD

Tài liệu phân tích cấu trúc mã nguồn file [`bai5.py`](file:///d:/python/ontapkiemtra/labpython/buoi7/bai5.py) phục vụ ôn tập kiểm tra OOP Python.

---

## 1. TỔNG QUAN KIẾN TRÚC CLASS `SinhVien`

Khác với Bài 4 (tạo class Quản lý riêng), Bài 5 sử dụng mô hình **Biến lớp dùng chung (`Class Attribute`)** và **Phương thức của lớp (`@classmethod`)**.

```
┌────────────────────────────────────────────────────────┐
│                   class SinhVien                       │
├────────────────────────────────────────────────────────┤
│ [Biến Class Dùng Chung]:                               │
│ - ds = []  (Danh sách lưu tất cả sinh viên toàn trường)│
│                                                        │
│ [Thuộc Tính Đối Tượng (Private)]:                      │
│ - __ma_sv: str (Đúng 10 ký tự, có mã hệ ở vị trí [2:4])│
│ - __ten_sv: str (Tối đa 20 ký tự)                      │
│ - __nam_sinh: int (1900 < năm <= năm hiện tại)         │
│ - __diem_trung_binh: float (0.0 đến 10.0)              │
├────────────────────────────────────────────────────────┤
│ [Getter / Setter]:                                     │
│ + get_ma_sv() / set_ma_sv(ma_sv)                       │
│ + get_ten_sv() / set_ten_sv(ten_sv)                   │
│ + get_nam_sinh() / set_nam_sinh(nam_sinh)             │
│ + get_diem_trung_binh() / set_diem_trung_binh(dtb)     │
│                                                        │
│ [Instance Methods (Phương thức đối tượng)]:            │
│ + input_info(): Nhập & validate vòng lặp while True    │
│ + them_vao_ds_sinh_vien(): Kiểm tra trùng mã & append  │
│ + xet_dieu_kien(): Điểm TB >= 5                        │
│ + sinh_vien_da_20(): Kiểm tra tuổi >= 20               │
│ + display(): In thông tin cá nhân                      │
│                                                        │
│ [Class Methods (@classmethod)]:                        │
│ + dem_sinh_vien_dh(cls): Đếm SV hệ Đại Học (ma[2:4])   │
│ + dem_sinh_vien_ten_lan(cls): Đếm SV có tên "Lan"      │
│ + dem_sinh_vien_ho_phan(cls): Đếm SV có họ "Phan"      │
└────────────────────────────────────────────────────────┘
```

---

## 2. PHÂN TÍCH CHI TIẾT CÁC THÀNH PHẦN

### A. Biến Lớp (Class Attribute) `ds = []` (Dòng 4)
- **Khai báo:** Đặt ngay dưới tên class:
  ```python
  class SinhVien:
      ds = []  # Danh sách dùng chung cho toàn bộ sinh viên
  ```
- **Ý nghĩa:** Mọi đối tượng sinh viên được tạo ra đều có thể truy cập danh sách này thông qua `SinhVien.ds` hoặc `cls.ds`.

---

### B. Bộ Getter / Setter & Điều Kiện Validation (Dòng 11 - 50)

| Thuộc tính | Điều kiện kiểm tra trong Setter | Cú pháp trong code |
| :--- | :--- | :--- |
| **Mã SV** (`__ma_sv`) | Bắt buộc đúng 10 ký tự | `if len(ma_sv) != 10: return False` |
| **Tên SV** (`__ten_sv`) | Không rỗng và tối đa 20 ký tự | `if len(ten_sv.strip()) == 0 or len(ten_sv) > 20: return False` |
| **Năm sinh** (`__nam_sinh`) | Lớn hơn 1900 và không vượt quá năm nay | `nam_hien_tai = int(datetime.date.today().year)`<br>`if nam_sinh <= 1900 or nam_sinh > nam_hien_tai: return False` |
| **Điểm TB** (`__diem_trung_binh`) | Thang điểm từ 0.0 đến 10.0 | `if dtb < 0.0 or dtb > 10.0: return False` |

---

### C. Phương Thức Nhập & Thêm Vào Danh Sách

#### 1. Hàm `input_info(self)` (Dòng 51 - 77)
Sử dụng mô hình chuẩn để nhập dữ liệu an toàn:
- Dùng `while True` gọi các hàm `setter`.
- Với năm sinh và điểm số: Bọc trong khối `try ... except ValueError` để chống crash khi người dùng nhập chữ.

#### 2. Hàm `them_vao_ds_sinh_vien(self)` (Dòng 78 - 86)
- **Kiểm tra trùng mã:** Duyệt qua danh sách chung `SinhVien.ds`:
  ```python
  for sv in SinhVien.ds:
      if sv.get_ma_sv() == self.get_ma_sv():
          print("Sinh viên này đã tồn tại trong danh sách!")
          return False
  ```
- **Thêm đối tượng:** Nếu không trùng mã thì thêm chính đối tượng hiện tại (`self`) vào danh sách:
  ```python
  SinhVien.ds.append(self)
  return True
  ```

---

### D. Các Phương Thức Lớp Thống Kê (`@classmethod`)

Đây là điểm nổi bật nhất của bài 5: Sử dụng `@classmethod` với tham số đại diện lớp là `cls`.

#### 1. Đếm sinh viên hệ Đại học: `dem_sinh_vien_dh(cls)` (Dòng 100 - 109)
- **Kỹ thuật cắt chuỗi (Slicing):** Cắt 2 ký tự từ vị trí index 2 đến index 3 (`ma[2:4]`).
  ```python
  chuoi_he_da_hoc = ma[2:4]
  if chuoi_he_da_hoc == "DH":
      dem += 1
  ```
  *(Ví dụ mã: `21DH110123` ➡️ `ma[2:4]` là `"DH"`)*

#### 2. Đếm sinh viên có tên "Lan": `dem_sinh_vien_ten_lan(cls)` (Dòng 111 - 121)
- **Kỹ thuật tách từ bằng `.split()`:**
  - `ho_va_ten = "Nguyen Thi Lan"`
  - `cac_tu = ho_va_ten.split()` ➡️ `['Nguyen', 'Thi', 'Lan']`
  - **Tên luôn là phần tử cuối cùng:** `cac_tu[-1]`
  - Kiểm tra không phân biệt hoa thường: `if cac_tu[-1].lower() == "lan": dem += 1`

#### 3. Đếm sinh viên có họ "Phan": `dem_sinh_vien_ho_phan(cls)` (Dòng 123 - 133)
- **Họ luôn là phần tử đầu tiên:** `cac_tu[0]`
- Kiểm tra: `if cac_tu[0].lower() == "phan": dem += 1`

---

### E. Hàm `main()` Điều Phối Chương Trình (Dòng 138 - 158)
1. Nhập số lượng `n`.
2. Vòng lặp `for i in range(n):`
   - Khởi tạo `sv = SinhVien()`
   - Gọi `sv.input_info()`
   - Gọi `sv.them_vao_ds_sinh_vien()`
3. In danh sách bằng cách duyệt `for sv in SinhVien.ds: sv.display()`.
4. Gọi các hàm `@classmethod` trực tiếp từ tên lớp `SinhVien.dem_...()`.

---

## 3. ĐIỂM ĂN ĐIỂM & KỸ THUẬT QUAN TRỌNG CẦN NHỚ

1. **Hiểu rõ `@classmethod` vs Instance Method**:
   - `input_info(self)`, `display(self)` có `self` vì chạy cho **từng sinh viên**.
   - `dem_sinh_vien_dh(cls)` có `@classmethod` và `cls` vì chạy thống kê trên **toàn bộ danh sách của lớp `cls.ds`**.
2. **Kỹ thuật xử lý Họ và Tên Tiếng Việt**:
   - Tách từ: `cac_tu = chuoi.strip().split()`
   - Họ: `cac_tu[0]`
   - Tên: `cac_tu[-1]`
   - Đệm: `cac_tu[1:-1]`
3. **Cắt chuỗi mã định danh (Sub-string Slicing)**:
   - `chuoi[start:end]` lấy từ index `start` đến `end - 1`.
