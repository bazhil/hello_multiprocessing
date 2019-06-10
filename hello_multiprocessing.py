import os
import time
from multiprocessing import Process, current_process

def square(numbers):
    """
    Функция, которая возводит число в квадрат
    :param numbers: список чисел
    :return:
    """
    for number in numbers:
        time.sleep(0.5)
        result = number * number
        process_id = os.getpid()
        process_name = current_process().name
        print(f'Process ID {process_id}, Process NAME {process_name}')
        print(f'The number {number} squares to {result}')


def cube(numbers):
    """
    Функция, которая возводит число в куб
    :param numbers: список чисел
    :return:
    """
    for number in numbers:
        time.sleep(0.5)
        result = number ** 3
        process_id = os.getpid()
        process_name = current_process().name
        print(f'Process ID {process_id}, Process NAME {process_name}')
        print(f'The number {number} cube to {result}')

if __name__ == '__main__':
    # Генерируем список чисел
    numbers = [i for i in range(11)]
    
    # инициализирум список для процессов
    processes = []

    # для каждого числа в списке запускаем два процесса
    for number in numbers:
        # Инициализируем первый процесс и добавляем его в список процессов
        process_one = Process(target=square, args=(numbers,))
        processes.append(process_one)

        # Инициализируем второй процесс и добавляем его в список процессов
        process_two = Process(target=cube, args=(numbers,))
        processes.append(process_two)

        # Запускаем первый процесс
        process_one.start()

        # Запускаем второй процесс
        process_two.start()



