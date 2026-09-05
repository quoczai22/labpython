n=int(input("Hay nhap vao so luong phan tu cua mang: "))

ds_songuyen=set()

for i in range(n):
    so=int(input(f"Hay nhap gia tri thu {i+1}: "))
    ds_songuyen.add(so)
    
print("Mang la: ",ds_songuyen)

kiemtraso=int(input("Hay nhap so ma ban muon kiem tra: "))

if kiemtraso in ds_songuyen:
    print("co")
else:
    print("khong")
