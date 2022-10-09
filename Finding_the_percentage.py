if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
value = student_marks[query_name]
length_ofValue = len(value)
# sum_value = sum(value) 

avg_marks = sum(value)/length_ofValue
print('%.2f' % avg_marks)


# print('{:.2}'.format(avg_marks))
#when i used format it is given output like
Your Output (stdout)
5.6e+01  #i dont understand y it is giving output like this 
