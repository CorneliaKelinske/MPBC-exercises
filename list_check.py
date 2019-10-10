def list_check(input):
    if all(type(i) == list for i in input ):
        return True
    return False

print(list_check([[],[1],[2,3]])) 