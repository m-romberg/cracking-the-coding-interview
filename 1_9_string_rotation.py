"""
Assume you have mthod is_substring which checks if a string is one word is a
substring of the other.

Given two strings, s1 and s2, write code to check if s2 is rotation of s1 using
only one call to is_substring
"""

def is_rotation(s1, s2):
    """
    Returns if s2 is rotation of s1

    >>> is_rotation("waterbottle", "erbottlewat")
    True

    >>> is_rotation("waterbottle", "bttloeawetr")
    False

    >>> is_rotation("waterbottle", "waterbottl")
    False
    """
    #quick check
    if len(s1) != len(s2): return False

    return s1 in (s2+s2)