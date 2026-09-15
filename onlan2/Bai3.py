from itertools import combinations

class TapHopCon:
    def __init__(self):
        self.danh_sach = []

    # Phương thức f1: Lấy danh sách số nguyên từ người dùng
    def f1(self):
        chuoi_nhap = input("Nhập các số nguyên, cách nhau bằng khoảng trắng: ")
        # Ép kiểu chuỗi thành danh sách số nguyên
        self.danh_sach = [int(x) for x in chuoi_nhap.split()]
        print(f"Đã nhận danh sách: {self.danh_sach}")

    # Phương thức f2: Tính toán tất cả các tập hợp con có thể của danh sách
    def f2(self):
        tat_ca_tap_con = []
        # Duyệt qua tất cả các độ dài có thể của tập con (từ 0 đến len(danh_sach))
        for r in range(len(self.danh_sach) + 1):
            # combinations trả về dạng tuple, ta chuyển sang list
            tap_con_do_dai_r = [list(comb) for comb in combinations(self.danh_sach, r)]
            tat_ca_tap_con.extend(tap_con_do_dai_r)
        return tat_ca_tap_con

# Chương trình chính (Menu lựa chọn)
def main():
    thiet_bi = TapHopCon()
    
    while True:
        print("\n--- MENU QUẢN LÝ TẬP HỢP CON ---")
        print("1. Nhập danh sách (f1)")
        print("2. In ra kết quả các tập hợp con (f2)")
        print("3. Thoát")
        
        chon = input("Chọn chức năng (1-3): ")
        
        if chon == "1":
            thiet_bi.f1()
        elif chon == "2":
            if not thiet_bi.danh_sach:
                print("Chưa có danh sách! Vui lòng nhập ở chức năng 1 trước.")
            else:
                ket_qua = thiet_bi.f2()
                print("Các tập hợp con có thể là:")
                for sub in ket_qua:
                    print(sub)
        elif chon == "3":
            print("Đã thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại!")

if __name__ == "__main__":
    main()