"""
basics/compare_append_insert.py  —  Part 1 task

Compare list.append() (add at the end) with list.insert(0, x) (add at the front).

Expected result:
    append  is O(n) overall   -> grows roughly linearly
    insert(0) is O(n^2)       -> every insert shifts the whole list right

Run it, then try doubling N and watch how each column changes.
"""

import time

N = 120_000          # keep this modest so it runs quickly


def time_append(n):
    lst = []
    start = time.perf_counter()
    for i in range(n):
        lst.append(i)                # O(1) each -> O(n) total
    return time.perf_counter() - start


def time_insert_front(n):
    lst = []
    start = time.perf_counter()
    for i in range(n):
        lst.insert(0, i)             # O(n) each -> O(n^2) total
    return time.perf_counter() - start


if __name__ == "__main__":
    t_append = time_append(N)
    t_insert = time_insert_front(N)

    print(f"n = {N:,}")
    print(f"append(i)     : {t_append:.5f}s   (O(n) total)")
    print(f"insert(0, i)  : {t_insert:.5f}s   (O(n^2) total)")
    print(f"insert is about {t_insert / t_append:,.0f}x slower")
    print()
    print("Try changing N to 40,000: append ~doubles, insert ~quadruples.")
