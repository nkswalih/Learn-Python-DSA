"""
arrays/move_zeroes.py  —  Part 2 problem (LeetCode 283)

Move all zeroes to the end while keeping the order of non-zero values.
Two-pointer "write" trick, in place: O(n) time, O(1) space.
"""


def move_zeroes(nums):
    write = 0                          # where the next non-zero goes
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write], nums[read] = nums[read], nums[write]
            write += 1
    return nums


if __name__ == "__main__":
    print(move_zeroes([0, 1, 0, 3, 12]))   # [1, 3, 12, 0, 0]
    print(move_zeroes([0, 0, 1]))          # [1, 0, 0]
    print(move_zeroes([1, 2, 3]))          # [1, 2, 3]
