class FoodItem:
    def __init__(self, item_id="", name="", price=0.0):
        self.item_id=item_id
        self.name=name
        self.price=price

    def nhap(self):
        self.item_id=input("Hay nhap ma mon an: ")
        self.name=input("Hay nhap ten mon an: ")
        while True:
            try:
                gia=float(input("Hay nhap don gia: "))
                if gia>0:
                    self.price=gia
                    break
                print("Don gia phai lon hon 0!")
            except ValueError:
                print("Don gia phai la so hop le!")

    def hien_thi(self):
        print(f"[{self.item_id}] {self.name} - Don gia: {self.price:,.0f} VND")


class FoodOrder:
    def __init__(self, distance_km=0.0):
        self.items=[] # danh sach cac tuple (food_item, quantity)
        self.distance_km=distance_km

    def add_item(self, food_item, quantity=1):
        if quantity<=0:
            print("So luong mon phai lon hon 0!")
            return False
        # Kiem tra neu mon da ton tai thi cong don so luong
        for i, (item, qty) in enumerate(self.items):
            if item.item_id==food_item.item_id:
                self.items[i]=(item, qty+quantity)
                return True
        self.items.append((food_item, quantity))
        return True

    def calculate_delivery_fee(self):
        # Phi ship luy tien theo khoang cach
        if self.distance_km<3.0:
            return 15000.0
        elif self.distance_km<6.0:
            return 25000.0
        else:
            return 50000.0

    def subtotal(self):
        return sum(item.price*qty for item, qty in self.items)

    def total_payment(self):
        return self.subtotal()+self.calculate_delivery_fee()

    def display_receipt(self):
        print("="*50)
        print(f"{'BIEN LAI DAT MON AN TRUC TUYEN':^50}")
        print("="*50)
        print(f"{'STT':<4}{'Ten mon an':<22}{'SL':>4}{'Don gia':>10}{'T.Tien':>10}")
        print("-"*50)
        for idx, (item, qty) in enumerate(self.items, 1):
            thanh_tien=item.price*qty
            print(f"{idx:<4}{item.name:<22}{qty:>4}{item.price:>10,.0f}{thanh_tien:>10,.0f}")
        print("-"*50)
        print(f"Khoang cach giao hang:{self.distance_km:>22.1f} km")
        print(f"Tong tien mon an (Subtotal):{self.subtotal():>22,.0f} VND")
        print(f"Phi giao hang (Delivery Fee):{self.calculate_delivery_fee():>21,.0f} VND")
        print("="*50)
        print(f"TONG THANH TOAN:{self.total_payment():>34,.0f} VND")
        print("="*50)


def main():
    # Danh muc mon an co san
    mon1=FoodItem("M01", "Com ga xoi mo", 45000)
    mon2=FoodItem("M02", "Tra sua tran chau", 30000)
    mon3=FoodItem("M03", "Banh mi pate dac biet", 25000)
    mon4=FoodItem("M04", "Khoai tay chien", 20000)

    print("--- MENU QUAN AN ---")
    mon1.hien_thi()
    mon2.hien_thi()
    mon3.hien_thi()
    mon4.hien_thi()

    # Khoi tao don hang voi khoang cach 4.5 km
    don_hang=FoodOrder(distance_km=4.5)
    don_hang.add_item(mon1, 2)
    don_hang.add_item(mon2, 3)
    don_hang.add_item(mon3, 1)

    print("\n--- IN BIEN LAI DON HANG ---")
    don_hang.display_receipt()


if __name__=="__main__":
    main()
