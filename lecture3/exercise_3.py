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
def do_twice(fun):
    fun()
    fun()

def do_fourth(fun):
    do_twice(fun)
    do_twice(fun)

def print_beam():
    print("+ " + "- "*4, end = '')

def print_block():
    print("/ " + "  "*4, end = '')

def print_line():
    do_twice(print_beam)
    print("+")

def print_block_line():
    do_twice(print_block)
    print("/")

def print_half_grid():
    print_line()
    do_fourth(print_block_line)

def grid():
    do_twice(print_half_grid)
    print_line()

grid()
