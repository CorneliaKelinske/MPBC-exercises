'''
find_the_duplicate([1,2,1,4,3,12]) # 1
find_the_duplicate([6,1,9,5,3,4,9]) # 9
find_the_duplicate([2,1,3,4]) # None
'''

def find_the_duplicate(input_list):
    no_duplicates = []
    result = []
    for item in input_list:
        if item not in no_duplicates:
            no_duplicates.append(item)            
        else:
            result.append(item)
        
    if result:        
        return result[0]
    return None

print(find_the_duplicate([1,2,1,4,3,12]))
print(find_the_duplicate([6,1,9,5,3,4,9]))
print(find_the_duplicate([2,1,3,4]))