"""
search_sort/insertion_sort.py  —  Part 5

Insertion sort: build a sorted prefix one item at a time, sliding each new
item into place. Worst O(n^2), but O(n) on nearly-sorted data — its strength.
"""


def insertion_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]                 # the item we're inserting
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]     # shift bigger item right
            j -= 1
        nums[j + 1] = key             # drop key into the gap
    return nums


if __name__ == "__main__":
    print(insertion_sort([5, 1, 4, 2, 8]))     # [1, 2, 4, 5, 8]
    print(insertion_sort([1, 2, 4, 3, 5]))     # nearly sorted -> very fast
