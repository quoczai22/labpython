# ==========================================
# BÀI 1: KIỂU DỮ LIỆU & RẼ NHÁNH CƠ BẢN
# ==========================================

# Câu 1: Chuyển đổi số nguyên sang float và str
def chuyensonguyenso(n): 
    return float(n), str(n)

# Câu 2: Kiểm tra chẵn lẻ
def kiemtrachanle(n):
    return n % 2 == 0

# Câu 3: Phân loại tuổi
def phanloaituoi(n):
    if n < 12:
        return "Trẻ em"
    elif n < 18:
        return "Thiếu niên"
    else:
        return "Người lớn"

# Câu 4: Tìm số lớn nhất trong 3 số
def solonnhattrong3so(a, b, c):
    return max(a, b, c)

# Câu 5: Kiểm tra năm nhuận
def namnhuan(n):
    return (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0)


# ==========================================
# BÀI 2: VÒNG LẶP
# ==========================================

# Câu 1: In số từ 1 đến 10
def insotu1den10():
    for i in range(1, 11):
        print(i)

# Câu 2: In bảng cửu chương
def bangcuuchuong(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

# Câu 3: Tính tổng từ 1 đến n
def tongtu1denn(n):
    return sum(range(1, n + 1))

# Câu 4: Vẽ tam giác vuông sao
def vetamgiacvuong(n):
    for i in range(1, n + 1):
        print("*" * i)


# ==========================================
# BÀI 3: CHUỖI (STRING)
# ==========================================

# Câu 1: Chuyển họ tên thành chữ thường
def chuyenhotenthanhchuthuong1(n):
    return n.lower()

# Câu 2a: Đếm số lượng ký tự có trong chuỗi
def demsoluongkytucotrongchuoi(n):
    return len(n)

# Câu 2b: Đếm số chữ số và chữ cái trong chuỗi
def demsochusovasochucai(n):
    demsochuso = 0
    demsochucai = 0
    for i in n:
        if i.isdigit():
            demsochuso += 1
        elif i.isalpha():
            demsochucai += 1
    return demsochucai, demsochuso

# Câu 3: Đếm số lần xuất hiện của mỗi từ trong câu
def demsolanxuathiencuatu(n):
    tu = n.split()
    demtu = {}
    for i in tu:
        demtu[i] = demtu.get(i, 0) + 1
    return demtu

def demsotuxuathien(n):
    dstu = n.split()
    for i in set(dstu):
        print(f"Từ '{i}' xuất hiện {dstu.count(i)} lần")

# Câu 4: Kiểm tra chuỗi đối xứng (Palindrome)
def kiemtrachuoidoiung(n):
    chuoi_chuan_hoa = n.lower().replace(" ", "")
    return chuoi_chuan_hoa == chuoi_chuan_hoa[::-1]


# ==========================================
# BÀI 4: DANH SÁCH (LIST)
# ==========================================

# Câu 1: Chuyển chuỗi các số cách nhau bởi khoảng trắng thành List số nguyên
def chuyenchuoi_thanhlistso(n):
    return [int(x) for x in n.split()]

# Câu 2: Tính tổng và giá trị lớn nhất trong List
def tinh_tong_va_max(n):
    return sum(n), max(n)

# Câu 3: Sắp xếp danh sách tên học sinh theo Alphabet
def sap_xep_ten(n):
    return sorted(n)

# Câu 4: Tính trung bình cộng của List số
def tbc(n):
    return sum(n) / len(n) if len(n) > 0 else 0

# Câu 5: Loại bỏ phần tử trùng lặp
def loaibotrunglap1(n):
    # Giữ nguyên thứ tự ban đầu
    ds_songuyen = []
    for i in n:
        if i not in ds_songuyen:
            ds_songuyen.append(i)
    return ds_songuyen

def loaibotrunglap2(n):
    # Dùng set (không đảm bảo thứ tự ban đầu)
    return list(set(n))

def chuyenhoathanhthuong(n):
    return n.lower()

# Câu 6: Trộn và sắp xếp 2 List
def tron(a, b):
    return a + b

def sapxep(n):
    return sorted(n)


# ==========================================
# BÀI 5: TẬP HỢP (SET)
# ==========================================

# Câu 1: Thêm phần tử vào Set
def themvaoset(s, pt):
    s.add(pt)
    return s

# Câu 2: Kiểm tra phần tử trong Set
def kiemtraphantuinset(s, pt):
    return pt in s

# Câu 3: Hiệu và giao của 2 Set
def hieu_va_giao_cua_2_set(s1, s2):
    hieu = s1 - s2
    giao = s1 & s2
    return hieu, giao

# Câu 4: Chuyển List sang Set và lọc lấy các số chẵn
def locsochan(l):
    return {x for x in l if x % 2 == 0}


# ==========================================
# BÀI 6: TỪ ĐIỂN (DICTIONARY)
# ==========================================

# Câu 1: Tạo dictionary thông tin sinh viên
def tao_dictionary_sinh_vien():
    return {"Tên": "Nguyễn Văn A", "Tuổi": 20, "Lớp": "12A1"}

# Câu 2: Thêm và xóa thuộc tính trong dictionary
def them_thuoc_tinh(dictionary, key, value):
    dictionary[key] = value
    return dictionary

def xoa_thuoc_tinh(dictionary, key):
    if key in dictionary:
        del dictionary[key]
    return dictionary

# Câu 3: Khởi tạo dictionary điểm các môn học
def init_dic_monhoc(toan, van, anh):
    return {"Toán": toan, "Văn": van, "Anh": anh}

# Câu 4: Tính điểm trung bình và lưu vào dictionary môn học
def dic_dtb(monhoc):
    # Chỉ tính trung bình các môn học, tránh cộng dồn nếu key "Điểm trung bình" đã tồn tại
    ds_diem = [v for k, v in monhoc.items() if k != "Điểm trung bình"]
    dtb = sum(ds_diem) / len(ds_diem) if ds_diem else 0
    them_thuoc_tinh(monhoc, "Điểm trung bình", dtb)
    return dtb

# Câu 5: Sắp xếp danh sách sinh viên theo ĐTB giảm dần
def dic_asc_dtb(sinh_vien):
    for ten, monhoc in sinh_vien.items():
        dic_dtb(monhoc)
    sorted_sinh_vien = dict(sorted(sinh_vien.items(), key=lambda item: item[1]["Điểm trung bình"], reverse=True))
    return sorted_sinh_vien 


# ==========================================
# PHẦN 3: LỚP VÀ ĐỐI TƯỢNG (OOP - CHƯƠNG 2)
# ==========================================

# Bài 1: Lớp Rectangle (Hình chữ nhật)
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def getWidth(self):
        return self.width
        
    def getHeight(self):
        return self.height
        
    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return (self.width + self.height) * 2

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height}, Area={self.getArea()})"


