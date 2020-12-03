print("Hello world")


class a():
    def __init__(self):
        print('a')

    def aa(self):
        print('aa')


class b():
    def __init__(self):
        print('b')


class lola(b, a):
    print('lola')


lol = lola()
