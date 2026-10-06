class SanPham():
    def __init__(self):
        self.so_luong=0
        self.gia=0
        self.ten_san_pham=""
        self.so_luong_ton=0
        self.gia_thong_thuong=0
        
    def input_info(self):
        self.gia=float(input("Hay nhap gia ban: "))
        self.ten_san_pham=input("Hay nhap ten san pham: ")
        self.so_luong_ton=int(input("So luong ton trong kho: "))
        self.gia_thong_thuong=float(input("Gia ban thong thuong: "))
        
    def get_price(self,so_luong):
        so_luong=int(input("Hay nhap so luong can mua: "))
        self.so_luong=so_luong
        if(self.so_luong<10):
            return self.gia_thong_thuong*self.so_luong
        if(self.so_luong<99):
            return self.gia*self.so_luong-self.gia*self.so_luong*0.1
        if(self.so_luong>=100):
            return  self.gia*self.so_luong-self.gia*self.so_luong*0.2
        
    def make_purchase(self,so_luong):
        so_luong=self.so_luong
        if so_luong>self.so_luong_ton:
            print("Het san pham can mua!")
            return
        
        self.so_luong_ton=self.so_luong_ton-self.so_luong
        return self.so_luong_ton
        
    def display(self):
        print(f"Ten san pham: {self.ten_san_pham} Gia san pham: {self.get_price(self.so_luong)}, So luong ton: {self.make_purchase(self.so_luong)}")

def main():
    sp1=SanPham()
    sp1.input_info()
    sp1.display()
    
if __name__=="__main__":
    main()
    
        
        