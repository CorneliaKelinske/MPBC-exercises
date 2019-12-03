'''
find_greater_numbers([1,2,3]) # 3 
find_greater_numbers([6,1,2,7]) # 4
find_greater_numbers([5,4,3,2,1]) # 0
find_greater_numbers([]) # 0
'''

def find_greater_numbers(numbers):
    list_of_numbers = [numbers[numbers.index(num) : len(numbers)] for num in numbers]
    return(list_of_numbers)
 
print(find_greater_numbers([2,6,5,7]))