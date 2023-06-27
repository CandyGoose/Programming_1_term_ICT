# Строка - это упорядоченная неизменяемая последовательность символов Юникода

''' 1. Как склеить две строки? '''
x = str("AXTR")   # x станет 's1'  
y = str(567)      # y станет '2'
xy = x + y
print(xy)

''' 2. Как склеить три строки? 
join() — метод, позволяющий склеить N строк с произвольным разделителем
join() — это метод объекта «строка», принимающий в качестве аргумента список
и возвращающий на выходе новую строку '''
names = ["John", "Paul", "Ringo", "George"]
allNames = "; ".join(names)
print(allNames)         # John; Paul; Ringo; George

""" Задание: реализуйте свою реализацию метода join()"""

''' 3. Как разделить строку?
Метод split() - применяется к целевой строке, а разделитель передаётся аргументом
      обратите внимание на различие в применении join и split'''
st = "Мама, мыла раму"
stm = st.split(",")
print(stm)              # ['Мама', ' мыла раму']

срезы (slices).
Срез s[x:y] позволяет получить подстроку с символа x до символа y. 
