"""
arrays/two_sum.py  —  Part 2 task (LeetCode 1)

Given a list of numbers and a target, return the indices of the two numbers
that add up to the target.

Brute force is O(n^2). This one-pass version is O(n) using a dict.
"""


def two_sum_brute(nums, target):
    """Slow but obvious: try every pair. O(n^2)."""
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def two_sum(nums, target):
    """
    Fast: remember each value's index as we go, and ask
    'have I already seen the number that completes this pair?'  O(n).
    """
    seen = {}                              # value -> index
    for i, x in enumerate(nums):
        needed = target - x
        if needed in seen:                 # O(1) lookup
            return [seen[needed], i]
        seen[x] = i
    return []


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print("brute force:", two_sum_brute(nums, target))   # [0, 1]
    print("fast       :", two_sum(nums, target))          # [0, 1]
