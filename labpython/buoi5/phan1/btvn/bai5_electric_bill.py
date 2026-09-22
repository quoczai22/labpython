class ElectricBill:
    def __init__(self):
        self.customer_id=""
        self.customer_name=""
        self.old_index=0
        self.new_index=0

    def inputInfo(self):
        self.customer_id=input("Hay nhap ma khach hang: ")
        self.customer_name=input("Hay nhap ten khach hang: ")
        self.old_index=float(input("Hay nhap chi so dien cu: "))
        self.new_index=float(input("Hay nhap chi so dien moi: "))
        if self.new_index<self.old_index:
            print("Chi so moi phai lon hon chi so cu")
            return False
        return True

    def consumption(self):
        return self.new_index-self.old_index

    def electricity_cost(self):
        kwh=self.consumption()
        cost=0
        tiers=[(50, 1984), (50, 2050), (100, 2380), (100, 2998), (100, 3350), (float('inf'), 3460)]
        remain=kwh
        for limit, price in tiers:
            if remain<=0:
                break
            used=min(remain, limit)
            cost+=used*price
            remain-=used
        return cost

    def vat(self):
        return self.electricity_cost()*0.1

    def total_payment(self):
        return self.electricity_cost()+self.vat()

    def display_bill(self):
        print(f"Ma khach hang: {self.customer_id}, Ten: {self.customer_name}")
        print(f"Chi so cu: {self.old_index}, Chi so moi: {self.new_index}, Dien tieu thu: {self.consumption()}")
        print(f"Tien dien chua thue: {self.electricity_cost()}, Tien VAT: {self.vat()}, Tong thanh toan: {self.total_payment()}")

def main():
    bill=ElectricBill()
    if bill.inputInfo():
        bill.display_bill()

if __name__=="__main__":
    main()
