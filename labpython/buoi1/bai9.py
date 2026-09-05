chuoi = str(input ("Hay nhap vao 1 cau: "))

dstu=chuoi.split()

tudien={}



#cach 1
for tu in dstu:
    if tu not in tudien:
        tudien[tu]=1
    else:
        tudien[tu]+=1
print("So lan xuat hien cua tu la ")
for tu,solan in tudien.items():
     print(f" tu {tu} xuat hien {solan}")
     
     

#cach 2
for i in set(dstu):
    print(f" tu {i} xuat hien {dstu.count(i)} lan")