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
        print(f"Ma sp: {self.product_id}, Ten: {self.product_name}, Don gia: {self.price}, So luong: {self.quantity}, Thanh tien: {self.amount()}")


class Cart:
    def __init__(self):
        self.products=[]

    def add_product(self, product):
        for p in self.products:
            if p.product_id==product.product_id:
                p.quantity+=product.quantity
                print("San pham da co trong gio, da tang so luong")
                return
        self.products.append(product)
        print("Them san pham vao gio hang thanh cong")

    def remove_product(self, product_id):
        for p in self.products:
            if p.product_id==product_id:
                self.products.remove(p)
                print("Xoa san pham khoi gio hang thanh cong")
                return
        print("San pham khong ton tai trong gio hang")

    def update_quantity(self, product_id, quantity):
        if quantity<=0:
            print("So luong phai lon hon 0")
            return
        for p in self.products:
            if p.product_id==product_id:
                p.quantity=quantity
                print("Cap nhat so luong thanh cong")
                return
        print("San pham khong ton tai trong gio hang")

    def subtotal(self):
        return sum(p.amount() for p in self.products)

    def discount(self):
        tong=self.subtotal()
        if tong<2000000:
            return 0
        elif tong<5000000:
            return tong*0.05
        else:
            return tong*0.1

    def total_payment(self):
        return self.subtotal()-self.discount()

    def display_cart(self):
        if not self.products:
            print("Gio hang chua co san pham nao")
        else:
            print("Danh sach san pham trong gio hang:")
            for p in self.products:
                p.display()
            print(f"Tong tien truoc giam: {self.subtotal()}")
            print(f"Tien giam: {self.discount()}")
            print(f"Tong tien phai thanh toan: {self.total_payment()}")

def main():
    cart=Cart()

    n=int(input("Hay nhap so luong san pham can mua: "))
    for i in range(n):
        sp=Product()
        sp.inputInfo()
        cart.add_product(sp)

    cart.display_cart()

    ma_sua=input("Hay nhap ma san pham muon sua so luong: ")
    sl_moi=int(input("Hay nhap so luong moi: "))
    cart.update_quantity(ma_sua, sl_moi)

    ma_xoa=input("Hay nhap ma san pham muon xoa: ")
    cart.remove_product(ma_xoa)

    cart.display_cart()

if __name__=="__main__":
    main()
