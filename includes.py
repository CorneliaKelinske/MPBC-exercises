def includes(col, val, *args):
    if type(col) == dict:        
        if val in col.values():
            return True
        return False
    if args:          
        if val in col[args[0] : len(col)]:            
            return True
        return False
    if val in col:
        return True
    return False

print(includes([1, 2, 3], 1)) # True 
print(includes([1, 2, 3], 1, 2 )) # False 
print(includes({ 'a': 1, 'b': 2 }, 1)) # True 
print(includes({ 'a': 1, 'b': 2 }, 'a')) # False
print(includes('abcd', 'b')) # True
print(includes('abcd', 'e')) # False