'''
three_odd_numbers([1,2,3,4,5]) # True
three_odd_numbers([0,-2,4,1,9,12,4,1,0]) # True
three_odd_numbers([5,2,1]) # False
three_odd_numbers([1,2,3,3,2]) # False
'''

def three_odd_numbers(numbers):
    while len(numbers) > 3:
        while sum(numbers[:3]) % 2 == 0:            
            del numbers[0]
        if sum(numbers[:3]) % 2 != 0 and len(numbers) >= 3:        
            return True
    return False

print(three_odd_numbers([1,2,3,3,2]))