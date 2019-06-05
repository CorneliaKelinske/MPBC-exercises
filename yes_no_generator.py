'''
gen = yes_or_no()
next(gen) # 'yes'
next(gen) # 'no'
next(gen) # 'yes'
next(gen) # 'no'
'''
#my less elegant solution:
def yes_or_no():
   results = ["yes", "no"]
   for result in results:
       yield result
       results.append(result)
#the Boot Camp solution:
def yes_or_no_elegant():
    answer = "yes"
    while True:
        yield answer
        answer = "no" if answer == "yes" else "yes"