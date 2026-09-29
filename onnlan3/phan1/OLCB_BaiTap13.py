from datetime import datetime

class BankAccount:
    def __init__(self, account_number="", owner="", balance=0.0):
        self.account_number=account_number
        self.owner=owner
        self.balance=balance if balance>=0 else 0.0
        self.transaction_history=[]

    def deposit(self, amount):
        if amount<=0:
            print("So tien gui phai lon hon 0!")
            return False
        self.balance+=amount
        time_str=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.transaction_history.append(f"[{time_str}] Nap tien: +{amount:,.0f} VND | So du: {self.balance:,.0f} VND")
        return True

    def withdraw(self, amount):
        if amount<=0:
            print("So tien rut phai lon hon 0!")
            return False
        if amount>self.balance:
            print("So du khong du de thuc hien giao dich!")
            return False
        self.balance-=amount
        time_str=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.transaction_history.append(f"[{time_str}] Rut tien: -{amount:,.0f} VND | So du: {self.balance:,.0f} VND")
        return True

    def display(self):
        print(f"STK: {self.account_number:<10} | Chu TK: {self.owner:<20} | So du: {self.balance:>12,.0f} VND")

    def show_history(self):
        print(f"\n--- LICH SU GIAO DICH CUA TK {self.account_number} ({self.owner}) ---")
        if not self.transaction_history:
            print("Chua co giao dich nao.")
        else:
            for item in self.transaction_history:
                print("  ", item)


class BankSystem:
    def __init__(self):
        self.accounts=[]

    def add_account(self, account):
        for acc in self.accounts:
            if acc.account_number==account.account_number:
                print(f"STK {account.account_number} da ton tai!")
                return False
        self.accounts.append(account)
        return True

    def find_account(self, account_number):
        for acc in self.accounts:
            if acc.account_number==account_number:
                return acc
        return None

    def transfer(self, from_acc_num, to_acc_num, amount):
        if amount<=0:
            print("So tien chuyen phai lon hon 0!")
            return False
        from_acc=self.find_account(from_acc_num)
        to_acc=self.find_account(to_acc_num)
        if not from_acc:
            print(f"Khong tim thay tai khoan nguon {from_acc_num}!")
            return False
        if not to_acc:
            print(f"Khong tim thay tai khoan dich {to_acc_num}!")
            return False
        if from_acc.balance<amount:
            print(f"Tai khoan {from_acc_num} khong du so du de chuyen {amount:,.0f} VND!")
            return False

        from_acc.balance-=amount
        to_acc.balance+=amount
        time_str=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        from_acc.transaction_history.append(f"[{time_str}] Chuyen khoan den {to_acc_num}: -{amount:,.0f} VND | So du: {from_acc.balance:,.0f} VND")
        to_acc.transaction_history.append(f"[{time_str}] Nhan tien tu {from_acc_num}: +{amount:,.0f} VND | So du: {to_acc.balance:,.0f} VND")
        print(f"Chuyen thanh cong {amount:,.0f} VND tu {from_acc_num} den {to_acc_num}.")
        return True


def main():
    bank=BankSystem()
    acc1=BankAccount("1001", "Nguyen Van An", 10000000)
    acc2=BankAccount("1002", "Tran Thi Binh", 5000000)
    bank.add_account(acc1)
    bank.add_account(acc2)

    print("--- THONG TIN BAN DAU ---")
    acc1.display()
    acc2.display()

    print("\n--- THUC HIEN GIAO DICH CHUYEN KHOAN ---")
    bank.transfer("1001", "1002", 3000000)
    acc1.deposit(2000000)

    print("\n--- THONG TIN SAU GIAO DICH ---")
    acc1.display()
    acc2.display()

    acc1.show_history()
    acc2.show_history()


if __name__=="__main__":
    main()
