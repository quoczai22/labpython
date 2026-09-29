class Vehicle:
    def __init__(self):
        self.__license_plate=""
        self.__vehicle_type=""
        self.__status="Dang gui"

    def get_license_plate(self):
        return self.__license_plate

    def get_vehicle_type(self):
        return self.__vehicle_type

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status=status

    def inputInfo(self):
        self.__license_plate=input("Hay nhap bien so xe: ")
        self.__vehicle_type=input("Hay nhap loai xe (xe dap/xe may/o to): ").strip().lower()

    def calculate_fee(self):
        if self.__vehicle_type=="xe dap":
            return 3000
        elif self.__vehicle_type=="xe may":
            return 5000
        elif self.__vehicle_type=="o to":
            return 20000
        return 5000

    def display(self):
        print(f"Bien so: {self.__license_plate}, Loai xe: {self.__vehicle_type}, Trang thai: {self.__status}")


class ParkingManager:
    def __init__(self):
        self.vehicles=[]

    def check_in(self, vehicle):
        for v in self.vehicles:
            if v.get_license_plate()==vehicle.get_license_plate() and v.get_status()=="Dang gui":
                print("Xe nay dang co trong bai, khong the gui trung")
                return False
        self.vehicles.append(vehicle)
        print("Gui xe vao bai thanh cong")
        return True

    def find_vehicle(self, license_plate):
        for v in self.vehicles:
            if v.get_license_plate()==license_plate:
                return v
        print("Khong tim thay xe trong bai")
        return None

    def check_out(self, license_plate):
        v=self.find_vehicle(license_plate)
        if v and v.get_status()=="Dang gui":
            v.set_status("Da lay")
            tien=v.calculate_fee()
            print(f"Tien gui xe la: {tien}")
            return tien
        else:
            print("Xe khong co trong bai hoac da lay")
            return 0

    def display_vehicles(self):
        print("Danh sach xe dang gui trong bai:")
        for v in self.vehicles:
            if v.get_status()=="Dang gui":
                v.display()

    def find_by_type(self, vehicle_type):
        print(f"Danh sach xe loai {vehicle_type}:")
        for v in self.vehicles:
            if v.get_vehicle_type()==vehicle_type and v.get_status()=="Dang gui":
                v.display()

    def count_vehicles(self):
        dap=0
        may=0
        oto=0
        for v in self.vehicles:
            if v.get_status()=="Dang gui":
                if v.get_vehicle_type()=="xe dap": dap+=1
                elif v.get_vehicle_type()=="xe may": may+=1
                elif v.get_vehicle_type()=="o to": oto+=1
        print(f"So xe dap: {dap}, So xe may: {may}, So o to: {oto}")

    def total_revenue(self):
        tong=0
        for v in self.vehicles:
            if v.get_status()=="Da lay":
                tong+=v.calculate_fee()
        return tong

def main():
    pm=ParkingManager()
    
    n=int(input("Hay nhap so luong xe can gui: "))
    for i in range(n):
        v=Vehicle()
        v.inputInfo()
        pm.check_in(v)

    pm.display_vehicles()

    bs_tim=input("Hay nhap bien so xe can tim: ")
    tim=pm.find_vehicle(bs_tim)
    if tim:
        tim.display()

    bs_ra=input("Hay nhap bien so xe can lay ra: ")
    pm.check_out(bs_ra)

    loai_tim=input("Hay nhap loai xe can tim: ")
    pm.find_by_type(loai_tim)

    pm.count_vehicles()

    print("Tong doanh thu bai xe la: ", pm.total_revenue())

if __name__=="__main__":
    main()
