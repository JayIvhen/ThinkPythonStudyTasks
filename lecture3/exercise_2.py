#!usr/bin/python3

""" Exercise 2

Exercise 2. Lecture link: http://greenteapress.com/thinkpython2/html/thinkpython2004.html

A function object is a value you can assign to a variable or pass as an argument. For example, do_twice is a function that takes a function object as an argument and calls it twice:

def do_twice(f):
    f()
    f()

Here’s an example that uses do_twice to call a function named print_spam twice.

def print_spam():
    print('spam')

do_twice(print_spam)

    Type this example into a script and test it.
    Modify do_twice so that it takes two arguments, a function object and a value, and calls the function twice, passing the value as an argument.
    Copy the definition of print_twice from earlier in this chapter to your script.
    Use the modified version of do_twice to call print_twice twice, passing 'spam' as an argument.
    Define a new function called do_four that takes a function object and a value and calls the function four times, passing the value as a parameter. There should be only two statements in the body of this function, not four.

Solution: http://thinkpython2.com/code/do_four.py.

"""

def do_twice(fun, arg):
    fun(arg)
    fun(arg)

def print_twice(bruce):
    print(bruce)
    print(bruce)

def do_four(fun, arg):
    do_twice(fun, arg)
    do_twice(fun, arg)


do_twice(print_twice, "spam")
do_four(print, "four")
