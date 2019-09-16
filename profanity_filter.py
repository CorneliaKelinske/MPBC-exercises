import re

def censor(text):
    profanity = re.compile(r'(frack)([a-z]+)?', re.I)
    result = profanity.sub("CENSORED", text)
    return result

print (censor("I fracking hate you"))
print (censor("FRACK"))


#bootcamp solution:
#import re
 
#def censor(input):
    #pattern = re.compile(r'\bfrack\w*\b', re.IGNORECASE)
    #return pattern.sub("CENSORED", input)