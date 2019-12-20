'''
rAvg = running_average()
rAvg(10) # 10.0
rAvg(11) # 10.5
rAvg(12) # 11

rAvg2 = running_average()
rAvg2(1) # 1
rAvg2(3) # 2
'''

def running_average(n1):
    
    def inner_function(n2):
        numbers = [n1]
        numbers.append(n2)
        print(numbers)
        return ((n1 + n2) / len(numbers))
    return inner_function

rAvg = running_average(1)
print(rAvg(3))
