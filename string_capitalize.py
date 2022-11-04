# first i splited with space then created a empty string  and iterated and applied capitalize to i 
# and append it to the empty lst then at last join the lst with space
def solve(s):
  split = s.split(" ")
  lst = []
  for i in split:
    lst.append(i.capitalize())
  final_str = ' '.join(lst)
  return final_str
