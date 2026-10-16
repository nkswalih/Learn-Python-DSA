"""
recursion/generate_subsets.py  —  Part 7 problem (LeetCode 78)

Generate every subset of a list (the power set).

Idea: each element is either IN or OUT. Recurse on the rest and branch twice.
There are 2^n subsets, so the work is O(2^n) — this is the classic
"backtracking" shape.
"""


def subsets(nums):
    result = []

    def backtrack(index, current):
        if index == len(nums):
            result.append(current[:])     # snapshot a complete subset
            return
        # choice 1: skip nums[index]
        backtrack(index + 1, current)
        # choice 2: include nums[index]
        current.append(nums[index])
        backtrack(index + 1, current)
        current.pop()                     # undo the choice (backtrack)

    backtrack(0, [])
    return result


if __name__ == "__main__":
    print(subsets([1, 2, 3]))
    # [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]
    print("count:", len(subsets([1, 2, 3])), "(2^3 = 8)")
