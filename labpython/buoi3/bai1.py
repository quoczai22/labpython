def cau1epchuoisonguyen(a):
    return float(a)

def cau2nhapvaodsduoidangchuoichuyenthanhlistsonguyen(chuoi):
  return list(chuoi)

def cau3nhanvaomoikieudulieuchuyenthanhstring(all):
   return str(all)

def cau4kiemtrasochanhayle(a):
    if a % 2 == 0:
        print("So nay la chan")
    else:
        print("So nay la le")
    return a

def cau5phanloaituoi(tuoi):
    if(tuoi<=13):
        print("Tre em")
    elif(tuoi<22):
        print("Thieu nien")
    else:
        print("Nguoi lon")
    return tuoi

def cau6timmaxtrbaso(a,b,c):
    return max(a,b,c)

def cau7kiemtranamnhuan(nam):
    if((nam%4==0 and nam%100!=0) or (nam%400==0)):
        print("La nam nhuan")
    else:
        print("Khong la nam nhuan")
    return nam

def cau8incacsotu1den10():
    i=1
    while i<11:
        print(i)
        i=i+1

def cau9bancuuchuongcua1so(a):
    b=1
    for i in range(10):
        print(f"{a}x{b}={a*b}")
        i=i+1
        b=b+1
    return a


    

def main():
    # a=int(input("Hay nhap so nguyen de ep qua kieu float: "))
    # print(cau1epchuoisonguyen(a))

    # chuoi=str(input("Hay nhap vao 1 chuoi: "))
    # print (cau2nhapvaodsduoidangchuoichuyenthanhlistsonguyen(chuoi))

    # all=(input("Hay nhap vao bien de chuyen thanh string: "))
    # print(cau3nhanvaomoikieudulieuchuyenthanhstring(all))

    # so=int(input("Hay nhap so de kiem tra xem no la chan hay le: "))
    # print(cau4kiemtrasochanhayle(so))

    # tuoi=int(input("Hay nhap vao so tuoi de xac dinh: "))
    # print(cau5phanloaituoi(tuoi))

    # a=int(input("Hay nhap vao bien a: "))
    # b=int(input("Hay nhap vao bien b: "))
    # c=int(input("Hay nhap vao bien c: "))

    # print(cau6timmaxtrbaso(a,b,c))

    # nam=int(input("Hay nhap vao nam ma ban muon xet: "))
    # print(cau7kiemtranamnhuan(nam))

    # print(cau8incacsotu1den10())

    # a=int(input("Hay nhap vao 1 so de biet bang cuu chuong: "))
    # cau9bancuuchuongcua1so(a)


    
if __name__ == "__main__":
    main()