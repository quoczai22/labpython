# SỔ TAY ÔN TẬP PYTHON OOP: GETTER, SETTER, ABSTRACT & METHOD

Tài liệu được tổng hợp bám sát cấu trúc các bài thực hành và đề thi trong thư mục thực hành Python.

---

## MỤC LỤC
1. [Getter & Setter (Tính Đóng Gói - Encapsulation)](#1-getter--setter-tính-đóng-gói)
2. [Bảng Điều Kiện Setter Thường Gặp & Cách Viết Chuẩn](#2-bảng-điều-kiện-setter-thường-gặp)
3. [Mẫu Vòng Lặp Nhập Kết Hợp Setter (Validation)](#3-mẫu-vòng-lặp-nhập-kết-hợp-setter)
4. [Lớp & Phương Thức Trừu Tượng (Abstract Class & Method)](#4-lớp--phương-thức-trừu-tượng-abstract)
5. [Phân Biệt Các Loại Method Trong OOP](#5-phân-biệt-các-loại-method-trong-oop)
6. [Bài Mẫu Chuẩn Tổng Hợp Đi Thi](#6-bài-mẫu-chuẩn-tổng-hợp-đi-thi)
7. [Các Lỗi Sai Kinh Điển Cần Tuyệt Đối Tránh](#7-các-lỗi-sai-kinh-điển-cần-tránh)

---

## 1. GETTER & SETTER (TÍNH ĐÓNG GÓI)

### Tại sao phải dùng?
- **Thuộc tính Private (`__ten_thuoc_tinh`)**: Ngăn chặn việc truy cập hoặc sửa đổi dữ liệu trực tiếp bừa bãi từ bên ngoài.
- **Getter**: Cung cấp quyền đọc dữ liệu an toàn.
- **Setter**: Cung cấp quyền gán dữ liệu kèm **kiểm tra tính hợp lệ (Validation)** trước khi lưu.

### Cú pháp cơ bản
```python
class SinhVien:
    def __init__(self, ma=""):
        self.__ma = ma  # Private attribute (2 dấu gạch dưới)

    # GETTER
    def get_ma(self):
        return self.__ma

    # SETTER: Luôn trả về True nếu hợp lệ, False nếu lỗi
    def set_ma(self, ma):
        ma = str(ma).strip()
        if not ma:
            print("Lỗi: Mã sinh viên không được để trống!")
            return False
        
        self.__ma = ma
        return True
```

---

## 2. BẢNG ĐIỀU KIỆN SETTER THƯỜNG GẶP

Dưới đây là các dạng điều kiện bắt buộc hay xuất hiện trong các bài lab:

| Trường dữ liệu | Điều kiện IF báo lỗi (Trả về False) | Giải thích ngắn gọn |
| :--- | :--- | :--- |
| **Chuỗi để trống** | `if not str(val).strip():` | Bỏ dấu cách 2 đầu, nếu rỗng thì báo lỗi |
| **Độ dài cố định** (Mã SV = 10 ký tự) | `if len(str(val).strip()) != 10:` | Khác 10 ký tự thì báo lỗi |
| **Độ dài tối đa** (Tên từ 1 - 20 ký tự) | `if len(val) == 0 or len(val) > 20:` | Rỗng hoặc dài hơn 20 ký tự thì báo lỗi |
| **Số lượng** (Phải là số nguyên > 0) | `if val <= 0:` | Nhỏ hơn hoặc bằng 0 thì báo lỗi |
| **Đơn giá / Tiền** (Không được âm) | `if val < 0:` | Nhỏ hơn 0 thì báo lỗi |
| **Điểm số** (Thang điểm 0 - 10) | `if val < 0 or val > 10:` | Ngoài khoảng 0 đến 10 thì báo lỗi |
| **Năm sinh** | `import datetime`<br>`nam_nay = datetime.date.today().year`<br>`if val <= 1900 or val > nam_nay:` | Hoặc viết gộp:<br>`if val <= 1900 or val > datetime.date.today().year:` |
| **Lựa chọn cho phép** (Whitelist) | `if val.lower() not in ["18k", "24k", "9999"]:` | Không nằm trong danh sách thì báo lỗi |
| **Ép kiểu số an toàn** | `try: val = float(val)`<br>`except ValueError: return False` | Bắt lỗi nếu người dùng nhập chữ thay vì số |

---

## 3. MẪU VÒNG LẶP NHẬP KẾT HỢP SETTER

Trong các phương thức nhập dữ liệu (`nhap` hoặc `input_info`), sử dụng vòng lặp `while True` để bắt người dùng nhập đến khi thỏa mãn điều kiện của setter mới cho đi tiếp:

```python
def input_info(self):
    print("--- NHẬP THÔNG TIN ---")
    
    # 1. Nhập mã (chuỗi)
    while True:
        ma = input("Nhập mã: ")
        if self.set_ma(ma):
            break  # Nhập đúng -> Thoát vòng lặp

    # 2. Nhập đơn giá (số thực)
    while True:
        gia = input("Nhập giá: ")
        if self.set_gia(gia):
            break

    # 3. Nhập số lượng (số nguyên)
    while True:
        sl = input("Nhập số lượng: ")
        if self.set_so_luong(sl):
            break
```

---

## 4. LỚP & PHƯƠNG THỨC TRỪU TƯỢNG (ABSTRACT)

### Nguyên tắc cốt lõi:
1. Import từ thư viện: `from abc import ABC, abstractmethod`
2. Lớp trừu tượng phải kế thừa từ `ABC`.
3. Phương thức trừu tượng phải gắn decorator `@abstractmethod` và thân hàm dùng `pass`.
4. **Không thể tạo đối tượng** trực tiếp từ lớp trừu tượng (Ví dụ: `HinhHoc()` sẽ báo lỗi `TypeError`).
5. Lớp con kế thừa **BẮT BUỘC phải cài đặt lại (override) TOÀN BỘ** các phương thức `@abstractmethod`.

### Cú pháp chuẩn
```python
from abc import ABC, abstractmethod

# Lớp trừu tượng cha
class HinhHoc(ABC):
    @abstractmethod
    def tinh_chu_vi(self):
        pass

    @abstractmethod
    def tinh_dien_tich(self):
        pass

# Lớp con kế thừa
class HinhChuNhat(HinhHoc):
    def __init__(self, dai=0.0, rong=0.0):
        self.dai = dai
        self.rong = rong

    # BẮT BUỘC CÀI ĐẶT LẠI 1:
    def tinh_chu_vi(self):
        return (self.dai + self.rong) * 2

    # BẮT BUỘC CÀI ĐẶT LẠI 2:
    def tinh_dien_tich(self):
        return self.dai * self.rong
```

---

## 5. PHÂN BIỆT CÁC LOẠI METHOD TRONG OOP

| Loại Method | Decorator | Tham số đầu | Mục đích sử dụng |
| :--- | :--- | :--- | :--- |
| **Instance Method** | *(Không có)* | `self` | Tác động lên **đối tượng cụ thể** (truy cập `self.__thuoc_tinh`). 90% method trong đề thi thuộc loại này. |
| **Class Method** | `@classmethod` | `cls` | Tác động lên **Class và biến chung của Class** (ví dụ: đếm tổng số đối tượng đã tạo, danh sách đối tượng dùng chung `cls.danh_sach`). |
| **Static Method** | `@staticmethod` | *(Không có `self`/`cls`)* | Hàm tiện ích độc lập (helper function) được nhóm chung vào class cho gọn gàng. |

```python
class ViDuMethod:
    so_luong_tao = 0  # Biến dùng chung của Class

    def __init__(self, ten):
        self.ten = ten
        ViDuMethod.so_luong_tao += 1

    # 1. Instance Method
    def chao(self):
        return f"Xin chào, tôi là {self.ten}"

    # 2. Class Method
    @classmethod
    def lay_so_luong(cls):
        return f"Đã khởi tạo tổng cộng {cls.so_luong_tao} đối tượng"

    # 3. Static Method
    @staticmethod
    def la_so_chan(n):
        return n % 2 == 0
```

---

## 6. BÀI MẪU CHUẨN TỔNG HỢP ĐI THI

```python
from abc import ABC, abstractmethod

# Lớp trừu tượng cha
class SanPham(ABC):
    def __init__(self, ma="", ten="", don_gia=0.0, so_luong=0):
        self.__ma = ma
        self.__ten = ten
        self.__don_gia = don_gia
        self.__so_luong = so_luong

    # Getter / Setter Mã
    def get_ma(self):
        return self.__ma

    def set_ma(self, ma):
        ma = str(ma).strip()
        if not ma:
            print("Lỗi: Mã không được để trống!")
            return False
        self.__ma = ma
        return True

    # Getter / Setter Đơn giá
    def get_don_gia(self):
        return self.__don_gia

    def set_don_gia(self, gia):
        try:
            gia = float(gia)
            if gia < 0:
                print("Lỗi: Đơn giá không được âm!")
                return False
            self.__don_gia = gia
            return True
        except ValueError:
            print("Lỗi: Đơn giá phải là số!")
            return False

    # Getter / Setter Số lượng
    def get_so_luong(self):
        return self.__so_luong

    def set_so_luong(self, sl):
        try:
            sl = int(sl)
            if sl <= 0:
                print("Lỗi: Số lượng phải > 0!")
                return False
            self.__so_luong = sl
            return True
        except ValueError:
            print("Lỗi: Số lượng phải là số nguyên!")
            return False

    # Phương thức nhập chuẩn với Validation
    def nhap(self):
        while True:
            if self.set_ma(input("Nhập mã sản phẩm: ")):
                break
        self.__ten = input("Nhập tên sản phẩm: ").strip()
        while True:
            if self.set_don_gia(input("Nhập đơn giá: ")):
                break
        while True:
            if self.set_so_luong(input("Nhập số lượng: ")):
                break

    # Phương thức trừu tượng
    @abstractmethod
    def tinh_thanh_tien(self):
        pass

    def xuat(self):
        print(f"Mã: {self.__ma} | Tên: {self.__ten} | Giá: {self.__don_gia} | SL: {self.__so_luong} | Tiền: {self.tinh_thanh_tien()}")


# Lớp con kế thừa
class SanPhamKhuyenMai(SanPham):
    def __init__(self, ma="", ten="", don_gia=0.0, so_luong=0, giam_gia=0.1):
        super().__init__(ma, ten, don_gia, so_luong)
        self.giam_gia = giam_gia

    # Cài đặt phương thức trừu tượng của lớp cha
    def tinh_thanh_tien(self):
        tien_goc = self.get_don_gia() * self.get_so_luong()
        return tien_goc * (1 - self.giam_gia)
```

---

## 7. CÁC LỖI SAI KINH ĐIỂN CẦN TRÁNH

1. **`if a is not float:`** ❌
   - `a` là giá trị người dùng nhập (chuỗi hoặc số), `float` là kiểu dữ liệu, `is` dùng so sánh định danh ô nhớ. Dòng này luôn sai logic!
   - 👉 **Sửa:** Dùng `try ... float(a) ... except ValueError:` hoặc `isinstance(a, (int, float))`.

2. **Quên `pass` trong `@abstractmethod`**:
   - Phương thức trừu tượng không được viết logic xử lý, chỉ để `pass`.

3. **Quên override hết các method trừu tượng ở lớp con**:
   - Nếu cha có 2 abstract method mà lớp con chỉ viết 1 cái, lớp con vẫn là abstract class và sẽ báo lỗi không khởi tạo được đối tượng.

4. **Trong lớp con cố tình truy cập trực tiếp `self.__ma` của lớp cha**:
   - Biến `__` là private của lớp cha, lớp con không đọc được trực tiếp.
   - 👉 **Sửa:** Gọi qua getter của cha: `self.get_ma()`.

5. **Quên `return True` / `return False` trong Setter**:
   - Khiến cho vòng lặp `while True: if self.set_ma(...): break` không thể nhận biết được lúc nào nhập đúng để thoát.
