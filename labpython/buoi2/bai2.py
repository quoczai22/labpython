soSV= int(input("Hay nhap so luong sinh vien ma ban muon nhap ten: "))
ds_hocsinh=[]

# =============================================================================
# for sohocsinh in range (soSV): # cach 1
#     hocsinh= input(f"hay nhap ten cua hoc sinh thu {sohocsinh+1}: ")
#     ds_hocsinh.append(hocsinh)
# =============================================================================

i=0 #cach 2
while i<soSV: 
    hocsinhthu= input(f"hay nhap ten cua hoc sinh thu {i+1}: ")
    ds_hocsinh.append(hocsinhthu)
    i+=1

ds_hocsinh.sort()

print ("Danh sach sinh vien")

for stt,ten in enumerate(ds_hocsinh,1):
    print(f"{stt}.{ten}")

