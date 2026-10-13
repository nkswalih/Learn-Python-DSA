"""
recursion/factorial.py  —  Part 7

Factorial, both recursive and iterative.
Recursive version: O(n) time, O(n) space (call stack depth).
Iterative version: O(n) time, O(1) space.
"""


def factorial_recursive(n):
    if n <= 1:                          # base case
        return 1
    return n * factorial_recursive(n - 1)   # n × (n-1)!


def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    print("recursive 5! :", factorial_recursive(5))   # 120
    print("iterative 5! :", factorial_iterative(5))   # 120
    print("recursive 0! :", factorial_recursive(0))   # 1
