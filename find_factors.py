def find_factors(num):
    return [i for i in range(1, num+1) if num%i == 0]

print(find_factors(321421))


#The Bootcamp solution:
def find_factors_BC(num):
    factors = []
    i = 1
    while(i <= num):
        if (num % i == 0):
            factors.append(i)
        i += 1
    return factors