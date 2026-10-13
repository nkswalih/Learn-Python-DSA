"""
hashing/common_elements.py  —  Part 6 task

Check whether two lists share any common elements, using set intersection.
This is O(n + m) — far faster than nested loops.
"""


def have_common(a, b):
    return len(set(a) & set(b)) > 0


def common_elements(a, b):
    return list(set(a) & set(b))


if __name__ == "__main__":
    a = [1, 2, 3, 4]
    b = [3, 5, 6, 7]
    print("any common?    :", have_common(a, b))       # True
    print("common elements:", common_elements(a, b))   # [3] (order may vary)

    c = [1, 2]
    d = [8, 9]
    print("any common?    :", have_common(c, d))       # False
