# first created empty list ,second i iterate it and coverted using condition and then i appended the satisfied conditioned i  
# then converted back to string using join()
def swap_case(s):
  lst = []
  for i in s:
    if i == i.lower():
      lst.append(i.upper())
    else: lst.append(i.lower())
  conver = ''.join(lst)
  return conver
