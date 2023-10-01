import math

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

def find_supercomposite_numbers(limit):
    supercomposite_numbers = []
    for n in range(2, limit):
        if count_factors(n) > count_factors(n - 1):
            supercomposite_numbers.append(n)
    return supercomposite_numbers

# Измерение времени выполнения
%timeit find_supercomposite_numbers(100000)
