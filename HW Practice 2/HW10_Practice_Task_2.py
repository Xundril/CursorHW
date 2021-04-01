import uuid


class NameError(Exception):
    pass


class EmailError(Exception):
    pass


class EmailLengthError(Exception):
    pass


class UserAlreadyExist(Exception):
    pass


class PasswordError(Exception):
    pass


class RepeatPasswordError(Exception):
    pass


class PasswordLengthError(Exception):
    pass


class AuthorizationError(Exception):
    pass


class UserToken:
    def __init__(self):
        self.__id = uuid.uuid4()

    def __str__(self):
        return self.__id


class Registration:
    user_database = {}
    user_token = UserToken()

    unacceptable_symbols = [',', ':', ';', '!', '?', '/', '|', '#', '$', '%', '^', '&', '*', '-', '+', '=', '(', ')', '{', '}', '[', ']', '<', '>', '`', '~', '_', '"']

    def registration(self, name: str, email: str, password: str):

        if self.check_name(name) is False:
            raise NameError("Invalid name")

        if self.check_email(email) is False:
            raise EmailError("Invalid email")

        if self.check_email_length(email) is False:
            raise EmailLengthError("Email max length validation is incorrect")

        if email in self.user_database.keys():
            raise UserAlreadyExist("This email is already used")

        if self.check_password(password) is False:
            raise PasswordError("Invalid password")

        if self.check_password_length(password) is False:
            raise PasswordLengthError("Invalid password size")

        else:
            self.user_database.update({email: password})
        print(self.user_database)
        return 200

    def authorization(self, email: str, password: str):
        if email in self.user_database and password in self.user_database.values():
            return self.user_token
        else:
            raise AuthorizationError("Invalid login or password")

    def check_name(self, name):
        for i in name:
            if i in self.unacceptable_symbols:
                return False

    def check_email(self, email):
        for i in email:
            if i in self.unacceptable_symbols:
                return False

    def check_email_length(self, email):
        if 12 <= len(email) <= 30:
            return True
        else:
            return False

    def check_password(self, password):
        for i in password:
            if i in self.unacceptable_symbols:
                return False

    def check_password_length(self, password):
        if 8 <= len(password) <= 12:
            return True
        else:
            return False


user = Registration()
user.registration("Mikhail", "Mikhail@gmail.com", "qwerty12345")