# Part 5 — Searching & Sorting

*Searching is "find this item." Sorting is "put these items in order." They're the two most common jobs in all of computing, and they're deeply linked: sorting data is often the trick that makes searching fast. This chapter builds both from scratch, then shows you the fast built-ins Python gives you.*

---

## 5.1 Searching — two ways to find something

A **search** answers: "Is this value here, and where?" There are two fundamentally different approaches, and the difference between them is enormous.

### Linear search — check one by one

Walk through the items until you find the target (or run out). It's the simplest possible search.

```python
def linear_search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i          # found — return its position
    return -1                 # not found
```

```python
print(linear_search([4, 2, 7, 1, 9], 7))    # 2
print(linear_search([4, 2, 7, 1, 9], 5))    # -1
```

Trace for target `7`:

```
index 0: 4 == 7? no
index 1: 2 == 7? no
index 2: 7 == 7? yes → return 2 ✅
```

**Cost:** `O(n)`. In the worst case you check every item. It works on **any** list, sorted or not — that's its strength.

**Real-world analogy:** looking for a name in an unsorted stack of papers, one page at a time.

### Binary search — cut the problem in half

Binary search is dramatically faster, but it has one strict requirement: **the data must already be sorted.**

The idea: look at the *middle* item.

- If it's the target → done.
- If the target is **smaller**, it must be in the left half → throw away the right half.
- If the target is **bigger**, it must be in the right half → throw away the left half.

Each step **halves** what's left. That's the source of its speed.

```python
def binary_search(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2      # middle index (integer division)
        if nums[mid] == target:
            return mid               # found
        elif nums[mid] < target:
            low = mid + 1            # target is in the right half
        else:
            high = mid - 1           # target is in the left half
    return -1                        # not found
```

```python
sorted_nums = [1, 3, 5, 7, 9, 11, 13]
print(binary_search(sorted_nums, 7))    # 3
print(binary_search(sorted_nums, 2))    # -1
```

Trace for target `7` in `[1, 3, 5, 7, 9, 11, 13]`:

```
low=0, high=6 → mid=3 → nums[3]=7 == 7 → found at index 3 ✅

Now try target 11:
low=0, high=6 → mid=3 → 7 < 11 → search right half, low=4
low=4, high=6 → mid=5 → 11 == 11 → found at index 5 ✅
```

In two steps we narrowed 7 items down to 1. For a million items, binary search needs about **20** steps. That's `O(log n)` — astonishing.

**Real-world analogy:** finding a word in a dictionary. You don't start at page 1 — you open to the middle, see whether your word comes before or after, and repeat.

### Conditions required for binary search

Binary search only works if **the data is sorted**. On unsorted data, "the target is in the right half" is a false assumption, and binary search will confidently return the wrong answer. Never run it on unsorted data. (If you need both, sort first — `O(n log n)` — then search — `O(log n)`.)

### Linear vs. binary search

| | Linear search | Binary search |
|---|---|---|
| Requires sorted data | No | **Yes** |
| Best case | `O(1)` (target first) | `O(1)` (target at middle) |
| Average case | `O(n)` | `O(log n)` |
| Worst case | `O(n)` | `O(log n)` |
| Works on unsorted data | ✅ | ❌ |
| Simple? | Very | A little trickier |

**Rule of thumb:** if the data is sorted (or you can cheaply sort it once and search many times), use binary search. Otherwise use linear search.

---

## 5.2 Sorting — putting data in order

So why do we sort? Because sorted data unlocks speed: binary search, finding the median, merging, deduplicating, and much more. Sorting is a *preparation step* that makes later work cheap.

We'll build three classic beginner sorts. None of them are the fastest — we build them to understand the *ideas*, then use Python's fast built-in at the end.

### Bubble sort — repeatedly swap neighbors that are out of order

The idea: compare each pair of neighbors. If they're out of order, swap them. Repeat passes until nothing swaps (the list is sorted).

```python
def bubble_sort(nums):
    n = len(nums)
    for pass_num in range(n - 1):
        swapped = False
        for i in range(n - 1 - pass_num):     # last items are already sorted
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]   # swap
                swapped = True
        if not swapped:                        # no swaps → already sorted, stop early
            break
    return nums
```

Trace `[5, 1, 4, 2]`:

```
Pass 1:  [5,1,4,2] → swap(5,1) → [1,5,4,2]
                     swap(5,4) → [1,4,5,2]
                     swap(5,2) → [1,4,2,5]   ← 5 bubbled to the end
Pass 2:  [1,4,2,5] → 1<4 ok → swap(4,2) → [1,2,4,5]   ← 4 in place
Pass 3:  [1,2,4,5] → no swaps → stop early ✅
```

**Cost:** `O(n²)` worst and average. **Best case `O(n)`** — if the list is already sorted, the `swapped` flag ends it after one pass. Good to know for interviews.

**Analogy:** bubbles rising to the surface — the largest value "bubbles" to the end each pass.

### Selection sort — repeatedly pick the smallest and place it

The idea: find the smallest item in the unsorted part, swap it to the front of that part, then move the boundary forward.

