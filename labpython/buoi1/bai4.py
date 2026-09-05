a = float(input(" Hay nhap bien a: "))
b = float(input(" Hay nhap bien b: "))

if a==0:
    if b==0:
        print(" Phuong trinh vo so nghiem")
    else:
        print ("Phuong trinh vo nghiem")
else:
    x = -b/a
    print (f"Phuong trinh bac 1 la:{x}")
