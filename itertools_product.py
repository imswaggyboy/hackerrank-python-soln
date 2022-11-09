#lets just import the module 
from itertools import product
#map the input string into integer and split it with ","
a = map(int, input().split())
# print(a)
b = map(int, input().split())
# print(b)
now i want the output in the string format so im going to map the product into string and by using ' '.join() lets join it with space
print(' '.join(map(str,(product(a, b)))))
