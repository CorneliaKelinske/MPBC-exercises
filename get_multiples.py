def get_multiples(num = 1, count = 10):
    b = 1
    while count > 0:
        yield num * b
        count -= 1
        b += 1

test = get_multiples(1,10)
print(next(test))
print(next(test))
print(next(test))

#And here is the bootcamp solution:
def get_multiples_bc(num=1, count=10):
    next_num = num
    while count > 0:
        yield next_num
        count -= 1
        next_num += num


