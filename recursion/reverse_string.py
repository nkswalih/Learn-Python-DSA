"""
recursion/reverse_string.py  —  Part 7

Reverse a string using recursion.
Idea: reverse of s == reverse(s without first char) + first char.
"""


def reverse_string(s):
    if len(s) <= 1:                     # base case
        return s
    return reverse_string(s[1:]) + s[0]


if __name__ == "__main__":
    print(reverse_string("hello"))       # olleh
    print(reverse_string("a"))           # a
    print(reverse_string(""))            # (empty)
