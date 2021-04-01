import unittest

from HW10_Practice_Task_1 import Robot_Cleaner


class TestRobotCleaner(unittest.TestCase):

    def setUp(self) -> None:
        self.robot = Robot_Cleaner(100, 0, 100)
        self.robot_1 = Robot_Cleaner('30', 0, 80)
        self.robot_2 = Robot_Cleaner(60, -10, 50.0)
        self.vacuum_cleaners = [self.robot, self.robot_1, self.robot_2]

    def test_init(self):
        with self.assertRaises(ValueError):
            Robot_Cleaner('a', 0, 50)

        for item in self.vacuum_cleaners:
            self.assertIsInstance(item.battery_charge, int)
            self.assertIsInstance(item.garbage_cell, int)
            self.assertIsInstance(item.amount_of_water, int)

    def test_move(self):
        self.assertNotEqual(Robot_Cleaner.battery_discharge, 0)
        self.values_1 = Robot_Cleaner(0, 100, 0)
        self.values_1.move()
        self.values_2 = Robot_Cleaner(100, 0, 100)
        self.values_2.clean_time = 2
        self.values_2.move()

    def test_wash(self):
        self.assertNotEqual(Robot_Cleaner.water_consumption, 0)

    def test_vacuum_cleaner(self):
        self.assertNotEqual(Robot_Cleaner.filling_the_cell, 20)

    def tearDown(self) -> None:
        print('Test Crashed - tearDown')