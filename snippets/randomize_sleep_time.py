import time
import random

time.sleep(float(format(random.uniform(0.01, 0.05), '.2f')))

def func1(**kwargs):
    k = kwargs
    print(type(k))
    func3(kwargs)
    # func2(my_param="test2", **k)

def func3(test_kwargs):
    print(type(test_kwargs))
    print(test_kwargs)
    if test_kwargs:
        print("not null")

def func2(my_param:str = None, **kwargs):
    print(my_param)
    print(kwargs)

if __name__ == "__main__":
    # func1(my_param = "test", my_param_2 = "alsotest")
    func1()

    # lst = list()
    # lst.append("test")
    # lst[0] += " me"
    # print(lst)
    # print(lst[0])