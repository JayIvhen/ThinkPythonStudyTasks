#!usr/bin/python
# Comulative summ

"""
Exercise 2  

Write a function called cumsum that takes a list of numbers and returns the cumulative sum; that is, a new list where the ith element is the sum of the first i+1 elements from the original list. For example:

>>> t = [1, 2, 3]
>>> cumsum(t)
[1, 3, 6]

"""

def cumsum(A):
    N = len(A)
    new_list = [A[0]]
    for index in range(1, N):
        new_list.append(A[index] + new_list[index-1])
    return new_list


def test(fun):
    print(fun.__name__)
    A = [1, 2, 3]
    A_ = fun(A)
    print("TEST#1: ", end="")
    print("OK" if A_ == [1, 3, 6] else "Fail")

    A = [1, 0]
    A_ = fun(A)
    print("TEST#2: ", end="")
    print("OK" if A_ == [1, 1] else "Fail")


if __name__ == "__main__":
    test(cumsum)
