from abc import ABC , abstractmethod
import math

class Hinhabstract(ABC):
    
    @abstractmethod
    def tinh_chu_vi(self):
        pass
    
    @abstractmethod
    def tinh_dien_tich(self):
        pass
    
class HinhTron(Hinhabstract):
    def __init__(self):
        self.ban_kinh=0
        
    def input_info(self):
        self.ban_kinh=float(input("Hay nhap ban kinh cua hinh tron: "))
        
    def tinh_chu_vi(self):
        return 2*self.ban_kinh*3.14
    
    def tinh_dien_tich(self):
        return self.ban_kinh**2*3.14
    
    def display(self):
        print(f"Chu vi cua hinh tron la: {self.tinh_chu_vi()} va dien tich cua hinh tron la: {self.tinh_dien_tich()}")
    
class HinhChuNhat(Hinhabstract):
    def __init__(self):
        self.chieu_dai=0
        self.chieu_rong=0
        
    def input_info(self):
        self.chieu_dai=float(input("Hay nhap chieu dai: "))
        self.chieu_rong=float(input("Hay nhap chieu rong: "))
                
    def tinh_chu_vi(self):
        return self.chieu_rong+self.chieu_rong*2
    
    def tinh_dien_tich(self):
        return self.chieu_dai*self.chieu_rong
    
    def display(self):
        print(f"Chu vi cua hinh chu nhat la: {self.tinh_chu_vi()} va dien tich cua hinh chu nhat la: {self.tinh_dien_tich()}")
        
class HinhTamGiac(Hinhabstract):
    def __init__(self):
        self.canh_a=0
        self.canh_b=0
        self.canh_c=0
        
    def input_info(self):
        self.canh_a=float(input("Hay nhap canh a: "))
        self.canh_b=float(input("Hay nhap canh b: "))
        self.canh_c=float(input("Hay nhap canh c: "))
        
    def tinh_chu_vi(self):
        return float(self.canh_a+self.canh_b+self.canh_c)
    
    def nua_chu_vi(self):
        return float(self.tinh_chu_vi()/2)
    
    def tinh_dien_tich(self):
        p=self.nua_chu_vi()
        return float(math.sqrt(p*(p-self.canh_a)*(p-self.canh_b)*(p-self.canh_c)))
    
    def display(self):
        print(f"Chu vi cua hinh tam giac la: {self.tinh_chu_vi()} va dien tich cua hinh tam giac la: {self.tinh_dien_tich()}")
        
def main():
    hcn1=HinhChuNhat()
    hcn1.input_info()
    hcn1.display()
    
    ht1=HinhTron()
    ht1.input_info()
    ht1.display()
    
    htg1=HinhTamGiac()
    htg1.input_info()
    htg1.display()
    
if __name__=="__main__":
    main()