'''
find_greater_numbers([1,2,3]) # 3 
find_greater_numbers([6,1,2,7]) # 4
find_greater_numbers([5,4,3,2,1]) # 0
find_greater_numbers([]) # 0
'''

def find_greater_numbers(numbers):
    count = 0
   
    for num in numbers:
        i = 1
        #print("doing the loop")
        #print(f"index is {i}")
        while numbers.index(num) + i <= len(numbers) - 1:
            if num < numbers[numbers.index(num)+ i]:
                i +=1
                count += 1
                #print(f"the count is {count}")
                #print(f"the number is {num}")

    return count

print(find_greater_numbers([6,1,2,7]))