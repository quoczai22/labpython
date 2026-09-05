# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 08:21:55 2026

@author: Administrator
"""


n = int(input("Hay nhap so luong so nguyen trong danh sach: "))
ds_tbcong = []


for i in range(n) :
    so=float(input(f"Hay nhap gia tri thu {i+1}: "))
    ds_tbcong.append(so)

tong=sum(ds_tbcong)
trung_binh=tong/len(ds_tbcong)

print(f"Trung binh cong cua danh sach vua nhap la: {trung_binh}") 