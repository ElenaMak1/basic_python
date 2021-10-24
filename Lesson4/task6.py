#from itertools import count, cycle
#import sys

#def integer_generator(start_from):
#    for el in count(start_from):
#        if el > start_from+10:
#            break
#        yield el

#for el in integer_generator(int(input('Введите стартовое число '))):
#        print(el)


iterable = "ABC"
c = 0

from itertools import cycle
for el in cycle("ABCDEF"):
    if el == iterable[0]:
        c += 1
    if c < 10:
        print(el)
    else:
        break



