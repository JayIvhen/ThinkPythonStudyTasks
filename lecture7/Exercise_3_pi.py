"""
Exercise 3  http://greenteapress.com/thinkpython2/html/thinkpython2008.html

The mathematician Srinivasa Ramanujan found an infinite series that can be used to generate a numerical approximation of 1 / π:
1
π
	 = 	
2	√	
2
9801
	  	
∞
∑
k=0
	 	
(4k)!(1103+26390k)
(k!)4 3964k
	 

Write a function called estimate_pi that uses this formula to compute and return an estimate of π. It should use a while loop to compute terms of the summation until the last term is smaller than 1e-15 (which is Python notation for 10−15). You can check the result by comparing it to math.pi.

Solution: http://thinkpython2.com/code/pi.py.

"""

import math

def pi_Srinivasa():
    """
    This function computes 1/pi
    """
    first_part =  math.sqrt(2)*2 / 9801
    second_part = 0
    n = 0
    total = 0
    term = 1
    while term > 10**-15:
        num = math.factorial(4*n) * (1103 + 26390*n)
        den = math.factorial(n)**4 * 396**(4*n)
        term = first_part * num / den
        n += 1
        total += term
    return 1/total
