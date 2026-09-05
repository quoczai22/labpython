# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 10:47:29 2026

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
    
print("Phan tu chi co trong mang 1 la: ", ds_songuyen_1-ds_songuyen_2)