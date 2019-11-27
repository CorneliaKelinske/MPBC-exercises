'''
EXAMPLES:


list1 = [
  [ 1, 2 ],
  [ 3, 4 ]
]
 
sum_up_diagonals(list1) # 10

list2 = [
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
]
 
sum_up_diagonals(list2) # 30
 
list3 = [
  [ 4, 1, 0 ],
  [ -1, -1, 0],
  [ 0, 0, 9]
]

sum_up_diagonals(list3) # 11

list4 = [
  [ 1, 2, 3, 4 ],
  [ 5, 6, 7, 8 ],
  [ 9, 10, 11, 12 ],
  [ 13, 14, 15, 16 ]
]
 
sum_up_diagonals(list4) # 68
'''

def sum_up_diagonals(list_N):
    diagonal_1 = 0
    diagonal_2 = 0    
    i1 = 0
    i2 = len(list_N)-1
    diagonal_sum = 0

    while i1 <= len(list_N)-1:
      for item in list_N:                
        diagonal_1 += item[i1]
        i1 +=1
    diagonal_sum += diagonal_1
    #print(diagonal_sum)

    while i2 >= 0:
      for item in list_N:        
          diagonal_2 += item[i2]
          i2 -= 1
    diagonal_sum += diagonal_2

    return diagonal_sum


list1 = [
  [ 1, 2 ],
  [ 3, 4 ]
]
 
print(sum_up_diagonals(list1))
