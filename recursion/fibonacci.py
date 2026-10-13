"""
recursion/fibonacci.py  —  Part 7

Fibonacci three ways:
  1. naive recursion  -> O(2^n)  (recomputes subproblems)
  2. memoized          -> O(n)    (remembers answers)
  3. iterative         -> O(n) time, O(1) space
"""

from functools import lru_cache


def fib_naive(n):
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


@lru_cache(maxsize=None)          # built-in memoization
def fib_memo(n):
    if n <= 1:
        return n
    return fib_memo(n - 1) + fib_memo(n - 2)


def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    print("naive     :", [fib_naive(i) for i in range(10)])
    print("memoized  :", [fib_memo(i) for i in range(10)])
    print("iterative :", [fib_iterative(i) for i in range(10)])

    # fib_naive(35) would be very slow; the other two are instant.
    print("fib_memo(50)     :", fib_memo(50))
    print("fib_iterative(50):", fib_iterative(50))
