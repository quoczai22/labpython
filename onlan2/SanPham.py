class SanPham():
    def __init__(self):
        self.ten_sp=""
        self.gia_ban=0
        self.so_luong_ton=0

    def inputInfo(self):
        self.ten_sp=input("Hay ten cua san pham: ")
        self.gia_ban=float(input("Hay nhap gia ban: "))
        self.so_luong_ton=int(input("Hay nhap so luong ton kho: "))

    def outputInfo(self):
        print(f"Ten san pham la: {self.ten_sp}, Gia ban: {self.gia_ban}, So luong: {self.so_luong_ton}")

    def get_price(self, so_luong_mua):
        tong_tien = self.gia_ban * so_luong_mua
        
        if so_luong_mua < 10:
            return tong_tien
        elif so_luong_mua < 100:
            return tong_tien * 0.9  
        else:
            return tong_tien * 0.8   

    def make_purchase(self,so_luong_mua):
        if so_luong_mua<=self.so_luong_ton:
            self.so_luong_ton=self.so_luong_ton-so_luong_mua
            tong_tien=self.get_price(so_luong_mua)
            print(f"Mua thành công {so_luong_mua} sản phẩm {self.ten_sp}. Tổng tiền: {tong_tien}")
        else:
            print("Không đủ hàng trong kho!")

        
def main():
    sp1=SanPham()
    sp1.inputInfo()
    sp1.outputInfo()
    n=int(input("Hay nhap so luong muon mua: "))
    sp1.make_purchase(n)

if __name__=="__main__":
    main()
