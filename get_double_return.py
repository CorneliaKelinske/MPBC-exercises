from functools import wraps

def double_return(fn):
    @wraps(fn)
    def wrapper (*args, **kwargs):
        val = fn(*args, **kwargs)
        return [val, val]
    return wrapper
    

@double_return
def greet(name):
    return "Hi I'm " + name

print(greet("Cornelia"))