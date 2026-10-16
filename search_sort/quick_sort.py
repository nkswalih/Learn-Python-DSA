"""
search_sort/quick_sort.py  —  Part 5

Pick a pivot, move everything smaller to its left and larger to its right,
then recurse on both sides. Average O(n log n), worst case O(n^2) (bad pivots).
In practice the fastest comparison sort. In place, using O(log n) stack space.

To avoid the worst case on already-sorted data we use a middle pivot.
"""


def quick_sort(nums):
    _quick_sort(nums, 0, len(nums) - 1)
    return nums


def _quick_sort(nums, lo, hi):
    if lo >= hi:
        return
    p = _partition(nums, lo, hi)
    _quick_sort(nums, lo, p - 1)
    _quick_sort(nums, p + 1, hi)


def _partition(nums, lo, hi):
    """Lomuto partition around a middle pivot. Returns the pivot's final index."""
    mid = (lo + hi) // 2
    nums[mid], nums[hi] = nums[hi], nums[mid]   # park pivot at the end
    pivot = nums[hi]
    i = lo
    for j in range(lo, hi):
        if nums[j] <= pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[hi] = nums[hi], nums[i]       # put pivot in place
    return i


if __name__ == "__main__":
    print(quick_sort([10, 7, 8, 9, 1, 5]))     # [1, 5, 7, 8, 9, 10]
    print(quick_sort([3, 3, 1, 2]))            # [1, 2, 3, 3]
    print(quick_sort([5, 4, 3, 2, 1]))         # [1, 2, 3, 4, 5]
