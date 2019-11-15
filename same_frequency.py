from collections import Counter

def same_frequency(num1, num2):
    
    if Counter(str(num1)) == Counter(str(num2)):
        return True
    return False


print(same_frequency(321142,3212215))
