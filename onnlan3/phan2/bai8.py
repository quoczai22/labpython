class LibraryBook:
    def __init__(self):
        self.ma_sach=""
        self.ten_sach=""
        self.tac_gia=""
        self.don_sach=0
        self.so_luong=0

#get

    def get_ma_sach(self):
        return self.__ma_sach

    def get_ten_sach(self):
        return self.__ten_sach

    def get_tac_gia(self):
        return self.__tac_gia

    def get_don_sach(self):
        return self.__don_sach

    def get_so_luong(self):
        return self.__so_luong

#set

    def set_ma_sach(self,ma_sach):
        if ma_sach.startswith("S") and len(ma_sach)==5:
            self.__ma_sach=ma_sach
            return True
        else:
            print("Mã sách phải có 5 kí tự và bắt đầu bằng S")
            return False

    def set_tac_gia(self,tac_gia):
        if tac_gia.strip()!="":
            self.__tac_gia=tac_gia
            return True
        else:
            print("Tên tác giả không được để trống")
            return False

    def set_ten_sach(self,ten_sach):
        if ten_sach.strip()!="":
            self.__ten_sach=ten_sach
            return True
        else:
            print("Tên sách không được để trống")
            return False

    def set_don_sach(self,don_sach):
        if don_sach>0:
            self.__don_sach=don_sach
            return True
        else:
            print("Đơn sách phải lớn hơn 0!")
            return False

    def set_so_luong(self,so_luong):
        if so_luong>=0:
            self.__so_luong=so_luong
            return True
        else:
            print("Số lượng phải lớn hơn hoặc bằng 0!")
            return False

    def inputInfo(self):
        while True:
            ma=input("Hay nhap ma sach: ")
            if self.set_ma_sach(ma):
                break

        while True:
            ten=input("Hay nhap ten sach: ")
            if self.set_ten_sach(ten):
                break

        while True:
            tg=input("Hay nhap ten tac gia: ")
            if self.set_tac_gia(tg):
                break

        while True:
            try:
                dg=float(input("Hay nhap vao don gia cua sach: "))
                if self.set_don_sach(dg):
                    break
            except ValueError:
                print("Đơn giá phải là số hợp lệ!")

        while True:
            try:
                sl=int(input("Hay nhap vao so luong cua sach: "))
                if self.set_so_luong(sl):
                    break
            except ValueError:
                print("Số lượng phải là số nguyên hợp lệ!")

    def borrow_book(self,quantity):
        if quantity<=0:
            print("So luong sach muon muon phai lon hon 0!")
            return False

        if self.__so_luong<quantity:
            print("So luong sach ton kho khong du de cho muon!")
            return False

        self.__so_luong=self.__so_luong-quantity
        print("Da cho muon thanh cong!")
        return True

    def restock(self,quantity):
        if quantity<=0:
            print("So luong sach nhap vao phai lon hon 0!")
            return False

        self.__so_luong=self.__so_luong+quantity
        print("Da nhap sach thanh cong!")
        return True

    def total_value(self):
        return self.__don_sach*self.__so_luong

    def display(self):
        print(f"Ma sach: {self.__ma_sach}, Ten sach: {self.__ten_sach}, Ten tac gia: {self.__tac_gia}, Don gia: {self.__don_sach}, So luong: {self.__so_luong}, Tong gia tri ton kho: {self.total_value()}")  

def main():
    sach1=LibraryBook()
    sach1.inputInfo()

    sach_muon=int(input("Hay nhap so sach ma ban muon muon: "))
    sach1.borrow_book(sach_muon)

    sach_nhap=int(input("Hay nhap vao so sach ma ban muon them vao: "))
    sach1.restock(sach_nhap)

    sach1.display()

if __name__=="__main__":
    main()
