'''
def add(a,b):
    return a+b

oneAddition = once(add)

oneAddition(2,2) # 4
oneAddition(2,2) # None
oneAddition(12,200) # None
'''

def once(input_function):
  
  def wrapper(*args, **kwargs):
   
    return input_function(*args, **kwargs)
  return wrapper
  

def add(a, b):
    return a+b

oneAddition = once(add)
print(oneAddition(2,2))
print(oneAddition(2,3))