class InventoryItem:
    def __init__(self):
        self.item_id=""
        self.item_name=""
        self.price=0
        self.stock=0

    def input(self):
        self.item_id=input("Hay nhap ma hang: ")
        self.item_name=input("Hay nhap ten hang: ")
        self.price=float(input("Hay nhap don gia: "))
        self.stock=int(input("Hay nhap so luong ton: "))

    def import_stock(self, quantity):
        if quantity<=0:
            print("So luong nhap phai lon hon 0")
        else:
            self.stock+=quantity
            print("Nhap kho thanh cong")

    def export_stock(self, quantity):
        if quantity<=0:
            print("So luong xuat phai lon hon 0")
        elif quantity>self.stock:
            print("Khong du hang de xuat kho")
        else:
            self.stock-=quantity
            print("Xuat kho thanh cong")

    def inventory_value(self):
        return self.price*self.stock

    def display(self):
        print(f"Ma: {self.item_id}, Ten: {self.item_name}, Don gia: {self.price}, Ton kho: {self.stock}, Gia tri ton: {self.inventory_value()}")


class InventoryManager:
    def __init__(self):
        self.items=[]

    def add_item(self, item):
        for it in self.items:
            if it.item_id==item.item_id:
                print("Ma hang da ton tai")
                return False
        self.items.append(item)
        print("Them hang thanh cong")
        return True

    def find_item(self, item_id):
        for it in self.items:
            if it.item_id==item_id:
                return it
        print("Khong tim thay mat hang")
        return None

    def import_item(self, item_id, quantity):
        it=self.find_item(item_id)
        if it:
            it.import_stock(quantity)

    def export_item(self, item_id, quantity):
        it=self.find_item(item_id)
        if it:
            it.export_stock(quantity)

    def low_stock_items(self, threshold=5):
        print("Cac mat hang sap het hang:")
        for it in self.items:
            if it.stock<threshold:
                it.display()

    def total_inventory_value(self):
        return sum(it.inventory_value() for it in self.items)

    def display_all(self):
        for it in self.items:
            it.display()

def main():
    kho=InventoryManager()

    n=int(input("Hay nhap so luong mat hang: "))
    for i in range(n):
        it=InventoryItem()
        it.input()
        kho.add_item(it)

    kho.display_all()

    ma_nhap=input("Hay nhap ma hang can nhap them: ")
    sl_nhap=int(input("Hay nhap so luong nhap: "))
    kho.import_item(ma_nhap, sl_nhap)

    ma_xuat=input("Hay nhap ma hang can xuat: ")
    sl_xuat=int(input("Hay nhap so luong xuat: "))
    kho.export_item(ma_xuat, sl_xuat)

    kho.low_stock_items(5)

    print("Tong gia tri ton kho la: ", kho.total_inventory_value())

if __name__=="__main__":
    main()
