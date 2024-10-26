a = float(input("Введите число a: "))
b = float(input("Введите число b: "))

print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")
operation = (input("Выберите операцию(1/2/3/4): "))


# Сложение
def addition(a, b):
    return a+b  
if operation == "1":
    print(addition(a,b))


# Вычитание
def subtract(a, b):
    return a - b  
if operation == "2":
    print(subtract(a,b))

# Умножение
def multiply(a, b):
    return a * b  
if operation == "3":
    print(multiply(a,b))

# Деление
def divide(a, b):
    if b==0:
        return "Деление на ноль невозможно."
    return a / b 
if operation == "4":
    print(divide(a,b))

else:
    print("Неверный номер операции.")




