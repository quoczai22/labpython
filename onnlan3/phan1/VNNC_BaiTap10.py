class Showtime:
    def __init__(self, show_id="", movie_name="", time="", ticket_price=0.0):
        self.show_id=show_id
        self.movie_name=movie_name
        self.time=time
        self.ticket_price=ticket_price

    def display(self):
        print(f"Suat chieu: [{self.show_id}] {self.movie_name} | Gio chieu: {self.time} | Gia ve: {self.ticket_price:,.0f} VND")


class CinemaRoom:
    def __init__(self, room_name="Phong 01", rows=5, cols=6):
        self.room_name=room_name
        self.rows=rows
        self.cols=cols
        # Ma tran 2 chieu: 0 la ghe trong, 1 la ghe da dat
        self.seat_matrix=[[0 for _ in range(cols)] for _ in range(rows)]

    def display_seats(self):
        print("\n" + "="*45)
        print(f"{'SO DO GHE NGOI - ' + self.room_name:^45}")
        print(f"{'====== MAN HINH (SCREEN) ======':^45}")
        print("="*45)
        
        # In so cot (1, 2, 3...)
        col_header="     " + "  ".join(f"{c+1:>3}" for c in range(self.cols))
        print(col_header)
        print("    " + "-"*(self.cols*5+2))

        # In cac hang (A, B, C...)
        for r in range(self.rows):
            row_label=chr(ord('A')+r)
            row_str=f" {row_label} |"
            for c in range(self.cols):
                seat_symbol="[X]" if self.seat_matrix[r][c]==1 else "[O]"
                row_str+=f" {seat_symbol}"
            print(row_str)
        print("="*45)
        print("Chu thich: [O] Ghế trống | [X] Ghế đã đặt")

    def book_seat(self, row_idx, col_idx):
        # Kiem tra chi so hop le trong ma tran
        if not (0<=row_idx<self.rows and 0<=col_idx<self.cols):
            row_label=chr(ord('A')+row_idx) if 0<=row_idx<26 else str(row_idx)
            print(f"Vi tri ghe ({row_label}{col_idx+1}) khong ton tai trong phong chieu!")
            return False

        row_label=chr(ord('A')+row_idx)
        seat_name=f"{row_label}{col_idx+1}"

        if self.seat_matrix[row_idx][col_idx]==1:
            print(f"Dat ve that bai: Ghe {seat_name} da co nguoi dat truoc do!")
            return False

        self.seat_matrix[row_idx][col_idx]=1
        print(f"Dat ghe thanh cong: Vi tri [{seat_name}] tai {self.room_name}.")
        return True

    def count_booked_seats(self):
        return sum(row.count(1) for row in self.seat_matrix)

    def calculate_revenue(self, showtime):
        return self.count_booked_seats()*showtime.ticket_price

    def display_ticket_receipt(self, row_idx, col_idx, showtime):
        row_label=chr(ord('A')+row_idx)
        seat_name=f"{row_label}{col_idx+1}"
        print("\n" + "*"*45)
        print(f"{'HOA DON VE XEM PHIM DIEN TU':^45}")
        print("*"*45)
        print(f"Phong chieu : {self.room_name}")
        print(f"Phim        : {showtime.movie_name}")
        print(f"Suat chieu  : {showtime.time} (Ma: {showtime.show_id})")
        print(f"Ghe ngoi    : {seat_name} (Hang {row_label}, Cot {col_idx+1})")
        print(f"Gia ve      : {showtime.ticket_price:,.0f} VND")
        print(f"Trang thai  : DA THANH TOAN THANH CONG")
        print("*"*45)


def main():
    # 1. Khoi tao suat chieu
    suat_chieu=Showtime("ST01", "Avatar: Dong Chay Cua Nuoc", "19:30", 90000)
    suat_chieu.display()

    # 2. Khoi tao phong chieu 5 hang x 6 cot (Hang A -> E, Cot 1 -> 6)
    phong=CinemaRoom("Phong Chieu IMAX 01", rows=5, cols=6)

    # 3. Hien thi so do ban dau
    print("\n--- SO DO PHONG CHIEU BAN DAU ---")
    phong.display_seats()

    # 4. Thuc hien dat ghe
    print("\n--- THUC HIEN DAT VE ---")
    # Dat ghe A1 (row 0, col 0)
    if phong.book_seat(0, 0):
        phong.display_ticket_receipt(0, 0, suat_chieu)

    # Dat ghe C3 (row 2, col 2)
    phong.book_seat(2, 2)

    # Dat ghe C4 (row 2, col 3)
    phong.book_seat(2, 3)

    # Thu dat lai ghe C3 (da bi dat)
    print("\n[Thu dat lai ghe da co nguoi]:")
    phong.book_seat(2, 2)

    # Thu dat ghe ngoai pham vi
    print("\n[Thu dat ghe ngoai pham vi]:")
    phong.book_seat(6, 8)

    # 5. Hien thi so do sau khi dat
    print("\n--- SO DO PHONG CHIEU SAU KHI DAT ---")
    phong.display_seats()

    # 6. Tong ket doanh thu phong chieu
    tong_so_ve=phong.count_booked_seats()
    doanh_thu=phong.calculate_revenue(suat_chieu)
    print(f"\n=> Tong so ghe da dat: {tong_so_ve} ghe")
    print(f"=> Tong doanh thu phong chieu: {doanh_thu:,.0f} VND")


if __name__=="__main__":
    main()
