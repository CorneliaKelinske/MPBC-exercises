'''
min_max_key_in_dictionary({2:'a', 7:'b', 1:'c',10:'d',4:'e'}) # [1,10]
min_max_key_in_dictionary({1: "Elie", 4:"Matt", 2: "Tim"}) # [1,4]
'''

def min_max_key_in_dictionary(dictionary):
    keys = [key for key in dictionary]
    max_key = max(keys)
    min_key = min(keys)
    return [min_key, max_key]
 
print(min_max_key_in_dictionary({1: "Elie", 4:"Matt", 2: "Tim"}))


def min_max_key_in_dictionary_PB(d):
    keys = d.keys()
    return [min(keys), max(keys)]