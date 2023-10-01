import math

def sign(a):
    return int(math.copysign(1, a))

# Примеры использования:
x = 5
y = -3
print(sign(x))  # Вывод: 1 (положительное число)
print(sign(y))  # Вывод: -1 (отрицательное число)