from collections import Counter

def same_frequency(num1, num2):
    
    if Counter(str(num1)) == Counter(str(num2)):
        return True
    return False


print(same_frequency(321142,3212215))

def same_frequency_BC(num1,num2):
    d1 = {letter:str(num1).count(letter) for letter in str(num1)}
    d2 = {letter:str(num2).count(letter) for letter in str(num2)}
  
    for key,val in d1.items():
        if not key in d2.keys():
            return False
        elif d2[key] != d1[key]:
            return False
    return True