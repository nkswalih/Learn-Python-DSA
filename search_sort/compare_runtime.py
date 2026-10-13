"""
search_sort/compare_runtime.py  —  Part 5 task

Time the three manual sorts against Python's built-in sorted().
Watch how the O(n^2) sorts blow up as n grows, while sorted() stays fast.
"""

import random
import time

from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort


def time_it(fn, data):
    copy = data[:]                       # work on a copy each time
    start = time.perf_counter()
    fn(copy)
    return time.perf_counter() - start


def run(n):
    data = [random.randint(0, 10_000) for _ in range(n)]
    print(f"\n--- sorting {n:,} random numbers ---")
    for name, fn in [
        ("bubble", bubble_sort),
        ("selection", selection_sort),
        ("insertion", insertion_sort),
        ("built-in", sorted),
    ]:
        seconds = time_it(fn, data)
        print(f"  {name:>10}: {seconds:.5f}s")


if __name__ == "__main__":
    run(500)
    run(1000)
    run(2000)
    print()
    print("Notice: doubling n makes the manual sorts ~4x slower (O(n^2)),")
    print("while sorted() barely changes (O(n log n)).")
