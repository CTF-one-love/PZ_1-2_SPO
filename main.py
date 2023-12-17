#Задача №1
import random
import string

products = ['Одежда', 'Телефон', 'Напиток', 'Видеоигра', 'Овощ', 'Обувь', 'Книга', 'Машина', 'Мебель', 'Квартира']

codes = []

for product in products:
    codes.append(product+str(random.randrange(1, 100)))

print(codes)

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
