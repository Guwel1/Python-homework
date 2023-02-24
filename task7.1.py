#Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
#Поскольку разобраться в его кричалках не настолько просто,
#насколько легко он их придумывает, Вам стоит написать программу.
#Винни-Пух считает, что ритм есть, если число слогов
#(т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
#Фраза может состоять из одного слова, если во фразе
#несколько слов, то они разделяются дефисами.
#Фразы отделяются друг от друга пробелами.
#Стихотворение Винни-Пух вбивает в программу с клавиатуры.
#В ответе напишите “Парам пам-пам”, если с ритмом все в порядке
#и “Пам парам”, если с ритмом все не в порядке
#пара-ра-рам рам-пам-папам па-ра-па-дам
#Парам пам-пам

import os
os.system('cls')



letters = 'а,е,ё,и,о,у,ы,э,ю,я'
frase=input("Введите фразу: ").split()
lst=[sum([True for i in word if i.lower() in letters]) for word in frase]
if all(lst) and len(set(lst)) == 1:
   res = "Парам пам-пам"  
else: res = "Пам парам"
print(res)


