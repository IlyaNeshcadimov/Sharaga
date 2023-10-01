import os
import sys

months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

try:
    dir_name = sys.argv[1]
except IndexError:
    print("Использование: python eg4-osmodule.py <каталог>")
    sys.exit(1)

if not os.path.exists(dir_name):
    print(f"Каталог '{dir_name}' не существует.")
    sys.exit(1)

for filename in os.listdir(dir_name):
    try:
        # Проверяем, что имя файла соответствует формату 'data-DD-MMM-YY.txt'
        if not filename.startswith('data-') or not filename.endswith('.txt'):
            raise ValueError("Некорректное имя файла")
        
        d, month, y = int(filename[5:7]), filename[8:11], int(filename[12:14])
        
        # Проверяем, что сокращенное обозначение месяца корректно
        month_lower = month.lower()
        if month_lower not in months:
            raise ValueError("Некорректное сокращенное обозначение месяца")
        
        m = months.index(month_lower) + 1
        newname = 'data-20{:02d}-{:02d}-{:02d}.txt'.format(y, m, d)
        newpath = os.path.join(dir_name, newname)
        oldpath = os.path.join(dir_name, filename)
        print(oldpath, '->', newpath)
        os.rename(oldpath, newpath)
    except (ValueError, IndexError):
        print(f"Пропущен файл '{filename}' из-за ошибки формата.")
