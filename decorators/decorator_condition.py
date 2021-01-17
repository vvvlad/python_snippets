
import functools
is_local = True

class localRun():
    def run(self, f, *args, **kwargs):
        print(f"in local run")
        f(*args, **kwargs)
        return f"local run done"

class remoteRun():
    def run(self, f, *args, **kwargs):
        print(f"in remote run")
        f(*args, **kwargs)
        return f"remote run done"

class decoratorWithArguments(object):

    # if decorated function is not None that means that the following equivalent of call happened:
    # result = decoratorWithArguments(sayHi)("a1", "a2", "a3", "a4")
    # else it means that we got args before the function, like this:
    # result = decoratorWithArguments(arg1=5)(sayHi)("a1", "a2", "a3", "a4")

    def __new__(cls, decorated_function=None, **kwargs):

        self = super().__new__(cls)
        self._init(**kwargs)
        print(f"kwargs are: ", kwargs)

        if not decorated_function:
            return self
        else:
            return self.__call__(decorated_function)

    def _init(self, arg1=[], arg2=[], arg3=[]):
        """

        """
        print ("Inside __init__()")
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        

    def __call__(self, f):
        """

        """
        print ("Inside __call__()")
        @functools.wraps(f)
        def wrapped_f(*args, **kwargs):
            print ("Inside wrapped_f()")
            print ("Decorator arguments:", self.arg1, self.arg2, self.arg3)
            run = localRun() if is_local else remoteRun()
            return run.run(f, *args, **kwargs)
            # f(*args, **kwargs)

        return wrapped_f

# If the decorator is used with arguments, than this equals:
# result = decoratorWithArguments(arg1=5)(sayHello)(a1, a2, a3, a4)
# But if the decorator is used without arguments, than this equals:
# result = decoratorWithArguments(sayHello)(a1, a2, a3, a4)

# def sayHi(a1, a2, a3, a4):
#     print ('sayHello arguments:', a1, a2, a3, a4)

# result = decoratorWithArguments(arg1=5)(sayHi)("a1", "a2", "a3", "a4")
# result = decoratorWithArguments(sayHi)("a1", "a2", "a3", "a4")


@decoratorWithArguments()
def noargs(a1, a2, a3, a4):
    print("no args")

noargs("say", "hello", "argument", "list")

@decoratorWithArguments(arg1 = "arg1", arg2="arg2", arg3="arg3")
def sayHello(a1, a2, a3, a4):
    print ('sayHello arguments:', a1, a2, a3, a4)

print(f"start execution")
first = sayHello("say", "hello", "argument", "list")
print(first)
is_local = False
print(f"second execution")
second = sayHello("again", "say", "hello","")

print(noargs.__name__)
print(sayHello.__name__)