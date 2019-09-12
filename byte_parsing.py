import re

def parse_bytes(input):
    byte_regex = re.compile(r'\b[0,1]{8}\b')
    return byte_regex.findall(input)

print (parse_bytes("11011010 101 323"))
print (parse_bytes("my data is 10101011 11111100"))
print (parse_bytes("asd"))