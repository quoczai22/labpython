class Temperature:
    def __init__(self):
        self.celsius=0

    def input(self):
        while True:
            c=float(input("Hay nhap nhiet do (do C): "))
            if c<-273.15:
                print("Nhiet do khong duoc nho hon -273.15 C, xin moi nhap lai")
            else:
                self.celsius=c
                break

    def to_fahrenheit(self):
        return (self.celsius*9/5)+32

    def to_kelvin(self):
        return self.celsius+273.15

    def display(self):
        print(f"Do C: {self.celsius}, Do F: {self.to_fahrenheit()}, Do K: {self.to_kelvin()}")

def main():
    t=Temperature()
    t.input()
    t.display()

if __name__=="__main__":
    main()
