# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 23:12:38 2020

@author: cihan
"""

import numpy as np 


numbers1 = np.random.randint(10,100,6)
numbers2 = np.random.randint(15,105,6)

result_sum = numbers1 + numbers2        #numbers1 ve number2 dizisinde ki verileri indexine göre toplar ve 
#yeni bir dizi üretir

result10 = numbers1 + 15 #numbers1 dizisinde ki tüm elemanlara 15 değerini ekler

resultsin = np.sin(numbers1)    #verdiğimiz dizinin sinüs değerini dizi olarak geri döndürür
resultcos = np.cos(numbers2)    # verdiğimiz dizinin cosinüs değerini bize dizi olarak geri döndürür

resultkok = np.sqrt(numbers1) #verdiğimiz dizinin her bir değerinin karekökünü alır ve bize dizi olarak geri döndürür


resultlog = np.log(numbers1) #verdiğimiz dizinin her bir değerinin logaritmasını bize geri döndürür

mnumbers1 = numbers1.reshape(2,3)  #diziyi matrise çevirir
mnumbers2 = numbers2.reshape(2,3)

resultv = np.vstack((mnumbers1,mnumbers2))   #2 matrisi dikey olarak birleştrir

resulth = np.hstack((mnumbers1,mnumbers2)) # 2 matrisi yatay birleştirir

result = numbers1 > 18 #◘bool türünde değer verir dizinin elemanlarına tek tek 
#bakıp belirtilen koşula uyup uymadığını sorgular


numbers3 = np.arange(1,50,5)        # 1 ile 50 arasın da 5'erli artacak şekilde bir değişken tanımladık 10 tane oluşturur
numbers4 = np.random.randint(10,100,10) #10 tane rastgele sayı üreten bir değişken belirledik

resultsum = numbers3 + numbers4 #değerlerin indekslerine göre toplanmasını sağladık

result = resultsum % 2 == 0 #bu toplanan değerlerin içerisin de çift olanları bulduk ve indekleri result değişkeni 
#içinde tutuluyor

print(resultsum[result]) #resultsum değişkeninin için de olan çift değerleri ekrana bastırdık
