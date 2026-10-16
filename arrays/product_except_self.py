"""
arrays/product_except_self.py  —  Part 2 problem (LeetCode 238)

For each index, compute the product of every other element — WITHOUT division,
in O(n).

Trick: a left-to-right pass holds products of everything to the left,
a right-to-left pass multiplies in products of everything to the right.
"""


def product_except_self(nums):
    n = len(nums)
    result = [1] * n

    left = 1
    for i in range(n):                 # result[i] = product of nums[0..i-1]
        result[i] = left
        left *= nums[i]

    right = 1
    for i in range(n - 1, -1, -1):     # multiply by product of nums[i+1..]
        result[i] *= right
        right *= nums[i]

    return result


if __name__ == "__main__":
    print(product_except_self([1, 2, 3, 4]))     # [24, 12, 8, 6]
    print(product_except_self([2, 3, 0, 4]))     # [0, 0, 24, 0]
