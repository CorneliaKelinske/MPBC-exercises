'''
truncate("Super cool", 2) # "Truncation must be at least 3 characters."
truncate("Super cool", 1) # "Truncation must be at least 3 characters."
truncate("Super cool", 0) # "Truncation must be at least 3 characters."
truncate("Hello World", 6) # "Hel..."
truncate("Problem solving is the best!", 10) # "Problem..."
truncate("Another test", 12) # "Another t..."
truncate("Woah", 4) # "W..."
truncate("Woah", 3) # "..."
truncate("Yo",100) # "Yo"
truncate("Holy guacamole!", 152) # "Holy guacamole!"
'''

def truncate(string, number):
    if number < 3:
        return "Truncation must be at least 3 characters."
    if len(string) < number:
        return string
    return string[:number-3] +"..."

print(truncate("super cool", 2))
print(truncate("Super cool", 1))
print(truncate("Super cool", 0)) 
print(truncate("Hello World", 6))
print(truncate("Problem solving is the best!", 10))
print(truncate("Another test", 12))
print(truncate("Woah", 4))
print(truncate("Woah", 3))
print(truncate("Holy guacamole!", 152))

#Bootcamp solution
def truncate_BC(string, n):
    if (n < 3):
        return "Truncation must be at least 3 characters."
    if (n > len(string) + 2):
        return string
 
    return string[:n - 3] + "..."
