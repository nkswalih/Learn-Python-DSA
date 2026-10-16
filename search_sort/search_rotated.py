"""
search_sort/search_rotated.py  —  Part 5 problem (LeetCode 33)

Search a SORTED array that has been rotated (e.g. [4,5,6,7,0,1,2]) for a
target, in O(log n).

Key insight: at any mid, one of the two halves is still fully sorted.
Decide which half is sorted, check whether the target lies inside it,
and throw away the other half.
"""


def search_rotated(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid

        if nums[lo] <= nums[mid]:               # left half is sorted
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1                    # target in the left half
            else:
                lo = mid + 1
        else:                                   # right half is sorted
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1


if __name__ == "__main__":
    print(search_rotated([4, 5, 6, 7, 0, 1, 2], 0))    # 4
    print(search_rotated([4, 5, 6, 7, 0, 1, 2], 3))    # -1
    print(search_rotated([1], 1))                      # 0
    print(search_rotated([5, 1, 3], 5))                # 0
