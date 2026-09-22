class Product:
    def __init__(self):
        self.product_id=""
        self.name=""
        self.price=0
        self.stock=0

    def input(self):
        self.product_id=input("Hay nhap ma san pham: ")
        self.name=input("Hay nhap ten san pham: ")
        self.price=float(input("Hay nhap don gia: "))
        self.stock=int(input("Hay nhap so luong ton kho: "))

    def display(self):
        print(f"Ma: {self.product_id}, Ten: {self.name}, Gia: {self.price}, Ton: {self.stock}")


class Customer:
    def __init__(self):
        self.customer_id=""
        self.name=""
        self.phone=""

    def input(self):
        self.customer_id=input("Hay nhap ma khach hang: ")
        self.name=input("Hay nhap ten khach hang: ")
        self.phone=input("Hay nhap so dien thoai: ")

    def display(self):
        print(f"Ma KH: {self.customer_id}, Ten: {self.name}, SDT: {self.phone}")


class Order:
    def __init__(self, order_id=""):
        self.order_id=order_id
        self.items=[]

    def add_item(self, product, quantity):
        if quantity>product.stock:
            print(f"Khong du hang ton kho cho san pham {product.name}")
            return False
        product.stock-=quantity
        self.items.append((product, quantity))
        print("Them san pham vao don hang thanh cong")
        return True

    def total_amount(self):
        return sum(p.price*q for p, q in self.items)

    def print_invoice(self):
        print(f"Hoa don ban hang ma {self.order_id}:")
        for p, q in self.items:
            print(f"San pham: {p.name}, So luong: {q}, Thanh tien: {p.price*q}")
        print("Tong tien phai thanh toan: ", self.total_amount())


class StoreManager:
    def __init__(self):
        self.products=[]
        self.customers=[]
        self.orders=[]

    def add_product(self, p):
        self.products.append(p)

    def add_customer(self, c):
        self.customers.append(c)

    def find_product(self, pid):
        for p in self.products:
            if p.product_id==pid:
                return p
        return None

    def total_revenue(self):
        return sum(o.total_amount() for o in self.orders)

    def stock_statistics(self):
        print("Thong ke ton kho:")
        for p in self.products:
            p.display()

def main():
    store=StoreManager()

    sp1=Product()
    sp1.input()
    store.add_product(sp1)

    kh1=Customer()
    kh1.input()
    store.add_customer(kh1)

    store.stock_statistics()

    dh=Order("DH01")
    sl_mua=int(input("Hay nhap so luong mua: "))
    dh.add_item(sp1, sl_mua)
    dh.print_invoice()
    store.orders.append(dh)

    print("Tong doanh thu cua hang la: ", store.total_revenue())
    store.stock_statistics()

if __name__=="__main__":
    main()
