import sys

def hailstone_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def stopping_time(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    return count

if len(sys.argv) != 2:
    print("Использование: python script.py <начальное_число>")
    sys.exit(1)

try:
    starting_number = int(sys.argv[1])
    if starting_number <= 0:
        raise ValueError("Начальное число должно быть положительным.")
except ValueError:
    print("Ошибка: Начальное число должно быть положительным целым числом.")
    sys.exit(1)

sequence = hailstone_sequence(starting_number)
time = stopping_time(starting_number)

print(f"Последовательность чисел-градин для числа {starting_number}:")
print(sequence)
print(f"Время останова: {time} шагов")
