class Temperature:
    def __init__(self, celsius=0.0):
        self.celsius=celsius if celsius>=-273.15 else 0.0

    def set_celsius(self, celsius):
        if celsius>=-273.15:
            self.celsius=celsius
            return True
        else:
            print("Nhiet do khong the nho hon do khong tuyet doi (-273.15 do C)!")
            return False

    def inputInfo(self):
        while True:
            try:
                c=float(input("Hay nhap nhiet do (do C): "))
                if self.set_celsius(c):
                    break
            except ValueError:
                print("Nhiet do phai la so hop le!")

    def to_fahrenheit(self):
        return (self.celsius*9/5)+32

    def to_kelvin(self):
        return self.celsius+273.15

    def display(self):
        print(f"Nhiet do Celsius   : {self.celsius:.2f} °C")
        print(f"Nhiet do Fahrenheit: {self.to_fahrenheit():.2f} °F")
        print(f"Nhiet do Kelvin    : {self.to_kelvin():.2f} K")


def main():
    t=Temperature()
    t.inputInfo()
    print("\n--- KET QUA CHUYEN DOI NHIET DO ---")
    t.display()


if __name__=="__main__":
    main()
