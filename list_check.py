def list_check(input):
    if all(type(i) == list for i in input ):
        return True
    return False

print(list_check([[],[1],[2,3]])) 

#shortened version, same idea:
#def list_check(vals):
    #return all(type(l) == list for l in vals)
