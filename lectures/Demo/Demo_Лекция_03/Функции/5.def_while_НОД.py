﻿""" 1. Подсчет количества итераций """
def Countgit(n):
    #n = int(input('Задайте число '))
    k = 0
    while n > 0:    # прекратить действия, когда n станет 0
        n = n//10   # Отбрасывание последней цифры числа n
        k = k + 1   # Увеличение значения переменной-счетчика
    #print("Количество цифр в числе", k)
    return k

#Countgit()
#h = Countgit()

n = int(input('Задайте число '))
h = Countgit(n)
print("Количество цифр в числе", h)


""" 2. Алгоритм Евклида """
"""
a = int(input('Задайте первое число '))
b = int(input('Задайте второе число '))

while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
        nod = a

print('НОД равен', nod) 
"""




