class Flight:
    def __init__(self, flight_code="", destination="", total_seats=100):
        self.flight_code=flight_code
        self.destination=destination
        self.total_seats=total_seats
        self.booked_seats=[] # danh sach ten khach hang

    def is_full(self):
        return len(self.booked_seats)>=self.total_seats

    def book_seat(self, passenger_name):
        if self.is_full():
            print(f"Dat ve that bai: Chuyen bay {self.flight_code} den {self.destination} da day cho!")
            return False
        if passenger_name in self.booked_seats:
            print(f"Khach hang '{passenger_name}' da co ten tren chuyen bay {self.flight_code}!")
            return False
        self.booked_seats.append(passenger_name)
        print(f"Dat ve thanh cong: Khach '{passenger_name}' - Chuyen bay {self.flight_code} ({self.destination}).")
        return True

    def cancel_seat(self, passenger_name):
        if passenger_name not in self.booked_seats:
            print(f"Huy ve that bai: Khong tim thay khach '{passenger_name}' tren chuyen bay {self.flight_code}!")
            return False
        self.booked_seats.remove(passenger_name)
        print(f"Huy ve thanh cong cho khach '{passenger_name}' tren chuyen bay {self.flight_code}.")
        return True

    def display(self):
        so_da_dat=len(self.booked_seats)
        so_con_lai=self.total_seats-so_da_dat
        trang_thai="HET VE" if self.is_full() else f"Con {so_con_lai} cho"
        print(f"Chuyen bay: {self.flight_code:<8} | Den: {self.destination:<16} | Tong: {self.total_seats:>3} cho | Da dat: {so_da_dat:>3} | Trang thai: {trang_thai}")


def main():
    # Quan ly 3 chuyen bay dong thoi
    flights=[
        Flight("VN123", "Ha Noi", total_seats=3),
        Flight("VJ456", "Da Nang", total_seats=5),
        Flight("QH789", "Phu Quoc", total_seats=4)
    ]

    print("--- TRANG THAI CAC CHUYEN BAY BAN DAU ---")
    for f in flights:
        f.display()

    print("\n--- THUC HIEN DAT VE ---")
    flights[0].book_seat("Nguyen Van An")
    flights[0].book_seat("Tran Thi Binh")
    flights[0].book_seat("Le Hoang Cuong")
    flights[0].book_seat("Pham Thi Dung") # thu vuot qua so cho

    flights[1].book_seat("Vu Hoang Giang")
    flights[1].book_seat("Do Mai Lan")

    print("\n--- THUC HIEN HUY VE ---")
    flights[0].cancel_seat("Tran Thi Binh")

    print("\n--- TRANG THAI CAC CHUYEN BAY SAU KHI GIAO DICH ---")
    for f in flights:
        f.display()


if __name__=="__main__":
    main()
