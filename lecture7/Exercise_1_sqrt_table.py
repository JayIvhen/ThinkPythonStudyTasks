#!usr/bin/python3

"""
Exercise 1  http://greenteapress.com/thinkpython2/html/thinkpython2008.html

Copy the loop from Section 7.5 and encapsulate it in a function called mysqrt that takes a as a parameter, chooses a reasonable value of x, and returns an estimate of the square root of a.

To test it, write a function named test_square_root that prints a table like this:

a   mysqrt(a)     math.sqrt(a)  diff
-   ---------     ------------  ----
1.0 1.0           1.0           0.0
2.0 1.41421356237 1.41421356237 2.22044604925e-16
3.0 1.73205080757 1.73205080757 0.0
4.0 2.0           2.0           0.0
5.0 2.2360679775  2.2360679775  0.0
6.0 2.44948974278 2.44948974278 0.0
7.0 2.64575131106 2.64575131106 0.0
8.0 2.82842712475 2.82842712475 4.4408920985e-16
9.0 3.0           3.0           0.0

The first column is a number, a; the second column is the square root of a computed with mysqrt; the third column is the square root computed by math.sqrt; the fourth column is the absolute value of the difference between the two estimates. 


"""

import math

def my_sqrt(n):
    x = n - 0.5
    sigma = 0.1**10
    y = (x + n/x) / 2
    while x != y:
        x = y
        y = (x + n/x) / 2
        if abs(y-x) < sigma:
            return x
    return x

def sqrt_table(n):
    name = "a"
    len_name = len(str(float(n)))
    name_filler = ''.join('-' for i in range(len(name)))

    fun_1 = "my_sqrt(a)"
    len_fun_1 = 13
    fun_1_filler = ''.join('-' for i in range(len(fun_1)))

    fun_2 = "math.sqrt(a)"
    len_fun_2 = 13
    fun_2_filler = ''.join('-' for i in range(len(fun_2)))

    diff = "diff"
    diff_filler = ''.join('-' for i in range(len(diff)))

    print("{:<{}s} {:<{}s} {:<{}s} {:<s}".format(
        name, len_name, fun_1, len_fun_1, fun_2, len_fun_2, diff))
    print("{:<{}} {:<{}} {:<{}} {:<}".format(
        name_filler, len_name, fun_1_filler, len_fun_1,
        fun_2_filler, len_fun_2, diff_filler))
    for i in range(1, n+1):
        print("{:<{}.1f} {:<{}.11g} {:<.11g} {:<g}".format(
            i, len_name, my_sqrt(i), len_fun_1, math.sqrt(i), my_sqrt(i) - math.sqrt(i)))







