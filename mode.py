'''
mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]) # 4
'''
def mode(numbers):
    count_dict = {}
    
    for num in numbers:
        if num not in count_dict.keys():
            count = 0
            for num2 in numbers:
                if num2 == num:
                    count +=1
        count_dict.update({num : count})
    return count_dict
    
print(mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]))