# SỔ TAY "BẪY ĐỀ THI" VÀ CÁC LỖI THƯỜNG GẶP TRONG OOP (LAB 4 & LAB 5)

Tổng hợp các "điểm đau" (pain points), lỗi logic kinh điển và những bẫy trừ điểm mà sinh viên hay mắc phải nhất khi làm bài kiểm tra phần OOP cơ bản và Đóng gói (Encapsulation).

---

## MỤC LỤC
1. [Bẫy 1: Bài Toán Tam Giác (Triangle) - Sai Số Thực & Thứ Tự Xét](#1-bẫy-1-bài-toán-tam-giác-triangle)
2. [Bẫy 2: Ngày Tháng Năm (Date) & Thuật Toán Tính Tuổi](#2-bẫy-2-ngày-tháng-năm-date--tính-tuổi)
3. [Bẫy 3: Đóng Gói (Encapsulation) - Biến Private `__` & Name Mangling](#3-bẫy-3-đóng-gói-encapsulation)
4. [Bẫy 4: Validate Trong Constructor `__init__` vs Setter](#4-bẫy-4-validate-trong-constructor-vs-setter)
5. [Bẫy 5: Crash Do Ép Kiểu & Vòng Lặp Nhập Dữ Liệu](#5-bẫy-5-crash-do-ép-kiểu--vòng-lặp-nhập)
6. [Bẫy 6: Bài Toán Phân Số (Fraction) & Chia Cho 0](#6-bẫy-6-bài-toán-phân-số-fraction)
7. [Bẫy 7: Xóa Phần Tử Khi Đang Duyệt Danh Sách (List Modification)](#7-bẫy-7-xóa-phần-tử-khi-duyệt-danh-sách)

---

## 1. BẪY 1: BÀI TOÁN TAM GIÁC (TRIANGLE)

### ❌ Lỗi 1: Quên điều kiện cạnh dương
Nhiều bạn chỉ kiểm tra bất đẳng thức tam giác:
```python
# SAI / THIẾU:
if a + b > c and a + c > b and b + c > a:  # Nếu nhập a = -3, b = -4, c = -5 sẽ ra sai!
```
👉 **ĐÚNG:** Bắt buộc 3 cạnh phải lớn hơn 0 trước:
```python
def is_valid(self):
    return (self.a > 0 and self.b > 0 and self.c > 0 and
            self.a + self.b > self.c and
            self.a + self.c > self.b and
            self.b + self.c > self.a)
```

### ❌ Lỗi 2: Kiểm tra Pitago bị sai số thực (Floating Point Error)
```python
# SAI:
if a**2 + b**2 == c**2:  # Nguy hiểm! Số thực trong máy tính bị lệch dấu phẩy động
```
👉 **ĐÚNG:** Sắp xếp 3 cạnh để xác định cạnh lớn nhất làm cạnh huyền `c`, sau đó dùng `math.isclose()`:
```python
import math

a, b, c = sorted([self.a, self.b, self.c])  # c luôn là cạnh lớn nhất
is_vuong = math.isclose(a**2 + b**2, c**2, rel_tol=1e-5)
```

### ❌ Lỗi 3: Sai thứ tự ưu tiên khi phân loại tam giác
Nếu bạn kiểm tra "Tam giác cân" trước thì **Tam giác đều** sẽ bị nhận nhầm là tam giác cân (vì tam giác đều cũng có 2 cạnh bằng nhau)!
👉 **Thứ tự chuẩn bắt buộc:**
1. **Đều** (`a == b == c`)
2. **Vuông cân** (`(a == b or b == c or a == c) and is_vuong`)
3. **Cân** (`a == b or b == c or a == c`)
4. **Vuông** (`is_vuong`)
5. **Thường**

---

## 2. BẪY 2: NGÀY THÁNG NĂM (DATE) & TÍNH TUỔI

### ❌ Lỗi 1: Viết thiếu điều kiện năm nhuận
Nhiều bạn nhớ nhầm chỉ cần chia hết cho 4:
```python
# SAI:
return self.year % 4 == 0  # Năm 1900 chia hết cho 4 nhưng KHÔNG PHẢI năm nhuận!
```
👉 **ĐÚNG:** Năm chia hết cho 4 nhưng không chia hết cho 100, HOẶC chia hết cho 400:
```python
def is_leap_year(self):
    return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)
```

### ❌ Lỗi 2: Số ngày trong tháng 2
Nhiều bạn fix cứng tháng 2 có 28 ngày mà quên năm nhuận có 29 ngày:
```python
def days_in_month(self):
    if self.month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif self.month in (4, 6, 9, 11):
        return 30
    elif self.month == 2:
        return 29 if self.is_leap_year() else 28
    return 0
```

### ❌ Lỗi 3: Tính tuổi "trừ chay" bằng năm
```python
# SAI:
tuoi = today.year - birth.year  
# Giả sử hôm nay 07/10/2026, người sinh 20/12/2004 CHƯA ĐẾN SINH NHẬT nên mới 21 tuổi, công thức trên sẽ ra 22 tuổi (SAI)!
```
👉 **ĐÚNG:** So sánh cặp `(month, day)` để trừ 1 nếu chưa tới sinh nhật:
```python
def calculate_age(self):
    today = date.today()
    birth = self.__ngay_sinh
    # Trừ đi 1 nếu (tháng, ngày) hiện tại nhỏ hơn (tháng, ngày) sinh nhật
    tuoi = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
    return tuoi
```

---

## 3. BẪY 3: ĐÓNG GÓI (ENCAPSULATION)

### ❌ Lỗi 1: Truy cập biến Private từ bên ngoài
```python
class Person:
    def __init__(self, ten):
        self.__ten = ten

p = Person("An")
print(p.__ten)  # ❌ LỖI: AttributeError: 'Person' object has no attribute '__ten'
```
- **Nguyên nhân:** Python đổi tên biến `__ten` thành `_Person__ten` (cơ chế Name Mangling).
- 👉 **Khắc phục:** Phải luôn thông qua Getter: `p.get_ten()`.

### ❌ Lỗi 2: Phân biệt `_` (Protected) và `__` (Private)
- `self.ten`: Public (ai cũng đọc/ghi được).
- `self._ten`: Protected (quy ước nội bộ trong lớp và lớp con, vẫn gọi được từ ngoài nhưng không khuyến khích).
- `self.__ten`: Private (bảo vệ nghiêm ngặt, chỉ nội bộ class đó mới dùng được).

---

## 4. BẪY 4: VALIDATE TRONG CONSTRUCTOR VS SETTER

### ❌ Lỗi sinh viên hay gặp:
Viết setter rất kỹ nhưng trong `__init__` lại gán biến trực tiếp mà không kiểm tra:
```python
class Customer:
    def __init__(self, tong_tien=0):
        # NGUY HIỂM: Nếu ai đó gọi Customer(tong_tien=-500) thì tiền âm vẫn lọt vào!
        self.__tong_tien = tong_tien  

    def set_tong_tien(self, tong_tien):
        if tong_tien < 0:
            return False
        self.__tong_tien = tong_tien
        return True
```
👉 **Cách khắc phục chuẩn:** Gán giá trị an toàn ngay trong `__init__` hoặc gọi chính setter:
```python
def __init__(self, tong_tien=0):
    self.__tong_tien = tong_tien if tong_tien >= 0 else 0
    # Hoặc: self.set_tong_tien(tong_tien)
```

---

## 5. BẪY 5: CRASH DO ÉP KIỂU & VÒNG LẶP NHẬP DỮ LIỆU

### ❌ Lỗi 1: Không bọc `try ... except ValueError`
Khi người dùng vô tình gõ chữ cái vào ô nhập số thực / số nguyên:
```python
# CRASH NGAY LẬP TỨC:
r = float(input("Nhập bán kính: ")) # Người dùng nhập "abc" -> ValueError
```
👉 **ĐÚNG:** Luôn bọc trong `try ... except`:
```python
while True:
    try:
        r = float(input("Nhập bán kính: "))
        if r > 0:
            self.radius = r
            break
        print("Bán kính phải > 0!")
    except ValueError:
        print("Lỗi: Phải nhập số hợp lệ!")
```

### ❌ Lỗi 2: Nhập sai một lần là tắt luôn chương trình
Trong hàm `inputInfo()`, nếu người dùng nhập sai dữ liệu mà bạn chỉ `print("Lỗi")` rồi kết thúc hàm thì đối tượng sẽ mang dữ liệu rác hoặc giá trị mặc định.
👉 **ĐÚNG:** Luôn dùng vòng lặp `while True` để bắt nhập lại cho đến khi đúng mới dừng.

---

## 6. BẪY 6: BÀI TOÁN PHÂN SỐ (FRACTION)

### ❌ Lỗi 1: Mẫu số bằng 0
Mẫu số của phân số **tuyệt đối không được bằng 0**:
```python
def set_mau_so(self, mau):
    if mau == 0:
        print("Lỗi: Mẫu số không thể bằng 0!")
        return False
    self.mau = mau
    return True
```

### ❌ Lỗi 2: Không tối giản phân số sau khi tính toán
Sau khi cộng, trừ, nhân, chia 2 phân số, luôn phải rút gọn bằng Ước chung lớn nhất (`math.gcd`):
```python
import math

def rut_gon(self):
    ucln = math.gcd(self.tu, self.mau)
    self.tu //= ucln
    self.mau //= ucln
    # Đẩy dấu âm lên tử số nếu mẫu số âm:
    if self.mau < 0:
        self.tu = -self.tu
        self.mau = -self.mau
```

---

## 7. BẪY 7: XÓA PHẦN TỬ KHI ĐANG DUYỆT DANH SÁCH

Khi làm bài Giỏ hàng ([bai7_cart.py](file:///d:/python/ontapkiemtra/labpython/buoi4/btvn/bai7_cart.py)) hoặc Quản lý sản phẩm ([bai6_product_manager.py](file:///d:/python/ontapkiemtra/labpython/buoi4/btvn/bai6_product_manager.py)):

### ❌ Lỗi kinh điển (Index Shifting Bug):
```python
# SAI RẤT NẶNG:
for sp in self.danh_sach:
    if sp.so_luong == 0:
        self.danh_sach.remove(sp)  # Khi xoá phần tử, danh sách bị co lại, phần tử kế tiếp sẽ BỊ BỎ QUA không được duyệt!
```
👉 **ĐÚNG: Cách 1 - Duyệt trên bản copy của danh sách:**
```python
for sp in self.danh_sach[:]:  # Dùng [:] để tạo bản copy
    if sp.so_luong == 0:
        self.danh_sach.remove(sp)
```
👉 **ĐÚNG: Cách 2 - Dùng List Comprehension tạo danh sách mới (Khuyên dùng):**
```python
self.danh_sach = [sp for sp in self.danh_sach if sp.so_luong > 0]
```
