"""
search_sort/merge_sort.py  —  Part 5

Divide-and-conquer sort: split in half, sort each half, merge the two sorted
halves. Guaranteed O(n log n) time (unlike quick sort's average), O(n) extra
space. Stable.
"""


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return _merge(left, right)


def _merge(left, right):
    """Merge two already-sorted lists into one sorted list. O(n)."""
    out = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:        # <= keeps it stable
            out.append(left[i])
            i += 1
        else:
            out.append(right[j])
            j += 1
    out.extend(left[i:])               # attach whatever is left
    out.extend(right[j:])
    return out


if __name__ == "__main__":
    data = [5, 2, 9, 1, 5, 6, 3]
    print("unsorted:", data)
    print("sorted  :", merge_sort(data))
    print("already :", merge_sort([1, 2, 3, 4]))
