# TỔNG HỢP CÁC DẠNG BÀI VÀ CÁCH TRIỂN KHAI LAB 6 (PYTHON OOP)

Tài liệu đúc kết toàn bộ kiến thức, các dạng bài tập thực hành trên lớp và BTVN của **Lab 6 - Lập trình hướng đối tượng (Kế thừa & Đa hình)**.

---

## MỤC LỤC
1. [Bản Chất Cốt Lõi Của Lab 6](#1-bản-chất-cốt-lõi-của-lab-6)
2. [Khung Mẫu Chuẩn (Template) Áp Dụng Cho Mọi Bài Lab 6](#2-khung-mẫu-chuẩn-template-cho-mọi-bài-lab-6)
3. [Tổng Hợp 5 Dạng Bài Điển Hình Trong Lab 6](#3-tổng-hợp-5-dạng-bài-điển-hình-trong-lab-6)
   - [Dạng 1: Quản lý Nhân viên & Tiền lương](#dạng-1-quản-lý-nhân-viên--tiền-lương-bai1-bai3_staff)
   - [Dạng 2: Hình học & Tính Chu vi / Diện tích](#dạng-2-hình-học--tính-chu-vi--diện-tích-bai2)
   - [Dạng 3: Phương tiện & Tính Chi phí / Khấu hao](#dạng-3-phương-tiện--tính-chi-phí--khấu-hao-bai4)
   - [Dạng 4: Hóa đơn điện & Dịch vụ Giao hàng](#dạng-4-hóa-đơn-điện--dịch-vụ-giao-hàng-bai6_delivery-bai4_electric)
   - [Dạng 5: Khóa học & Sản phẩm kinh doanh](#dạng-5-khóa-học--sản-phẩm-kinh-doanh-bai1_product-bai5_course)
4. [Cách Triển Khai Danh Sách Đa Hình & Menu Điều Khiển](#4-cách-triển-khai-danh-sách-đa-hình--menu-điều-khiển)
5. [Checklist Các Lỗi Hay Bị Trừ Điểm Khi Đi Thi](#5-checklist-các-lỗi-hay-bị-trừ-điểm-khi-đi-thi)

---

## 1. BẢN CHẤT CỐT LÕI CỦA LAB 6

Lab 6 tập trung vào **Kế thừa (Inheritance)** và **Ghi đè phương thức (Method Overriding)**:
- **Lớp Cha (Base Class):** Gom tất cả các thuộc tính chung (Mã, Tên, Giá, Ngày, ...) và định nghĩa các phương thức chung.
- **Lớp Con (Derived Class):** Kế thừa lớp cha, chỉ cần khai báo thêm thuộc tính đặc thù của riêng mình.
- **`super().__init__(...)`:** Gọi hàm tạo của cha để cha gán các thuộc tính chung, con không cần gán lại.
- **`super().nhap()`:** Gọi hàm nhập của cha để nhập thông tin chung, con chỉ nhập thêm phần riêng.
- **Ghi đè (Overriding):** Lớp con viết lại hàm tính toán (ví dụ: `tinh_luong()`, `tinh_tien()`, `tinh_dien_tich()`) theo công thức riêng của nó.
- **Đa hình (Polymorphism):** Lưu mọi loại đối tượng con vào chung 1 danh sách, khi duyệt chỉ cần gọi `obj.tinh_tien()` hay `obj.hien_thi()`, Python sẽ tự biết gọi đúng hàm của lớp con đó.

---

## 2. KHUNG MẪU CHUẨN (TEMPLATE) CHO MỌI BÀI LAB 6

Mọi bài toán Lab 6 đều có thể giải quyết nhanh chóng bằng mẫu khung chuẩn 3 tầng sau:

```python
# TẦNG 1: LỚP CHA CHUNG
class LopCha:
    def __init__(self, ma="", ten="", gia_co_ban=0.0):
        self.ma = ma
        self.ten = ten
        self.gia_co_ban = gia_co_ban

    def nhap(self):
        self.ma = input("Nhập mã: ").strip()
        self.ten = input("Nhập tên: ").strip()
        while True:
            try:
                val = float(input("Nhập giá cơ bản: "))
                if val >= 0:
                    self.gia_co_ban = val
                    break
                print("Lỗi: Giá phải >= 0!")
            except ValueError:
                print("Lỗi: Vui lòng nhập số hợp lệ!")

    def tinh_thanh_tien(self):
        return self.gia_co_ban  # Công thức mặc định

    def hien_thi(self):
        print(f"Mã: {self.ma} | Tên: {self.ten} | Tiền: {self.tinh_thanh_tien():,.0f} VND")


# TẦNG 2: LỚP CON LOẠI 1
class LopConA(LopCha):
    def __init__(self, ma="", ten="", gia_co_ban=0.0, he_so=1.0):
        super().__init__(ma, ten, gia_co_ban)  # 1. Gọi hàm tạo cha
        self.he_so = he_so                     # 2. Thuộc tính riêng của con

    def nhap(self):
        super().nhap()  # 1. Gọi nhập của cha
        # 2. Nhập thêm thuộc tính riêng
        while True:
            try:
                self.he_so = float(input("Nhập hệ số: "))
                break
            except ValueError:
                print("Lỗi: Phải nhập số!")

    # 3. Ghi đè (Override) công thức tính toán của riêng con A
    def tinh_thanh_tien(self):
        return self.gia_co_ban * self.he_so


# TẦNG 3: LỚP CON LOẠI 2
class LopConB(LopCha):
    def __init__(self, ma="", ten="", gia_co_ban=0.0, phu_phi=0.0):
        super().__init__(ma, ten, gia_co_ban)
        self.phu_phi = phu_phi

    def nhap(self):
        super().nhap()
        while True:
            try:
                self.phu_phi = float(input("Nhập phụ phí: "))
                break
            except ValueError:
                print("Lỗi: Phải nhập số!")

    # 3. Ghi đè (Override) công thức tính toán của riêng con B
    def tinh_thanh_tien(self):
        return self.gia_co_ban + self.phu_phi
```

---

## 3. TỔNG HỢP 5 DẠNG BÀI ĐIỂN HÌNH TRONG LAB 6

### Dạng 1: Quản lý Nhân viên & Tiền lương ([bai1.py](file:///d:/python/ontapkiemtra/labpython/buoi6/bai1.py), [bai3_staff.py](file:///d:/python/ontapkiemtra/labpython/buoi6/btvn/bai3_staff.py))
- **Lớp Cha `NhanVien`:** `ma_nv`, `ho_ten`, `luong_co_ban`.
  - Thuế thu nhập: `if luong >= 15_000_000: return luong * 0.05 else: 0`
  - Thực lãnh = `Lương - Thuế`.
- **Lớp Con 1 `NhanVienVanPhong`:** Thêm `so_ngay_lam`.
  - Công thức: `luong = luong_co_ban + so_ngay_lam * 200_000`
- **Lớp Con 2 `NhanVienSanXuat`:** Thêm `so_san_pham`.
  - Công thức: `luong = luong_co_ban + so_san_pham * 50_000`
- **Lớp Con 3 `QuanLy`:** Thêm `phu_cap_chuc_vu`.
  - Công thức: `luong = luong_co_ban + phu_cap_chuc_vu`

---

### Dạng 2: Hình học & Tính Chu vi / Diện tích ([bai2.py](file:///d:/python/ontapkiemtra/labpython/buoi6/bai2.py))
- **Lớp Cha `Hinh`:** `tinh_dien_tich() -> 0`, `tinh_chu_vi() -> 0`.
- **Lớp Con 1 `HinhChuNhat`:** Thêm `chieu_dai`, `chieu_rong`.
  - `tinh_dien_tich()` = `dai * rong`
  - `tinh_chu_vi()` = `(dai + rong) * 2`
- **Lớp Con 2 `HinhTron`:** Thêm `ban_kinh`.
  - `tinh_dien_tich()` = `math.pi * ban_kinh**2`
  - `tinh_chu_vi()` = `2 * math.pi * ban_kinh`
- **Lớp Con 3 `HinhTamGiac`:** Thêm 3 cạnh `a, b, c`.
  - Kiểm tra hợp lệ: `a + b > c and a + c > b and b + c > a`
  - Nửa chu vi: `p = (a + b + c) / 2`
  - Diện tích (Heron): `math.sqrt(p * (p-a) * (p-b) * (p-c))`

---

### Dạng 3: Phương tiện & Tính Chi phí / Khấu hao ([bai4.py](file:///d:/python/ontapkiemtra/labpython/buoi6/bai4.py))
- **Lớp Cha `PhuongTien`:** `ma_pt`, `hang_sx`, `nam_sx`.
  - Tính tuổi xe: `tinh_tuoi_xe() = datetime.now().year - self.nam_sx`
- **Lớp Con 1 `XeMay`:** Thêm `so_km`.
  - Chi phí bảo dưỡng = `so_km * 500 + tuoi_xe * 100_000`
- **Lớp Con 2 `OTo`:** Thêm `so_cho_ngoi`, `so_km`.
  - Chi phí = `so_km * 1_500 + so_cho_ngoi * 500_000`

---

### Dạng 4: Hóa đơn điện & Dịch vụ Giao hàng ([bai6_delivery.py](file:///d:/python/ontapkiemtra/labpython/buoi6/btvn/bai6_delivery.py), [bai4_electric_bill.py](file:///d:/python/ontapkiemtra/labpython/buoi6/btvn/bai4_electric_bill.py))
- **Đơn Hàng Giao Hàng (`DonHang`):** `ma_don`, `ten_khach`, `khoang_cach` (km), `khoi_luong` (kg).
  - Phí cơ bản = `khoang_cach * 5_000 + khoi_luong * 2_000`
  - `GiaoHangTieuChuan`: Không có phụ phí.
  - `GiaoHangHoaToc`: Phụ phí cố định `30_000 VND` (hoặc tính thêm nếu nặng quá 5kg).
- **Hóa Đơn Điện (`HoaDonDien`):** `ma_hd`, `ten_chu_ho`, `so_kwh`.
  - `DienSinhHoat`: Tính theo bậc thang luỹ tiến (0-50 kWh giá rẻ, 51-100 giá cao hơn...).
  - `DienKinhDoanh`: Thêm giờ cao điểm (`so_kwh_cao_diem * don_gia_cao`).

---

### Dạng 5: Khóa học & Sản phẩm kinh doanh ([bai1_product.py](file:///d:/python/ontapkiemtra/labpython/buoi6/btvn/bai1_product.py), [bai5_course.py](file:///d:/python/ontapkiemtra/labpython/buoi6/btvn/bai5_course.py))
- **Sản Phẩm (`SanPham`):** `ma_sp`, `ten_sp`, `gia_goc`.
  - `SanPhamDienTu`: Thêm thời gian bảo hành, phí bảo hành.
  - `SanPhamGiaDung`: Thêm phí vận chuyển cồng kềnh.
- **Khóa Học (`KhoaHoc`):** `ma_kh`, `ten_kh`, `hoc_phi_goc`.
  - `KhoaHocOnline`: Giảm giá 20% do học qua mạng.
  - `KhoaHocOffline`: Cộng thêm phụ phí tài liệu & phòng lab.

---

## 4. CÁCH TRIỂN KHAI DANH SÁCH ĐA HÌNH & MENU ĐIỀU KHIỂN

Đây là hàm `main()` chuẩn cho mọi bài thi Lab 6:

```python
def main():
    danh_sach = []
    
    while True:
        print("\n" + "="*30)
        print("CHUONG TRINH QUAN LY (LAB 6)")
        print("1. Nhap doi tuong loai 1")
        print("2. Nhap doi tuong loai 2")
        print("3. Xuat tat ca danh sach")
        print("4. Tinh tong thanh tien")
        print("5. Tim doi tuong co tien cao nhat")
        print("0. Thoat")
        print("="*30)
        
        chon = input("Chon chuc nang (0-5): ").strip()
        
        if chon == "1":
            obj = LopConA()
            obj.nhap()
            danh_sach.append(obj)
            print(">> Da them thanh cong!")
            
        elif chon == "2":
            obj = LopConB()
            obj.nhap()
            danh_sach.append(obj)
            print(">> Da them thanh cong!")
            
        elif chon == "3":
            if not danh_sach:
                print("Danh sach dang trong!")
            else:
                print("\n--- DANH SACH CHI TIET ---")
                for i, obj in enumerate(danh_sach, start=1):
                    print(f"[{i}] ", end="")
                    obj.hien_thi()  # Tự động gọi đúng hien_thi() của từng lớp con
                    
        elif chon == "4":
            # Tinh tong dung sum
            tong = sum(obj.tinh_thanh_tien() for obj in danh_sach)
            print(f">> Tong thanh tien tat ca: {tong:,.0f} VND")
            
        elif chon == "5":
            if not danh_sach:
                print("Danh sach trong!")
            else:
                # Tim max theo ham tinh_thanh_tien
                obj_max = max(danh_sach, key=lambda x: x.tinh_thanh_tien())
                print(">> Doi tuong co tien cao nhat la:")
                obj_max.hien_thi()
                
        elif chon == "0":
            print("Ket thuc chuong trinh. Tam biet!")
            break
        else:
            print("Lua chon khong hop le!")
```

---

## 5. CHECKLIST CÁC LỖI HAY BỊ TRỪ ĐIỂM KHI ĐI THI

1. **Quên gọi `super().__init__(...)` trong hàm tạo của con:**
   - ❌ Lỗi: Lớp con tự khai báo lại `self.ma = ma`, `self.ten = ten`. Thầy cô chấm sẽ đánh giá là chưa nắm được tính kế thừa.
   - 👉 **Sửa:** Luôn gọi `super().__init__(ma, ten, ...)`.

2. **Quên gọi `super().nhap()` trong hàm nhập của con:**
   - ❌ Lỗi: Nhập lại từ đầu mã và tên ở lớp con.
   - 👉 **Sửa:** Dùng `super().nhap()` để kế thừa phần nhập của cha, rồi mới viết tiếp phần nhập thuộc tính riêng.

3. **Lỗi crash chương trình khi nhập chuỗi vào trường số:**
   - Luôn bọc trong khối `while True:` kết hợp `try ... float(input(...)) ... except ValueError:`.

4. **Sai tên phương thức khi ghi đè (Overriding):**
   - Cha đặt là `tinh_tien()`, con lại viết nhầm thành `tinh_tong_tien()`. Lúc này tính đa hình sẽ bị gãy!
   - 👉 Tên phương thức ở lớp con phải **trùng khớp 100%** với phương thức ở lớp cha.
