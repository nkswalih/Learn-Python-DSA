"""
stack/sort_stack.py  —  Part 4 problem (LeetCode 912 variant, stack version)

Sort a stack so the smallest value is on top, using only stack operations
(push, pop, peek) and no other data structure.
O(n^2) time, O(n) extra stack space.
"""


def sort_stack(stack):
    """stack: a Python list used as a stack (end = top). Returns a new sorted stack."""
    temp = []                          # holds values in order
    while stack:
        value = stack.pop()
        # pop back into the main stack until we find the right place
        while temp and temp[-1] > value:
            stack.append(temp.pop())
        temp.append(value)
    return temp                        # top is the smallest


if __name__ == "__main__":
    s = [3, 1, 4, 1, 5, 9, 2, 6]
    print("before:", s)
    print("after :", sort_stack(s))    # smallest on top
