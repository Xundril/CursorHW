# Task 1
# Напишіть калькулятор в якого будуть реалізовані операції додавання, віднімання, множення, ділення, піднесення в степінь,
# взяття з під кореня, пошук відсотку від числа
#
# Огорніть в конструкцію try... except... потенційно "небезпечні" місця, наприклад отримання числа і приведення до типу даних
# або інструкції математичних операцій
#
# заповніть ваш скрипт логами
# Логи здебільшого інформаційні (викликали таку функцію з такими аргументами)
# + логи з помилками
# причому логи повинні записуватись у файл, тому що в консолі ви будете взаємодіяти з калькулятором,
# лог файл завжди відкриваєтсья в режимі дозапису.
# так як ви працюєте з файлом не забудьте про те що це потенційне місце поломки

import logging

log_template = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, filename='hw9.log', filemode='a', format=log_template)


logging.info('!Start!')
print('!Calculator V 1.0!')
print('Percentage: first value - %, second value - number!')
while True:
    str_a = input('First value: ')
    try:
        a = int(str_a)
    except ValueError:
        print('a - invalid value')
        continue
    logging.info(f'Entered first value {a}')
    str_b = input('Second value: ')
    try:
        b = int(str_b)
    except ValueError:
        print('b - invalid value')
        continue
    logging.info(f'Entered second value {b}')
    method = ["+", "-", "*", "/", "sqrt", "%", "**"]
    action = input('Value actions: (+, -, *, /, sqrt, %, **): ')
    while action not in method:
        print(f'No method {action} found!')
        action = input('Value actions: (+, -, *, /, sqrt, %, **): ')
    logging.info('Checked action')

    def calc():
        if action == "+":
            return a + b
        elif action == "-":
            return a - b
        elif action == "**":
            return a ** b
        elif action == "*":
            return a * b
        elif action == "/":
            try:
                c = a / b
                logging.info(f'division is finished, {a}, {b}')
                return c
            except ZeroDivisionError:
                print('Second value: 0, ZeroDivisionError')
                logging.error('Divide by zero')
                return 0
        elif action == "sqrt":
            return pow(a, .5)
        else:
            return a * b / 100
    logging.info(f'Choosed action {action}')
    c = calc()
    logging.info('Called function calc')
    print(f'Result: {c}')
    logging.info(f'Printed result: {c}')
    logging.info('!End!')
    break

# Task 2
# Напишіть клас робота пилососа
# в ініт приймається заряд батареї, заповненість сміттєбака і кількість води
#
# реалізуйте функцію move() - нескінченний цикл який на кожній ітерації "замерзає" на 1 сек
# окрім цього на кожній ітерації викликаються функції "wash" і "vacuum cleaner"
# (в цих функціях повинні стояти прніти "wash" і "vacuum cleaner" відповідно),
# також на кожній ітерації прінтиться "move"
# + на кожній ітерації цикла заряд батареї і кількість води зменшується на певну кількість
# (задайте в статік аргументах класу як конфіг пилососа, або в окремому конфіг файлі),
# а кількість сміття збільшується
#
# Напишіть власні ексепшини які кидаються коли заряд батареї менше ніж 20%, заряд батареї 0%, кількість води - 0, кількість сміття більша ніж певне число
# опрацюйте ваші ексепшини (наприклад якщо заряд батареї менше 20% то цикл робить ще певну кількість ітерацій і зупиняється,
# якщо вода закінчилась то пилосос тепер не миє підлогу а тільки пилососить,
# 0 відсотків заряду - пилосос кричить щоб його занесли на зарядку бо сам доїхати не може)
#
# можете придумати ще свої ексепшини і як їх опрацьовувати

from time import sleep

class Low_Battery(Exception):
    pass

class Empty_Battery(Exception):
    pass

class Lack_of_Water(Exception):
    pass

class Cell(Exception):
    pass

class Robot_Cleaner:
    battery_discharge = 5
    water_consumption = 10
    filling_the_cell = 10

    def __init__(self):
        self.battery_charge = 100
        self.garbage_cell = 0
        self.amount_of_water = 100

    def move(self):
        print('Loading...')
        while True:
            sleep(1)
            try:
                print(f'Vacuum cleaner moves \n'
                      f'battery charge - {self.battery_charge} % \n')
                self.battery_charge -= self.battery_discharge
                if self.battery_charge <= 20:
                    if self.battery_charge == 0:
                        raise Empty_Battery
                    raise Low_Battery
            except Low_Battery:
                print(f'!Warning! Low battery - {self.battery_charge} % \n'
                      '!!!Need charging!!! \n')
            except Empty_Battery:
                print(f'Battery is discharged!')
                break

            try:
                print('Vacuum cleaner working')
                self.vacuum_cleaner()
                if self.garbage_cell == 100:
                    raise Cell
            except Cell:
                print('Garbage cell is full')
                input('Press "Enter" to clean cell... ')
                print()
                self.garbage_cell = 0

            try:
                if self.amount_of_water > 0:
                    print('Vacuum cleaner washes')
                    self.wash()
                else:
                    raise Lack_of_Water
            except Lack_of_Water:
                print('!Warning! Run out of water \n')

    def wash(self):
        self.amount_of_water -= self.water_consumption
        print(f'Water level - {self.amount_of_water} % \n')

    def vacuum_cleaner(self):
        self.garbage_cell += self.filling_the_cell
        print(f'Garbage level  - {self.garbage_cell} % \n')


