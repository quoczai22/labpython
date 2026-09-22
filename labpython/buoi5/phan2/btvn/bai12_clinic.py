class Patient:
    def __init__(self):
        self.patient_id=""
        self.name=""
        self.age=0

    def input(self):
        self.patient_id=input("Hay nhap ma benh nhan: ")
        self.name=input("Hay nhap ten benh nhan: ")
        self.age=int(input("Hay nhap tuoi benh nhan: "))


class Doctor:
    def __init__(self):
        self.doctor_id=""
        self.name=""
        self.specialty=""

    def input(self):
        self.doctor_id=input("Hay nhap ma bac si: ")
        self.name=input("Hay nhap ten bac si: ")
        self.specialty=input("Hay nhap chuyen khoa: ")


class Appointment:
    def __init__(self):
        self.appointment_id=""
        self.patient=None
        self.doctor=None
        self.date=""
        self.time=""
        self.fee=150000
        self.status="Da dat"

    def display(self):
        ten_bn=self.patient.name if self.patient else ""
        ten_bs=self.doctor.name if self.doctor else ""
        print(f"Ma lich: {self.appointment_id}, Ngay: {self.date} {self.time}, Benh nhan: {ten_bn}, Bac si: {ten_bs}, Phi: {self.fee}, Trang thai: {self.status}")


class ClinicManager:
    def __init__(self):
        self.appointments=[]

    def book_appointment(self, app):
        for a in self.appointments:
            if a.doctor.doctor_id==app.doctor.doctor_id and a.date==app.date and a.time==app.time and a.status!="Da huy":
                print("Bac si da co lich kham vao gio nay roi")
                return False
        self.appointments.append(app)
        print("Dat lich kham thanh cong")
        return True

    def cancel_appointment(self, app_id):
        for a in self.appointments:
            if a.appointment_id==app_id:
                a.status="Da huy"
                print("Huy lich kham thanh cong")
                return
        print("Khong tim thay lich kham")

    def complete_appointment(self, app_id):
        for a in self.appointments:
            if a.appointment_id==app_id:
                a.status="Hoan thanh"
                print("Lich kham da hoan thanh")
                return
        print("Khong tim thay lich kham")

    def total_revenue(self):
        return sum(a.fee for a in self.appointments if a.status=="Hoan thanh")

    def display_all(self):
        for a in self.appointments:
            a.display()

def main():
    clinic=ClinicManager()

    bs=Doctor()
    bs.doctor_id="BS01"
    bs.name="Nguyen Van B"
    bs.specialty="Noi"

    bn=Patient()
    bn.patient_id="BN01"
    bn.name="Tran Van A"
    bn.age=20

    lich1=Appointment()
    lich1.appointment_id="LK01"
    lich1.patient=bn
    lich1.doctor=bs
    lich1.date=input("Hay nhap ngay kham: ")
    lich1.time=input("Hay nhap gio kham: ")
    clinic.book_appointment(lich1)

    clinic.display_all()

    clinic.complete_appointment("LK01")

    print("Tong doanh thu phong kham la: ", clinic.total_revenue())

if __name__=="__main__":
    main()
