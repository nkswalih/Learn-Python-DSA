# Part 6 — Hashing, Sets & Dictionaries

*This is the most useful chapter in the book. Hashing is the trick that turns "search" from a slow scan into an instant lookup. Once you understand it, a whole class of problems that looked hard becomes easy — and you'll convert slow `O(n²)` solutions into fast `O(n)` ones.*

---

## 6.1 The problem hashing solves

Suppose you have a list of 10,000 names and someone asks: "Is `Priya` in this list?"

```python
if "Priya" in names_list:      # scans name by name → O(n)
    ...
```

Python checks names one at a time until it finds `Priya` (or reaches the end). That's `O(n)` — for a big list, slow. And if you ask again for a different name, you scan from scratch.

The dream: what if I could compute *exactly where* `Priya` is, in one step, without scanning? That's what a **hash table** does. It turns "search" into "compute."

**Real-world analogy — a coat check at a party.** You hand over your coat; they give you a numbered ticket. To get your coat back, you show the ticket and they walk to the exact hook — no searching through hundreds of coats. The number *is* the location.

---

## 6.2 How a hash table works

A **hash table** stores **key → value** pairs. Two ideas make it work:

1. A **hash function** turns a key into a number.
2. That number decides *which slot* in an internal array the key goes into.

```
        KEY          HASH FUNCTION           SLOT INDEX
     "Priya"  ──▶  hash("Priya") = 9182...  ──▶  9182 % 8 = 6
                                                       │
                                                       ▼
     Internal array ("buckets"):
     ┌────┬────┬────┬────┬────┬────┬───────────────┬────┐
     │ 0  │ 1  │ 2  │ 3  │ 4  │ 5  │ 6             │ 7  │
     └────┴────┴────┴────┴────┴────┴───────┬───────┴────┘
                                           ▼
                                  "Priya" → "555-1234"
```

To look up `"Priya"` later:

1. Compute `hash("Priya")` → same number as before.
2. Reduce it to a slot index (`% 8` here).
3. Go **straight** to that slot.

No scanning. That's why a hash-table lookup is `O(1)` on average. The magic is that the *same key always produces the same number*, so you always land in the same place.

**Key-value mapping** is simply that: each key maps to a value. Python's `dict` is exactly this.

```python
phone = {"Priya": "555-1234", "Sam": "555-9876"}
phone["Priya"]        # "555-1234"  — instant, no scanning
phone["Leo"] = "555-0000"   # add a new pair
```

---

## 6.3 The collision problem

Here's the catch. A hash function produces a *big* number, and we squeeze it into a *small* array of slots. Two different keys can easily land on the **same slot**.

**That's a collision:** two different keys have the same slot index.

```
hash("apple") → slot 5
hash("grape") → slot 5   ← collision! different keys, same slot
```

Collisions are not a bug you can avoid — they're **mathematically guaranteed**. (There are infinitely many possible keys but only finitely many slots.) So every hash table needs a plan for handling them.

### Handling collisions — separate chaining

The most common approach: **each slot holds a small list** of everything that hashes there. When you look up a key, you go to its slot and search only that short list.

```
Slot 5's chain:
     "apple" → 3
     "grape" → 1
     "melon" → 7
```

If the chains stay **short**, a lookup is still basically `O(1)`. Keeping them short is the whole engineering challenge — and the solution is to keep the table from getting too crowded.

### Handling collisions — open addressing

The alternative: when a slot is taken, **probe forward** to the next free slot.

```
Insert "grape" (wants slot 5, but it's taken):
     slot 5: "apple"
     slot 6: ← "grape" goes here instead
```

Lookups then follow the same probing rule. This uses less memory but gets complicated when you delete (you need special "tombstone" markers). You don't need to implement this — just know the name.

### Load factor — why hash tables stay fast

The **load factor** is `items ÷ slots`. If it gets too high (the table is too crowded), chains grow long and lookups slow down. So when the load factor passes a threshold (commonly around 0.75), the table **doubles its number of slots and re-places every item** (recomputing their slots).

