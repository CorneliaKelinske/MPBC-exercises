# def firstn(n):
#     num = 0
#     while num < n:
#         yield num
#         num += 1

  
# sum_of_first_n = sum(firstn(3))
# print(sum_of_first_n)
'''
primes = next_prime()
[next(primes) for i in range(25)]
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
'''
def is_prime(number):
    divisors = []
    for num in range(1,number+1):
        if number % num == 0:
            divisors.append(num)            
    if len(divisors) != 2:
        return False
    
    return True


def next_prime(n):
    num = 0
    while num <= n:
        if is_prime(num):
            yield num
            num += 1


#print(is_prime(10))
primes = next_prime(25)
