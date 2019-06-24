from functools import wraps

# my solution including unnecessary list comprehension
def ensure_fewer_than_three_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        args_list = [arg for arg in args]
        if len(args_list) >= 3:
            raise ValueError ("Too many arguments!")
        return fn (*args, **kwargs)
    return wrapper

@ensure_fewer_than_three_args
def add_all(*nums):
    return sum(nums)

print(add_all(2, 4))

print(add_all(4, 5, 8, 9))

# more elegant Boot Camp solution:

def ensure_fewer_than_three_args_BC(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if len(args) < 3:
            return fn(*args, **kwargs)
        return "Too many arguments!"
    return wrapper