That rebuild is `O(n)`, but it's rare, so — just like `list.append` in Part 2 — the **amortized cost stays `O(1)`**. This is exactly why dicts and sets feel instant no matter how many items you add.

---

## 6.4 Python's `dict` and `set`

Now you understand the engine. Let's meet Python's two hash-table tools.

### `dict` — keys mapped to values

```python
ages = {"alice": 30, "bob": 25}

ages["alice"]          # 30 — look up by key, O(1)
ages["charlie"] = 40   # add a new pair
ages["alice"] = 31     # update an existing key
"bob" in ages          # True — membership check, O(1)
del ages["bob"]        # remove a key
```

**Key facts:**
- Lookups, inserts, and deletes are `O(1)` on average.
- **Keys are unique.** Assigning to an existing key *updates* it (doesn't add a second one).
- Since Python 3.7, dicts remember **insertion order** when you loop over them.

### `set` — a collection of unique items

A set is basically a dict that stores only keys (no values). Its job is uniqueness and fast membership.

```python
seen = {1, 2, 3}

2 in seen              # True — O(1)
seen.add(3)            # no change — 3 is already there
seen.add(4)            # now {1, 2, 3, 4}
seen.discard(1)        # remove 1
```

**Key facts:**
- No duplicates, ever.
- Membership tests are `O(1)`.
- Unordered (don't rely on a set's order).
- Great for "have I seen this before?" and removing duplicates.

### `dict` vs `set` — which one?

| You need... | Use |
|---|---|
| Look something up by a key | `dict` |
| Count how many times each item appears | `dict` |
| Group items by a category | `dict` |
| Just know "seen / not seen" | `set` |
| Remove duplicates | `set` |
| Compare two collections (membership/overlap) | `set` |

**Relationship to remember:** a `set` is a `dict` with no values. Everything about hashing applies to both.

---

## 6.5 Hashable vs. non-hashable — an important rule

Remember: a key's hash decides where it lives. If a key could **change** after being stored, its hash would change, and the table would lose track of it. So Python requires keys to be **immutable** (unchangeable).

```python
# ✅ HASHABLE — usable as dict keys / set members:
d = {}
d[42] = "int"
d["abc"] = "string"
d[(1, 2)] = "tuple"           # tuples are immutable → hashable
d[3.14] = "float"
d[True] = "bool"

# ❌ UNHASHABLE — Python refuses:
d[[1, 2]] = "list"           # TypeError: unhashable type: 'list'
d[{1, 2}] = "set"            # TypeError: unhashable type: 'set'
d[{}] = "dict"               # TypeError: unhashable type: 'dict'
```

**Why lists are banned:** a list can be changed. If you used it as a key and then mutated it, its hash would change and the dict couldn't find it anymore. Banned.
**Why tuples are allowed:** tuples can't be changed, so their hash is stable.

**Practical tip:** need to use a list-like key? Convert it to a tuple.
```python
key = tuple([1, 2, 3])        # (1, 2, 3) — now it can be a dict key
```

---

## 6.6 The `hash()` function

Python exposes hashing directly via the built-in `hash()`:

```python
hash(42)        # 42 (small ints hash to themselves)
hash("abc")     # some big integer, stable within a run
hash((1, 2))    # a number combining the hash of the elements
hash(3.14)      # derived from the float
```

You rarely call `hash()` yourself — the `dict`/`set` machinery does it. But two facts are worth knowing:

1. **Equal values have equal hashes.** If `a == b`, then `hash(a) == hash(b)`. (The reverse is not guaranteed: different values *can* share a hash — that's a collision, handled by the chain.)
2. **String hashes are randomized per run.** Python deliberately varies them between program runs (`PYTHONHASHSEED`) as a security feature, so attackers can't craft inputs that all collide and slow your program down. This means `hash("abc")` differs between runs of your program — so never store raw hash values expecting them to persist.

### Custom objects as keys

If you write your own class and want to use its instances as dict keys, you can — but you must define `__eq__` and `__hash__` consistently (advanced, but good to know it exists):

```python
class Player:
    def __init__(self, name):
        self.name = name
    def __eq__(self, other):
        return self.name == other.name
    def __hash__(self):
        return hash(self.name)
```

**The contract:** if two objects are equal, they must have the same hash. Break that and your objects become invisible inside dicts and sets.

---

## 6.7 Frequency counting — the #1 interview pattern

This is where dicts earn their keep: counting how often things appear. Learn these patterns cold.

### Count occurrences of each element

```python
nums = [1, 2, 2, 3, 3, 3]

# Manual way (know this for interviews)
freq = {}
for x in nums:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1
print(freq)   # {1: 1, 2: 2, 3: 3}
```

There's a shorter idiom using `.get(key, default)`:

```python
freq = {}
for x in nums:
    freq[x] = freq.get(x, 0) + 1   # if x is missing, start from 0
```

`freq.get(x, 0)` means "give me `freq[x]` if it exists, otherwise 0." It avoids a KeyError on the first occurrence.

### Using `collections.Counter` (the easy way)

```python
from collections import Counter

freq = Counter([1, 2, 2, 3, 3, 3])
print(freq)                    # Counter({3: 3, 2: 2, 1: 1})
print(freq[2])                 # 2 — count of the value 2
print(freq.most_common(1))     # [(3, 3)] — the most frequent item
```

`Counter` is a dict subclass, so everything you know about dicts applies.

### Character frequency in a string

```python
from collections import Counter

counts = Counter("mississippi")
print(counts)          # Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
```

### Word frequency

```python
text = "the cat the dog the bird"
words = text.split()
word_counts = Counter(words)
print(word_counts)     # Counter({'the': 3, 'cat': 1, 'dog': 1, 'bird': 1})
```

### The transformation that makes code fast

Here's the big idea, worth framing clearly:

```
SLOW (O(n²)):                         FAST (O(n)):
for each item:                        build a lookup dict/set once:
    search the whole list again           counts = Counter(...)
    to count/check occurrences            then look up in O(1)
```

Whenever your inner loop is *searching for something you already computed*, cache it in a dict or set. This one move fixes dozens of slow solutions.

---

## 6.8 Common use cases (with examples)

### 1. Duplicate detection

```python
def has_duplicate(nums):
    return len(set(nums)) < len(nums)
```

### 2. Fast lookups / membership

```python
banned = {"spam", "scam", "phishing"}     # O(1) membership
if word in banned:
    print("blocked")
```

### 3. Counting and grouping

```python
# Group words by their first letter
groups = {}
for word in ["apple", "avocado", "banana", "berry", "cherry"]:
    groups.setdefault(word[0], []).append(word)
# {'a': ['apple', 'avocado'], 'b': ['banana', 'berry'], 'c': ['cherry']}
```

### 4. Set operations (intersection, union, difference)

```python
a = {1, 2, 3}
b = {3, 4, 5}

a & b   # {3}          intersection — what's in both
a | b   # {1,2,3,4,5}  union — everything
a - b   # {1, 2}       difference — in a but not b
```

### 5. Two Sum — the pattern that appears everywhere

Find two numbers that add up to a target. The slow way is nested loops (`O(n²)`). The hash way is one pass:

```python
def two_sum(nums, target):
    seen = {}                 # value → its index
    for i, x in enumerate(nums):
        needed = target - x
        if needed in seen:    # O(1) "have I seen the complement?"
            return [seen[needed], i]
        seen[x] = i
    return []
```

**The insight:** instead of looking for the pair directly, we remember everything we've seen and ask "what number would complete the pair?" That's `O(1)` per item → `O(n)` total.

### 6. Remove duplicates while keeping order

```python
nums = [3, 1, 3, 2, 1]
unique = list(dict.fromkeys(nums))   # [3, 1, 2] — order preserved
```

---

## 6.9 Dict/set vs. list vs. sorted array

| Task | Best choice | Why |
|---|---|---|
| Is `x` in the collection? | `set` / `dict` | `O(1)` vs list's `O(n)` |
| Count frequencies | `dict` / `Counter` | one pass, `O(n)` |
| Access by position | `list` | `O(1)` index |
| Keep items in sorted order | `sorted list` | hashing has no order |
| Find items in a range (5 to 10) | `sorted list` + binary search | hash tables can't do ranges |
| Tiny collection (a handful) | `list` | simplifies; overhead barely matters |
| Remove duplicates | `set` | automatic |

**The two big limitations of hash tables to remember:**
1. **No order/range queries.** "Keys between 5 and 10" needs sorting or a tree — a dict can't help.
2. **Average, not guaranteed.** `O(1)` is the *average*; a pathological input could degrade it. Python's hash randomization bakes in protection.

---

## 6.10 Common beginner mistakes

1. **Using a list where a set belongs.** `if x in my_list` in a loop is `O(n)` → use a set.
2. **Trying to use a list as a dict key.** Convert it to a tuple first.
3. **Getting a `KeyError`.** Use `freq.get(x, 0)` or `collections.defaultdict` when keys may be missing.
4. **Assuming a set is ordered.** It isn't. If order matters, use a dict (insertion-ordered) or a list.
5. **Forgetting counts start at zero for new keys.** The `+ 1` idiom handles it with `.get(x, 0)`.
6. **Expecting hash values to be stable across runs.** String hashes are randomized on purpose.

---

## 6.11 Recap — test yourself

1. **Hashing turns search into...** → compute (a direct lookup).
2. **Hash table stores...** → key → value pairs.
3. **Hash function's job** → turn a key into a number (the slot).
4. **Collision** → two keys landing on the same slot.
5. **Collision handling — two approaches** → separate chaining (lists per slot), open addressing (probe for the next slot).
6. **Load factor & resizing** → keep the table uncrowded; when too full, double and rehash; amortized `O(1)`.
7. **Average lookup cost** → `O(1)`.
8. **`dict` vs `set`** → dict stores key→value; set stores only unique items.
9. **Hashable = ?** → immutable types (int, str, tuple, float).
10. **Why not a list as a key?** → it's mutable, so its hash could change.
11. **`hash(a) == hash(b)` when...** → when `a == b` (not the reverse).
12. **Frequency counting idiom** → `freq[x] = freq.get(x, 0) + 1` or `Counter`.
13. **Two Sum's insight** → store seen values, look up the complement in `O(1)`.
14. **Two things hash tables can't do** → ordered iteration / range queries.

---

## 6.12 Tasks (the `hashing/` folder)

1. **Count character frequency in a string** using a dict (manual), then again with `Counter`. Compare.
2. **Find the first non-repeating character** in a string using a dict. (Count everything, then scan for the first character whose count is 1.)
3. **Check if two lists share any common elements** using set intersection:
   ```python
   common = set(a) & set(b)
   ```
4. **Detect duplicates** in a list using a set.
5. **Two Sum** — implement it, then explain out loud why it's `O(n)` instead of `O(n²)`.
6. **Group anagrams** — words that are made of the same letters (e.g., "eat", "tea", "ate"). Group them with a dict keyed by the sorted letters.
7. **Demonstrate a collision** — pick a few strings and print `hash(s) % 8` for each; find two that land on the same slot. (Remember: because of hash randomization, run it a couple of times.)
8. **Compare dict/set vs list** for membership: build a list of 100,000 numbers and a set of the same, then time `x in collection` for many random checks. Explain the gap.
9. **Reusable helper file:** create `hashing/hash_utils.py` with `char_frequency`, `first_non_repeating`, and `has_duplicate` functions.

---

**Previous:** [Part 5 — Searching & Sorting](04-searching-and-sorting.md) · **Next:** [Part 7 — Recursion & Problem Solving](06-recursion-and-problem-solving.md)
