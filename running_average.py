'''
rAvg = running_average()
rAvg(10) # 10.0
rAvg(11) # 10.5
rAvg(12) # 11

rAvg2 = running_average()
rAvg2(1) # 1
rAvg2(3) # 2
'''

# def running_average(n1):
#     numbers = 0
#     def inner_function():
        
#         numbers.append(n2)
#         print(numbers)
#         return round((n1 + n2) / len(numbers), 2)
#     return inner_function

# rAvg = running_average(1)
# print(rAvg(2))

def running_average():
    numbers = []
    
    def get_average(num):
        numbers.append(num)
        #print(numbers)
        return round((sum(numbers) / len(numbers)), 2)
    return get_average

rAvg = running_average()
print(rAvg(10))
print(rAvg(11))
print(rAvg(12))

rAvg2 = running_average()
print(rAvg2(1)) # 1
print(rAvg2(3)) # 2
