n = int(input ("Hay nhap so luong mang: "))

ds_songuyen=[]


for i in range(n):
    so=int(input(f"Hay nhap gia tri thu {i+1}: "))
    if so not in ds_songuyen:
        ds_songuyen.append(so)
    
   
print("Mang sau khi loai bo phan tu giong nhau:")
print(ds_songuyen)
     