# Bài 2: Lớp Person (Khai báo tham số mặc định)
class Person:
    # Tham số age và gender có giá trị mặc định
    def __init__(self, name, age=1, gender="Male"):
        self.name = name
        self.age = age
        self.gender = gender
        
    def showInfo(self):
        print("Name:  ", self.name)
        print("Age:   ", self.age)
        print("Gender:", self.gender)
        print("-" * 20)


# Bài 3: Lớp Player (Quản lý thuộc tính động)
class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Bài 4: Lớp Car (Phân biệt thuộc tính lớp và thuộc tính đối tượng)
class Car:
    # Thuộc tính của Lớp (Class Attribute) - dùng chung cho mọi đối tượng
    loaixe = "Ô tô 4 bánh" 
    
    def __init__(self, tenxe, mausac, nguyenlieu):
        # Thuộc tính thực thể (Instance Attribute) - riêng biệt cho từng đối tượng
        self.tenxe = tenxe
        self.mausac = mausac
        self.nguyenlieu = nguyenlieu

    def hien_thi_thong_tin(self):
        print(f"Loại xe: {Car.loaixe} | Tên: {self.tenxe} | Màu: {self.mausac} | Nhiên liệu: {self.nguyenlieu}")


def test_oop():
    print("\n" + "=" * 45)
    print("--- TEST PHẦN 3: LỚP VÀ ĐỐI TƯỢNG (OOP) ---")
    print("=" * 45)

    print("\n--- TEST LỚP RECTANGLE ---")
    r1 = Rectangle(10, 5)
    print(f"r1.width = {r1.width}")
    print(f"r1.getArea() = {r1.getArea()}")

    print("\n--- TEST LỚP PERSON ---")
    aimee = Person("Aimee", 21, "Female")
    aimee.showInfo()
    
    alice = Person("Alice") # Sử dụng giá trị mặc định cho age và gender
    alice.showInfo()
    
    tran = Person("Tran", 37)
    tran.showInfo()

    print("\n--- TEST LỚP PLAYER VÀ HÀM THUỘC TÍNH ---")
    player1 = Player("Tom", 20)
    
    # getattr: Lấy giá trị thuộc tính
    print("getattr(player1, 'name') =", getattr(player1, "name"))
    
    # setattr: Đặt giá trị mới cho thuộc tính đã có, hoặc tạo thuộc tính mới
    setattr(player1, "age", 21) 
    print("player1.age sau khi setattr =", player1.age)
    
    # hasattr: Kiểm tra xem thuộc tính có tồn tại không
    print("hasattr(player1, 'address')?", hasattr(player1, "address"))
    
    # Tạo thuộc tính mới address
    setattr(player1, "address", "USA")
    print("player1.address =", player1.address)
    
    # delattr: Xóa thuộc tính
    delattr(player1, "address")
    print("Đã xóa thuộc tính address.")

    print("\n--- TEST LỚP CAR ---")
    toyota = Car("Vios", "Trắng", "Xăng")
    # Truy cập thuộc tính class
    print("Loại xe (Class Attribute):", Car.loaixe)
    # Truy cập thuộc tính đối tượng
    print(f"Xe Toyota: {toyota.tenxe}, màu {toyota.mausac}, chạy {toyota.nguyenlieu}")


