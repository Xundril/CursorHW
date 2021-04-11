import unittest
from HW10_Practice_Task_2 import *


class TestRegistration(unittest.TestCase):
    def setUp(self) -> None:
        self.user = Registration()

    def test_registration(self):
        with self.assertRaises(NameError):
            self.user.registration("M$ks", "Maks@gmail.com", "dojfr86")
        with self.assertRaises(EmailError):
            self.user.registration("John", "John_k@gmail.com", "kwjlfew7")
        with self.assertRaises(EmailLengthError):
            self.user.registration("Anna", "Annafgheegyrggg1234567890@gmail.com", "llleyu0935")
        with self.assertRaises(UserAlreadyExist):
            self.user.registration("Mike", "Mikhail@gmail.com", "qwerty12345")
        with self.assertRaises(PasswordError):
            self.user.registration("Andrii", "Andrii@gmail.com", "zxcvb_987")
        with self.assertRaises(PasswordLengthError):
            self.user.registration("Andrii", "Andrii@gmail.com", "zxcvb98787whfohf")
        self.assertEqual(self.user.registration("Mike", "Mikle@gmail.com", "qwerty123"), 200)

    def test_authorization(self):
        with self.assertRaises(AuthorizationError):
            self.user.authorization("Mikhail@gmail.com", "qwerty123")
        self.user.authorization("Mikhail@gmail.com", "qwerty12345")

    def tearDown(self) -> None:
        print('Test Crashed - tearDown')