```python
def selection_sort(nums):
    n = len(nums)
    for start in range(n - 1):
        min_index = start
        for i in range(start + 1, n):          # scan the unsorted part
            if nums[i] < nums[min_index]:
                min_index = i                  # remember where the smallest is
        nums[start], nums[min_index] = nums[min_index], nums[start]  # place it
    return nums
```

Trace `[5, 1, 4, 2]`:

```
start=0: smallest in [5,1,4,2] is 1 at index 1 → swap → [1,5,4,2]
start=1: smallest in [5,4,2]   is 2 at index 3 → swap → [1,2,4,5]
start=2: smallest in [4,5]     is 4 at index 2 → swap → [1,2,4,5] (no change)
sorted ✅
```

**Cost:** `O(n²)` in **all** cases (best, average, worst) — it always scans the whole unsorted part to find the minimum. This makes it predictable but never fast.

**Analogy:** sorting a hand of playing cards by repeatedly finding the lowest card and moving it to the left.

### Insertion sort — build a sorted region one item at a time

The idea: think of the first item as a sorted "hand." Take the next item and insert it into the correct spot in the sorted region, shifting bigger items right to make room.

```python
def insertion_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]                 # the card we're inserting
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]     # shift bigger item right
            j -= 1
        nums[j + 1] = key             # drop the key into the gap
    return nums
```

Trace `[5, 1, 4, 2]`:

```
i=1: key=1 → shift 5 right → [1, 5, 4, 2]
i=2: key=4 → 5>4 shift → then 1<4 stop → [1, 4, 5, 2]
i=3: key=2 → 5>2,4>2 shift → 1<2 stop → [1, 2, 4, 5] ✅
```

**Cost:** `O(n²)` worst and average, but **`O(n)` best case** — if the list is already sorted, each item is already in place and nothing shifts. For *nearly sorted* data, insertion sort is genuinely fast.

**Analogy:** the way most people sort a small hand of cards — pick up a card and slide it into the right spot.

### Which of the three should you know?

All three, for interviews and intuition. The one-line summary:

| Sort | Best | Average | Worst | Stable? | Key idea |
|---|---|---|---|---|---|
| Bubble | `O(n)` | `O(n²)` | `O(n²)` | Yes | Swap out-of-order neighbors |
| Selection | `O(n²)` | `O(n²)` | `O(n²)` | No | Pick the smallest, place it |
| Insertion | `O(n)` | `O(n²)` | `O(n²)` | Yes | Insert each item into a sorted prefix |

**"Stable"** means equal items keep their original relative order — often useful when sorting by multiple keys.

---

## 5.3 Python's built-in sorting (use this in real code)

Now the practical part. Python has sorting built in, and it's excellent — it uses an algorithm called **Timsort** that is `O(n log n)` and specially fast on partially-sorted data. **In real code, always use the built-ins.** You learn the manual sorts for understanding and interviews, not to ship them.

Python gives you two ways to sort:

### `sorted()` — returns a NEW sorted list

```python
nums = [3, 1, 2]
result = sorted(nums)
print(result)     # [1, 2, 3]
print(nums)       # [3, 1, 2]   ← original untouched
```

### `.sort()` — sorts a list IN PLACE

```python
nums = [3, 1, 2]
nums.sort()
print(nums)       # [1, 2, 3]   ← the same list, now sorted
```

### The difference in one table

| | `sorted(x)` | `x.sort()` |
|---|---|---|
| Returns | a new sorted list | `None` (sorts in place) |
| Original changed | No | Yes |
| Works on | any iterable (list, tuple, string, dict views) | only lists |
| Use when | you need to keep the original | you want to sort in place |

**Beginner trap:**
```python
nums = [3, 1, 2]
result = nums.sort()      # ❌ result is None!
print(result)             # None
```
`.sort()` returns `None` because it sorts in place. Use `sorted()` if you want the sorted list as a return value.

### Sorting by custom keys (a superpower)

Both accept a `key` function and a `reverse` flag:

```python
words = ["banana", "apple", "cherry"]

sorted(words, key=len)                 # shortest first: ['apple', 'banana', 'cherry']
sorted(words, reverse=True)            # reverse alphabetical
sorted(words, key=lambda w: w[-1])     # sort by last letter

# Sort a list of tuples/records by one field
people = [("Alice", 30), ("Bob", 25), ("Cara", 35)]
sorted(people, key=lambda p: p[1])     # by age: [('Bob', 25), ('Alice', 30), ('Cara', 35)]
```

### Built-in vs manual — the honest comparison

| | Manual sort | Python's `sorted`/`.sort` |
|---|---|---|
| Speed | pure Python, slow | written in C, fast |
| Complexity | same `O(n log n)` at best | `O(n log n)` guaranteed |
| Length of code | dozens of lines | one line |
| Use it for | learning, interviews | real code, always |

Even though a hand-written merge sort and Python's `sorted` share the same `O(n log n)`, Python's is typically **10–50x faster** because it runs in optimized C. That's a constant-factor win, but a big one.

---

## 5.4 Complexity comparison — the full table

One table to keep. Learn the shapes, not just the symbols.

