#!usr/bin/python3

"""

Exercise 4  http://greenteapress.com/thinkpython2/html/thinkpython2007.html

A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a function called is_power that takes parameters a and b and returns True if a is a power of b. Note: you will have to think about the base case.

"""

def is_power(a ,b):
    if not a%b:
        if a/b == 1:
            return True
        else:
            return is_power(a/b, b)
    else:
        return False

print(is_power(100,5))
