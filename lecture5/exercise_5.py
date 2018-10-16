#!usr/bin/python3

"""
Exercise 6 http://greenteapress.com/thinkpython2/html/thinkpython2006.html

The Koch curve is a fractal that looks something like Figure 5.2. To draw a Koch curve with length x, all you have to do is

    Draw a Koch curve with length x/3.
    Turn left 60 degrees.
    Draw a Koch curve with length x/3.
    Turn right 120 degrees.
    Draw a Koch curve with length x/3.
    Turn left 60 degrees.
    Draw a Koch curve with length x/3.

The exception is if x is less than 3: in that case, you can just draw a straight line with length x.

    Write a function called koch that takes a turtle and a length as parameters, and that uses the turtle to draw a Koch curve with the given length.
    Write a function called snowflake that draws three Koch curves to make the outline of a snowflake.

    Solution: http://thinkpython2.com/code/koch.py.
    The Koch curve can be generalized in several ways. See http://en.wikipedia.org/wiki/Koch_snowflake for examples and implement your favorite.

"""

import turtle

def koch(turt, length):
    if length < 10:
        turt.fd(length)
        return
    koch(turt, length/3)
    turt.lt(60)
    koch(turt, length/3)
    turt.right(120)
    koch(turt, length/3)
    turt.lt(60)
    koch(turt, length/3)

def koch_snowflake(turt, length):
    for i in range(3):
        koch(turt, length)
        turt.rt(120)

bob = turtle.Turtle()
bob.speed(0)
koch_snowflake(bob, 100)
    
