from functools import wraps

# 1. double_result
# This decorator function should return the result of another function multiplied by two


def double_result(func):
    @wraps(func)
    def inner(a, b):
        return func(a, b) * 2
    return inner


def add(a, b):
    return a + b


print(f'Add function = {add(5, 5)}')

# Output: Add function = 10

@double_result
def add(a, b):
    return a + b


print(f'Add function with multiplied by two  = {add(5, 5)}')

# Output: Add function with multiplied by two = 20

# 2. only_odd_parameters
# This decorator function should only allow a function to have odd numbers as parameters,
# otherwise return the string "Please use only odd numbers!"

def only_odd_parameters(func):
    @wraps(func)
    def inner(*args, **kwargs):
        for i in args:
            if i % 2 == 0:
                return print('Please use only odd numbers!')
        return func(*args, **kwargs)

    return inner


@only_odd_parameters
def add(a, b):
    return print(f'Add function = {a + b}')


add(5, 5)  # 10
add(4, 4)  # 'Please use only odd numbers!'

# Output:
# Add function = 10
# Please use only odd numbers!


@only_odd_parameters
def multiply(a, b, c, d, e):
    return print(f'Multiply function =  {a * b * c * d * e}')


multiply(9, 7, 5, 3, 1)
multiply(2, 6, 4, 8, 5)  # 'Please use only odd numbers!'

# Output:
# Multiply function =  945
# Please use only odd numbers!

# 3.* logged
# Write a decorator which wraps functions to log function arguments and the return value on each call.
# Provide support for both positional and named arguments (your wrapper function should take both *args
# and **kwargs and print them both):


def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(f"you called {func.__name__}({args}, {kwargs})")
        print(f"it returned {func(*args, **kwargs)}")
        return func(*args, **kwargs)

    return with_logging


@logged
def func(*args, **kwargs):
    return 3 + len(args) + len(kwargs)


print(func(4, 4, 4))
# you called func((4, 4, 4), {})
# it returned 6

# Output:6

print(func(5, 6, 7, x=10, y=-3))

# you called func((5, 6, 7), {'x': 10, 'y': -3})
# it returned 8

# Output: 8

# 4. type_check
# you should be able to pass 1 argument to decorator - type.
# decorator should check if the input to the function is correct based on type.
# If it is wrong, it should print(f"Wrong Type: {type}"), otherwise function should be executed.


def type_check(correct_type):
      def decorator(func):
        def inner(arg):
            if isinstance(arg, correct_type):
                return func(arg)
            else:
                print(f"Wrong type: {type(arg).__name__}")
        return inner
      return decorator


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
times2('Not A Number')  # "Wrong Type: string" should be printed, since non-int passed to decorated function

# Output:
# Wrong type: str
# H

@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
first_letter(['Not', 'A', 'String'])  # "Wrong Type: list" should be printed, since non-str passed to decorated function

# Output:
# Wrong type: list