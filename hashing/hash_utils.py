"""
hashing/hash_utils.py  —  Part 6

Reusable hashing helpers. Each one shows the core hash-table move:
turn a repeated SEARCH into a single LOOKUP.
"""

from collections import Counter


# ---------------------------------------------------------
#  Frequency counting
# ---------------------------------------------------------

def char_frequency(text):
    """Return a dict of {character: count} using a plain dict. O(n)."""
    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1     # .get avoids KeyError on new keys
    return freq


def char_frequency_counter(text):
    """The same thing with collections.Counter."""
    return dict(Counter(text))


def most_common(items):
    """Return the most frequent item. O(n)."""
    if not items:
        return None
    counts = Counter(items)
    return counts.most_common(1)[0][0]


def first_non_repeating(text):
    """Return the first character that appears exactly once, or None. O(n)."""
    counts = Counter(text)
    for ch in text:                        # scan in original order
        if counts[ch] == 1:
            return ch
    return None


def count_words(text):
    """Return {word: count} for a sentence. O(n)."""
    return dict(Counter(text.split()))


# ---------------------------------------------------------
#  Set membership
# ---------------------------------------------------------

def has_duplicate(items):
    """True if any value appears more than once. O(n)."""
    return len(set(items)) < len(items)


def common_elements(a, b):
    """Values present in both lists. O(n + m)."""
    set_b = set(b)
    return [x for x in a if x in set_b]


def unique_elements(items):
    """De-duplicate while keeping first-seen order. O(n)."""
    seen = set()
    out = []
    for x in items:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out


# ---------------------------------------------------------
#  Pair / complement lookups
# ---------------------------------------------------------

def two_sum(nums, target):
    """Return indices [i, j] with nums[i] + nums[j] == target, or []. O(n)."""
    seen = {}                              # value -> index
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return [seen[need], i]
        seen[x] = i
    return []


def count_pairs_with_sum(nums, target):
    """Count pairs (i < j) that add up to target. O(n)."""
    seen = {}
    pairs = 0
    for x in nums:
        need = target - x
        pairs += seen.get(need, 0)         # how many earlier complements
        seen[x] = seen.get(x, 0) + 1
    return pairs


# ---------------------------------------------------------
#  Anagrams
# ---------------------------------------------------------

def is_anagram(a, b):
    """True if a and b are anagrams. O(n)."""
    if len(a) != len(b):
        return False
    return Counter(a) == Counter(b)


def group_anagrams(words):
    """Group words that are anagrams of each other. O(n * k log k)."""
    groups = {}
    for word in words:
        key = "".join(sorted(word))        # anagram signature
        groups.setdefault(key, []).append(word)
    return list(groups.values())


# ---------------------------------------------------------
#  Consecutive runs
# ---------------------------------------------------------

def longest_consecutive(nums):
    """Length of the longest run of consecutive integers. O(n)."""
    values = set(nums)
    best = 0
    for n in values:
        if n - 1 not in values:            # n is the start of a run
            length = 1
            while n + length in values:
                length += 1
            best = max(best, length)
    return best


if __name__ == "__main__":
    print("char freq     :", char_frequency("mississippi"))
    print("most common   :", most_common([1, 3, 3, 2, 3]))       # 3
    print("first uniq    :", first_non_repeating("aabbcdd"))     # c
    print("duplicates    :", has_duplicate([1, 2, 3, 2]))        # True
    print("common elems  :", common_elements([1, 2, 3], [2, 3, 4]))
    print("unique (order):", unique_elements([3, 1, 3, 2, 1]))   # [3,1,2]
    print("two sum       :", two_sum([2, 7, 11, 15], 9))         # [0,1]
    print("count pairs   :", count_pairs_with_sum([1, 1, 1, 1], 2))  # 6
    print("is anagram    :", is_anagram("listen", "silent"))     # True
    print("group anagram :", group_anagrams(["eat", "tea", "tan", "ate", "nat"]))
    print("longest run   :", longest_consecutive([100, 4, 200, 1, 3, 2]))  # 4
