import functools

class MyClassDecorator(object):
    num_calls = 0

    def __init__(self, arg1, arg2="default"):
        print(f"Decorator args:{arg1} {arg2}")
        self.arg1 = arg1
        self.arg2 = arg2
        
    def __call__(self, func):
        self.func = func
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            MyClassDecorator.num_calls += 1
            print(f"Call {MyClassDecorator.num_calls} of {self.func.__name__!r}")
            print(f"using arg: {self.arg1}")
            return self.func(*args, **kwargs)
        return wrapper

my_class_decorator = MyClassDecorator

@my_class_decorator("test1")
def print_args(param):
    print(f"param is {param}")

@my_class_decorator("test2")
def print_args2(param):
    print(f"param is {param}")


print_args(1)
print_args2(2)

print(f"num of calls of the decorator: {my_class_decorator.num_calls}")