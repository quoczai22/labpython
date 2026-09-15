from abc import ABC, abstractmethod
import math

# 1. Tạo lớp trừu tượng
class HinhHoc(ABC):
    @abstractmethod
    def tinh_dien_tich(self):
        pass

# 2. Lớp con Hình Tròn
class HinhTron(HinhHoc):
    def __init__(self, ban_kinh):
        self.ban_kinh = ban_kinh
        
    # Ghi đè phương thức tính diện tích (Công thức: pi * r^2)
    def tinh_dien_tich(self):
        return math.pi * (self.ban_kinh ** 2)

# 3. Lớp con Hình Chữ Nhật
class HinhChuNhat(HinhHoc):
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong
        
    # Ghi đè phương thức tính diện tích (Công thức: dài * rộng)
    def tinh_dien_tich(self):
        return self.dai * self.rong

def main_bai4():
    # 4. Tạo danh sách chứa các đối tượng hình học khác nhau
    danh_sach_hinh = [
        HinhTron(5),          # Bán kính 5
        HinhChuNhat(4, 6),    # Dài 4, rộng 6
        HinhTron(2.5),        # Bán kính 2.5
        HinhChuNhat(10, 5)    # Dài 10, rộng 5
    ]
    
    print("--- THỂ HIỆN TÍNH ĐA HÌNH KHI TÍNH DIỆN TÍCH ---")
    # Dùng vòng lặp duyệt qua và gọi phương thức
    for i, hinh in enumerate(danh_sach_hinh, 1):
        # hinh.__class__.__name__ để lấy tên của Class phục vụ việc in kết quả rõ ràng
        ten_hinh = hinh.__class__.__name__
        dien_tich = hinh.tinh_dien_tich()
        print(f"Đối tượng {i} ({ten_hinh}): Diện tích = {dien_tich:.2f}")

# Chạy thử chương trình
if __name__ == "__main__":
    main_bai4()