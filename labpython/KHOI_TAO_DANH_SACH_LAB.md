# CÁC CÁCH KHỞI TẠO VÀ QUẢN LÝ DANH SÁCH ĐỐI TƯỢNG TRONG BÀI LAB PYTHON OOP

Tài liệu tổng hợp các mô hình quản lý danh sách (List) thường gặp nhất trong các bài thực hành và đề thi OOP.

---

## MỤC LỤC
1. [Mô Hình 1: Tạo Lớp Quản Lý Riêng (Manager Class - Chuẩn & Tốt Nhất)](#mô-hình-1-tạo-lớp-quản-lý-riêng-manager-class)
2. [Mô Hình 2: Dùng Biến Lớp Dùng Chung (Class Variable)](#mô-hình-2-dùng-biến-lớp-dùng-chung-class-variable)
3. [Mô Hình 3: Danh Sách Đơn Giản Trong Hàm `main()`](#mô-hình-3-danh-sách-đơn-giản-trong-hàm-main)
4. [Mô Hình 4: Thuộc Tính Danh Sách Trong Đối Tượng](#mô-hình-4-thuộc-tính-danh-sách-trong-đối-tượng)
5. [Tổng Hợp 7 Thao Tác Bắt Buộc Phải Thuộc Khi Xử Lý Danh Sách OOP](#5-tổng-hợp-7-thao-tác-bắt-buộc-phải-thuộc)

---

## 🎯 ĐI THI NÊN CHỌN CÁCH NÀO? (RECOMMENDATION)

Khi vào phòng thi, bạn hãy chọn theo **2 tình huống** sau:

### 🥇 TÌNH HUỐNG 1: Đề bài yêu cầu cụ thể (90% ĐỀ THI LAB)
- Đề bài ghi: *"Hãy xây dựng lớp `DanhSachSinhVien`..."* hoặc *"Xây dựng lớp `QuanLyGiaoDich`..."*
- 👉 **BẮT BUỘC DÙNG [MÔ HÌNH 1: MANAGER CLASS](#mô-hình-1-tạo-lớp-quản-lý-riêng-manager-class)**
  - Khởi tạo: `class QuanLy: def __init__(self): self.danh_sach = []`
  - **Ưu điểm:** Đúng 100% chuẩn OOP của giáo viên, điểm tối đa, code rành mạch không sợ bị trừ điểm kiến trúc.

### ⚡ TÌNH HUỐNG 2: Đề bài tự do / Thời gian làm bài sắp hết
- Đề bài chỉ ghi: *"Tạo lớp `SinhVien`, sau đó nhập vào danh sách n sinh viên, in ra và tính tổng..."*
- 👉 **KHUYÊN DÙNG [MÔ HÌNH 3: LIST TRONG `main()`](#mô-hình-3-danh-sách-đơn-giản-trong-hàm-main)**
  - Khởi tạo: `danh_sach = []` ngay trong `main()`
  - **Ưu điểm:** **Nhanh nhất, ngắn nhất, không bao giờ nhầm lẫn**. Bạn không phải tốn thời gian tạo thêm class hay nhớ cú pháp `@classmethod` và `cls`.

> ⚠️ **LỜI KHUYÊN:** **KHÔNG NÊN** tự ý dùng Mô hình 2 (`SinhVien.ds = []` với `@classmethod`) trừ khi đề bài ép buộc, vì cú pháp `@classmethod` và `cls` rất dễ viết sai và làm rối logic khi đang bị áp lực thời gian!

---

## MÔ HÌNH 1: TẠO LỚP QUẢN LÝ RIÊNG (MANAGER CLASS)
> **Gặp ở:** [buoi7/btvn/bai4.py](file:///d:/python/ontapkiemtra/labpython/buoi7/btvn/bai4.py) (`QuanLyGiaoDich`) và [buoi7/btvn/bai3.py](file:///d:/python/ontapkiemtra/labpython/buoi7/btvn/bai3.py) (`DanhSachSinhVien`).  
> **Đánh giá:** Đây là cách thiết kế chuẩn OOP nhất, dễ mở rộng thêm sửa xóa và được chấm điểm cao nhất.

### Bước 1: Phải có Lớp Dữ Liệu (`GiaoDich`) trước
Trước khi quản lý, bạn cần có một khuôn mẫu định nghĩa một giao dịch cụ thể gồm những gì:

```python
class GiaoDich:
    def __init__(self, ma="", don_gia=0.0, so_luong=0):
        self.__ma = ma
        self.__don_gia = don_gia
        self.__so_luong = so_luong

    def get_ma(self):
        return self.__ma

    def get_so_luong(self):
        return self.__so_luong

    def xuat(self):
        print(f"Mã: {self.__ma} | Giá: {self.__don_gia} | SL: {self.__so_luong}")
```

---

### Bước 2: Tạo Lớp Quản Lý (`QuanLyGiaoDich`)
Lớp này giữ một danh sách `self.danh_sach = []`.  
> 💡 **GIẢI THÍCH QUAN TRỌNG:** Biến `gd` truyền vào các hàm dưới đây chính là **một đối tượng (instance) của class `GiaoDich`** (được tạo ra từ Bước 1). Vì `gd` là một `GiaoDich` nên ta mới gọi được `gd.get_ma()`, `gd.get_so_luong()`, `gd.xuat()`.

```python
class QuanLyGiaoDich:
    def __init__(self):
        # KHỞI TẠO: Tạo một list rỗng làm thuộc tính của đối tượng quản lý
        self.danh_sach = []

    # 1. Thêm: 'gd' là một đối tượng thuộc class GiaoDich được truyền vào
    def them_giao_dich(self, gd):
        self.danh_sach.append(gd)

    # 2. Tìm kiếm theo mã: 'gd' lấy từ danh sách ra, nên gọi được gd.get_ma()
    def tim_theo_ma(self, ma):
        for gd in self.danh_sach:
            if gd.get_ma().strip().lower() == ma.strip().lower():
                return gd  # Trả về chính đối tượng GiaoDich đó
        return None

    # 3. Xoá đối tượng theo mã
    def xoa_theo_ma(self, ma):
        gd = self.tim_theo_ma(ma)
        if gd:
            self.danh_sach.remove(gd)  # Xoá đối tượng gd khỏi list
            return True
        return False

    # 4. Xuất toàn bộ danh sách: Mỗi phần tử 'gd' tự gọi hàm gd.xuat() của nó
    def xuat_danh_sach(self):
        if not self.danh_sach:
            print("Danh sách đang trống!")
            return
        
        for i, gd in enumerate(self.danh_sach, start=1):
            print(f"[{i}] ", end="")
            gd.xuat()

    # 5. Tính tổng số lượng
    def tong_so_luong(self):
        return sum(gd.get_so_luong() for gd in self.danh_sach)
```

---

### Bước 3: Xem hàm `main()` liên kết 2 lớp lại với nhau như thế nào
```python
def main():
    # 1. Khởi tạo đối tượng quản lý (bên trong có self.danh_sach = [])
    ql = QuanLyGiaoDich()

    # 2. Khởi tạo các đối tượng từ class GiaoDich
    gd1 = GiaoDich("GD01", 20000.0, 5)
    gd2 = GiaoDich("GD02", 50000.0, 2)

    # 3. Truyền đối tượng gd1, gd2 vào làm tham số cho ql.them_giao_dich()
    ql.them_giao_dich(gd1)
    ql.them_giao_dich(gd2)

    # 4. Hiển thị danh sách
    print("Danh sách các giao dịch vừa thêm:")
    ql.xuat_danh_sach()
```

---

## MÔ HÌNH 2: DÙNG BIẾN LỚP DÙNG CHUNG (CLASS VARIABLE)
> **Gặp ở:** [buoi7/bai5.py](file:///d:/python/ontapkiemtra/labpython/buoi7/bai5.py) (`SinhVien.ds = []`).  
> **Đặc điểm:** Không cần tạo thêm class quản lý. Mọi đối tượng tạo ra đều được gom chung vào một danh sách của chính Class đó.

### Cách viết:
```python
class SinhVien:
    # KHỞI TẠO: Đặt danh sách ngay dưới khai báo class (biến dùng chung cho cả lớp)
    ds = []

    def __init__(self, ma="", ten=""):
        self.__ma = ma
        self.__ten = ten

    # Phương thức của đối tượng: Tự thêm chính nó (self) vào danh sách lớp
    def them_vao_ds(self):
        # Kiểm tra trùng mã
        for sv in SinhVien.ds:
            if sv.get_ma() == self.__ma:
                print("Mã sinh viên đã tồn tại!")
                return False
        
        SinhVien.ds.append(self)
        return True

    # Phương thức của Lớp (@classmethod): Thao tác trên danh sách chung
    @classmethod
    def xuat_tat_ca(cls):
        for sv in cls.ds:
            sv.display()

    @classmethod
    def dem_so_luong(cls):
        return len(cls.ds)
```

### Cách dùng trong `main()`:
```python
def main():
    sv1 = SinhVien("SV01", "Nguyen Van A")
    sv1.them_vao_ds()   # Tự thêm sv1 vào SinhVien.ds

    sv2 = SinhVien("SV02", "Tran Thi B")
    sv2.them_vao_ds()

    # Gọi qua tên Class:
    SinhVien.xuat_tat_ca()
```

---

## MÔ HÌNH 3: DANH SÁCH ĐƠN GIẢN TRONG HÀM `MAIN()`
> **Gặp ở:** Các bài tập cơ bản yêu cầu: *"Nhập vào n sinh viên / hình học rồi in ra"*.

### Cách viết:
```python
def main():
    # KHỞI TẠO: List thông thường trong main
    danh_sach = []
    
    n = int(input("Nhập số lượng đối tượng cần tạo: "))
    for i in range(n):
        print(f"\n--- Nhập đối tượng thứ {i+1} ---")
        sp = SanPham()
        sp.input_info()
        danh_sach.append(sp)  # Thêm vào danh sách

    # Duyệt và hiển thị
    print("\n--- DANH SÁCH ĐÃ NHẬP ---")
    for sp in danh_sach:
        sp.display()
```

---

## MÔ HÌNH 4: THUỘC TÍNH DANH SÁCH TRONG ĐỐI TƯỢNG
> **Gặp ở:** [buoi7/bai4.py](file:///d:/python/ontapkiemtra/labpython/buoi7/bai4.py) (`WordPlay`) hoặc bài toán Quản lý Hóa đơn có chứa danh sách các mặt hàng con.

### Cách viết:
```python
class WordPlay:
    def __init__(self):
        # Khởi tạo list rỗng
        self.ds_tu = []

    def input_info(self):
        # Tách chuỗi người dùng nhập thành danh sách các từ
        chuoi = input("Nhập danh sách từ cách nhau bởi khoảng trắng: ")
        self.ds_tu = chuoi.split()

    def tim_tu_do_dai(self, do_dai):
        # Lọc danh sách thỏa mãn điều kiện
        return [tu for tu in self.ds_tu if len(tu) == do_dai]
```

---

## 5. TỔNG HỢP 7 THAO TÁC BẮT BUỘC PHẢI THUỘC

Khi làm việc với danh sách đối tượng OOP, đây là 7 thao tác xuất hiện 100% trong đề thi:

### 1. Kiểm tra danh sách rỗng
```python
if not self.danh_sach:
    print("Danh sách đang trống!")
    return
```

### 2. Duyệt có kèm số thứ tự (STT) bằng `enumerate`
```python
for i, item in enumerate(self.danh_sach, start=1):
    print(f"STT: {i}", end=" | ")
    item.xuat()
```

### 3. Tìm kiếm theo mã (không phân biệt hoa thường)
```python
def tim(self, ma_tim):
    for item in self.danh_sach:
        if item.get_ma().strip().lower() == ma_tim.strip().lower():
            return item
    return None
```

### 4. Xóa đối tượng khỏi danh sách
```python
obj = self.tim(ma_can_xoa)
if obj:
    self.danh_sach.remove(obj)
    print("Xóa thành công!")
```

### 5. Lọc đối tượng theo lớp con bằng `isinstance`
```python
# Lấy danh sách chỉ gồm các đối tượng GiaoDichVang
ds_vang = [x for x in self.danh_sach if isinstance(x, GiaoDichVang)]
```

### 6. Tính tổng tiền / số lượng (dùng hàm `sum()`)
```python
# Tính tổng thành tiền của tất cả giao dịch:
tong_tien = sum(x.thanh_tien() for x in self.danh_sach)

# Tính tổng tiền CHỈ RIÊNG giao dịch vàng:
tong_tien_vang = sum(x.thanh_tien() for x in self.danh_sach if isinstance(x, GiaoDichVang))
```

### 7. Sắp xếp danh sách đối tượng
```python
# Sắp xếp tăng dần theo điểm trung bình:
self.danh_sach.sort(key=lambda x: x.get_dtb())

# Sắp xếp giảm dần theo thành tiền (reverse=True):
self.danh_sach.sort(key=lambda x: x.thanh_tien(), reverse=True)
```
