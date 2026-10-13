"""
search_sort/linear_search.py  —  Part 5

Linear search: check items one by one until the target is found.
Works on any list (sorted or not). O(n).
"""


def linear_search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i          # found at this index
    return -1                 # not found


if __name__ == "__main__":
    data = [4, 2, 7, 1, 9, 3]
    print("find 7 :", linear_search(data, 7))    # 2
    print("find 9 :", linear_search(data, 9))    # 4
    print("find 5 :", linear_search(data, 5))    # -1
