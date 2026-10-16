"""
arrays/rotate_array.py  —  Part 2 problem (LeetCode 189)

Rotate a list right by k steps, in place.

Trick (reverse three times), O(n) time, O(1) space:
    [1,2,3,4,5], k=2
    reverse all      -> [5,4,3,2,1]
    reverse first k  -> [4,5,3,2,1]
    reverse rest     -> [4,5,1,2,3]   <- rotated right by 2
"""


def _reverse_range(nums, lo, hi):
    while lo < hi:
        nums[lo], nums[hi] = nums[hi], nums[lo]
        lo += 1
        hi -= 1


def rotate_right(nums, k):
    n = len(nums)
    if n == 0:
        return nums
    k %= n
    _reverse_range(nums, 0, n - 1)
    _reverse_range(nums, 0, k - 1)
    _reverse_range(nums, k, n - 1)
    return nums


if __name__ == "__main__":
    print(rotate_right([1, 2, 3, 4, 5], 2))    # [4, 5, 1, 2, 3]
    print(rotate_right([1, 2, 3], 1))          # [3, 1, 2]
    print(rotate_right([1, 2, 3, 4], 4))       # [1, 2, 3, 4] (k % n == 0)
