#i just used my whole damn brain to get output with list comprehension,slicing,formulas 
#but the answer lies in the question (they used text wrap module
----------------here the code--------------------(right one)
import textwrap

def wrap(string, max_width):
  return textwrap.fill(string,max_width)


----------this is the code for which i have used my idiotic brain-------------------(X)

def wrap(string, max_width):
  jj =[string[i*max_width:(i+1)*max_width] for i in range(7)]  
  for j in jj:
    return j
