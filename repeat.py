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

#The Bootcamp solution:
def repeat_BC(string, num):
    if (num == 0):
        return ''
    i = 0
    newStr = ''
    while (i < num):
        newStr += string
        i += 1
    return newStr