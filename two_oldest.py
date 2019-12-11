'''
two_oldest_ages( [1, 2, 10, 8] ) # [8, 10]
two_oldest_ages( [6,1,9,10,4] ) # [9,10]
two_oldest_ages( [4,25,3,20,19,5] ) # [20,25]
'''
def two_oldest_ages(numbers):
    sorted_numbers = sorted(numbers)
    return sorted_numbers[len(numbers)-2 : len(numbers)]

print(two_oldest_ages([6,1,9,10,4]))

def two_oldest_ages_BC(ages):
    return sorted(ages)[-2:]