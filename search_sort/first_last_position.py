"""
search_sort/first_last_position.py  —  Part 5 problem (LeetCode 34)

Given a sorted array, find the first and last index of a target.

Trick: run binary search TWICE with a twist. When you find the target, keep
searching one side to squeeze the range. O(log n) overall.
"""


def lower_bound(nums, target):
    """First index where target appears, or -1."""
    lo, hi = 0, len(nums) - 1
    ans = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            ans = mid
            hi = mid - 1                 # keep looking LEFT
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return ans


def upper_bound(nums, target):
    """Last index where target appears, or -1."""
    lo, hi = 0, len(nums) - 1
    ans = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            ans = mid
            lo = mid + 1                 # keep looking RIGHT
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return ans


def search_range(nums, target):
    return [lower_bound(nums, target), upper_bound(nums, target)]


if __name__ == "__main__":
    print(search_range([5, 7, 7, 8, 8, 10], 8))   # [3, 4]
    print(search_range([5, 7, 7, 8, 8, 10], 6))   # [-1, -1]
    print(search_range([1, 1, 1], 1))             # [0, 2]
