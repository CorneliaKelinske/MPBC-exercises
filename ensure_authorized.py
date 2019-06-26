from functools import wraps

def ensure_authorized(fn):
    @wraps(fn)
    def wrapper (*args, **kwargs):
        if "role" in kwargs:
            if kwargs["role"] == "admin":
        #if any {key : value for key, value in kwargs.items() if key == "role" and value == "admin"}:
                return fn(*args, **kwargs)
        return "Unauthorized"
    return wrapper



@ensure_authorized
def show_secrets(*args, **kwargs):
    return "Shh! Don't tell anybody!"

print(show_secrets(role="admin"))
print(show_secrets(role="nobody"))
print(show_secrets(a="b"))


#and the more elegant solution, with more expert use of dictionary:
def ensure_authorized_better(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs.get("role") == "admin":
            return fn(*args, **kwargs)
        return "Unauthorized"
    return wrapper