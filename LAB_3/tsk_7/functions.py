import threading
import time 
import queue

# функция для суммирования части массива
def sum_array_part(array, start, end, result_queue):
    partial_sum = sum(array[start:end])  # вычисляем частичную сумму
    result_queue.put(partial_sum)  # добавляем результат в очередь

# функция для вычисления суммы с использованием N потоков 
def calculate_sum(N, array, result_label):
    start_time = time.time()

    threads = []
    result_queue = queue.Queue()  # создаем очередь для хранения результатов
    chunk_size = len(array) // N  # размер части массива, которую будет обрабатывать каждый поток.

    for i in range(N):
        # диапазон индексов массива
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < N - 1 else len(array)
        thread = threading.Thread(target=sum_array_part, args=(array, start, end, result_queue))
        threads.append(thread)
        thread.start()

    # ожидаем завершения всех потоков 
    for thread in threads:
        thread.join()

    total_sum = 0
    while not result_queue.empty():  # извлекаем результаты из очереди
        total_sum += result_queue.get()

    end_time = time.time()

    result_label.config(text=f"N = {N}, Общая сумма: {total_sum}, Время выполнения: {end_time - start_time:.4f} секунд")