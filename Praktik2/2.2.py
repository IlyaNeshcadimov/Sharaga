# Не было [image.png](attachment:image.png)

import sys
import math

def haversine(lat1, lon1, lat2, lon2):
    # Радиус Земли в километрах
    R = 6378.1

    # Переводим градусы в радианы
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Разница в широте и долготе
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Вычисляем haversin угла
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    # Вычисляем расстояние
    distance = R * c
    return distance

if len(sys.argv) != 3:
    print("Использование: python greatcircle.py <широта1,долгота1> <широта2,долгота2>")
    sys.exit(1)

try:
    lat1, lon1 = map(float, sys.argv[1].split(','))
    lat2, lon2 = map(float, sys.argv[2].split(','))
except ValueError:
    print("Ошибка: Некорректный формат координат.")
    sys.exit(1)

distance = haversine(lat1, lon1, lat2, lon2)
print(f"{int(distance)} km")
