"""
hashing/group_anagrams.py  —  Part 6 problem (LeetCode 49)

Group words that are anagrams of each other.

Trick: two anagrams share the SAME sorted word. Use that sorted signature
as a dict key; every word that maps to it belongs in the same group.
O(n * k log k) where k is the longest word length.
"""


def group_anagrams(words):
    groups = {}
    for word in words:
        key = "".join(sorted(word))        # canonical form
        groups.setdefault(key, []).append(word)
    return list(groups.values())


if __name__ == "__main__":
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(group_anagrams(words))
    # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    # Same idea using character counts as the key (avoids sorting):
    def group_by_count(words):
        groups = {}
        for word in words:
            key = [0] * 26
            for ch in word:
                key[ord(ch) - ord("a")] += 1
            groups.setdefault(tuple(key), []).append(word)
        return list(groups.values())

    print(group_by_count(words))
