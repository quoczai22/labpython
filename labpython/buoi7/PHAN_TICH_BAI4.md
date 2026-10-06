# PHÂN TÍCH CHI TIẾT BÀI 4 - LAB 7 (BÀI TẬP TRÊN LỚP)
## ĐỀ TÀI: LỚP XỬ LÝ DANH SÁCH TỪ (CLASS WORDPLAY)

Tài liệu phân tích cấu trúc mã nguồn file [`buoi7/bai4.py`](file:///d:/python/ontapkiemtra/labpython/buoi7/bai4.py) phục vụ ôn tập kiểm tra OOP & Xử lý Chuỗi (String) trong Python.

---

## 1. TỔNG QUAN CLASS `WordPlay`

Khác với các bài quản lý sinh viên hay giao dịch, bài 4 là bài toán **xử lý chuỗi và danh sách từ (String & List Algorithms)** được đóng gói trong một Class.

```
┌──────────────────────────────────────────────────────────────┐
│                       class WordPlay                         │
├──────────────────────────────────────────────────────────────┤
│ [Thuộc tính đối tượng]:                                      │
│ - self.ds_tu = [] (Danh sách các từ được tách ra)            │
├──────────────────────────────────────────────────────────────┤
│ [Phương thức nhập & hiển thị]:                               │
│ + input_info(): Nhập chuỗi từ bàn phím và .split()           │
│ + display(tieu_de, danh_sach_ket_qua): In kết quả với .join()│
│                                                              │
│ [Các thuật toán lọc từ (Filter Methods)]:                     │
│ + words_with_length(length): Lọc từ có độ dài bằng length    │
│ + started_with_s(s): Lọc từ bắt đầu bằng tiền tố s           │
│ + end_with_s(s): Lọc từ kết thúc bằng hậu tố s               │
│ + only_L(L): Lọc từ CHỈ chứa các ký tự thuộc tập L           │
│ + avoids_L(L): Lọc từ KHÔNG chứa bất kỳ ký tự nào thuộc L    │
└──────────────────────────────────────────────────────────────┘
```

---

## 2. PHÂN TÍCH TỪNG PHƯƠNG THỨC TRONG CODE

### A. Phương thức Khởi Tạo & Nhập Liệu (Dòng 2 - 7)
```python
def __init__(self):
    self.ds_tu = []  # Khởi tạo list từ rỗng

def input_info(self):
    ds_tu = input("Hay nhap danh sach chu tach nhau boi space: ")
    self.ds_tu = ds_tu.split()  # .split() tự động tách theo khoảng trắng
```
- **Hàm `.split()`**: Tách một chuỗi thành danh sách các từ, tự động loại bỏ khoảng trắng thừa ở giữa và 2 đầu.  
  *(Ví dụ: `"  apple   banana cat "` ➡️ `['apple', 'banana', 'cat']`)*.

---

### B. Lọc từ theo độ dài: `words_with_length(self, length)` (Dòng 9 - 14)
```python
def words_with_length(self, length):
    ket_qua = []
    for tu in self.ds_tu:
        if len(tu) == length:
            ket_qua.append(tu)
    return ket_qua
```
- **Ý nghĩa:** Kiểm tra độ dài từng từ bằng hàm `len(tu)`. Nếu bằng `length` thì đưa vào danh sách kết quả.
- 💡 **Cách viết ngắn gọn (List Comprehension):**
  ```python
  return [tu for tu in self.ds_tu if len(tu) == length]
  ```

---

### C. Lọc từ theo chữ cái bắt đầu và kết thúc (Dòng 16 - 28)

#### 1. Bắt đầu bằng chuỗi `s`: `started_with_s(self, s)`
```python
for tu in self.ds_tu:
    if tu.startswith(s):  # Kiểm tra tiền tố bắt đầu
        ket_qua.append(tu)
```
- Sử dụng hàm chuẩn của string: `tu.startswith(s)`.  
  *(Ví dụ: `"apple".startswith("a")` ➡️ `True`)*.

#### 2. Kết thúc bằng chuỗi `s`: `end_with_s(self, s)`
```python
for tu in self.ds_tu:
    if tu.endswith(s):  # Kiểm tra hậu tố kết thúc
        ket_qua.append(tu)
```
- Sử dụng hàm chuẩn của string: `tu.endswith(s)`.  
  *(Ví dụ: `"cat".endswith("t")` ➡️ `True`)*.

---

### D. Lọc từ CHỈ chứa ký tự trong tập L: `only_L(self, L)` (Dòng 30 - 40)
> **Yêu cầu đề:** Mọi ký tự trong từ đó **bắt buộc phải nằm trong tập `L`**. Nếu có dù chỉ 1 ký tự không thuộc `L` thì từ đó bị loại.

```python
def only_L(self, L):
    ket_qua = []
    for tu in self.ds_tu:
        gia_tri = True
        for chu in tu:
            if chu not in L:     # Tìm thấy ký tự lạ không có trong L
                gia_tri = False  # Đánh dấu không hợp lệ
                break            # Dừng ngay, không cần xét tiếp từ này
        if gia_tri is True:
            ket_qua.append(tu)
    return ket_qua
```
- **Kỹ thuật Cờ Hiệu (Flag):** Đặt `gia_tri = True`. Khi phát hiện `chu not in L`, đổi thành `False` và `break`.
- 💡 **Cách viết ngắn bằng hàm `all()`:**
  ```python
  return [tu for tu in self.ds_tu if all(chu in L for chu in tu)]
  ```

---

### E. Lọc từ KHÔNG chứa ký tự nào thuộc tập L: `avoids_L(self, L)` (Dòng 42 - 52)
> **Yêu cầu đề:** Trong từ đó **không được phép xuất hiện bất kỳ ký tự nào trong `L`**.

```python
def avoids_L(self, L):
    ket_qua = []
    for tu in self.ds_tu:
        gia_tri = True
        for chu in tu:
            if chu in L:         # Phát hiện ký tự bị cấm xuất hiện
                gia_tri = False
                break
        if gia_tri is True:
            ket_qua.append(tu)
    return ket_qua
```
- Ngược lại với `only_L`: Ở đây điều kiện loại là `if chu in L:`.
- 💡 **Cách viết ngắn bằng hàm `any()`:**
  ```python
  return [tu for tu in self.ds_tu if not any(chu in L for chu in tu)]
  ```

---

### F. Phương thức hiển thị: `display(self, tieu_de, danh_sach_ket_qua)` (Dòng 54 - 60)
```python
def display(self, tieu_de, danh_sach_ket_qua):
    print(f"\n{tieu_de}:")
    if len(danh_sach_ket_qua) == 0:
        print("   (Không tìm thấy từ nào thỏa mãn)")
    else:
        # Nối các từ lại bằng dấu phẩy
        print(f"   Kết quả: {', '.join(danh_sach_ket_qua)}")
```
- **Hàm `', '.join(list)`:** Ghép toàn bộ các phần tử chuỗi trong list lại với nhau, phân cách bởi dấu phẩy và khoảng trắng.  
  *(Ví dụ: `['apple', 'ant']` ➡️ `"apple, ant"`)*.

---

## 3. TỔNG KẾT BẢNG HÀM XỬ LÝ CHUỖI CẦN THUỘC KHI ĐI THI

| Thao tác xử lý | Cú pháp chuẩn trong Python | Ý nghĩa |
| :--- | :--- | :--- |
| **Tách chuỗi thành danh sách từ** | `s.split()` | Tự động cắt theo dấu cách |
| **Kiểm tra bắt đầu bằng chữ X** | `s.startswith("a")` | Trả về `True` nếu bắt đầu bằng `"a"` |
| **Kiểm tra kết thúc bằng chữ X** | `s.endswith("t")` | Trả về `True` nếu kết thúc bằng `"t"` |
| **Kiểm tra ký tự có trong chuỗi** | `if chu in tap_ky_tu:` | Kiểm tra sự tồn tại của phần tử |
| **Ghép danh sách thành chuỗi đẹp** | `", ".join(danh_sach)` | Nối các từ lại, cách nhau dấu phẩy |
| **Độ dài chuỗi / danh sách** | `len(s)` | Đếm số lượng ký tự hoặc từ |
| **Viết hoa / viết thường** | `s.lower()`, `s.upper()` | Chuẩn hoá trước khi so sánh |
