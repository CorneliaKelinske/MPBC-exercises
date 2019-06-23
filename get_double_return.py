from functools import wraps

def double_return(fn):
    @wraps(fn)
    def wrapper (*args, **kwargs):
        
        return [fn(*args, **kwargs), fn(*args, **kwargs)]
    return wrapper
    

@double_return
def greet(name):
    return "Hi I'm " + name

print(greet("Cole"))