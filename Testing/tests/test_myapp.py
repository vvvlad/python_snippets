from Testing.src.myapp import MyApp


# In order to test use: python -m pytest .

class TestMyApp(object):

    def test_me(self):
        MyApp("name")
