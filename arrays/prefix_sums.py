"""
arrays/prefix_sums.py  —  Part 2 helper

Prefix sums let you answer "sum of a range" in O(1) after an O(n) setup.

    prefix[i] = nums[0] + nums[1] + ... + nums[i-1]
    sum of nums[lo..hi] = prefix[hi+1] - prefix[lo]
"""


def build_prefix(nums):
    """Return a prefix array of length n+1 with prefix[0] = 0."""
    prefix = [0] * (len(nums) + 1)
    for i, x in enumerate(nums):
        prefix[i + 1] = prefix[i] + x
    return prefix


def range_sum(prefix, lo, hi):
    """Sum of nums[lo..hi] inclusive, in O(1)."""
    return prefix[hi + 1] - prefix[lo]


if __name__ == "__main__":
    nums = [2, 4, 1, 7, 3]
    prefix = build_prefix(nums)
    print("nums      :", nums)
    print("prefix    :", prefix)
    print("sum [1..3]:", range_sum(prefix, 1, 3))   # 4+1+7 = 12
    print("sum [0..4]:", range_sum(prefix, 0, 4))   # 17
