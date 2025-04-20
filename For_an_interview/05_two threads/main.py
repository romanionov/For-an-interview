import queue
import random
import string
import threading
import time


stop_event = threading.Event()


def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_letters, k=length))


# Функция первого потока: генерация строк
def string_generator(q):
    while not stop_event.is_set():
        random_string = generate_random_string()
        print(f"Сгенерированная строка: {random_string}")
        q.put(random_string)
        time.sleep(2)


# Функция второго потока: сортировка строк
def string_sorter(q):
    while not stop_event.is_set():
        try:
            random_string = q.get(timeout=0)
            sorted_string = ''.join(sorted(random_string, reverse=True))
            print(f"Отсортированная строка: {sorted_string}", end='\n\n')
            q.task_done()
        except queue.Empty:
            continue


# Основная функция
def main():
    q = queue.Queue()

    generator_thread = threading.Thread(target=string_generator, args=(q,))
    sorter_thread = threading.Thread(target=string_sorter, args=(q,))

    generator_thread.start()
    sorter_thread.start()

    time.sleep(10)

    stop_event.set()

    generator_thread.join()
    sorter_thread.join()


main()
