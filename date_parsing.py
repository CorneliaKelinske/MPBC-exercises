import re

def parse_date(input):
    date_regex = re.compile(r'^(?P<d>(\d{2}))[,/.](?P<m>(\d{2}))[,/.](?P<y>(\d{4}))$')
    matches = date_regex.search(input)
    if matches:
        return {"d": matches.group('d'), "m" : matches.group('m'), "y" : matches.group('y')}
    return None


print (parse_date("01/12/1999"))
print (parse_date("01,12,1999"))
print (parse_date("01.12.1999"))
print (parse_date("01/12/19999"))