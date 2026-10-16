"""
hashing/subarray_sum_k.py  —  Part 6 problem (LeetCode 560)

Count contiguous subarrays whose sum equals k.

Trick: a running (prefix) sum plus a dict of how often each prefix sum has
been seen. If prefix_now - k was seen before, the subarray between them sums
to k. O(n) time, O(n) space. (This is NOT the sliding-window trick — sliding
window breaks on negative numbers.)
"""


def subarray_sum(nums, k):
    seen = {0: 1}                 # empty prefix sums to 0, seen once
    running = 0
    count = 0
    for x in nums:
        running += x
        count += seen.get(running - k, 0)   # prefixes that make this sum to k
        seen[running] = seen.get(running, 0) + 1
    return count


if __name__ == "__main__":
    print(subarray_sum([1, 1, 1], 2))          # 2  -> [1,1] at (0,1) and (1,2)
    print(subarray_sum([1, 2, 3], 3))          # 2  -> [3], [1,2]
    print(subarray_sum([1, -1, 0], 0))         # 3
