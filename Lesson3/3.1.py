import math
import 
def count_factors(n):
    count = 0
    sqrt_n = int(math.sqrt(n))
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            count += 2  # Учитываем и делитель, и соответствующий ему множитель
    # Если n - полный квадрат, убираем лишний счетчик
    if sqrt_n * sqrt_n == n:
        count -= 1
    return count

# Пример использования
n = 12
print(count_factors(n))  # Вывод: 6 (1, 2, 3, 4, 6, 12)


import math

def count_factors_loop(n):
    count = 0
    sqrt_n = int(math.sqrt(n))
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            count += 2
    if sqrt_n * sqrt_n == n:
        count -= 1
    return count

def count_factors_generator(n):
    sqrt_n = int(math.sqrt(n))
    factors = [(i, n // i) for i in range(1, sqrt_n + 1) if n % i == 0]
    if sqrt_n * sqrt_n == n:
        factors.pop()
    return len(factors) * 2

# Измерение времени выполнения для обоих вариантов
n = 1000000
%timeit count_factors_loop(n)
%timeit count_factors_generator(n)
