# tutorial
# https://medium.com/better-programming/python-decorators-5-advanced-features-to-know-17dd9be7517b


# import time
# from time import sleep

# Example of basic decorator without args

# def logging_time(func):
#     """Decorator that logs time"""
#     def logger():
#         """Function that logs time"""
#         start = time.time()
#         func()
#         print(f"Calling {func.__name__}: {time.time() - start:.5f}")

#     return logger

# @ logging_time
# def calculate_sum():
#     sleep(1)
#     return sum(range(10000))

# calculate_sum()

# Example of a decorator with args

# def logging_time(func):
#     """Decorator that logs time"""
#     def logger(*args, **kwargs):
#         """Function that logs time"""
#         start = time.time()
#         func(*args, **kwargs)
#         print(f"Calling {func.__name__}: {time.time() - start:.5f}")

#     return logger


# @ logging_time
# def calculate_sum_n(n):
#     return sum(range(n))

# @ logging_time
# def say_hi(whom, greeting="Hello"):
#     print(f"{greeting}, {whom}!")

# calculate_sum_n(100000)
# say_hi("John", greeting="Hi")

# Example with wrap that preserves docstrings and get argument

import time
from functools import wraps

def logging_time(unit):
    """Decorator that logs time"""
    def logger(func):
        @wraps(func)
        def inner_logger(*args, **kwargs):
            """Function that logs time"""
            start = time.time()
            func(*args, **kwargs)
            scaling = 1000 if unit == "ms" else 1
            print(f"Calling {func.__name__}: {(time.time() - start) * scaling:.5f} {unit}")

        return inner_logger

    return logger


@logging_time("ms")
def calculate_sum_ms(n):
    """Calculate sum of 0 to n-1"""
    return sum(range(n))

calculate_sum_ms(100000)

@logging_time("s")
def calculate_sum_s(n):
    """Calculate sum of 0 to n-1"""
    return sum(range(n))


calculate_sum_s(100000)
