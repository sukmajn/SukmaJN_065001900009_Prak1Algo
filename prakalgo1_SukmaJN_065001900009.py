# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 22:21:34 2021

@author: Sukma Julia Nada
"""

import math

a=input("Masukkan angka pertama : ")

p1 = a.split(",")

b=input("Masukkan angka kedua : ")

p2 = b.split(",")

jarak = math.sqrt( ((int(p1[0])-int(p2[0]))*2)+((int(p1[1])-int(p2[1]))*2) )

print("Jarak antara ", a,"dan", b, "adalah",jarak)