from functools import wraps
from time import sleep

def delay(time):
       def inner(fn):
           
           print ("Waiting {} before running {}".format(time, fn.__name__))
           sleep(time)
           @wraps(fn)
           def wrapper(*args, **kwargs):
               return fn(*args, **kwargs)
           return wrapper
       return inner

@delay(3)
def say_hi():
    return "hi"

print(say_hi())
