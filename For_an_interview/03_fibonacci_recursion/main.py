# Функция для вывода n-ого числа Фибоначчи с
# использованием рекурсии (m = fibonacci(n), где n - целое число)

def fibonacci(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


# Пример использования
n = 4
print(f"Число Фибоначчи для n={n} равно {fibonacci(n)}")