def main():
    # Chạy kiểm tra phần OOP
    test_oop()

    # --- ĐOẠN CODE HOÀN THIỆN CHO BÀI 6 (DICTIONARY) ---
    print("\n" + "=" * 45)
    print("=== CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN (BÀI 6) ===")
    print("=" * 45)
    n = int(input("Hãy nhập số lượng sinh viên mà bạn muốn nhập: "))
    ds_sinh_vien = {}

    for i in range(n):
        print(f"\n--- Nhập thông tin sinh viên thứ {i+1} ---")
        ten = input("Nhập tên sinh viên: ")
        toan = float(input("Nhập điểm Toán: "))
        van = float(input("Nhập điểm Văn: "))
        anh = float(input("Nhập điểm Anh: "))
        
        # Khởi tạo dic điểm và lưu vào ds_sinh_vien
        ds_sinh_vien[ten] = init_dic_monhoc(toan, van, anh)
    
    # Sắp xếp và hiển thị
    ds_da_sap_xep = dic_asc_dtb(ds_sinh_vien)
    
    print("\n--- DANH SÁCH SINH VIÊN ĐÃ SẮP XẾP THEO ĐTB GIẢM DẦN ---")
    for ten, thong_tin in ds_da_sap_xep.items():
        print(f"Tên: {ten:<15} | Điểm trung bình: {thong_tin['Điểm trung bình']:.2f} | Chi tiết: {thong_tin}")


if __name__ == "__main__":
    main()