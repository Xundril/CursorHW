"""
1. Write the method that return the number of threads currently in execution.
Also prepare the method that will be executed with threads and run during the first method counting.
"""
from threading import Thread
import time
import random


def function(delay):
    time.sleep(delay)


if __name__ == '__main__':
    threads = [Thread(target=function, daemon=True, args=(random.randint(5, 10),))for _ in range(10)]
    for thread in threads:
        thread.start()

    while any([t.is_alive() for t in threads]):
        print(f'{[t.is_alive() for t in threads].count(True)} active threads')
        time.sleep(1)
    print('All threads completed')

# Output:

# 10 active threads
# 10 active threads
# 10 active threads
# 10 active threads
# 10 active threads
# 6 active threads
# 6 active threads
# 6 active threads
# 4 active threads
# 2 active threads
# All threads completed

"""
2. Print current date by using 2 threads.
# 1. Define a subclass using Thread class.
# 2. Instantiate the subclass and trigger the thread.
"""
from threading import Thread
import datetime


class CurrentDateClass(Thread):
    def run(self) -> None:
        print(f"{self.name}. Date is {datetime.date.today()}")


thread_1 = CurrentDateClass()
thread_2 = CurrentDateClass()

thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()

# Output:

# Thread-1. Date is 2021-04-14
# Thread-2. Date is 2021-04-14

"""
3. Use Pool.apply() to get the row wise common items in list_a and list_b.
"""
from multiprocessing import Pool


def common_items():
    list_a = [[1, 2, 3], [5, 6, 7, 8], [10, 11, 12], [20, 21]]
    list_b = [[2, 3, 4, 5], [6, 9, 10], [11, 12, 13, 14], [21, 24, 25]]
    return [set(a).intersection(b) for a, b in zip(list_a, list_b)]


if __name__ == '__main__':
    with Pool() as pool:
        print(pool.apply(common_items))

# Output:

# [{2, 3}, {6}, {11, 12}, {21}]

"""
4. Divide the work between 2 methods: print_cube that returns the cube of number
and print_square that returns the square of number. These two methods should be executed by using 2 different processes.
"""
from multiprocessing import current_process, Process


def print_cube(n):
    print(f'Cube of {n} is {n ** 3}, Done by {current_process().name}')
    return n ** 3


def print_square(n):
    print(f'Square of {n} is {n ** 2},Done by {current_process().name}')
    return n ** 2


if __name__ == '__main__':
    i = int(input("Value: "))
    process1 = Process(target=print_cube, args=(i,))
    process2 = Process(target=print_square, args=(i,))
    process1.start()
    process2.start()
    process1.join()
    process2.join()

# Output:

# Value: 7
# Cube of 7 is 343, Done by Process-1
# Square of 7 is 49,Done by Process-2