class Product:
    def __init__(self, product_id="", product_name="", price=0, quantity=0):
        self.product_id=product_id
        self.product_name=product_name
        self.price=price
        self.quantity=quantity
        
    def inputInfo(self):
        self.product_id=input("Hay nhap ma san pham: ")
        self.product_name=input("Hay nhap ten san pham: ")
        self.price=float(input("Hay nhap gia tri san pham: "))
        self.quantity=int(input("Hay nhap so luong: "))
    
    def display(self):
        print(f"Ma san pham: {self.product_id}, Ten san pham: {self.product_name}, Gia san pham: {self.price}, So luong: {self.quantity}, Thanh tien: {self.amount()}, Tien giam: {self.discount()}, So tien phai tra la: {self.payment()}")
        
    def amount(self):
        return self.price*self.quantity
    
    def discount(self):
        if self.quantity>=10:
            giam_gia=0.05
        else:
            giam_gia=0
        tien_giam=giam_gia*self.amount()
        return tien_giam
    
    def payment(self):
        return self.amount()-self.discount()

SanPham = Product
    
def main():
    sp1=Product()
    sp1.inputInfo()
    sp1.display()
    
if __name__=="__main__":
    main()