"""
arrays/array_utils.py  —  Part 2

Manual array (list) operations written by hand, plus a few reusable helpers.
Everything here runs in O(n) or better unless noted.
"""

import bisect


# ---------------------------------------------------------
#  Core manual operations
# ---------------------------------------------------------

def insert_at(lst, index, value):
    """Insert value at index, shifting later items right. O(n)."""
    lst.append(None)
    for i in range(len(lst) - 1, index, -1):
        lst[i] = lst[i - 1]
    lst[index] = value
    return lst


def delete_at(lst, index):
    """Remove the item at index, shifting later items left. O(n)."""
    for i in range(index, len(lst) - 1):
        lst[i] = lst[i + 1]
    lst.pop()
    return lst


def search(lst, target):
    """Index of target, or -1. O(n)."""
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1


def reverse_in_place(lst):
    """Reverse with two pointers. O(n) time, O(1) space."""
    i, j = 0, len(lst) - 1
    while i < j:
        lst[i], lst[j] = lst[j], lst[i]
        i += 1
        j -= 1
    return lst


# ---------------------------------------------------------
#  Extra helpers
# ---------------------------------------------------------

def find_max_min(lst):
    """Return (max, min) in one pass. O(n)."""
    if not lst:
        raise ValueError("empty list")
    biggest = smallest = lst[0]
    for x in lst[1:]:
        if x > biggest:
            biggest = x
        if x < smallest:
            smallest = x
    return biggest, smallest


def count_occurrences(lst, target):
    """Count how many times target appears. O(n)."""
    count = 0
    for x in lst:
        if x == target:
            count += 1
    return count


def is_palindrome(lst):
    """True if the list reads the same both ways. O(n)."""
    i, j = 0, len(lst) - 1
    while i < j:
        if lst[i] != lst[j]:
            return False
        i += 1
        j -= 1
    return True


def insert_sorted(lst, value):
    """Insert into an already-sorted list, keeping it sorted.
    O(log n) to find the spot, O(n) to shift."""
    bisect.insort(lst, value)
    return lst


def dedupe_preserve_order(lst):
    """Remove duplicates while keeping first-seen order. O(n)."""
    seen = set()
    out = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out


def rotate_right(lst, k):
    """Rotate the list right by k steps, in place, using reversal. O(n)."""
    n = len(lst)
    if n == 0:
        return lst
    k %= n
    _reverse_range(lst, 0, n - 1)      # 1) reverse the whole list
    _reverse_range(lst, 0, k - 1)      # 2) reverse the first k
    _reverse_range(lst, k, n - 1)      # 3) reverse the rest
    return lst


def _reverse_range(lst, lo, hi):
    """Reverse lst[lo..hi] in place."""
    while lo < hi:
        lst[lo], lst[hi] = lst[hi], lst[lo]
        lo += 1
        hi -= 1


if __name__ == "__main__":
    nums = [10, 20, 30, 40]
    print("insert 15 @ 1 :", insert_at(nums[:], 1, 15))
    print("delete @ 2    :", delete_at(nums[:], 2))
    print("search 30     :", search(nums, 30))
    print("reverse       :", reverse_in_place(nums[:]))
    print("max/min       :", find_max_min([3, 1, 9, 4]))
    print("count 20      :", count_occurrences([1, 2, 2, 3, 2], 2))
    print("palindrome    :", is_palindrome([1, 2, 3, 2, 1]))
    print("insert sorted :", insert_sorted([1, 3, 5, 7], 4))
    print("dedupe order  :", dedupe_preserve_order([3, 1, 3, 2, 1]))
    print("rotate right 2:", rotate_right([1, 2, 3, 4, 5], 2))
