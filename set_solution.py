Q1.Introduction to Sets

def average(array):
#   use set() to convert list into set
  set_of_list = set(lst)
  # print(set_of_list)
#   take the sum of set using sum() func and get the len of set using len() and use the avg formula i.e sum of the set divided by total element in the set (len of set)
  avg = sum(set_of_list)/len(set_of_list)
#   then round it to 3 so that we get precision 3 and return it 
  return round(avg,3)
