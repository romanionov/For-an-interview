import queue
import random
import string
import threading
import time

# Флаг для остановки потоков
stop_event = threading.Event()



# Функция для генерации случайной строки
def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_letters, k=length))


# Функция первого потока: генерация строк
def string_generator(q):
    while not stop_event.is_set():  # Проверяем флаг остановки
        random_string = generate_random_string()
        print(f"Сгенерированная строка: {random_string}")
        q.put(random_string)  # Отправляем строку во второй поток
        time.sleep(2)  # Периодичность генерации (2 секунды)


# Функция второго потока: сортировка строк
def string_sorter(q):
    while not stop_event.is_set():  # Проверяем флаг остановки и очередь
        try:
            random_string = q.get(timeout=0)  # Получаем строку из очереди с таймаутом
            sorted_string = ''.join(sorted(random_string, reverse=True))  # Сортируем строку
            print(f"Отсортированная строка: {sorted_string}", end='\n\n')
            q.task_done()  # Уведомляем, что задача выполнена
        except queue.Empty:
            continue  # Если очередь пуста, продолжаем


# Основная функция
def main():
    q = queue.Queue()  # Создаем очередь для передачи данных между потоками

    # Создаем потоки
    generator_thread = threading.Thread(target=string_generator, args=(q,))
    sorter_thread = threading.Thread(target=string_sorter, args=(q,))

    # Запускаем потоки
    generator_thread.start()
    sorter_thread.start()

    # Ожидаем 10 секунд
    time.sleep(10)

    # Устанавливаем флаг остановки
    stop_event.set()

    # Ждем завершения потоков
    generator_thread.join()
    sorter_thread.join()


main()
