Q1.Introduction to Sets

def average(array):
#   use set() to convert list into set
  set_of_list = set(lst)
  # print(set_of_list)
#   take the sum of set using sum() func and get the len of set using len() and use the avg formula i.e sum of the set divided by total element in the set (len of set)
  avg = sum(set_of_list)/len(set_of_list)
#   then round it to 3 so that we get precision 3 and return it 
  return round(avg,3)
________________________________________________________________________________________________________________________________________________________________          
Q2.symmetric_difference()

solu1 :
  
# i dont know why i am taking the size of each set but i have to take it
size_of_a = int(input())
#lets split the input and use map() to convert it into integer and at outside i put set to get the 'a' in set
a = set(map(int,input().split()))
size_of_b = int(input())
b = set(map(int,input().split()))
#creating empty set so that we update or add the element 
c={}
# used difference method so that i put different element from the b 
c = a.difference(b)
# here i am going to update the difference element of b from a 
c.update(b.difference(a))
# as set is unordered so we have to sort it and we cannot use .sort() method as it is only for list so  we are going to sorted() function to sort c
sort_c = sorted(c)
# iterate it through c and print the i 
for i in sort_c:
  print(i)
Solu2:
  
size_of_a = int(input())
a = set(map(int,input().split()))
size_of_b = int(input())
b = set(map(int,input().split()))
# We can also find symmetric difference from two sets using ‘^’ operator in Python.
c = a^b
print(c)
# now iterate thought c and print i
for i in c:
  print(i)
________________________________________________________________________________________________________________________________________________________________          
