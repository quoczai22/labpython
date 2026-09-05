n = int(input("Hay nhap so luong sinh vien: "))
ds_sinhvien = []

for i in range(n):
    print(f"\n--- Nhap cho sinh vien thu {i + 1} ---")
    ten = input("Ten sinh vien: ")
    m1 = float(input("Diem mon 1: "))
    m2 = float(input("Diem mon 2: "))
    m3 = float(input("Diem mon 3: "))
    
    dtb = round((m1 + m2 + m3) / 3, 2)
    
    sv = {
        "ten": ten,
        "diem_cac_mon": {"Mon 1": m1, "Mon 2": m2, "Mon 3": m3},
        "diem_tb": dtb
    }
    
    ds_sinhvien.append(sv)

for i in range(len(ds_sinhvien)):
    for j in range(i + 1, len(ds_sinhvien)):
        if ds_sinhvien[i]["diem_tb"] < ds_sinhvien[j]["diem_tb"]:
            ds_sinhvien[i], ds_sinhvien[j] = ds_sinhvien[j], ds_sinhvien[i]

print("\nDANH SACH SINH VIEN THEO DIEM TRUNG BINH GIAM DAN:")
for sv in ds_sinhvien:
    print(f"Ten: {sv['ten']} | DTB: {sv['diem_tb']}")
