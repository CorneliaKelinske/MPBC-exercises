'''
nth(['a', 'b', 'c', 'd'], 1)  # 'b' 
nth(['a', 'b', 'c', 'd'], -2) #  'c'
nth(['a', 'b', 'c', 'd'], 0)  # 'a'
nth(['a', 'b', 'c', 'd'], -4) #  'a'
nth(['a', 'b', 'c', 'd'], -1) #  'd'
nth(['a', 'b', 'c', 'd'], 3)  # 'd'
'''

def nth(list, num):
    if num < 0:
        return list[len(list) + num]
    return list[num]

print(nth(['a', 'b', 'c', 'd'], -1))

def nth_BC(arr, idx):
    if idx >= 0:
        return arr[idx]
    return arr[idx + len(arr)]

