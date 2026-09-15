from abc import ABC, abstractmethod
import math

# Lớp trừu tượng cha
class HinhHoc(ABC):
    @abstractmethod
    def tinh_dien_tich(self):
        pass

# Lớp con Hình Tròn kế thừa từ HinhHoc
class HinhTron(HinhHoc):
    def __init__(self, ban_kinh):
        self.ban_kinh = ban_kinh

    # Bắt buộc phải cài đặt lại phương thức trừu tượng của lớp cha
    def tinh_dien_tich(self):
        return math.pi * (self.ban_kinh ** 2)

# Lớp con Hình Chữ Nhật kế thừa từ HinhHoc
class HinhChuNhat(HinhHoc):
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong

    def tinh_dien_tich(self):
        return self.dai * self.rong