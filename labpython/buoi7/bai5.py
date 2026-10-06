import datetime 

class SinhVien:
    ds = []
    def __init__(self):
        self.__ma_sv = ""
        self.__ten_sv = ""
        self.__nam_sinh = 0
        self.__diem_trung_binh = 0.0
        
    def get_ma_sv(self):
        return self.__ma_sv
    
    def set_ma_sv(self, ma_sv):
        if len(ma_sv) != 10:
            print("Lỗi: Mã sinh viên phải đúng 10 ký tự!")
            return False
        self.__ma_sv = ma_sv
        return True
        
    def get_ten_sv(self):
        return self.__ten_sv
    
    def set_ten_sv(self, ten_sv):
        if len(ten_sv.strip()) == 0 or len(ten_sv) > 20:
            print("Lỗi: Tên sinh viên không được để trống và phải tối đa 20 ký tự!")
            return False
        self.__ten_sv = ten_sv
        return True
    
    def get_nam_sinh(self):
        return self.__nam_sinh
    
    def set_nam_sinh(self, nam_sinh):
        if nam_sinh <= 1900 or nam_sinh > int(datetime.date.today().year):
            print("Lỗi: Năm sinh không hợp lệ!")
            return False
        self.__nam_sinh = nam_sinh
        return True
        
    def get_diem_trung_binh(self):
        return self.__diem_trung_binh
        
    def set_diem_trung_binh(self, dtb):
        if dtb < 0.0 or dtb > 10.0:
            print("Lỗi: Điểm trung bình phải từ 0.0 đến 10.0!")
            return False
        self.__diem_trung_binh = dtb
        return True
        
    def input_info(self):
        while True:
            ma_sv = input("Nhập mã sinh viên (đúng 10 ký tự): ")
            if self.set_ma_sv(ma_sv):
                break
                
        while True:
            ten_sv = input("Nhập tên sinh viên (tối đa 20 ký tự): ")
            if self.set_ten_sv(ten_sv):
                break
                
        while True:
            try:
                nam_sinh = int(input("Nhập năm sinh (số nguyên): "))
                if self.set_nam_sinh(nam_sinh):
                    break
            except ValueError:
                print("Lỗi: Vui lòng nhập vào một số nguyên!")
                
        while True:
            try:
                dtb = float(input("Nhập điểm trung bình (số thực a): "))
                if self.set_diem_trung_binh(dtb):
                    break
            except ValueError:
                print("Lỗi: Vui lòng nhập vào một số thực!")
        
    def them_vao_ds_sinh_vien(self):
        for sv in SinhVien.ds:
            if sv.get_ma_sv() == self.get_ma_sv():
                print("Sinh viên này đã tồn tại trong danh sách!")
                return False
        
        SinhVien.ds.append(self)
        print("Đã thêm sinh viên thành công!")
        return True
        
    def xet_dieu_kien(self):
        if self.__diem_trung_binh >= 5:
            return True
        else:
            return False
        
    def sinh_vien_da_20(self):
        nam_hien_tai = int(datetime.date.today().year)
        if nam_hien_tai - self.__nam_sinh < 20:
            return False
        return True
    
    @classmethod
    def dem_sinh_vien_dh(cls):
        dem = 0
        for sv in cls.ds:
            ma = sv.get_ma_sv()
            if len(ma) >= 4:
                chuoi_he_da_hoc = ma[2:4]
                if chuoi_he_da_hoc == "DH":
                    dem = dem + 1
        return dem
    
    @classmethod
    def dem_sinh_vien_ten_lan(cls):
        dem = 0
        for sv in cls.ds:
            ho_va_ten = sv.get_ten_sv().strip()
            cac_tu = ho_va_ten.split()
            if len(cac_tu) > 0:
                ten = cac_tu[-1]
                if ten.lower() == "lan":
                    dem = dem + 1
        return dem

    @classmethod
    def dem_sinh_vien_ho_phan(cls):
        dem = 0
        for sv in cls.ds:
            ho_va_ten = sv.get_ten_sv().strip()
            cac_tu = ho_va_ten.split()
            if len(cac_tu) > 0:
                ho = cac_tu[0]
                if ho.lower() == "phan":
                    dem = dem + 1
        return dem
    
    def display(self):
        print(f"Mã SV: {self.__ma_sv}, Tên SV: {self.__ten_sv}, Năm sinh: {self.__nam_sinh}, ĐTB: {self.__diem_trung_binh}")
    
def main():
    n = int(input("Nhập số lượng sinh viên bạn muốn nhập: "))
    
    for i in range(n):
        print(f"\n--- Nhập thông tin sinh viên thứ {i+1} ---")
        sv = SinhVien()
        sv.input_info()
        sv.them_vao_ds_sinh_vien()
        
    print("\n" + "="*15 + " DANH SÁCH SINH VIÊN " + "="*15)
    for sv in SinhVien.ds:
        sv.display() 
        
    print("\n" + "="*15 + " KẾT QUẢ THỐNG KÊ " + "="*15)
    print(f"Số sinh viên hệ Đại học: {SinhVien.dem_sinh_vien_dh()}")
    print(f"Số sinh viên có tên 'Lan': {SinhVien.dem_sinh_vien_ten_lan()}")
    print(f"Số sinh viên có họ 'Phan': {SinhVien.dem_sinh_vien_ho_phan()}")
    print("=" * 48)
        
if __name__ == "__main__":
    main()