"""
basics/max_and_min.py  —  Part 1 task

Find the maximum and minimum values in a list WITHOUT using max() or min().

Time complexity: O(n)  — one pass over the list.
Space complexity: O(1) — only two extra variables.
"""


def find_max_min(nums):
    """Return (max_value, min_value). Assumes nums is non-empty."""
    if not nums:
        raise ValueError("find_max_min() requires a non-empty list")

    biggest = nums[0]
    smallest = nums[0]

    for x in nums[1:]:          # start from the second item
        if x > biggest:
            biggest = x
        if x < smallest:
            smallest = x

    return biggest, smallest


def find_max_min_using_builtins(nums):
    """The Pythonic one-liner — fine in real code, but learn the manual way."""
    return max(nums), min(nums)


if __name__ == "__main__":
    data = [3, 7, 1, 9, 4, -2, 8]

    biggest, smallest = find_max_min(data)
    print("list      :", data)
    print("max       :", biggest)
    print("min       :", smallest)
    print("builtins  :", find_max_min_using_builtins(data))
