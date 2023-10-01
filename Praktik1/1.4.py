def generate_alkane_structure(stoichiometry):
    if not stoichiometry.startswith('C') or 'H' not in stoichiometry:
        print("Некорректный формат стехиометрии.")
        return

    # Разбиваем стехиометрию на количество атомов углерода и водорода
    carbon_count = int(stoichiometry[1:stoichiometry.index('H')])
    hydrogen_count = int(stoichiometry[stoichiometry.index('H')+1:])

    # Генерируем структурную формулу алкана
    structure = 'H3C'
    for i in range(carbon_count - 1):
        structure += '-CH2'
    structure += f'-CH3'

    return structure

# Пример использования
stoichiometry = 'C8H18'
result = generate_alkane_structure(stoichiometry)
if result:
    print(result)