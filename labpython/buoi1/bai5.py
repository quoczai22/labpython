import math
a = float (input( "Hay nhap bien a: "))
b = float (input( "Hay nhap bien b: "))
c = float (input( "Hay nhap bien c: "))

denta = b*b -4 * a *c

if a==0:
    if b==0:
        if c==0:
            print("Phuong trinh vo so nghiem")
        else:
            print("Phuong trinh vo nghiem")
    else:
        x=-c/b
        print(f"Phuong trinh co 1 nghiem duy nhat {x}")
elif denta > 0:
    x1 = (-b + math.sqrt(denta))/2*a
    x2 = (-b - math.sqrt(denta))/2*a
    print(f"Phuong trinh co 2 nghiem x1 la: {x1} va x2 la: {x2}")
elif denta ==0:
    x = -b/(2*a)
    print(f"Phuong trinh co nghiem kep la: {x}")
else :
    print("Phuong trinh vo nghiem")