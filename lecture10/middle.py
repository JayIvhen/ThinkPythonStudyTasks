#!usr/bin/python
# midddle

"""
Exercise 3  

Write a function called middle that takes a list and returns a new list that contains all but the first and last elements. For example:

>>> t = [1, 2, 3, 4]
>>> middle(t)
[2, 3]

"""


def middle(A):
    new = A[1:-1]
    return new


def test(fun):
    A = [1, 2, 3, 4]
    A_ = fun(A)
    A_test = [2,3]
    print("OK" if A_ == A_test else "Fail")

if __name__ == "__main__":
    test(middle)