| Algorithm | Best | Average | Worst | Space | Notes |
|---|---|---|---|---|---|
| Linear search | `O(1)` | `O(n)` | `O(n)` | `O(1)` | Any list |
| Binary search | `O(1)` | `O(log n)` | `O(log n)` | `O(1)` | **Needs sorted data** |
| Bubble sort | `O(n)` | `O(n²)` | `O(n²)` | `O(1)` | Early-exit helps sorted data |
| Selection sort | `O(n²)` | `O(n²)` | `O(n²)` | `O(1)` | Always `n²`; few swaps |
| Insertion sort | `O(n)` | `O(n²)` | `O(n²)` | `O(1)` | Fast on nearly-sorted data |
| Python `sorted`/`.sort` (Timsort) | `O(n)` | `O(n log n)` | `O(n log n)` | `O(n)` | Use this in practice |

**How to read this:** the "best case" is the happiest possible input, "worst case" the meanest. Interviews expect the worst case unless you say otherwise.

For scale, recall from Part 1: at `n = 100,000`, an `O(n²)` sort does 10 billion comparisons (too slow), while `O(n log n)` does about 1.7 million (instant). **This is why we never use bubble sort on real data.**

---

## 5.5 When to sort, when to search

A quick decision guide:

- **Searching once in unsorted data** → linear search. Sorting first would be overkill.
- **Searching many times in the same data** → sort once (`O(n log n)`), then binary search each time (`O(log n)`). The sorting cost pays off after a few searches.
- **Just need the items in order** → `sorted()` / `.sort()`.
- **Need items sorted by a custom rule** → use the `key=` argument.
- **Data already sorted** → binary search, and don't re-sort.
- **Small list (say under 10 items)** → don't overthink; linear search and simple sorts are fine — constant factors dominate at tiny sizes.

---

## 5.6 Common beginner mistakes

1. **Running binary search on unsorted data.** It silently gives wrong answers. Sort first.
2. **Off-by-one in binary search.** Use `low <= high` and `mid + 1` / `mid - 1`. Writing `low < high` or forgetting the ±1 causes infinite loops or missed items.
3. **Overflow-style mid bug** (other languages, worth knowing): `(low + high) // 2` can overflow in fixed-width languages; `low + (high - low) // 2` avoids it. In Python integers are unbounded, so either is fine.
4. **Using `result = nums.sort()`.** It's `None`. Use `sorted(nums)`.
5. **Forgetting the `swapped` early-exit in bubble sort** (or knowing it exists for the best case).
6. **Assuming all sorts are equal.** They have different best cases and stability.
7. **Sorting inside a loop unnecessarily.** Sort once, reuse.

---

## 5.7 Recap — test yourself

1. **Linear search** → check items one by one; `O(n)`; works on any list.
2. **Binary search** → halve the range each step; `O(log n)`; **needs sorted data**.
3. **Why is binary search fast?** → It halves the problem each step.
4. **Bubble sort idea** → swap out-of-order neighbors until sorted.
5. **Selection sort idea** → find the smallest, place it, repeat.
6. **Insertion sort idea** → insert each item into a growing sorted prefix.
7. **Best case of bubble & insertion sort** → `O(n)` on already-sorted data.
8. **Best case of selection sort** → `O(n²)` — it never gets lucky.
9. **Stable sort** → equal items keep their original order.
10. **`sorted(x)` vs `x.sort()`** → new list vs in-place (returns `None`).
11. **Which sort to use in production?** → Python's `sorted`/`.sort` (Timsort, `O(n log n)`, fast C).
12. **Sorting then binary searching — why?** → Sorting once makes many searches cheap.

---

## 5.8 Tasks (the `search_sort/` folder)

1. **Implement linear search** and **binary search** from scratch. Test both on the same data (remember: binary search needs sorted data).
2. **Implement bubble, selection, and insertion sort** from scratch.
3. **Compare their runtime** using the `time` module. Sort the same random list of, say, 1,000 numbers with each and print the times:
   ```python
   import time, random

   data = [random.randint(0, 10000) for _ in range(1000)]

   for name, fn in [("bubble", bubble_sort),
                    ("selection", selection_sort),
                    ("insertion", insertion_sort),
                    ("built-in", sorted)]:
       copy = data[:]                    # don't let one sort affect the next
       start = time.perf_counter()
       fn(copy)
       print(f"{name:>10}: {time.perf_counter() - start:.4f}s")
   ```
   Which is fastest? Which is slowest? Does it match the complexity table? Now try `n = 2000` and watch the `O(n²)` sorts get *four times* slower while the built-in barely changes.
4. **Document the complexity table** in a file in `search_sort/` so you can revise it later.
5. **Sort by a custom key:** given a list of words, sort them by length, then alphabetically for ties. (Hint: `key=lambda w: (len(w), w)`.)
6. **Challenge:** implement binary search *recursively* (you'll be ready after Part 7) and confirm it matches the loop version.

---

**Previous:** [Part 4 — Stacks & Queues](03-stacks-and-queues.md) · **Next:** [Part 6 — Hashing, Sets & Dictionaries](05-hashing-sets-and-dicts.md)
