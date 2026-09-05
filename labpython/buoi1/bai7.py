chuoi =str(input("Hay nhap vao 1 chuoi: "))

so_ky_tu =len(chuoi)
chu = sum(c.isalpha() for c in chuoi)
so = sum(s.isalpha() for s in chuoi)


print (f" So ky tu cua chuoi tren la: {so_ky_tu}")
print (f"So chu so {so}")
print (f"So chu {chu}")
