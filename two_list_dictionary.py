def two_list_dictionary(list_1, list_2):
    return dict(zip(list_1, list_2))

print(two_list_dictionary([1, 2, 3, 4], ["A", "B", "C"]))