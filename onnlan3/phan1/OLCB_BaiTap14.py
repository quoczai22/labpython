class Product:
    def __init__(self, product_id="", name="", price=0.0):
        self.product_id=product_id
        self.name=name
        self.price=price


class OrderItem:
    def __init__(self, product, quantity=1):
        self.product=product
        self.quantity=quantity if quantity>0 else 1

    def subtotal(self):
        return self.product.price*self.quantity


class Order:
    def __init__(self, order_id="", voucher_discount=0.0):
        self.order_id=order_id
        self.order_items=[]
        # voucher_discount tu 0.0 (0%) den 0.5 (50%)
        self.voucher_discount=voucher_discount if 0.0<=voucher_discount<=0.5 else 0.0

    def add_item(self, product, quantity=1):
        if quantity<=0:
            print("So luong phai > 0!")
            return False
        for item in self.order_items:
            if item.product.product_id==product.product_id:
                item.quantity+=quantity
                return True
        self.order_items.append(OrderItem(product, quantity))
        return True

    def calculate_subtotal(self):
        return sum(item.subtotal() for item in self.order_items)

    def calculate_discount(self):
        return self.calculate_subtotal()*self.voucher_discount

    def calculate_total(self):
        return self.calculate_subtotal()-self.calculate_discount()

    def display_order(self):
        print("\n" + "="*52)
        print(f"{'HOA DON BAN LE':^52}")
        print(f"Ma don hang: {self.order_id}")
        print("="*52)
        print(f"{'STT':<4}{'Ten san pham':<22}{'SL':>4}{'Don gia':>10}{'T.Tien':>12}")
        print("-"*52)
        for idx, item in enumerate(self.order_items, 1):
            print(f"{idx:<4}{item.product.name:<22}{item.quantity:>4}{item.product.price:>10,.0f}{item.subtotal():>12,.0f}")
        print("-"*52)
        print(f"Tong tien hang:{self.calculate_subtotal():>37,.0f} VND")
        print(f"Giam gia Voucher ({self.voucher_discount*100:.0f}%):{-self.calculate_discount():>31,.0f} VND")
        print("="*52)
        print(f"TONG THANH TOAN:{self.calculate_total():>36,.0f} VND")
        print("="*52)


def main():
    p1=Product("SP01", "Ao khoac Gio", 350000)
    p2=Product("SP02", "Giay Sneaker", 650000)
    p3=Product("SP03", "Tat co cao", 30000)

    order=Order("DH2026-001", voucher_discount=0.15) # Giam 15%
    order.add_item(p1, 1)
    order.add_item(p2, 2)
    order.add_item(p3, 5)

    order.display_order()


if __name__=="__main__":
    main()
