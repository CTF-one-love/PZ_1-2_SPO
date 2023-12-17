"""Задача №2"""
import random
import string
import pandas as pd

products = ['Холодильник', 'Телефон', 'Компьютер', 'Диск', 'Фрукт', 'Мерч', 'Книга', 'Футболка', 'Автомобиль', 'Квартира']
buy_price = {}
sell_price = {}
razn = {}
dis_codes = []

def tovr_code(p=[]):
    dis_code = []
    for product in p:
      dis_code.append(product+str(random.randrange(1000, 10000)))
    return dis_code

dis_codes = tovr_code(products)
print(*dis_codes, sep=" " + "\n" )


"""
#Задача №1
import random
import string

products = ['Одежда', 'Телефон', 'Напиток', 'Видеоигра', 'Овощ', 'Обувь', 'Книга', 'Машина', 'Мебель', 'Квартира']

codes = []

for product in products:
    codes.append(product+str(random.randrange(1, 100)))

print(codes)

#адача №2
buy_price = {}
sell_price = {}
margin = {}
for code in codes:
    buy_price[code] = random.randrange(100, 1000)
    sell_price[code] = buy_price[code] + random.random()*300
    margin[code] = round(sell_price[code]-buy_price[code], 2)

print(margin)
#Задача №3

for key, value in sell_price.items():
    print(f'Только сегодня {key} стоит {value} рублей!')

#Задача №4

names = {}

for product in products:
    limit = 0
    length = 2
    names[product] = []
    while limit != 10:
      names[product].append(product + '_' + ''.join(random.choice(string.ascii_letters) for x in range(length)))
      length += 1
      limit += 1

print(names[product])

for product in products:
  print(max(names[product], key=len))
  print(min(names[product], key=len))
  """