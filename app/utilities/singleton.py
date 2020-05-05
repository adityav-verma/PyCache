from functools import wraps


def singleton(_class):
    """Makes a class Singleton"""
    _instances = {}

    @wraps(_class)
    def wrapper(*args, **kwargs):
        if _class not in _instances:
            _instances[_class] = _class(*args, **kwargs)
        return _instances[_class]
    return wrapper
