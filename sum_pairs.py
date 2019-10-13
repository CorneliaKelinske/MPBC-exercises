def sum_pairs(numbers, sum):
    for n1 in numbers:
        for n2 in numbers:
            if n1 + n2 == sum:
                return [n1, n2]
    return []

print(sum_pairs([11,20,4,2,1,5], 100))


#the bootcamp solution; here, there is no problem with duplicate numbers like in my code
def sum_two(ints, s):
    already_visited = set()
    for i in ints:
        difference = s - i
        if difference in already_visited:
            return [difference, i]
        already_visited.add(i)
    return []