robot = Robot_Cleaner()
robot.move()

# Output:

# Loading...
# Vacuum cleaner moves
# battery charge - 100 %
#
# Vacuum cleaner working
# Garbage level  - 10 %
#
# Vacuum cleaner washes
# Water level - 90 %
#
# Vacuum cleaner moves
# battery charge - 95 %
#
# Vacuum cleaner working
# Garbage level  - 20 %
#
# Vacuum cleaner washes
# Water level - 80 %
#
# Vacuum cleaner moves
# battery charge - 90 %
#
# Vacuum cleaner working
# Garbage level  - 30 %
#
# Vacuum cleaner washes
# Water level - 70 %
#
# Vacuum cleaner moves
# battery charge - 85 %
#
# Vacuum cleaner working
# Garbage level  - 40 %
#
# Vacuum cleaner washes
# Water level - 60 %
#
# Vacuum cleaner moves
# battery charge - 80 %
#
# Vacuum cleaner working
# Garbage level  - 50 %
#
# Vacuum cleaner washes
# Water level - 50 %
#
# Vacuum cleaner moves
# battery charge - 75 %
#
# Vacuum cleaner working
# Garbage level  - 60 %
#
# Vacuum cleaner washes
# Water level - 40 %
#
# Vacuum cleaner moves
# battery charge - 70 %
#
# Vacuum cleaner working
# Garbage level  - 70 %
#
# Vacuum cleaner washes
# Water level - 30 %
#
# Vacuum cleaner moves
# battery charge - 65 %
#
# Vacuum cleaner working
# Garbage level  - 80 %
#
# Vacuum cleaner washes
# Water level - 20 %
#
# Vacuum cleaner moves
# battery charge - 60 %
#
# Vacuum cleaner working
# Garbage level  - 90 %
#
# Vacuum cleaner washes
# Water level - 10 %
#
# Vacuum cleaner moves
# battery charge - 55 %
#
# Vacuum cleaner working
# Garbage level  - 100 %
#
# Garbage cell is full
# Press "Enter" to clean cell...
#
# Vacuum cleaner washes
# Water level - 0 %
#
# Vacuum cleaner moves
# battery charge - 50 %
#
# Vacuum cleaner working
# Garbage level  - 10 %
#
# !Warning! Run out of water
#
# Vacuum cleaner moves
# battery charge - 45 %
#
# Vacuum cleaner working
# Garbage level  - 20 %
#
# !Warning! Run out of water
#
# Vacuum cleaner moves
# battery charge - 40 %
#
# Vacuum cleaner working
# Garbage level  - 30 %
#
# !Warning! Run out of water
#
# Vacuum cleaner moves
# battery charge - 35 %
#
# Vacuum cleaner working
# Garbage level  - 40 %
#
# !Warning! Run out of water
#
# Vacuum cleaner moves
# battery charge - 30 %
#
# Vacuum cleaner working
# Garbage level  - 50 %
#
# !Warning! Run out of water
#
# Vacuum cleaner moves
# battery charge - 25 %
#
# !Warning! Low battery - 20 %
# !!!Need charging!!!
#
# Vacuum cleaner working
# Garbage level  - 60 %
#
# !Warning! Run out of water
#
# Vacuum cleaner moves
# battery charge - 20 %
#
# !Warning! Low battery - 15 %
# !!!Need charging!!!
#
# Vacuum cleaner working
# Garbage level  - 70 %
#
# !Warning! Run out of water
#
# Vacuum cleaner moves
# battery charge - 15 %
#
# !Warning! Low battery - 10 %
# !!!Need charging!!!
#
# Vacuum cleaner working
# Garbage level  - 80 %
#
# !Warning! Run out of water
#
# Vacuum cleaner moves
# battery charge - 10 %
#
# !Warning! Low battery - 5 %
# !!!Need charging!!!
#
# Vacuum cleaner working
# Garbage level  - 90 %
#
# !Warning! Run out of water
#
# Vacuum cleaner moves
# battery charge - 5 %
#
# Battery is discharged!