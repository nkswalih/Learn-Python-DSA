"""
basics/analyze_find_max.py  —  Part 1 task

A small exercise in reading code and naming its complexity.

Look at each function below, guess the Big O BEFORE reading the comment,
then run the file to confirm nothing surprising.
"""


def find_max(nums):
    """O(n) — one loop through the list."""
    biggest = nums[0]
    for x in nums:
        if x > biggest:
            biggest = x
    return biggest


def find_duplicates_nested(nums):
    """O(n^2) — a loop inside a loop."""
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


def find_duplicates_fast(nums):
    """O(n) — the set does the checking in O(1)."""
    return len(set(nums)) < len(nums)


def has_pair_summing_to(nums, target):
    """O(n) — 'have I seen the complement?' with a set."""
    seen = set()
    for x in nums:
        if (target - x) in seen:
            return True
        seen.add(x)
    return False


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    print("find_max              :", find_max(data))
    print("find_duplicates_nested:", find_duplicates_nested([1, 2, 2]))
    print("find_duplicates_fast  :", find_duplicates_fast([1, 2, 2]))
    print("has_pair_summing_to 9 :", has_pair_summing_to(data, 9))
