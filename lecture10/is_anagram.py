#usr/bin/python3
# is anagram

"""
Exercise 6  

Two words are anagrams if you can rearrange the letters from one to spell the other. Write a function called is_anagram that takes two strings and returns True if they are anagrams. 

"""

def is_anagram(first, second):
    if len(first) != len(second):
        return False
    lookup = list(second)
    for char in first:
        try:
            lookup.remove(char)
        except ValueError:
            pass
    return False if lookup else True


print(is_anagram('wera','erwa'))      
