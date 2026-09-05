n=5

ds_songuyen=set()

for i in range(n):
    so=int(input(f"Hay nhap gia tri thu {i+1}: "))
    ds_songuyen.add(so)
    
print("Mang luc dau la: ",ds_songuyen)

m=int(input("Hay nhap so luong phan tu ma ban muon them: "))

for k in range(m):
    songuyen=int(input("Hay nhap phan tu ma ban muon them vao mang: "))
    ds_songuyen.add(songuyen)
    
print("Mang sau khi them la: ",ds_songuyen)

soluongxoa=int(input("Hay nhap so luong phan tu ma ban muon xoa: "))

for l in range(soluongxoa):
    soxoa=int(input("Hay nhap so ban muon xoa: "))
    if soxoa in  ds_songuyen:
        ds_songuyen.remove(soxoa)
    else: 
        print("e khong co so nguyen can xoa trong mang!!!")
    
print("Mang sau khi xoa la: ",ds_songuyen)

