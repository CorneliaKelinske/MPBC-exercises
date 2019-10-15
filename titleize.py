def titleize(title):
    result =""
    title = [word[0].upper() + word[1 : len(word)] for word in title.split()]
    
    for item in title:
        result = result +" " + item 
        result = result.strip()

    return result

print(titleize("this is awesome"))