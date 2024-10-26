# Игра "Угадай число"
num = int(input("Введите число от 1 до 10: "))
 
if num < 8:
    print("Число больше")

if num > 8:
    print("Число меньше")

if num == 8:
    print("Вы угадали число")

if num > 10:
    print("Неверное число")



# Простое, составное
num = int(input("Введите число: "))


for x in range(2, int(num**0.5) + 1):
        if num % x == 0:
            print("Число составное")

def isprime(num):
    if num // 1 == num and num // num == 1:     
        print("Число простое")

    
if num == 0:
    print("Не простое и не составное число")


# Цельсии, Фаренгейт
temp = int(input("Введите температуру в ℃: "))
def F(temp):
     return temp*9/5+32
print (F(temp))


#Школа
age = int(input("Введите ваш возраст: "))

if age < 6:
    print("Ты ещё не учишься в школе.")
if age >= 6 and age < 18:
    print("Ты уже можешь учиться в школе.")
if age > 18:
    print("Ты уже закончил школу")    
    