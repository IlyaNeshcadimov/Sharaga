def normalize_list(a):
    # Находим минимальное и максимальное значения в списке
    min_val = min(a)
    max_val = max(a)

    # Вычисляем разницу между максимальным и минимальным значениями
    range_val = max_val - min_val

    # Нормализуем каждый элемент в списке
    normalized_a = [(x - min_val) / range_val for x in a]
    
    return normalized_a

# Пример использования
a = [2, 4, 10, 6, 8, 4]
normalized_a = normalize_list(a)
print(normalized_a)
