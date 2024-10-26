
# Сложение
def addition(a, b):
    return a+b  # Результат суммы a и b


# Вычитание
def subtract(a, b):
    return a - b  # Результат разности a и b

# Умножение
def multiply(a, b):
    return a * b  # Результат произведения a и b

# Деление
def divide(a, b):
    if b==0:
        return "Деление на ноль невозможно"
    return a / b  # Результат частное a и b
a=5
b=0
print(addition(a,b))
print(subtract(a,b))
print(multiply(a,b))
print(divide(a,b))

