"""
hashing/character_frequency.py  —  Part 6 task

Count how often each character appears in a string.
Two ways: the manual dict idiom, and collections.Counter.
"""

from collections import Counter


def count_manual(text):
    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1
    return freq


def count_counter(text):
    return Counter(text)


if __name__ == "__main__":
    s = "banana"
    print("manual :", count_manual(s))     # {'b':1,'a':3,'n':2}
    print("Counter:", count_counter(s))    # Counter({'a': 3, 'n': 2, 'b': 1})
