class HotelRoom:
    def __init__(self, room_number="", room_type="Standard", price_per_night=500000.0, is_available=True):
        self.room_number=room_number
        self.room_type=room_type # Standard / Deluxe / Suite
        self.price_per_night=price_per_night
        self.is_available=is_available

    def display(self):
        trang_thai="Trong" if self.is_available else "Da dat"
        print(f"Phong: {self.room_number:<6} | Loai: {self.room_type:<10} | Gia/dem: {self.price_per_night:>10,.0f} VND | Trang thai: {trang_thai}")


class HotelManager:
    def __init__(self):
        self.rooms=[]

    def add_room(self, room):
        for r in self.rooms:
            if r.room_number==room.room_number:
                print(f"Phong so {room.room_number} da ton tai!")
                return False
        self.rooms.append(room)
        return True

    def find_available_rooms(self):
        available=[r for r in self.rooms if r.is_available]
        print("\n--- DANH SACH PHONG CON TRONG ---")
        if not available:
            print("Hien tai khong con phong trong.")
        else:
            for r in available:
                r.display()
        return available

    def book_room(self, room_number):
        for r in self.rooms:
            if r.room_number==room_number:
                if not r.is_available:
                    print(f"Dat phong that bai: Phong {room_number} da co khach dat!")
                    return False
                r.is_available=False
                print(f"Dat phong {room_number} thanh cong!")
                return True
        print(f"Khong tim thay phong so {room_number}!")
        return False

    def check_out(self, room_number, nights):
        if nights<=0:
            print("So dem luu tru phai lon hon 0!")
            return 0.0
        for r in self.rooms:
            if r.room_number==room_number:
                if r.is_available:
                    print(f"Phong {room_number} hien dang trong, khong the tra phong!")
                    return 0.0
                total=r.price_per_night*nights
                r.is_available=True
                print(f"Tra phong {room_number} thanh cong. So dem: {nights}, Tong tien: {total:,.0f} VND")
                return total
        print(f"Khong tim thay phong so {room_number}!")
        return 0.0


def main():
    ql=HotelManager()
    ql.add_room(HotelRoom("P101", "Standard", 400000))
    ql.add_room(HotelRoom("P102", "Standard", 400000))
    ql.add_room(HotelRoom("P201", "Deluxe", 800000))
    ql.add_room(HotelRoom("P301", "Suite", 1500000))

    ql.find_available_rooms()

    print("\n--- DAT PHONG ---")
    ql.book_room("P101")
    ql.book_room("P201")
    ql.book_room("P101") # thu dat lai

    ql.find_available_rooms()

    print("\n--- TRA PHONG & THANH TOAN ---")
    ql.check_out("P101", 3)
    ql.find_available_rooms()


if __name__=="__main__":
    main()
