
def vowel_count(string):
    vowels = {"a":0, "e":0, "i":0, "o":0, "u":0}
    string = string.lower()
    for letter in string:
        if letter == "a":
            vowels["a"] += 1
        elif letter == "e":
            vowels["e"] +=1
        elif letter == "i":
            vowels["i"] +=1
        elif letter == "o":
            vowels["o"] +=1
        elif letter == ["u"]:
            vowels["u"] += 1
    
    return {key:value for (key,value) in vowels.items() if vowels[key] != 0}


print(vowel_count('Colt'))