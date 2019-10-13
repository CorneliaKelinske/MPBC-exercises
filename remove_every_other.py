def remove_every_other(list):
    return list[::2]

print(remove_every_other([1]))

#The bootcamp solution using the enumerate() function
#def remove_every_other(lst):
    #return [val for i,val in enumerate(lst) if i % 2 == 0]