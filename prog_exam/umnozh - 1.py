import json

'''
Напишите программу, которая ожидает ввод последовательно произвольного количества вещественных чисел и добавляет их 
в список. Затем умножает каждое числом меньшее 10 на 1.13, большее 10 – умножает на 0.18, равное точно 10 – оставляет 
без изменения. После этого сортирует полученный список, и наконец, печатает его, округлив до двух знаков после запятой. 
Реализуете также возможность сохранения указанных данных в файл. Тип файла выберите на свое усмотрение, в комментариях 
обоснуйте свой выбор.
'''

spisok_new = []
a = 1.13
b = 0.18

n = input('Введите числа через пробел: ')
spisok = [float(value) for value in n.split(' ')]

for i in range(len(spisok)):
    if spisok[i] < 10:
        c = spisok[i] * a
        spisok_new.append(round(c, 2))
    elif spisok[i] > 10:
        c = spisok[i] * b
        spisok_new.append(round(c, 2))
    else:
        spisok_new.append(spisok[i])

spisok_new.sort()
print('Полученный список:', spisok_new)
with open('result1.txt', 'w') as fw:  # txt открывается практически на всех устройствах
    json.dump(spisok_new, fw)