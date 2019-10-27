'''
repeat('*', 3) # '***' 
repeat('abc', 2) # 'abcabc' 
repeat('abc', 0) # ''
'''

def repeat(string, number):
    if number > 0:
        return(str(string*number))
    
    return ""
    

print(repeat('abc', 5))