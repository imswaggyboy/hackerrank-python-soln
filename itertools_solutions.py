Q1. itertools.product()

from itertools import product
a = map(int, input().split())
# print(a)
b = map(int, input().split())
# print(b)
print(' '.join(map(str,(product(a, b)))))
_____________________________________________________________________________________________________________________
Q2. itertools.permutations()

from itertools import permutations
n ,m = input().split()
m = int(m)
permu = list(permutations(n,m))
for i in sorted(permu):
    print(''.join(i)
_____________________________________________________________________________________________________________________
Q3. itertools.combinations()
# we are going to use the combinations from itertools 
from itertools import combinations
#here we will split the input given in a single line
name, k = input().split()
#convert the k into int
k = int(k)
# im using nested for loop because i came only only come up with this 
for i in range(k):
 #so the hackerrank problem say we have to sort the name into exicographic sorted order so that's why i sorted the name first and used combinations 
    result = combinations(sorted(name) ,i+1)
    for comb in sorted(result):
 #then to print the only word without any space and tuple form i used ''.join()
        print(''.join(comb))
_____________________________________________________________________________________________________________________
Q4. itertools.combinations_with_replacement()

from itertools import combinations_with_replacement

name , k = input().split()
k = int(k)
combo_wid_repla = combinations_with_replacement(sorted(name),k)
for i in combo_wid_repla:
    print(''.join(i))
_____________________________________________________________________________________________________________________
Q5. Compress the String!

# imported the required library or module 
from itertools import groupby
# take the input from user
num_str = input()
# now we have to split the input so i used list comprehension that will append the individual value and i converted the each x in int 
split_num = [int(x) for x in num_str]
# does required sorting  as per the question but whenever we use the groupby() function we have to sort the values
#split_num.sort()
#as i dont have the key value so by default it will the element present in the list as a key
group = groupby(split_num)
# again here i used list comprehension to get the key and value and using the list comprehension it is easy to do things in single line
group_by = [(len(list(value)),key) for key,value in group]
# okay at the last iterate through the list and the element using index  and used the end=' ' so that new value does not print in next line
for i in range(len(group_by)):
  print(group_by[i],end = ' ')
 
_____________________________________________________________________________________________________________________
Q6. iterables and iterators 

# In this problem i didnt utilized the n i.e length of the list 
# written solution in two format:
# 1) where i used only combinations from itertools and normal for loop to get the count of a in the tuple
# 2) here i used combinations from itertools and list comprehension where i put the tuple which contains 'a' and returned its len

Solution 1:
          
from itertools import combinations
n = int(input())
N = input().lower()
k = int(input())
split_N = N.split()
combo = list(combinations(split_N,k))
len_combo = len(combo)
count = 0
for i in range(len_combo):
    if 'a' in combo[i]:
        count = count+1
#print(len_combo)
#print(count)
probability = round(count/len_combo,3)
print(probability)

Solution 2:
          
from itertools import combinations
# take input from user
n = int(input())
# take the string from user and convert it into lower() case i dont know it is necessary or not i just did it
N = input().lower()
# take the k value to make the combinations or to divide the string to make the combinations
k = int(input())
# splited the input(string)
split_N = N.split()
# used the combinations library or module or function to make combinations , here i used the k to make combinations
combo = list(combinations(split_N,k))
#lets get the length of the combinations we just made so that we find the probability of the 'a'
len_combo = len(combo)
# here i used the list comprehension which really comes handy to avoid multiple code so here i made a list of tuples that contains the 'a' in the each tuple 
# taken its length len() so we get the numerator
count = len([combo[i] for i in range(len_combo) if 'a' in combo[i]])
# finally lets divide it and get the probability and i used the round function to keep the precision upto 3
probability = round(count/len_combo,3)
print(probability)

_________________________________________________________________________________________________________________________
