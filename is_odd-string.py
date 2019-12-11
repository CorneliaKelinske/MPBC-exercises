'''
is_odd_string('a') # True
is_odd_string('aaaa') # False
is_odd_string('amazing') # True
is_odd_string('veryfun') # True
is_odd_string('veryfunny') # False
'''

def is_odd_string(string):
    if sum([(ord(letter) -96) for letter in string.lower()]) % 2 == 0:
        return False
    return True

print(is_odd_string('aaaa'))

def is_odd_string_BC(string):
    total = sum((ord(c) - 96) for c in string.lower()) or 0
    return total % 2 == 1


