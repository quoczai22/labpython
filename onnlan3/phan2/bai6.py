class BankAccount:
    def __init__(self):
        self.__account_number=""
        self.__owner=""
        self.__balance=0
        self.__status="Hoat dong"
        self.__history=[]

    def get_balance(self):
        return self.__balance

    def get_status(self):
        return self.__status

    def get_account_number(self):
        return self.__account_number

    def inputInfo(self):
        self.__account_number=input("Hay nhap so tai khoan: ")
        self.__owner=input("Hay nhap ten chu tai khoan: ")
        self.__balance=float(input("Hay nhap so du ban dau: "))

    def deposit(self, amount):
        if self.__status=="Khoa":
            print("Tai khoan dang bi khoa khong the gui tien")
            return
        if amount<=0:
            print("So tien gui phai lon hon 0")
        else:
            self.__balance+=amount
            self.__history.append(f"Gui tien: +{amount}, So du: {self.__balance}")
            print("Gui tien thanh cong!")

    def withdraw(self, amount):
        if self.__status=="Khoa":
            print("Tai khoan dang bi khoa khong the rut tien")
            return
        if amount<=0:
            print("So tien rut phai lon hon 0")
        else:
            if amount>self.__balance:
                print("So tien rut khong duoc lon hon so du")
            else:
                self.__balance-=amount
                self.__history.append(f"Rut tien: -{amount}, So du: {self.__balance}")
                print("Rut tien thanh cong!")

    def transfer(self, other, amount):
        if self.__status=="Khoa" or other.get_status()=="Khoa":
            print("Tai khoan bi khoa khong the chuyen tien")
            return
        if amount<=0:
            print("So tien chuyen phai lon hon 0")
        elif amount>self.__balance:
            print("So du khong du de chuyen tien")
        else:
            self.__balance-=amount
            other.__balance+=amount
            self.__history.append(f"Chuyen tien den {other.get_account_number()}: -{amount}, So du: {self.__balance}")
            other.__history.append(f"Nhan tien tu {self.__account_number}: +{amount}, So du: {other.get_balance()}")
            print("Chuyen tien thanh cong!")

    def lock_account(self):
        self.__status="Khoa"
        print("Tai khoan da bi khoa")

    def unlock_account(self):
        self.__status="Hoat dong"
        print("Tai khoan da mo khoa")

    def show_history(self):
        print(f"Lich su giao dich cua {self.__account_number}:")
        for h in self.__history:
            print(h)

    def display(self):
        print(f"So tai khoan: {self.__account_number}, Chu tai khoan: {self.__owner}, So du: {self.__balance}, Trang thai: {self.__status}")

def main():
    tk1=BankAccount()
    tk1.inputInfo()
    tk1.display()

    tk2=BankAccount()
    tk2.inputInfo()
    tk2.display()

    amount=float(input("Hay nhap so tien can gui vao tk1: "))
    tk1.deposit(amount)

    amount_rut=float(input("Hay nhap so tien can rut khoi tk1: "))
    tk1.withdraw(amount_rut)

    amount_chuyen=float(input("Hay nhap so tien can chuyen tu tk1 sang tk2: "))
    tk1.transfer(tk2, amount_chuyen)

    tk1.display()
    tk2.display()

    print("Khoa tai khoan 2 de thu nghiem:")
    tk2.lock_account()
    tk2.withdraw(1000)

    tk1.show_history()
    tk2.show_history()

    try:
        print(tk1.__balance)
    except AttributeError:
        print("Khong the truy cap truc tiep __balance vi la private")

if __name__=="__main__":
    main()
