import math
def kiemtranhapso():
    try:
        n=int(input("Hay nhap so thu nhat"))
        m=int(input("Hay nhap so thu hai"))
        
        b=n/m
    except ValueError:
        print("Vui long nhap so hop le")
    except ZeroDivisionError:
        print("Vui long nhap so thu 2 lon hon khong")
        
def kiemtrasonguyen():
    try:
        n=int(input("Hay nhap so "))
        print("So nguyen da nhap la",n)
    except ValueError:
        print("Vui long nhap so nguyen")
        
def kiemtradocfile():
    try:
        ten_file="data.txt"
        with open(ten_file,"r",encoding="utf-8") as file:
            noi_dung=file.read()
            print("Noi dung file la",noi_dung)
    except FileNotFoundError:
        print("Khong tim thay file")
        
def kiemtracanbac():
    try :
        n=int(input("Hay nhap so "))
        if(n>0):
            math.sqrt(n)
        else:
            raise ValueError ("Khong the nhap vao so am") 
    except ValueError:
        print("Nhap vao la so nguyen duong")
    
def main():
# =============================================================================
#     kiemtranhapso()
# =============================================================================
# =============================================================================
#     kiemtrasonguyen()
# =============================================================================
# =============================================================================
#     kiemtradocfile()
# =============================================================================
    kiemtracanbac()
if __name__ == "__main__":
    main()

