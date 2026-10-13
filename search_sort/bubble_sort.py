"""
search_sort/bubble_sort.py  —  Part 5

Bubble sort: repeatedly swap neighbours that are out of order.
Worst case O(n^2), best case O(n) thanks to the early-exit flag.
"""


def bubble_sort(nums):
    n = len(nums)
    for pass_num in range(n - 1):
        swapped = False
        for i in range(n - 1 - pass_num):     # last items already sorted
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        if not swapped:                        # already sorted -> stop early
            break
    return nums


if __name__ == "__main__":
    print(bubble_sort([5, 1, 4, 2, 8]))     # [1, 2, 4, 5, 8]
    print(bubble_sort([1, 2, 3, 4, 5]))     # already sorted (one pass)
    print(bubble_sort([]))                  # []
