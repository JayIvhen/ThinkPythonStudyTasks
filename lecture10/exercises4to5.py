#!usr/bin/python3
# Exercise 4-5

"""
Exercise 4  

Write a function called chop that takes a list, modifies it by removing the first and last elements, and returns None. For example:

>>> t = [1, 2, 3, 4]
>>> chop(t)
>>> t
[2, 3]

Exercise 5   Write a function called is_sorted that takes a list as a parameter and returns True if the list is sorted in ascending order and False otherwise. For example:

>>> is_sorted([1, 2, 2])
True
>>> is_sorted(['b', 'a'])
False

"""

def ex_4(A):
    del(A[0])
    del(A[-1])
    return A

def ex_5(A):
    N = len(A)
    flag = True
    for index in range (1, N):
        if A[index] < A[index - 1]:
            flag = False
            break
    return flag



