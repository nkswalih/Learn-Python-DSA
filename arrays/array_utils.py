"""
arrays/array_utils.py  —  Part 2

Manual array (list) operations, written by hand so you can see the shifting
that Python's built-ins do for you. Reusable helpers for later chapters.
"""


def insert_at(lst, index, value):
    """Insert value at the given index, shifting later items right. O(n)."""
    lst.append(None)                           # make room at the end
    for i in range(len(lst) - 1, index, -1):   # shift right, from the back
        lst[i] = lst[i - 1]
    lst[index] = value
    return lst


def delete_at(lst, index):
    """Remove the item at the given index, shifting later items left. O(n)."""
    for i in range(index, len(lst) - 1):       # shift left, from the front
        lst[i] = lst[i + 1]
    lst.pop()                                  # drop the duplicate tail
    return lst


def search(lst, target):
    """Return the index of target, or -1 if absent. O(n)."""
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1


def reverse_in_place(lst):
    """Reverse using two pointers. O(n) time, O(1) extra space."""
    i, j = 0, len(lst) - 1
    while i < j:
        lst[i], lst[j] = lst[j], lst[i]
        i += 1
        j -= 1
    return lst


def count_occurrences(lst, target):
    """Count how many times target appears. O(n), single pass."""
    count = 0
    for x in lst:
        if x == target:
            count += 1
    return count


def is_palindrome(lst):
    """True if the list reads the same forwards and backwards. O(n)."""
    i, j = 0, len(lst) - 1
    while i < j:
        if lst[i] != lst[j]:
            return False
        i += 1
        j -= 1
    return True


if __name__ == "__main__":
    nums = [10, 20, 30, 40]

    print("start            :", nums)
    print("insert 15 @ 1    :", insert_at(nums[:], 1, 15))
    print("delete @ 2       :", delete_at(nums[:], 2))
    print("search 30        :", search(nums, 30))
    print("reverse in place :", reverse_in_place(nums[:]))
    print("count of 20      :", count_occurrences([1, 2, 2, 3, 2], 2))
    print("is palindrome    :", is_palindrome([1, 2, 3, 2, 1]))
