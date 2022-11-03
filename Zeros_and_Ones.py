# the input is in the form of string i.e '3 3 3' so i just had to split it and convert it into interger
# for that i used map function
import numpy as np

arr  = list(map(int, input().split()))
ones = np.ones(arr,dtype= int)
zeros = np.zeros(arr, dtype = int)
print(zeros)
print(ones)
