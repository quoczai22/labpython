# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 09:10:53 2026

@author: Administrator
"""

n = int(input (f"Hay nhap so luong mang 1: "))

m = int(input (f"Hay nhap so luong mang 2: "))

ds_songuyen_1=[]

ds_songuyen_2=[]

for i in range(n):
    so_1=int(input(f"Hay nhap gia tri thu {i+1} cua mang 1: "))
    ds_songuyen_1.append(so_1)
    
for k in range(m):
    so_2=int(input(f"Hay nhap gia tri thu {k+1} cua mang 2: "))
    ds_songuyen_2.append(so_2)
    
ds_tron=ds_songuyen_1+ds_songuyen_2

ds_sapxep=sorted(ds_tron)
ds_sapxep_dao = ds_sapxep[::-1]

print(ds_sapxep_dao)
