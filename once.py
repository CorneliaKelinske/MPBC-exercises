'''
def add(a,b):
    return a+b

oneAddition = once(add)

oneAddition(2,2) # 4
oneAddition(2,2) # None
oneAddition(12,200) # None
'''


# def once(fn):
#     fn.is_called = False
#     def inner(*args):
#         if not(fn.is_called):
#             fn.is_called = True
#             return fn(*args)
#     return inner

def once(fn):
 count = []
 def inner(*args):
    if len(count) == 0:
      count.append(1)
      return fn(*args)
 return inner

def add(a,b):
  return a + b

oneAddition = once(add)
print(oneAddition(2,2))
print(oneAddition(2,3))