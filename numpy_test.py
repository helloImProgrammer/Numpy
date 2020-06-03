# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 23:41:03 2020

@author: cihan
"""

import numpy as np 


#1 (10,15,30,45,60) değerlerine sahip numpy dizisi oluştur

numbers = np.array([10,15,45,60])

#2 (5-15) arasındaki sayılarla numpy dizisi oluşturunuz

numbers = np.arange(5,15)

#3 (50-100) arasında 5'er 5'er artarak numpy dizisi oluştur

numbers = np.arange(50,100,5)


#4 10 elemanlı sıfırlardan oluşan bir dizi oluşturun

numbersZeros = np.zeros(10)


#5 10 elemanlı birlerden oluşan bir dizi oluşturun

numbersOnce = np.ones(10)


#6 (0-100) arasında eşit aralıklı 5 sayı üretin 

numberslin = np.linspace(0,100,5) # (başlangıç değeri,bitiş değeri(dahil),kaça bölüneceği)

#7 (10-30) arasında rastgele 5 tane tamsayı üretin

num10 = np.random.randint(10,30,5)


# 8 [-1 ile 1] arasında 10 adet sayı üretin

numflo = np.random.randn(10)

#9 (3x5) boyutlarında (10-50) arasında rastgele sayı matrisi oluşturun

numMatris = np.random.randint(10,50,15).reshape(3,5)

#10 üretilen matrisin satır ve sütun sayıları toplamlarını hesaplayınız

result0 = np.sum(numMatris,axis = 0)    #dizinin süütunlarını toplar
result1 = np.sum(numMatris,axis = 1)    #dizinin satırlarını toplar

#print(numMatris.sum(axis = 0)) => bu şekilde de kullanım yapabilirsin

#11 üretilen matrisin en büyük , en küçük ve ortalaması nedir

resultMin = np.min(numMatris)   #dizinin en küçük değerini verir
resultMax = np.max(numMatris)   #dizinin en büyük elemanını verir
resultMean = np.mean(numMatris) #dizinin ortalamasını verir

#12 üretilen matrisin en büyük değerinin indeksi kaçtır

resultMaxIndex = np.argmax(numMatris)

#13 (10-20) arasındaki sayıları içeren dizinin ilk 3 elemanını seçiniz

numbers1 = np.arange(10,20)

print(numbers[:3])


#14 üretilen dizinin elemanlarını tersten yazdırın

print(numbers1[::-1])


#15 üretilen matrisin ilk satırını seçiniz

print(numMatris[0])

#16 üretilen matrisin 2.satır 3.sütundaki elemanı hangisidir  ?

print(numMatris[1,2])

#17 üretilen  matrisin tüm satırlardaki ilk elemanı seçiniz

print(numMatris[:,0])

#18 üretilen matrisin her bir elemanının karesini alınız

resultSquare =np.square(numMatris)

#19 üretilen matris elemanlarının hangisi pozitif çift sayıdır
#   aralığı (-50,+50) arasında yap


newNumMatris = np.random.randint(-50,50,15).reshape(3,5)

resultplus = (newNumMatris >= 0) & (newNumMatris %2 ==0) # and =  &


print(newNumMatris[resultplus])