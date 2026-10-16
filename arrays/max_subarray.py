"""
arrays/max_subarray.py  —  Part 2 problem (LeetCode 53, Kadane's algorithm)

Find the largest sum of any contiguous subarray.

Idea: keep a running sum. At each step, either extend the current run
or start fresh from the current element — whichever is larger.
O(n) time, O(1) space.
"""


def max_subarray(nums):
    if not nums:
        return 0
    best = current = nums[0]
    for x in nums[1:]:
        current = max(x, current + x)   # extend or restart
        best = max(best, current)
    return best


if __name__ == "__main__":
    print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))   # 6  -> [4,-1,2,1]
    print(max_subarray([1]))                                 # 1
    print(max_subarray([-5, -2, -8]))                        # -2
