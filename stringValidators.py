# Definition and Usage (built-in function)
# The any() function returns True if any item in an iterable are true, otherwise it returns False.

# If the iterable object is empty, the any() function will return False.

if __name__ == '__main__':
    s = input()
    
    print(any([i.isalnum() for i in s]))
    print(any([i.isalpha() for i in s]))
    print(any([i.isdigit() for i in s]))
    print(any([i.islower() for i in s]))
    print(any([i.isupper() for i in s]))
