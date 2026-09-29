class BankAccount:
    def __init__(self):
        self.account_number=""
        self.owner_name=""
        self.balance=0
        
    def inputInfo(self):
        self.account_number=input("Hay nhap so tai khoan: ")
        self.owner_name=input("Hay nhap ten tai khoan: ")
        self.balance=float(input("Hay nhap so du tai khoan: "))
        
    def deposit(self, amount):
        if amount<=0:
            print("So tien gui phai lon hon 0")
        else:
            self.balance=amount+self.balance
            print("Gui tien thanh cong!")
        return self.balance
    
    def withdraw(self, amount):
        if amount<=0:
            print("So tien rut phai lon hon 0")
        else:
            if amount>self.balance:
                print("So tien rut khong duoc lon hon so du")
            else:
                self.balance=self.balance-amount
                print("Rut tien thanh cong!")
                
        return self.balance
    
    def display(self):
        print(f"So tai khoan la:{self.account_number}, Ten tai khoan: {self.owner_name}, So du la: {self.balance}")
        
    def show_balance(self):
        return self.balance
        
def main():
    tk1=BankAccount()
    tk1.inputInfo()
    tk1.display()
    
    tk2=BankAccount()
    tk2.inputInfo()
    tk2.display()
    
    amount=float(input("Hay nhap so tien can chuyen: "))
    tk1.deposit(amount)
    tk2.withdraw(amount)
    
    print("So tien hien tai cua tk1 la: ",tk1.show_balance())
    print("So tien hien tai cua tk2 la: ",tk2.show_balance())

if __name__=="__main__":
    main()