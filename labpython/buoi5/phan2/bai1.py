from datetime import date, datetime

class Person:
    def __init__(self, ho_ten="", quoc_gia="", ngay_sinh=None):
        self.__ho_ten=ho_ten
        self._quoc_gia=quoc_gia
        self.__ngay_sinh=ngay_sinh
        
    def get_ho_ten(self):
        return self.__ho_ten
    
    def set_ho_ten(self, ho_ten):
        if ho_ten.strip():
            self.__ho_ten=ho_ten
            return True
        else:
            print("Ban phai nhap ho ten")
            return False
    
    def get_ngay_sinh(self):
        return self.__ngay_sinh
    
    def set_ngay_sinh(self, ngay_sinh):
        if isinstance(ngay_sinh, str):
            for fmt in ("%d/%m/%Y", "%Y-%m-%d", "%d-%m-%Y"):
                try:
                    ngay_sinh=datetime.strptime(ngay_sinh.strip(), fmt).date()
                    break
                except ValueError:
                    pass
            if isinstance(ngay_sinh, str):
                print("Dinh dang ngay sinh khong hop le (dung dd/mm/yyyy hoac yyyy-mm-dd)")
                return False

        if ngay_sinh>date.today():
            print("Ngay sinh khong duoc lon hon ngay hien tai")
            return False
        else:
            self.__ngay_sinh=ngay_sinh
            return True

    def inputInfo(self):
        while True:
            ho_ten=input("Hay nhap ho ten cua ban: ")
            if self.set_ho_ten(ho_ten):
                break
        
        self._quoc_gia=input("Hay nhap quoc gia cua ban: ")
        
        while True:
            ngay_sinh=input("Hay nhap ngay sinh cua ban (dd/mm/yyyy): ")
            if self.set_ngay_sinh(ngay_sinh):  
                break
            
    def calculate_age(self):
        if not self.__ngay_sinh:
            return 0
        today=date.today()
        birth=self.__ngay_sinh
        age=today.year-birth.year-((today.month, today.day)<(birth.month, birth.day))
        return age
    
    def display(self):
        ns_str=self.__ngay_sinh.strftime("%d/%m/%Y") if self.__ngay_sinh else ""
        print(f"Ho ten la: {self.get_ho_ten()}, Quoc gia: {self._quoc_gia}, Ngay sinh: {ns_str}, Tuoi: {self.calculate_age()}")
    
def main():
    p1=Person()
    p1.inputInfo()
    p1.display()

    print("\n--- Kiem tra getter / setter ---")
    print("Doc ho ten bang getter:", p1.get_ho_ten())
    p1.set_ho_ten("Nguyen Van Moi")
    print("Ho ten sau khi cap nhat setter:", p1.get_ho_ten())

    print("\n--- Thu truy cap thuoc tinh tu ben ngoai ---")
    print("Truy cap _quoc_gia (protected):", p1._quoc_gia, "-> Co the truy cap duoc nhung khong khuyen khich.")
    try:
        print("Truy cap __ho_ten (private):", p1.__ho_ten)
    except AttributeError:
        print("Truy cap __ho_ten that bai: Thuoc tinh private da bi Name Mangling an di de dam bao dong goi.")

if __name__=="__main__":
    main()