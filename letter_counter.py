'''
counter = letter_counter('Amazing')
counter('a') # 2
counter('m') # 1

counter2 = letter_counter('This Is Really Fun!')
counter2('i') # 2
counter2('t') # 1 
'''

def letter_counter(input_string):

    def inner_counter(letter):
        
        count = 0
        letter = letter.lower()
               
        for char in input_string.lower():
            if char == letter:
                count += 1
        return count
    return inner_counter


counter = letter_counter('Amazing')
print(counter('A'))
print(counter('m'))

counter2 = letter_counter('This Is Really Fun!')
print(counter2('i'))
print(counter2('t'))