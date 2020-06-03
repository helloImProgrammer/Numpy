# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 22:45:26 2020

@author: cihan
"""

import numpy as np

numbers = np.array([[5,10,15],[3,6,9],[7,14,21]]) 
# 3 * 3 matris oluşur
print(numbers[:,1])     #tüm satırlarda ki indexi 1 olan değerleri verir 
print(numbers[1,2])     # 1. satır 2 indexli
print(numbers[-1,:])

print(numbers[:2,:2])


arr1 = np.arange(1,10)
#arr2 = arr1  bellek adresini alır ve arr2 de değişiklik yapmamız o adresteki verileri deiştirmemiz demektir
#yani arr2 de yapacağımız bir değişiklik arr1de de değişiklik yapar aynı adrese sahip oldukları için

arr2 = arr1.copy() #copy() metodunu kullandığımız da o adreste ki verileri kopyalar ve arr2 de değişiklik yapmamız
# arr1 i etkilemez

arr2[0] = 60

print(arr1)
print(arr2)

