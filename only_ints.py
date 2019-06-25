from functools import wraps

def only_ints(fn):
    @wraps(fn)
    def wrapper (*args, **kwargs):
        if any ([arg for arg in args if type(arg) != int]):
            return "Please only invoke with integers."          
        return fn(*args, *kwargs)
    return wrapper

@only_ints
def add(x, y):
    return x + y

print(add(1, 3.5))
