"""
search_sort/selection_sort.py  -  Part 5

Selection sort: find the smallest item in the unsorted part, swap it to the
front of that part, move the boundary forward. Always O(n^2).
"""


def selection_sort(nums):
    n = len(nums)
    for start in range(n - 1):
        min_index = start
        for i in range(start + 1, n):
            if nums[i] < nums[min_index]:
                min_index = i
        nums[start], nums[min_index] = nums[min_index], nums[start]
    return nums


if __name__ == "__main__":
    print(selection_sort([5, 1, 4, 2, 8]))   # [1, 2, 4, 5, 8]
    print(selection_sort([3, 3, 1, 2, 1]))   # [1, 1, 2, 3, 3]
