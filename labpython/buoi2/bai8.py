# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 10:28:11 2026

@author: Administrator
"""

n = int(input (f"Hay nhap so luong mang 1: "))

m = int(input (f"Hay nhap so luong mang 2: "))

ds_songuyen_1=set()

ds_songuyen_2=set()

for i in range(n):
    so_1 = int(input(f"Hay nhap gia tri thu {i+1} cua mang 1: "))
    ds_songuyen_1.add(so_1)
    
for k in range(m):
    so_2 = int(input(f"Hay nhap gia tri thu {k+1} cua mang 2: "))
    ds_songuyen_2.add(so_2)
    
ds_hop=ds_songuyen_1.union(ds_songuyen_2)

print("Mang 1 hop voi mang 2 la: ",ds_hop)

ds_giao=ds_songuyen_1.intersection(ds_songuyen_2)

print("Mang 1 giao voi mang 2 la: ",ds_giao)

ds_hieu_1v2=ds_songuyen_1.difference(ds_songuyen_2)

print("Mang 1 hieu voi mang 2 la:  ",ds_hieu_1v2)

ds_hieu_2v1= ds_songuyen_2.difference(ds_songuyen_1)

print("Mang 2 hieu voi mang 1 la: ",ds_hieu_2v1)



