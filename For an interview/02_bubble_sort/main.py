import random


# Функция для сортировки входного
# целочисленного массива методом пузырьковой сортировки
def bubble_sort(arr):
    n = len(arr)
    swap = True

    while swap:
        swap = False
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swap = True
        n -= 1

    return arr


# Пример использования
array = [random.randint(0, 100) for _ in range(10)]

print("Исходный массив:", array)
print("Отсортированный массив:", bubble_sort(array))
