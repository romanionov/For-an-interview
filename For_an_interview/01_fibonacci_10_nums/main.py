# Функция для печати первых 10 чисел Фибоначчи
def fibonacci_10_nums():
    a, b = 0, 1
    for _ in range(10):
        print(a, end=' ')
        a, b = b, a + b


# Вызываем функцию
fibonacci_10_nums()
