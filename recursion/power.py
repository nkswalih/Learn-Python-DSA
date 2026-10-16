"""
recursion/power.py  —  Part 7 problem (LeetCode 50)

Compute base^exp with fast (binary) exponentiation.

    x^n = x^(n/2) * x^(n/2)            if n is even
    x^n = x * x^(n/2) * x^(n/2)        if n is odd

Halving the exponent each step gives O(log n) instead of O(n).
"""


def power(base, exp):
    if exp < 0:
        return 1 / power(base, -exp)       # negative exponent -> reciprocal
    if exp == 0:
        return 1                           # base case
    half = power(base, exp // 2)
    if exp % 2 == 0:
        return half * half
    return base * half * half


if __name__ == "__main__":
    print("2^10  :", power(2, 10))     # 1024
    print("3^0   :", power(3, 0))      # 1
    print("2^-2  :", power(2, -2))     # 0.25
    print("5^13  :", power(5, 13))     # 1220703125
