#Find a string

len_string = len(string)
len_subString = len(sub_string)
count = 0
for i in range(len_string):
  if string[i:len_subString+i] == sub_string:
    count = count+1
    return count

#using list comprehension
def count_substring(string, sub_string):
  count = [i for i in range(len(string)) if string[i:len(sub_string)+i]==sub_string]
  return len(count
