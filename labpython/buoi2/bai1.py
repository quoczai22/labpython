
ds_songuyen= []

for songuyen in range (1,6):
    so= int(input("Hay nhap so nguyen: "))
    ds_songuyen.append(so)
    
print("Tong danh sach so nguyen la: ",sum(ds_songuyen))
    
print ("Gia tri lon nhat cua ds so nguyen la: ",max(ds_songuyen))
