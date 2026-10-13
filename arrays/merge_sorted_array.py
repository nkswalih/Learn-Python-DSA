"""
arrays/merge_sorted_array.py  —  Part 2 task (LeetCode 88)

Merge two already-sorted lists into a single sorted list.

Two pointers, O(n + m) time.
"""


def merge_sorted(a, b):
    """Return a new sorted list containing all items of a and b."""
    i = j = 0
    merged = []

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1

    # append whatever is left over
    merged.extend(a[i:])
    merged.extend(b[j:])
    return merged


if __name__ == "__main__":
    a = [1, 3, 5, 7]
    b = [2, 4, 6, 8]
    print("a     :", a)
    print("b     :", b)
    print("merged:", merge_sorted(a, b))   # [1, 2, 3, 4, 5, 6, 7, 8]
