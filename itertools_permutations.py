# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
n ,m = input().split()
m = int(m)
permu = list(permutations(n,m))
for i in sorted(permu):
    print(''.join(i))
