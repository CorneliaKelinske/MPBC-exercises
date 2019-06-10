def get_unlimited_multiples(num=1):
    factor = 1
    while True:
        yield num * factor
        factor += 1


sevens = get_unlimited_multiples(7)
print([next(sevens) for i in range(15)])

#And the BC solution:

def get_unlimited_multiples_bc(num=1):
    next_num = num
    while True:
        yield next_num
        next_num += num