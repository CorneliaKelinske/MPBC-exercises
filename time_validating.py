import re

def is_valid_time(input):
    time_regex = re.compile(r'^\d{1,2}:\d{2}$')
    match = time_regex.search(input)
    if match:
        return True
    return False

print(is_valid_time("10:45"))
print(is_valid_time("2:33"))
print(is_valid_time("123:45"))
print(is_valid_time("it is 12:34"))