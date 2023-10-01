def hailstone_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

# Пример использования для n = 27
starting_number = 27
sequence = hailstone_sequence(starting_number)
print(sequence)


def stopping_time(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    return count

# Пример использования для n = 27
starting_number = 27
time = stopping_time(starting_number)
print(f"Время останова для числа {starting_number}: {time} шагов")
