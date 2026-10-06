# SỔ TAY CÚ PHÁP DATETIME, STRPTIME VÀ STRFTIME TRONG PYTHON

Tài liệu hướng dẫn toàn diện về cách xử lý ngày giờ, chuyển đổi định dạng và validation trong Python.

---

## MỤC LỤC
1. [Mẹo Phân Biệt Siêu Dễ: strptime vs strftime](#1-mẹo-phân-biệt-strptime-vs-strftime)
2. [Cách Import Thường Dùng](#2-cách-import-thường-dùng)
3. [Lấy Ngày Giờ Hiện Tại & Các Thuộc Tính](#3-lấy-ngày-giờ-hiện-tại--thuộc-tính)
4. [Bảng Mã Định Dạng (Format Codes) Đầy Đủ](#4-bảng-mã-định-dạng-format-codes)
5. [Cú Pháp Chuyển Đổi Chi Tiết & Ví Dụ](#5-cú-pháp-chuyển-đổi-chi-tiết)
6. [So Sánh & Tính Toán Khoảng Cách Ngày (timedelta)](#6-so-sánh--tính-toán-ngày)
7. [Các Mẫu Code Chuẩn Để Đi Thi (Áp Dụng Vào Lab & OOP)](#7-các-mẫu-code-chuẩn-để-đi-thi)

---

## 1. MẸO PHÂN BIỆT: STRPTIME VS STRFTIME

Rất nhiều bạn hay bị nhầm lẫn giữa 2 hàm này. Hãy nhớ quy tắc chữ cái:

| Hàm | Viết tắt của | Chức năng | Hướng chuyển đổi | Ngữ cảnh dùng |
| :--- | :--- | :--- | :--- | :--- |
| **`strptime`** | String **P**arse Time | **Parse (Phân tích cú pháp)** | `str` ➡️ `datetime` | Khi người dùng nhập chuỗi từ bàn phím, chuyển thành kiểu ngày để kiểm tra/lưu. |
| **`strftime`** | String **F**ormat Time | **Format (Định dạng)** | `datetime` ➡️ `str` | Khi có đối tượng ngày, muốn in ra màn hình theo định dạng đẹp (vd: `13/03/2024`). |

---

## 2. CÁCH IMPORT THƯỜNG DÙNG

Có 2 cách import phổ biến:

### Cách 1: `import datetime` (Cách đề thi và các bài Lab hay dùng)
```python
import datetime

# Khi dùng phải gọi datetime.<tên_lớp>
ngay_nay = datetime.date.today()
bay_gio = datetime.datetime.now()
ngay = datetime.datetime.strptime("15/10/2024", "%d/%m/%Y").date()
```

### Cách 2: `from datetime import datetime, date, timedelta` (Cách viết ngắn gọn)
```python
from datetime import datetime, date, timedelta

# Gọi trực tiếp tên lớp:
ngay_nay = date.today()
bay_gio = datetime.now()
ngay = datetime.strptime("15/10/2024", "%d/%m/%Y").date()
```

---

## 3. LẤY NGÀY GIỜ HIỆN TẠI & THUỘC TÍNH

```python
import datetime

# 1. Chỉ lấy NGÀY hôm nay (kiểu date)
hom_nay = datetime.date.today()        # Kết quả: 2026-10-07
print(hom_nay.year)                    # 2026 (Năm)
print(hom_nay.month)                   # 10   (Tháng)
print(hom_nay.day)                     # 7    (Ngày)

# 2. Lấy cả NGÀY VÀ GIỜ hiện tại (kiểu datetime)
bay_gio = datetime.datetime.now()      # Kết quả: 2026-10-07 05:45:12.123456
print(bay_gio.hour)                    # 5    (Giờ)
print(bay_gio.minute)                  # 45   (Phút)
print(bay_gio.second)                  # 12   (Giây)

# 3. Tạo một ngày cụ thể bất kỳ: date(năm, tháng, ngày)
ngay_sinh = datetime.date(2004, 8, 15)
```

---

## 4. BẢNG MÃ ĐỊNH DẠNG (FORMAT CODES)

Các ký tự định dạng được đặt sau dấu `%`:

### Nhóm Ngày, Tháng, Năm (Thường thi nhất):
| Ký tự | Ý nghĩa | Dải giá trị / Ví dụ |
| :---: | :--- | :--- |
| **`%d`** | Ngày trong tháng (2 chữ số, có số 0 ở đầu) | `01` đến `31` |
| **`%m`** | Tháng dạng số (2 chữ số) | `01` đến `12` |
| **`%Y`** | **Năm đủ 4 chữ số** (Y hoa) | `2024`, `2026` |
| **`%y`** | Năm rút gọn 2 chữ số (y thường) | `24`, `26` |
| **`%b`** | Tên tháng viết tắt tiếng Anh | `Jan`, `Feb`, `Oct` |
| **`%B`** | Tên tháng đầy đủ tiếng Anh | `January`, `October` |

### Nhóm Giờ, Phút, Giây:
| Ký tự | Ý nghĩa | Ví dụ |
| :---: | :--- | :--- |
| **`%H`** | Giờ theo chuẩn 24h | `00` đến `23` |
| **`%I`** | Giờ theo chuẩn 12h | `01` đến `12` |
| **`%p`** | Buổi sáng / tối (đi kèm `%I`) | `AM` hoặc `PM` |
| **`%M`** | Phút (M hoa - tránh nhầm với %m là tháng) | `00` đến `59` |
| **`%S`** | Giây | `00` đến `59` |

### Nhóm Thứ trong tuần:
| Ký tự | Ý nghĩa | Ví dụ |
| :---: | :--- | :--- |
| **`%w`** | Thứ dạng số (0 là Chủ Nhật, 1 là Thứ Hai) | `0`, `1`, ..., `6` |
| **`%a`** | Tên thứ viết tắt tiếng Anh | `Mon`, `Tue`, `Sun` |
| **`%A`** | Tên thứ đầy đủ tiếng Anh | `Monday`, `Sunday` |

---

## 5. CÚ PHÁP CHUYỂN ĐỔI CHI TIẾT

### A. `strptime()`: Chuyển Chuỗi (string) ➡️ Ngày (`datetime`)
> Cú pháp: `datetime.datetime.strptime(chuỗi_cần_chuyển, định_dạng)`

```python
import datetime

chuoi_nhap = "13/03/2017"

# 1. Chuyển thành đối tượng datetime
obj_dt = datetime.datetime.strptime(chuoi_nhap, "%d/%m/%Y")
print(obj_dt)        # 2017-03-13 00:00:00 (kiểu datetime)

# 2. Nếu chỉ muốn lấy phần ngày (date) mà không cần giờ:
obj_date = obj_dt.date()
print(obj_date)      # 2017-03-13 (kiểu date)
```

**Các kiểu chuỗi nhập thông dụng:**
- Dạng ngày/tháng/năm: `strptime(s, "%d/%m/%Y")` (ví dụ: `15/10/2024`)
- Dạng năm-tháng-ngày: `strptime(s, "%Y-%m-%d")` (ví dụ: `2024-10-15`)
- Dạng ngày-tháng-năm: `strptime(s, "%d-%m-%Y")` (ví dụ: `15-10-2024`)
- Dạng có cả giờ: `strptime(s, "%d/%m/%Y %H:%M")` (ví dụ: `15/10/2024 14:30`)

---

### B. `strftime()`: Chuyển Ngày (`datetime`/`date`) ➡️ Chuỗi (string)
> Cú pháp: `doi_tuong_ngay.strftime(định_dạng_muốn_in)`

```python
import datetime

ngay_hien_tai = datetime.date.today()

# Định dạng thành chuỗi Việt Nam: ngày/tháng/năm
chuoi_vn = ngay_hien_tai.strftime("%d/%m/%Y")
print(chuoi_vn)      # "07/10/2026"

# Định dạng chuẩn quốc tế: năm-tháng-ngày
chuoi_iso = ngay_hien_tai.strftime("%Y-%m-%d")
print(chuoi_iso)     # "2026-10-07"

# Định dạng có chữ:
chuoi_dep = ngay_hien_tai.strftime("Ngày %d tháng %m năm %Y")
print(chuoi_dep)     # "Ngày 07 tháng 10 năm 2026"
```

---

## 6. SO SÁNH & TÍNH TOÁN NGÀY

### A. So sánh 2 mốc thời gian
Chỉ cần dùng các toán tử so sánh thông thường `>`, `<`, `==`, `<=`, `>=`:
```python
import datetime

ngay_mua = datetime.date(2024, 5, 20)
ngay_han = datetime.date(2024, 6, 1)

if ngay_mua < ngay_han:
    print("Còn hạn sử dụng")

# Kiểm tra một ngày có vượt quá hôm nay không:
if ngay_mua > datetime.date.today():
    print("Ngày không được lớn hơn ngày hiện tại!")
```

### B. Cộng/Trừ thời gian với `timedelta`
```python
import datetime

hom_nay = datetime.date.today()

# 1. Cộng thêm 7 ngày (ví dụ: hạn bảo hành, ngày giao hàng)
bay_ngay_sau = hom_nay + datetime.timedelta(days=7)

# 2. Lùi lại 30 ngày:
thang_truoc = hom_nay - datetime.timedelta(days=30)

# 3. Tính khoảng cách số ngày giữa 2 mốc:
ngay1 = datetime.date(2026, 1, 1)
ngay2 = datetime.date(2026, 1, 10)
khoang_cach = (ngay2 - ngay1).days   # 9 ngày
```

---

## 7. CÁC MẪU CODE CHUẨN ĐỂ ĐI THI

### Mẫu 1: Nhập ngày và Validate chặt chẽ (Như trong Bài 4 Lab 7)
```python
import datetime

def nhap_ngay_hop_le():
    while True:
        chuoi = input("Nhập ngày (dd/mm/yyyy): ").strip()
        try:
            # Bước 1: Parse từ chuỗi sang date
            ngay = datetime.datetime.strptime(chuoi, "%d/%m/%Y").date()
            
            # Bước 2: Kiểm tra điều kiện logic (không quá hôm nay)
            if ngay > datetime.date.today():
                print("Lỗi: Ngày không được lớn hơn ngày hôm nay!")
                continue
            
            return ngay  # Trả về đối tượng date hợp lệ
        except ValueError:
            print("Lỗi: Định dạng ngày không đúng! Vui lòng nhập theo dạng dd/mm/yyyy (ví dụ: 15/08/2023)")
```

### Mẫu 2: Setter ngày trong Class OOP
```python
import datetime

class DonHang:
    def __init__(self):
        self.__ngay_tao = datetime.date.today()

    def get_ngay_str(self):
        # Xuất chuỗi định dạng dd/mm/yyyy ra màn hình
        return self.__ngay_tao.strftime("%d/%m/%Y")

    def set_ngay(self, ngay_input):
        # Hỗ trợ nhận vào cả kiểu chuỗi lẫn kiểu datetime.date
        if isinstance(ngay_input, str):
            try:
                ngay_input = datetime.datetime.strptime(ngay_input.strip(), "%d/%m/%Y").date()
            except ValueError:
                print("Lỗi: Sai định dạng ngày!")
                return False

        if isinstance(ngay_input, datetime.date):
            if ngay_input > datetime.date.today():
                print("Lỗi: Ngày vượt quá hiện tại!")
                return False
            self.__ngay_tao = ngay_input
            return True
        return False
```

### Mẫu 3: Tính tuổi chính xác từ ngày sinh
```python
import datetime

def tinh_tuoi(ngay_sinh):
    # ngay_sinh là kiểu datetime.date
    hom_nay = datetime.date.today()
    tuoi = hom_nay.year - ngay_sinh.year
    # Nếu chưa tới ngày sinh nhật trong năm nay thì trừ đi 1
    if (hom_nay.month, hom_nay.day) < (ngay_sinh.month, ngay_sinh.day):
        tuoi -= 1
    return tuoi
```
