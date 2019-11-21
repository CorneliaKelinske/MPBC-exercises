def range_in_list(input_list, start=0, *args):
    if not input_list:
        return 0
    elif args and args[0] <= len(input_list):        #end = args[0]
        result_list = [item for item in range (input_list[start], input_list[args[0]]+1)]
    else:
        result_list = [item for item in range (input_list[start], len(input_list)+1)]

    return sum(result_list)

print(range_in_list([1,2,3,4],0,2)) #  6
print(range_in_list([1,2,3,4],0,3)) # 10
print(range_in_list([1,2,3,4],1)) #  9
print(range_in_list([1,2,3,4])) # 10
print(range_in_list([1,2,3,4],0,100)) # 10
print(range_in_list([],0,1)) # 0

def range_in_list_BC(lst, start=0, end=None):
    end = end or lst[-1]
    return sum(lst[start:end+1])