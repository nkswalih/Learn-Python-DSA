"""
queue/sliding_window_max.py  —  Part 4 problem (LeetCode 239)

For every window of size k, report the maximum value.

Trick: a deque holds INDICES of candidates in decreasing value order.
    - drop indices that fell out of the window (from the left)
    - drop indices whose value is smaller than the newcomer (from the right)
    - the front is always the window maximum
O(n) time, because each index enters and leaves the deque once.
"""

from collections import deque


def sliding_window_max(nums, k):
    if not nums or k <= 0:
        return []
    result = []
    dq = deque()                     # holds indices, values decreasing

    for i, x in enumerate(nums):
        # 1) remove indices that are now outside the window
        if dq and dq[0] <= i - k:
            dq.popleft()
        # 2) remove smaller values from the back — they can never win now
        while dq and nums[dq[-1]] <= x:
            dq.pop()
        dq.append(i)
        # 3) once the window is full, the front is the maximum
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


if __name__ == "__main__":
    print(sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3))
    # [3, 3, 5, 5, 6, 7]
    print(sliding_window_max([9, 11, 8, 5, 7, 10], 2))
