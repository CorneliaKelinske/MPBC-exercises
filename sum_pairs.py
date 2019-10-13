def sum_pairs(numbers, sum):
    for n1 in numbers:
        for n2 in numbers:
            if n1 + n2 == sum:
                return [n1, n2]
    return []

print(sum_pairs([11,20,4,2,1,5], 100))