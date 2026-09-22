class Room:
    def __init__(self):
        self.room_number=""
        self.room_type=""
        self.price=0
        self.status="Trong"
        self.nights=0

    def input(self):
        self.room_number=input("Hay nhap so phong: ")
        self.room_type=input("Hay nhap loai phong: ")
        self.price=float(input("Hay nhap gia phong moi dem: "))

    def display(self):
        print(f"Phong: {self.room_number}, Loai: {self.room_type}, Gia: {self.price}, Trang thai: {self.status}")


class HotelManager:
    def __init__(self):
        self.rooms=[]
        self.total_revenue=0

    def add_room(self, room):
        for r in self.rooms:
            if r.room_number==room.room_number:
                print("So phong da ton tai")
                return False
        self.rooms.append(room)
        print("Them phong thanh cong")
        return True

    def find_available_rooms(self):
        print("Danh sach phong con trong:")
        for r in self.rooms:
            if r.status=="Trong":
                r.display()

    def book_room(self, room_number, nights):
        for r in self.rooms:
            if r.room_number==room_number:
                if r.status=="Trong":
                    r.status="Da dat"
                    r.nights=nights
                    print("Dat phong thanh cong")
                    return True
                else:
                    print("Phong nay da co nguoi dat")
                    return False
        print("Khong tim thay so phong")
        return False

    def checkout(self, room_number):
        for r in self.rooms:
            if r.room_number==room_number:
                if r.status=="Da dat":
                    tien=r.price*r.nights
                    self.total_revenue+=tien
                    r.status="Trong"
                    print(f"Tra phong thanh cong, so tien phai tra la: {tien}")
                    return tien
                else:
                    print("Phong dang trong khong the tra")
                    return 0
        print("Khong tim thay so phong")
        return 0

    def revenue(self):
        return self.total_revenue

def main():
    hotel=HotelManager()

    n=int(input("Hay nhap so luong phong can tao: "))
    for i in range(n):
        r=Room()
        r.input()
        hotel.add_room(r)

    hotel.find_available_rooms()

    so_dat=input("Hay nhap so phong can dat: ")
    so_dem=int(input("Hay nhap so dem muon o: "))
    hotel.book_room(so_dat, so_dem)

    so_tra=input("Hay nhap so phong can tra: ")
    hotel.checkout(so_tra)

    print("Tong doanh thu khach san la: ", hotel.revenue())

if __name__=="__main__":
    main()
