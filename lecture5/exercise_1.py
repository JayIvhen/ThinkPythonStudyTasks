#!usr/bin/python

"""
Exercise 1  http://greenteapress.com/thinkpython2/html/thinkpython2006.html

The time module provides a function, also named time, that returns the current Greenwich Mean Time in “the epoch”, which is an arbitrary time used as a reference point. On UNIX systems, the epoch is 1 January 1970.

>import time
>time.time()
1437746094.5735958

Write a script that reads the current time and converts it to a time of day in hours, minutes, and seconds, plus the number of days since the epoch.


"""

import time
t = time.time

def time_from_ep():
    seconds = round(t()%60)
    minutes = t()//60%60
    hours = t()//60//60%24
    days = t()//60//60//24
    print(hours,":",minutes,":",seconds,"+",days)

time_from_ep()
