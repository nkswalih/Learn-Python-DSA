"""
arrays/majority_element.py  —  Part 2 problem (LeetCode 169, Boyer-Moore)

Find the element that appears more than n/2 times.

Boyer-Moore voting: keep a candidate and a counter. Matching votes up,
different votes cancel down. The true majority survives.
O(n) time, O(1) space.
"""


def majority_element(nums):
    candidate = None
    count = 0
    for x in nums:
        if count == 0:
            candidate = x            # pick a new candidate
        count += 1 if x == candidate else -1
    return candidate


if __name__ == "__main__":
    print(majority_element([3, 2, 3]))              # 3
    print(majority_element([2, 2, 1, 1, 1, 2, 2]))  # 2
