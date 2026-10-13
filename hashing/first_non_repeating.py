"""
hashing/first_non_repeating.py  —  Part 6 task

Find the first character in a string that does not repeat.
Two passes: count everything (O(n)), then scan for the first count of 1 (O(n)).
"""

from collections import Counter


def first_non_repeating(text):
    counts = Counter(text)
    for ch in text:
        if counts[ch] == 1:
            return ch
    return None


if __name__ == "__main__":
    print(first_non_repeating("aabbcdd"))      # c
    print(first_non_repeating("aabbcc"))       # None
    print(first_non_repeating("leetcode"))     # l
