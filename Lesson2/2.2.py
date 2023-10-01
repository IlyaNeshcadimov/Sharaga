def str_vector(v):
    assert isinstance(v, (list, tuple)), 'Аргумент для str_vector должен быть списком или кортежем'
    assert len(v) in (2, 3), 'Вектор должен быть 2D или 3D в str_vector'
    
    for component in v:
        assert isinstance(component, (int, float)), 'Элемент вектора должен быть действительным числом'

    unit_vectors = ['i', 'j', 'k']
    components = []

    for i, component in enumerate(v):
        if component != 0:
            components.append('{}{}'.format(component, unit_vectors[i]))

    if not components:
        return '0'

    return '+'.join(components).replace('+-', '-')

# Пример использования с некорректным элементом (строка)
try:
    print(str_vector([-2, 3.5, 'a']))
except AssertionError as e:
    print(f'Произошла ошибка: {e}')