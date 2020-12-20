import functools

####################################
# most basic decorator
####################################

def say1(func):
    def wrapper():
        print("before func")
        func()
        print("after func")
    return wrapper

@say1
def dec1():
    print("decorated function")

# dec1()

####################################
# decorated function with arguments
####################################

def say2(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper

@say2
def dec2(name="Liya"):
    print(f"decorated function with arg {name}")

# dec2("Vlad")
# dec2()

####################################
# decorated function with return value
####################################


def say3(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@say3
def dec3(name="Liya"):
    return f"Return value is {name}"

# print(dec3("Vlad"))
# print(dec3())

####################################
# decorator with generic arguments
####################################

def repeat(*args_, **kwargs_):

    def inner_function(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(args_[0]):
                func(*args, **kwargs)
        return wrapper

    return inner_function

@repeat(2)
def dec4(name="Liya"):
    print(f"Name is {name}")

# dec4()

####################################
# decorator with named arguments
####################################
def repeat2(reps=3, param2=5, param3=6):

    def inner_function(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(reps):
                func(*args, **kwargs)
        return wrapper

    return inner_function

@repeat2(param2=7)
def dec5(name="Liya"):
    print(f"Name is {name}")

dec5()