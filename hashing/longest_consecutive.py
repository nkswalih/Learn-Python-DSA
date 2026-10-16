"""
hashing/longest_consecutive.py  —  Part 6 problem (LeetCode 128)

Length of the longest run of consecutive integers, in O(n).

Trick: put everything in a set. A number is the START of a run only if
(n - 1) is NOT in the set. Only start counting from run-starts, so each
number is visited a constant number of times.
"""


def longest_consecutive(nums):
    values = set(nums)
    best = 0
    for n in values:
        if n - 1 not in values:            # n begins a run
            length = 1
            while n + length in values:
                length += 1
            best = max(best, length)
    return best


if __name__ == "__main__":
    print(longest_consecutive([100, 4, 200, 1, 3, 2]))   # 4 -> 1,2,3,4
    print(longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9
    print(longest_consecutive([]))                       # 0
