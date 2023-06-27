﻿# Последовательность Фибоначчи
'''
функцию, которая возвращает числа последовательности Фибоначчи,
можно записать с помощью синтаксиса генератора
'''
def fib(a=0, b=1):
    '''
    функция возвращает объект типа generator — специальный итератор,
    который умеет сохранять контекст выполнения
    '''
    while True:
        yield a
        a, b = b, a + b


f = fib()

'''
Можно извлекать новые значения генераторов,
как если бы они были итераторами, с помощью функции next() и циклов:
'''
print(', '.join(str(next(f)) for _ in range(10)))
# 0, 1, l, 2, 3, 5, 8, 13, 21, 34


