#!usr/bin/python
# Nested sum

"""
Write a function called nested_sum that takes a list of lists of integers and adds up the elements from all of the nested lists. For example:

>>> t = [[1, 2], [3], [4, 5, 6]]
>>> nested_sum(t)
21

"""

def nested_sum(A):
    accumulator = 0
    for item in A:
        if type(item) == list:
            for item_2 in item:
                accumulator += item_2
        else:
            accumulator += item
    return accumulator


def test(fun):
    print(fun.__name__)
    A = [[1, 2], [3], [4, 5, 6]]
    sum_ = fun(A)
    print("TEST#1: ", end = "")
    print("OK" if sum_ == 21 else "Fail")

    A = [[1, 2], [], [4, 5, 6]]
    sum_ = fun(A)
    print("TEST#2: ", end = "")
    print("OK" if sum_ == 18 else "Fail")

    A = [[0, 2], [3], [4, 5, 6]]
    sum_ = fun(A)
    print("TEST#3: ", end = "")
    print("OK" if sum_ == 20 else "Fail")

    A = [1, [0, 2], [3], [4, 5, 6]]
    sum_ = fun(A)
    print("TEST#4: ", end = "")
    print("OK" if sum_ == 21 else "Fail")


if __name__ == "__main__":
    test(nested_sum)

