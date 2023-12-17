#Задача №1
import random
import string

products = ['Одежда', 'Телефон', 'Напиток', 'Видеоигра', 'Овощ', 'Обувь', 'Книга', 'Машина', 'Мебель', 'Квартира']

codes = []

for product in products:
    codes.append(product+str(random.randrange(1, 100)))

print(codes)
