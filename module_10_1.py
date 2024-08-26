import time
from time import sleep
from threading import Thread

time_start = time.time()


def wite_words(word_count, file_name):
    with open(file_name, "a") as f:
        for i in range(word_count):
            f.write(f'Какое-то слово № {i + 1}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')

time_end = time.time()
print(f'Работа потоков {time_end - time_start} секунд')
print()

time_start = time.time()


def wite_words(word_count, file_name):
    with open(file_name, "a") as f:
        for i in range(word_count):
            f.write(f'Какое-то слово № {i}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


thr_first = Thread(target=wite_words, args=(10, 'example5.txt'))
thr_second = Thread(target=wite_words, args=(30, 'example6.txt'))
thr_third = Thread(target=wite_words, args=(200, 'example7.txt'))
thr_fourth = Thread(target=wite_words, args=(100, 'example8.txt'))

thr_first.start()
thr_second.start()
thr_third.start()
thr_fourth.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_third.join()

time_end = time.time()
print(f'Работа потоков {time_end - time_start} секунд')
