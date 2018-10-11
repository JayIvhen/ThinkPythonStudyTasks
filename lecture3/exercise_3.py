#!usr/bin/python

"""Execise 3

Exercise 3  chapter link: http://greenteapress.com/thinkpython2/html/thinkpython2004.html

Note: This exercise should be done using only the statements and other features we have learned so far.

    Write a function that draws a grid like the following:

    + - - - - + - - - - +
    |         |         |
    |         |         |
    |         |         |
    |         |         |
    + - - - - + - - - - +
    |         |         |
    |         |         |
    |         |         |
    |         |         |
    + - - - - + - - - - +

    Hint: to print more than one value on a line, you can print a comma-separated sequence of values:

    print('+', '-')

    By default, print advances to the next line, but you can override that behavior and put a space at the end, like this:

    print('+', end=' ')
    print('-')

    The output of these statements is '+ -' on the same line. The output from the next print statement would begin on the next line.
    Write a function that draws a similar grid with four rows and four columns.

Solution: http://thinkpython2.com/code/grid.py. Credit: This exercise is based on an exercise in Oualline, Practical C Programming, Third Edition, O’Reilly Media, 1997.

"""
def print_line_type1():
    print("+", "- "*4 + "+", "- "*4 +  "+")

def print_line_type2():
    print(("/" + "  "*4 + " ")*2 + "/")

def grid():
    print_line_type1()
    print_line_type2()
    print_line_type2()
    print_line_type2()
    print_line_type2()
    print_line_type1()
    print_line_type2()
    print_line_type2()
    print_line_type2()
    print_line_type2()
    print_line_type1()

grid()





