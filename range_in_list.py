def range_in_list(input_list, start=0, *args):
    if args:
        result_list = [item for item in range (input_list[start], input_list[args])]
    else:
        result_list = [item for item in range (input_list[start], len(input_list)+1)]

    return result_list

print(range_in_list([1,2,3]))