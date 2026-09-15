from abc import ABC, abstractmethod

class NhanVien(ABC):
    def __init__(self):
        self.ten = ""
        self.tuoi = 0
        self.dia_chi = ""
        self.tien_luong = 0
        self.tong_gio_lam = 0

    def inputInfo(self):
        self.ten = input("Hay nhap ho va ten cua ban: ")
        self.tuoi = int(input("Hay nhap vao tuoi cua ban: "))
        self.dia_chi = input("Hay nhap dia chi cua ban: ")
        self.tien_luong = float(input("Hay nhap vao tien luong: "))
        self.tong_gio_lam = int(input("Hay nhap vao tong gio lam: "))

    def outputInfo(self):
        print(f"Ten la: {self.ten}, Tuoi la: {self.tuoi}, Dia chi là: {self.dia_chi}, Tien luong la: {self.tien_luong}, Tong gio lam la: {self.tong_gio_lam}, Tien thuong la: {self.tinhThuong()}")

    def tinhThuong(self):
        thuong = 0.0
        if self.tong_gio_lam >= 200:
            thuong = self.tien_luong * 0.2
        elif self.tong_gio_lam >= 100:
            thuong = self.tien_luong * 0.1
        else:
            thuong = 0.0
        return thuong

    @abstractmethod
    def tinhLuong(self):
        pass

class NhanVienChinhThuc(NhanVien):
    def __init__(self):
        super().__init__() # Nhớ gọi init của lớp cha để khởi tạo đủ thuộc tính
        self.luong_co_ban = 0
        self.he_so_luong = 0

    def inputInfo(self):
        super().inputInfo() # Gọi nhập thông tin chung của NhanVien
        self.luong_co_ban = float(input("Hay nhap luong co ban cua ban: "))
        self.he_so_luong = float(input("Hay nhap he so luong cua ban: "))

    def outputInfo(self): # Đổi tên từ output thành outputInfo để đồng bộ đa hình
        super().outputInfo()
        print(f"Luong co ban la: {self.luong_co_ban}, He so luong la: {self.he_so_luong}")

    def tinhLuong(self):
        return self.he_so_luong * self.luong_co_ban

class NhanVienThoiVu(NhanVien):
    def __init__(self):
        super().__init__() # Nhớ gọi init của lớp cha
        self.so_gio_lam = 0
        self.muc_luong_gio = 0

    def inputInfo(self):
        NhanVien.inputInfo(self) # Hoặc dùng super().inputInfo()
        self.so_gio_lam = int(input("Hay nhap so gio lam: "))
        self.muc_luong_gio = float(input("Muc luong theo gio la: "))

    def outputInfo(self):
        NhanVien.outputInfo(self)
        print(f"So gio lam la: {self.so_gio_lam}, Muc luong theo gio la: {self.muc_luong_gio}")

    def tinhLuong(self):
        return self.so_gio_lam * self.muc_luong_gio


def main():
    ds_nv = []
    n = int(input("Hay nhap so nhan vien ma ban muon nhap: "))
    
    for i in range(n):
        print(f"\n--- Nhập thông tin nhân viên thứ {i+1} ---")
        loai = input("Bạn muốn nhập nhân viên nào? (1: Chính thức, 2: Thời vụ): ")
        
        if loai == "1":
            nv = NhanVienChinhThuc()
        else:
            nv = NhanVienThoiVu()
            
        nv.inputInfo()      # Nhập dữ liệu
        ds_nv.append(nv)    # Lưu vào danh sách (List Storage)

    # In danh sách và thể hiện tính đa hình (Polymorphism)
    print("\n\n================ DANH SÁCH NHÂN VIÊN ================")
    for i, nv in enumerate(ds_nv, 1):
        print(f"\nNhân viên {i}:")
        nv.outputInfo()
        print(f"=> Tổng lương thực nhận (tinhLuong): {nv.tinhLuong()}")

if __name__ == "__main__":
    main()