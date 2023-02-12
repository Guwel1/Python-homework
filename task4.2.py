#Задача про чернику


import os
os.system('cls')

from random import randint
arrayberry = [randint(1, 20) for _ in range (int(input("Введите количество кустов: ")))]
print(arrayberry)
maxberrycount = 0
berrycount = 0
i=0
berrycount = arrayberry[len(arrayberry)-1] + arrayberry[i] + arrayberry[i+1]
maxberrycount = berrycount
i+=1
while i < len(arrayberry)-1 and i!= 0:
        berrycount = arrayberry[i-1] + arrayberry[i] + arrayberry[i+1]
        i+=1
        while (maxberrycount < berrycount):
              maxberrycount = berrycount
        if (i == len(arrayberry)-1):
            berrycount = arrayberry[i-1] + arrayberry[i] + arrayberry[0]
        if (maxberrycount < berrycount):
            maxberrycount = berrycount
print(maxberrycount)
