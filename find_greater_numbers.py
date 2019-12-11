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


def find_greater_numbers_BC(arr):
    count = 0
    i = 0
    j = 1
    while i < len(arr):
        while j < len(arr):
            if arr[j] > arr[i]:
                count += 1
            j+=1
        j = i+1
        i+=1
    return count;