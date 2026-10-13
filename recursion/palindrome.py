"""
recursion/palindrome.py  —  Part 7

Check if a string is a palindrome using recursion:
compare the two ends, then recurse on the inside.
"""


def is_palindrome(s):
    if len(s) <= 1:                     # base case: 0 or 1 char is a palindrome
        return True
    if s[0] != s[-1]:                   # ends differ -> not a palindrome
        return False
    return is_palindrome(s[1:-1])       # check the inside


if __name__ == "__main__":
    print(is_palindrome("racecar"))     # True
    print(is_palindrome("hello"))       # False
    print(is_palindrome("abba"))        # True
    print(is_palindrome(""))            # True
