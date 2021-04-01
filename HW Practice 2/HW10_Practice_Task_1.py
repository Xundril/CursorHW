from time import sleep

class Low_Battery(Exception):
    pass

class Empty_Battery(Exception):
    pass

class Lack_of_Water(Exception):
    pass

class Cell(Exception):
    pass

class StopClean(Exception):
    pass

class Robot_Cleaner:
    battery_discharge = 5
    water_consumption = 10
    filling_the_cell = 10
    clean_time = 5

    def __init__(self, battery_charge, garbage_cell, amount_of_water):
        self.battery_charge = int(battery_charge)
        self.garbage_cell = int(garbage_cell)
        self.amount_of_water = int(amount_of_water)

    def move(self):
        print('Loading...')
        while self.clean_time != 0:
            sleep(1)
            try:
                self.clean_time -= 1
                if self.clean_time == 0:
                    raise StopClean
            except StopClean:
                print('Cleaning finished')
                break
            try:
                print(f'Vacuum cleaner moves \n'
                      f'battery charge - {self.battery_charge} % \n')
                self.battery_charge -= self.battery_discharge
                if self.battery_charge <= 20:
                    if self.battery_charge == 0 or self.battery_charge < 0:
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


robot = Robot_Cleaner(100, 0, 100)
robot.move()

