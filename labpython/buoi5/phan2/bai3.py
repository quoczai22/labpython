class ComplexNumber:
    def __init__(self, real=0, imag=0):
        self.__real=real
        self.__imag=imag

    def get_real(self):
        return self.__real

    def set_real(self, real):
        self.__real=real

    def get_imag(self):
        return self.__imag

    def set_imag(self, imag):
        self.__imag=imag

    def input_number(self):
        while True:
            try:
                real_val=float(input("Hay nhap phan thuc: "))
                self.set_real(real_val)
                imag_val=float(input("Hay nhap phan ao: "))
                self.set_imag(imag_val)
                break
            except ValueError:
                print("Phan thuc va phan ao phai la so hop le!")

    def display(self):
        if self.__imag>=0:
            print(f"Hien thi so phuc theo dang: {self.__real} + {self.__imag}i")
        else:
            print(f"Hien thi so phuc theo dang: {self.__real} - {abs(self.__imag)}i")

    def add(self, other):
        real_sum=self.__real+other.get_real()
        imag_sum=self.__imag+other.get_imag()
        return ComplexNumber(real_sum, imag_sum)

    def subtract(self, other):
        real_diff=self.__real-other.get_real()
        imag_diff=self.__imag-other.get_imag()
        return ComplexNumber(real_diff, imag_diff)

def main():
    print("--- Nhap so phuc thu nhat ---")
    c1=ComplexNumber()
    c1.input_number()
    c1.display()

    print("\n--- Nhap so phuc thu hai ---")
    c2=ComplexNumber()
    c2.input_number()
    c2.display()

    print("\n--- Kiem tra getter va setter tren so phuc 1 ---")
    print(f"Getter: phan thuc = {c1.get_real()}, phan ao = {c1.get_imag()}")
    c1.set_real(c1.get_real()+1)
    print(f"Sau khi dung setter tang phan thuc len 1:")
    c1.display()

    print("\n--- Ket qua phep cong hai so phuc ---")
    sum_result=c1.add(c2)
    sum_result.display()

    print("\n--- Ket qua phep tru hai so phuc ---")
    diff_result=c1.subtract(c2)
    diff_result.display()

    print("\n--- Thu truy cap truc tiep thuoc tinh private __real ---")
    try:
        print("Gia tri __real:", c1.__real)
    except AttributeError:
        print("Truy cap __real that bai: Thuoc tinh private da bi an di!")

if __name__=="__main__":
    main()
