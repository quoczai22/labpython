chuoi = input("Hay nhap chuoi la: ")

chuoi_chuan_hoa= chuoi.lower().replace(" ","")

if chuoi_chuan_hoa==chuoi_chuan_hoa[::-1]:
    print(" Phai la chuoi doi xung")
else:
    print(" Khong phai la chuoi doi xung")

