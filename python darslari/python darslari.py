# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
narh = 15000
choy = 1
salat = 1


if choy and salat:
    narh = narh + 10000
elif choy or salat:
     narh = narh + 5000
print(f"Jami {narh} so'm")  



narh = 15000
choy = True
salat = False
non = True
kompot = True
assorti = False
if choy:
    print("Mijoz choy oldi")
    narh = narh + 3000
if salat:
    print("Mijoz salat oldi")
    narh = narh + 2000
if non:
    print("Mijoz non oldi")
    narh = narh + 5000
if kompot:
    print("Mijoz kompot oldi")
    narh = narh + 5000
if assorti:
    print("Mijoz assorti oldi")
    narh = narh + 10000
print(f"Jami {narh} so'm ")








menu = ['osh','shashlik','somsa','manti','qazon kabob','shorva']
buyurtmalar = ['somsa','shorva','manti','qazi']
if buyurtmalar:
    for taom in buyurtmalar:
        if taom in menu:
            print((F"Menuda {taom} bor"))
        else:
            print(F"Kechirasiz menuda {taom} yo'q")
else:
    print("Savatchangiz o';sh")
        







son = -9
if son<0:
    print("Manfiy son")
else:
    print("Musbat son")
    
    
print ("hello world")

    
print("o'ngacha sanaymiz") 
for b in range(10):
    print(b+1)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    