# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 10:45:03 2026

@author: Administrator
"""

n=int(input("Hay nhap vao so luong phan tu cua mang: "))

ds_songuyen=set()

for i in range(n):
    so=int(input(f"Hay nhap gia tri thu {i+1}: "))
    if(so%2==0):
        ds_songuyen.add(so)
print("Tap hop cac so chan trong mang vua nhap la: ",ds_songuyen)
