# Первый способ будет использовать оператора "^" - битовое исключающее ИЛИ, оператор ^ выполняет операцию XOR для каждой пары битов в двоичном представлении чисел и возвращает соответствующий бит в результирующем числе.

def xor_operator(a, b):
    return a ^ b

#Проверка
a = 5  # бинарное представление: 0101
b = 3  # бинарное представление: 0011

result = a ^ b  # Результат XOR: 0110 (бинарно) или 6 (десятично)


# Второй способ использует выражение (a and not b) or (not a and b) вернет True только в случае, когда a и b имеют разные значения (True и False или False и True). 

def xor_logical(a, b):
    return (a or b) and not (a and b)

#Проверка
a = True
b = True
result = (a and not b) or (not a and b)  # Результат: False

a = False
b = True
result = (a and not b) or (not a and b)  # Результат: True


