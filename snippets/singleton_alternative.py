# as mentioned in various places, implementation of singleton is less pythonic and more leftover from languages like java

# more pythonic way is to have a simple factory and global var:

class MyManager():
    pass

_manager_instance = None

def get_manager():
    global _manager_instance
    if _manager_instance is None:
        _manager_instance = MyManager()
    return _manager_instance

