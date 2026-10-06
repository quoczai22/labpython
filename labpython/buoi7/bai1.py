class Nguoi:
    def __init__(self):
        self.name=""
    
        
class NhanVien(Nguoi):
    def __init__(self):
        super().__init__()
        self.luong=0
        
    def speak(self):
        return "toi la nhan vien"
    
class SinhVien(Nguoi):
    def __init__(self):
        super().__init__()
        self.gpa=0
        
    def speak(self):
        return "toi la sinh vien"
    
def main():
    nv1=NhanVien()
    sv1=SinhVien()
    
    print(f"Neu nguoi la nhan vien se noi: {nv1.speak()} \n con neu la sinh vien se noi: {sv1.speak()}")
    
if __name__ == "__main__":
    main()
    