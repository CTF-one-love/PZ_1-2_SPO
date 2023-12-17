"""Задача №2"""
import random
import string

products = ['Холодильник', 'Телефон', 'Компьютер', 'Диск', 'Фрукт', 'Мерч', 'Книга', 'Футболка', 'Автомобиль', 'Квартира']
dis_codes = []

buy_price = {}
sell_price = {}
margin = {}
marig = {}

def tovr_code(p=[]):
    dis_code = []
    for product in p:
      dis_code.append(product+str(random.randrange(1000, 10000)))
    return dis_code

dis_codes = tovr_code(products)

def razn(dis=[]):
    for code in dis:
        buy_price[code] = random.randrange(100, 1000)
        sell_price[code] = buy_price[code] + random.random()*500
        marig[code] = round(sell_price[code]-buy_price[code], 2)
    return marig[code]

margin = razn(dis_codes)
print(margin )
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
