import math

def powr(a, b):
    if a == 0 and b == 0:
        raise ValueError("Both base and exponent cannot be zero.")
    return math.pow(a, b)

# Примеры использования
try:
    result = powr(2, 3)
    print(result)

    result = powr(0, 5)
    print(result)

    result = powr(0, 0) #ValueError
    print(result)
except ValueError as e:
    print(f"Произошла ошибка: {e}")

# Эта функция сначала проверяет, равны ли a и b нулю. 
# если оба равны нулю, то она генерирует исключение ValueError, 
# в противном случае она использует math.pow для вычисления значения.