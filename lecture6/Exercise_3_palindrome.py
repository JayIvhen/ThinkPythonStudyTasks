#!usr/bin/python3

"""

Exercise 3 http://greenteapress.com/thinkpython2/html/thinkpython2007.html

A palindrome is a word that is spelled the same backward and forward, like “noon” and “redivider”. Recursively, a word is a palindrome if the first and last letters are the same and the middle is a palindrome.

The following are functions that take a string argument and return the first, last, and middle letters

def first(word)
    return word[0]

def last(word)
    return word[-1]

def middle(word)
    return word[1:-1]

We’ll see how they work in Chapter 8.

    Type these functions into a file named palindrome.py and test them out. What happens if you call middle with a string with two letters? One letter? What about the empty string, which is written '' and contains no letters?
    Write a function called is_palindrome that takes a string argument and returns True if it is a palindrome and False otherwise. Remember that you can use the built-in function len to check the length of a string.

Solution: http://thinkpython2.com/code/palindrome_soln.py.
"""

def is_polindrome(word):
    if len(word) % 2:
        return "word len is not odd"
    if len(word)>2:
        if word[0] == word[-1]:
            return is_polindrome(word[1:-1])
        else:
            return False
    elif len(word) == 2 and word[0]==word[1]:
        return True
    else:
        return False
