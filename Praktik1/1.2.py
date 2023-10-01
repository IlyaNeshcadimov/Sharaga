import math

def arithmetic_geometric_mean(x, y, epsilon=1e-10, max_iterations=1000):
    a = x
    b = y
    
    iteration = 0
    while iteration < max_iterations:
        a_next = 0.5 * (a + b)
        b_next = math.sqrt(a * b)
        
        if abs(a_next - a) < epsilon and abs(b_next - b) < epsilon:
            return (a_next + b_next) / 2.0
        
        a = a_next
        b = b_next
        iteration += 1

    raise Exception("Не удалось достичь необходимой точности")

# Вычисление константы Гаусса
G = 1 / arithmetic_geometric_mean(1, math.sqrt(2))

print("Константа Гаусса G =", G)