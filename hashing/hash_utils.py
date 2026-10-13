"""
hashing/hash_utils.py  —  Part 6

Reusable hashing helpers: frequency counting, duplicate detection,
first non-repeating character.
"""

from collections import Counter


def char_frequency(text):
    """Return a dict of {character: count} using a plain dict. O(n)."""
    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1     # .get avoids KeyError on new keys
    return freq


def char_frequency_counter(text):
    """The same thing with collections.Counter."""
    return dict(Counter(text))


def first_non_repeating(text):
    """Return the first character that appears exactly once, or None. O(n)."""
    counts = Counter(text)
    for ch in text:                        # scan in original order
        if counts[ch] == 1:
            return ch
    return None


def has_duplicate(items):
    """True if any value appears more than once. O(n)."""
    return len(set(items)) < len(items)


def count_words(text):
    """Return {word: count} for a sentence. O(n)."""
    return dict(Counter(text.split()))


if __name__ == "__main__":
    print("char freq  :", char_frequency("mississippi"))
    print("via Counter:", char_frequency_counter("mississippi"))
    print("first uniq :", first_non_repeating("aabbcdd"))   # c
    print("duplicates :", has_duplicate([1, 2, 3, 2]))      # True
    print("word count :", count_words("the cat the dog"))
