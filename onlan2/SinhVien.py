class SinhVien:
    # Hàm khởi tạo đầy đủ tham số
    def __init__(self, ma_sv, ten, nam_sinh, diem_tb):
        self.ma_sv = ma_sv
        self.ten = ten
        self.nam_sinh = nam_sinh
        self.diem_tb = diem_tb

def dem_sinh_vien_len_lop(danh_sach_sv):
    dem = 0
    print("\n--- DANH SÁCH SINH VIÊN ĐỦ ĐIỀU KIỆN LÊN LỚP ---")
    for sv in danh_sach_sv:
        # Kiểm tra điều kiện điểm trung bình >= 5
        if sv.diem_tb >= 5.0:
            print(f"Mã SV: {sv.ma_sv} | Tên: {sv.ten} | ĐTB: {sv.diem_tb}")
            dem += 1
    return dem

def main_bai3():
    n = int(input("Nhập số lượng sinh viên n = "))
    danh_sach = []
    
    # Nhập danh sách sinh viên
    for i in range(n):
        print(f"\nNhập thông tin sinh viên thứ {i+1}:")
        ma_sv = input("Mã SV (10 ký tự): ")
        ten = input("Tên (Tối đa 20 ký tự): ")
        nam_sinh = int(input("Năm sinh: "))
        diem_tb = float(input("Điểm trung bình: "))
        
        # Khởi tạo đối tượng và thêm vào danh sách
        sv = SinhVien(ma_sv, ten, nam_sinh, diem_tb)
        danh_sach.append(sv)
        
    # Gọi hàm đếm và in kết quả
    so_luong = dem_sinh_vien_len_lop(danh_sach)
    print(f"\n=> Tổng cộng có {so_luong} sinh viên đủ điều kiện lên lớp.")

# Chạy thử chương trình
if __name__ == "__main__":
    main_bai3()