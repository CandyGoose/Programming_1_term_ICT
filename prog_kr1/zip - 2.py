'''
Создайте программу, которая автоматически высчитывает наценку на продукты и при помощи метода zip() соединяет
название продукта, изначальную стоимость и стоимость с наценкой в список.
'''

product = ['яблоки', 'апельсины', 'клубника', 'вишня', 'молоко', 'печенье', 'бананы', 'кофе', 'чай', 'лимон']
cost = [100, 160, 250, 350, 80, 60, 100, 230, 80, 60]
price = []
nats = 1.15
for i in range(len(product)):
    price.append(cost[i] * nats)
spisok = list(zip(product, cost, price))
print(spisok)