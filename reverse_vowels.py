'''
reverse_vowels("Hello!") # "Holle!" 
reverse_vowels("Tomatoes") # "Temotaos" 
reverse_vowels("Reverse Vowels In A String") # "RivArsI Vewols en e Streng"
reverse_vowels("aeiou") # "uoiea"
reverse_vowels("why try, shy fly?") # "why try, shy fly?"
'''

def reverse_vowels(input_str):
    input_str =list(input_str)
    vowels = [item for item in input_str if item in ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]]
    reversed_vowels = []
    result = ""
    for item in input_str:
        if item not in ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]:
            reversed_vowels.append(item)
        else:
            reversed_vowels.append(vowels.pop())
    return result.join(reversed_vowels)


print(reverse_vowels("why try, shy fly?"))