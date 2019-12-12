'''
valid_parentheses("()") # True 
valid_parentheses(")(()))") # False 
valid_parentheses("(") # False 
valid_parentheses("(())((()())())") # True 
valid_parentheses('))((') # False
valid_parentheses('())(') # False
valid_parentheses('()()()()())()(') # False
'''

def valid_parentheses(parens):    
    while "()" in parens:
        parens = parens.replace("()", "")
        
    if parens:
        return False
    return True

print(valid_parentheses('())('))