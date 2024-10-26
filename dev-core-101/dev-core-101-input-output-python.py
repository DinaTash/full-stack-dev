name = input("Введите ваше имя: ")
age = int(input("Введите ваш возраст: "))

import datetime
today = datetime.datetime.now()
x = today.year

birth_year = x - age
year_100 = birth_year + 100
    


print("Привет,", name)
print("Тебе", age, "лет")
print (f"В {year_100} тебе исполнится 100 лет")
