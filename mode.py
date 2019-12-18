'''
mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]) # 4
'''
from collections import Counter
def mode(numbers):
    count_dict = {}
    
    for num in numbers:
        if num not in count_dict.keys():            
            count = 0
            for num2 in numbers:
                if num2 == num:
                    count +=1
            count_dict.update({num : count})
    return Counter(count_dict).most_common()[0][0]
    
print(mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]))