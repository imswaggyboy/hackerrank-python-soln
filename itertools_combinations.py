# Enter your code here. Read input from STDIN. Print output to STDOUT
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
