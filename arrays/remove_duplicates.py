"""
arrays/remove_duplicates.py  —  Part 2 task (LeetCode 26)

Remove duplicates from a SORTED list, in place, and return the new length.
The classic two-pointer "read / write" trick: O(n) time, O(1) extra space.
"""


def remove_duplicates_sorted(nums):
    """Works only on a sorted list. Returns the count of unique items."""
    if not nums:
        return 0

    write = 1                       # where the next unique value goes
    for read in range(1, len(nums)):
        if nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1

    del nums[write:]                # truncate the leftover tail
    return write


if __name__ == "__main__":
    nums = [1, 1, 2, 2, 2, 3, 4, 4]
    print("before:", nums)
    length = remove_duplicates_sorted(nums)
    print("after :", nums)          # [1, 2, 3, 4]
    print("unique count:", length)  # 4
