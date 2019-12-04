'''
find_greater_numbers([1,2,3]) # 3 
find_greater_numbers([6,1,2,7]) # 4
find_greater_numbers([5,4,3,2,1]) # 0
find_greater_numbers([]) # 0
'''

def find_greater_numbers(numbers):
    count = 0
    list_of_numbers = [numbers[numbers.index(num) : len(numbers)] for num in numbers]
    for item in list_of_numbers:
        count += count_greater_numbers(item)
        
    return count
 

def count_greater_numbers(list_n):
    return len([item for item in list_n if item > list_n[0]])
    

print(find_greater_numbers([]))