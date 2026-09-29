class Product:
    def __init__(self):
        self.product_id=""
        self.product_name=""
        self.price=0
        self.quantity=0

    def inputInfo(self):
        self.product_id=input("Hay nhap ma san pham: ")
        self.product_name=input("Hay nhap ten san pham: ")
        self.price=float(input("Hay nhap don gia: "))
        self.quantity=int(input("Hay nhap so luong: "))

    def amount(self):
        return self.price*self.quantity

    def display(self):
        print(f"Ma sp: {self.product_id}, Ten sp: {self.product_name}, Gia: {self.price}, So luong: {self.quantity}, Thanh tien: {self.amount()}")


class ProductManager:
    def __init__(self):
        self.products=[]

    def add_product(self, product):
        for p in self.products:
            if p.product_id==product.product_id:
                print("San pham da ton tai khong the them")
                return False
        self.products.append(product)
        print("Them san pham thanh cong")
        return True

    def display_products(self):
        if not self.products:
            print("Danh sach san pham rong")
        else:
            for p in self.products:
                p.display()

    def find_by_id(self, product_id):
        for p in self.products:
            if p.product_id==product_id:
                return p
        print("Khong tim thay san pham")
        return None

    def update_price(self, product_id, new_price):
        p=self.find_by_id(product_id)
        if p:
            p.price=new_price
            print("Cap nhat gia thanh cong")

    def delete_product(self, product_id):
        p=self.find_by_id(product_id)
        if p:
            self.products.remove(p)
            print("Xoa san pham thanh cong")

    def sort_by_amount(self):
        self.products.sort(key=lambda p: p.amount(), reverse=True)
        print("Da sap xep san pham theo thanh tien giam dan")

def main():
    manager=ProductManager()
    
    n=int(input("Hay nhap so luong san pham can them: "))
    for i in range(n):
        sp=Product()
        sp.inputInfo()
        manager.add_product(sp)

    manager.display_products()

    ma_tim=input("Hay nhap ma san pham can tim: ")
    tim=manager.find_by_id(ma_tim)
    if tim:
        tim.display()

    ma_sua=input("Hay nhap ma san pham can sua gia: ")
    gia_moi=float(input("Hay nhap gia moi: "))
    manager.update_price(ma_sua, gia_moi)

    ma_xoa=input("Hay nhap ma san pham can xoa: ")
    manager.delete_product(ma_xoa)

    manager.sort_by_amount()
    manager.display_products()

if __name__=="__main__":
    main()
