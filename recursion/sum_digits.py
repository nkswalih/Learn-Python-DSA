"""
recursion/sum_digits.py  —  Part 7 problem

Add all the digits of a number, recursively.

    sum_digits(1234) = 4 + sum_digits(123) = ... = 10

O(d) time where d = number of digits.
"""


def sum_digits(n):
    n = abs(n)
    if n < 10:
        return n                       # base case: single digit
    return (n % 10) + sum_digits(n // 10)   # last digit + rest


def digital_root(n):
    """Keep summing digits until one digit remains."""
    while n >= 10:
        n = sum_digits(n)
    return n


if __name__ == "__main__":
    print("sum_digits(1234) :", sum_digits(1234))    # 10
    print("sum_digits(999)  :", sum_digits(999))     # 27
    print("digital_root(999):", digital_root(999))   # 9
