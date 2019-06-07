'''
kombucha_song = make_song(5, "kombucha")
next(kombucha_song) # '5 bottles of kombucha on the wall.'
next(kombucha_song) # '4 bottles of kombucha on the wall.'
next(kombucha_song) # '3 bottles of kombucha on the wall.'
next(kombucha_song) # '2 bottles of kombucha on the wall.'
next(kombucha_song) # 'Only 1 bottle of kombucha left!'
next(kombucha_song) # 'No more kombucha!'
next(kombucha_song) # StopIteration

default_song = make_song()
next(default_song) # '99 bottles of soda on the wall.'
'''
#my too long solution:
#def make_song(max = 99, beverage = "soda"):
    #count = max
    #while True:
       # if count > 1:
           # yield "{} bottles of {} on the wall".format(count, beverage)
        #elif count == 1:
           # yield "Only 1 bottle of {} left!".format(beverage)
       # count -= 1
#better one:
def make_song(verses=99, beverage="soda"):
    for num in range(verses, -1, -1):
        if num > 1:
            yield "{} bottles of {} on the wall.".format(num, beverage)
        elif num == 1:
            yield "Only 1 bottle of {} left!".format(beverage)
        else:
            yield "No more {}!".format(beverage)

coke = make_song(3, "coke")

print(next(coke))
print(next(coke))
print(next(coke))
print(next(coke))
