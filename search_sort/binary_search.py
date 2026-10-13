"""
search_sort/binary_search.py  —  Part 5

Binary search: halve the search range at each step. O(log n).
REQUIRES the data to be sorted.
"""


def binary_search(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1        # go right
        else:
            high = mid - 1       # go left
    return -1


def binary_search_recursive(nums, target, low=None, high=None):
    """The same algorithm, written with recursion (see Part 7)."""
    if low is None:
        low = 0
    if high is None:
        high = len(nums) - 1
    if low > high:
        return -1
    mid = (low + high) // 2
    if nums[mid] == target:
        return mid
    if nums[mid] < target:
        return binary_search_recursive(nums, target, mid + 1, high)
    return binary_search_recursive(nums, target, low, mid - 1)


if __name__ == "__main__":
    data = [1, 3, 5, 7, 9, 11, 13]      # MUST be sorted
    print("find 7  :", binary_search(data, 7))                 # 3
    print("find 13 :", binary_search(data, 13))                # 6
    print("find 2  :", binary_search(data, 2))                 # -1
    print("recursive 7:", binary_search_recursive(data, 7))    # 3
