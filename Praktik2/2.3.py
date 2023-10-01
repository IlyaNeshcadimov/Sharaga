import os
import xml.etree.ElementTree as ET

# Создание каталога 'test' в домашнем каталоге пользователя
user_home = os.path.expanduser("~")
test_directory = os.path.join(user_home, "test")
os.makedirs(test_directory, exist_ok=True)

# Генерация 20 файлов SVG с анимацией
for i in range(20):
    filename = os.path.join(test_directory, f"fig{i:02d}.svg")
    
    svg_root = ET.Element("svg", xmlns="http://www.w3.org/2000/svg", xmlns_xlink="http://www.w3.org/1999/xlink", width="500", height="500", style="background: #ffffff")
    
    outer_circle = ET.Element("circle", cx="250.0", cy="250.0", r="200", style="stroke: black; stroke-width: 2px; fill: none;")
    inner_circle = ET.Element("circle", cx=str(250 + i * 10), cy="250.0", r="20", style="stroke: red; fill: red;")

    svg_root.append(outer_circle)
    svg_root.append(inner_circle)

    with open(filename, "w") as svg_file:
        svg_file.write(ET.tostring(svg_root, encoding="utf-8").decode())

print("Создан каталог 'test' и сгенерированы файлы SVG с анимацией.")


#convert -delay 5 -loop 0 fig*.svg animation.gif
