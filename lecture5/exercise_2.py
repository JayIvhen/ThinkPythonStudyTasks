#!usr/bin/python3

"""
Exercise 2  http://greenteapress.com/thinkpython2/html/thinkpython2006.html

Fermat’s Last Theorem says that there are no positive integers a, b, and c such that
a**n + b**n = c**n 

for any values of n greater than 2.

    Write a function named check_fermat that takes four parameters—a, b, c and n—and checks to see if Fermat’s theorem holds. If n is greater than 2 and
    an + bn = cn 

    the program should print, “Holy smokes, Fermat was wrong!” Otherwise the program should print, “No, that doesn’t work.”
    Write a function that prompts the user to input values for a, b, c and n, converts them to integers, and uses check_fermat to check whether they violate Fermat’s theorem


"""



def check_fermat(a, b, c, n):
    if n>2:
        if a**n + b**n == c**n:
            print("Holy smokes, Fermat was wrong!")
        else:
            print("No, that doesn’t work.")
    else:
        if a**n + b**n == c**n:
            print("n<=2, it works!")
        else:
            print("n<=2, bit it dont works")

def u_input():
    return eval(input())

while True:
    check_fermat(*u_input())
