# Part 1 — Core Concepts & Big O

*Before we touch a single algorithm, you need three things: (1) a clear picture of what DSA actually is, (2) a quick tour of the tools Python already gives you, and (3) a way to measure whether one solution is better than another. This chapter gives you all three.*

---

## 1.1 What is DSA, really?

DSA stands for **Data Structures and Algorithms**. Two words, two simple jobs:

- A **data structure** is a way of *arranging* your data. It's a choice about how things are stored so that certain operations become easy.
- An **algorithm** is a *step-by-step recipe* that takes some input and produces the output you want.

Neither one is scary. You already use both every day.

**Everyday analogy — your kitchen.**

- *Data structure* = how you organize your kitchen. Spices in a rack, plates in a cupboard, leftovers in the fridge. If someone asks for "salt", a good arrangement (salt in the rack, labeled) gets it to you fast. A bad arrangement (everything in one giant bin) makes every request slow.
- *Algorithm* = the recipe you follow. "Boil water, add pasta, wait 10 minutes, drain." A clear sequence of steps.

That's the entire field. Now the insight that makes it worth studying:

> **The way you arrange data determines how fast your recipe runs.**

Same problem, two arrangements, two completely different speeds. Here is a concrete taste. Suppose you want to know if a list of numbers contains any duplicates:

```python
# Arrangement 1: keep the list as-is and compare everything to everything.
def has_duplicate_slow(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

# Arrangement 2: first drop the numbers into a "set" (a bag that
# automatically removes duplicates), then just check if its size shrank.
def has_duplicate_fast(nums):
    return len(set(nums)) < len(nums)
```

On a list of 100,000 numbers:

- `has_duplicate_slow` performs about **5 billion** comparisons. That can take minutes.
- `has_duplicate_fast` performs about **100,000** operations. That's instant.

Both give the same answer. The only difference is that the second one *chose a better arrangement of the data*. That choice is what DSA is about.

---

## 1.2 Why it matters (the honest, non-hype version)

You will hear "DSA is important for interviews." True — but that's not the whole story, and it's a bad reason to learn something.

Here are the real reasons:

**1. It's how software stops being slow.**
Fast software isn't magic. It's someone making a good structural choice. Autocomplete uses a tree. A GPS route uses shortest-path search. A undo button uses a stack. Every time you've thought "this app is snappy," DSA is somewhere underneath.

**2. It teaches you to see problems clearly.**
Most problems feel impossible because we attack them as one big blob. DSA trains you to ask: *What is the expensive part? What structure would make that part cheap?* That habit generalizes far beyond coding.

**3. It is the standard way engineers prove they can think.**
Interviews ask DSA because it's the cheapest way to test: Can you break a problem into parts? Do you know the cost of what you write? Can you reason clearly under a little pressure? Those are the skills the job actually needs.

---

## 1.3 Python's built-in data structures — a quick tour

Good news: Python already hands you four of the most useful data structures in existence. You'll use them constantly, so let's get the intuition right now. The details come in later chapters — for now, just meet them.

### `list` — a numbered row of boxes

A list holds items in order, and you can reach any item by its position (index).

```python
fruits = ["apple", "banana", "cherry"]
fruits[0]        # "apple"   (indexes start at 0!)
fruits[2]        # "cherry"
fruits[-1]       # "cherry"  (negative = count from the end)
```

**Mental picture:** a row of numbered lockers. "Give me locker 2" is instant, no matter how long the row is.

**Use a list when:** order matters and you want to go through items, or grab them by position.

### `tuple` — a sealed parcel

A tuple is like a list that *cannot be changed* after you create it.

```python
point = (3, 5)          # an (x, y) coordinate
point[0]                # 3
point[0] = 9            # TypeError! tuples are immutable
```

**Mental picture:** a parcel sealed with tape. You can look inside, but you can't add, remove, or swap items without making a whole new parcel.

**Use a tuple when:** the data is a fixed group that shouldn't change (a coordinate, a date, an RGB color), or when you need to use the group as a key in a dictionary.

### `dict` — a phonebook

A dictionary stores **key → value** pairs and looks things up by key instantly.

```python
ages = {"alice": 30, "bob": 25}
ages["alice"]           # 30  — instant lookup by name
ages["charlie"] = 40    # add a new entry
```

**Mental picture:** a phonebook. You don't scan every name to find "Bob" — you jump straight to it using the name as the key.

**Use a dict when:** you want to look something up by a label (a name, an ID, a word), or count/group things.

### `set` — a bag of unique items

A set stores items with **no duplicates** and **no particular order**.

```python
seen = {1, 2, 3}
2 in seen               # True  — instant membership check
seen.add(3)             # still {1, 2, 3} — adding a duplicate changes nothing
len(seen)               # 3
```

**Mental picture:** a bag of uniquely-numbered stamps. If you try to add a stamp you already have, nothing happens. Asking "do I have stamp #7?" is instant.

**Use a set when:** you need to remove duplicates or quickly ask "have I seen this before?"

### Quick reference table

| Structure | Ordered? | Changeable? | Duplicates? | Best at |
|---|---|---|---|---|
| `list` | Yes | Yes | Yes | Access by position, going through items |
| `tuple` | Yes | No | Yes | Fixed groups; using as dict keys |
| `dict` | Yes (insertion order) | Yes | Keys unique | Looking up values by a key |
| `set` | No | Yes | No | Removing duplicates, membership checks |

**You do not need to memorize this today.** Just remember: *list = ordered boxes, tuple = sealed boxes, dict = phonebook, set = unique bag.* We'll use each one soon enough that it becomes automatic.

> **Note on strings:** text in Python (`"hello"`) is also a sequence — a row of characters. Many list techniques (indexing, slicing, going through each character) work on strings too. We'll use them throughout.

---

## 1.4 How do we measure "fast"? Time & space complexity

Here's a natural first instinct: *"I'll just time my code with a stopwatch."*

```python
import time
start = time.time()
# ... do some work ...
print("took", time.time() - start, "seconds")
```

This is useful, but it has a fatal flaw for comparing algorithms: **the number you get depends on the machine, the language, and what else is running.**

- On a fast laptop, code runs 3x quicker than on an old one — but it's the *same algorithm*.
- The same code in C runs ~50x faster than in Python — but it's the *same algorithm*.

So the stopwatch measures the *machine*, not the *idea*. We need a way to measure the idea itself — something that stays the same regardless of hardware.

That's exactly what **complexity** gives us. Instead of asking "how many seconds?", we ask:

> **As the input gets bigger, how much more work does the algorithm do?**

That's the whole game. Notice the question is about **growth**, not raw speed. An algorithm that's slow-but-stays-slow and one that's fast-now-but-explodes on big inputs are very different, and complexity tells them apart.

### Time vs. space

- **Time complexity** = how the *amount of work* grows as input grows.
- **Space complexity** = how the *extra memory used* grows as input grows.

We usually care about time more, but space matters too — for example, a solution might be fast but use so much memory it crashes on a large input.

---

## 1.5 Big O notation — the basics

**Big O** is the language we use to describe growth. When you write `O(n)`, you're saying: *"This algorithm's work grows in proportion to the input size `n`."*

Let's build it up with real, memorable examples.

### The input size, `n`

First, what is `n`? It's whatever "amount of stuff" the input has:

- Searching a list of 100 names → `n = 100`.
- Sorting an array of 5,000 numbers → `n = 5000`.
- Processing a string of 20 characters → `n = 20`.

### The common complexities, from best to worst

| Big O | Name | Meaning in one line | Everyday example |
|---|---|---|---|
| `O(1)` | Constant | Same work no matter how big the input | Grabbing the first page of a book |
| `O(log n)` | Logarithmic | Work shrinks as the input grows (you halve the problem each step) | Finding a word in a dictionary by flipping to the middle |
| `O(n)` | Linear | Twice the input, twice the work | Reading every page of a book |
| `O(n log n)` | Linearithmic | Slightly more than linear | Efficient sorting (Python's `sorted`) |
| `O(n²)` | Quadratic | Twice the input, **four times** the work | Comparing every guest at a party with every other guest |
| `O(2ⁿ)` | Exponential | Adding one item **doubles** the work | Trying every possible subset of a set |

### Seeing the difference with numbers

This table is the single most useful thing in the chapter. Look at how the columns race apart as `n` grows:

| `n` | `O(1)` | `O(log n)` | `O(n)` | `O(n log n)` | `O(n²)` | `O(2ⁿ)` |
|---:|---:|---:|---:|---:|---:|---:|
| 10 | 1 | 3 | 10 | 33 | 100 | 1,024 |
| 100 | 1 | 7 | 100 | 664 | 10,000 | 10³⁰ |
| 1,000 | 1 | 10 | 1,000 | 10,000 | 1,000,000 | astronomical |
| 1,000,000 | 1 | 20 | 1,000,000 | 20,000,000 | 1,000,000,000,000 | useless |

The takeaway: **`O(n²)` and `O(2ⁿ)` blow up.** For large inputs, no amount of a faster computer saves them. Picking the right complexity is often the difference between "works" and "impossible."

### A rough speed sanity check

A modern computer does roughly **100 million simple operations per second** (order of magnitude; don't hold me to it). That means:

- `n = 1,000` with `O(n²)` = 1,000,000 ops → instant.
- `n = 100,000` with `O(n²)` = 10,000,000,000 ops → **about 100 seconds.** Too slow.
- `n = 100,000` with `O(n)` = 100,000 ops → instant.

So when you read a problem and see "the array can have up to 100,000 elements," you immediately know: *a double loop (`O(n²)`) is off the table.* This instinct — reading the constraints and knowing which complexity is allowed — is a superpower. You'll use it constantly.

> **Rule of thumb:** if the maximum `n` is…
> - up to ~1,000 → `O(n²)` is usually fine
> - up to ~10⁵ → you need `O(n log n)` or better
> - up to ~10⁶ or more → you need `O(n)` or `O(log n)`

---

## 1.6 How to figure out the Big O of your own code

You don't need calculus. Just a few rules of thumb. We'll use small code snippets.

### Rule 1: Drop the constants

If your code does `3n` operations, we call it `O(n)`. Constant multipliers don't change the *shape* of growth, so we throw them away.

```python
for x in items:      # n operations
    print(x)
for x in items:      # n operations
    print(x)
# Total: 2n → we write O(n), NOT O(2n)
```

### Rule 2: Drop the smaller terms

If your code does `n² + 100n + 50` operations, we call it `O(n²)`. When `n` is large, the `n²` term dwarfs everything else.

```python
for i in items:          # O(n)
    print(i)
for i in items:          # O(n²) total — this nested part dominates
    for j in items:
        print(i, j)
# The n² part wins → O(n²)
```

### Rule 3: A single loop over the input is `O(n)`

```python
def find_max(nums):
    biggest = nums[0]
    for x in nums:              # one loop through n items
        if x > biggest:
            biggest = x
    return biggest
# O(n) — work grows in step with the input
```

### Rule 4: A loop inside a loop is usually `O(n²)`

```python
def has_duplicate(nums):
    for i in range(len(nums)):          # for each item...
        for j in range(i + 1, len(nums)):  # ...compare to all the rest
            if nums[i] == nums[j]:
                return True
    return False
# O(n²) — the comparisons grow with n × n
```

### Rule 5: Cutting the input in half each step is `O(log n)`

```python
def count_halvings(n):
    steps = 0
    while n > 1:
        n = n // 2          # input shrinks by half every step
        steps += 1
    return steps
# count_halvings(1_000_000) = 20. Even a billion gives ~30.
# That's why O(log n) is astonishingly fast.
```

### Rule 6: Accessing an item by its index is `O(1)`

```python
def second_item(nums):
    return nums[1]          # jumping to a known position is one step,
                            # regardless of how long the list is
# O(1)
```

### Putting it together — a worked example

```python
def example(nums):
    total = 0
    for x in nums:              # O(n)
        total += x

    nums.sort()                 # O(n log n)  (see Part 5)

    for i in range(len(nums)):  # O(n²)
        for j in range(len(nums)):
            pass

    return total
```

Which part dominates? `O(n)` and `O(n log n)` are both smaller than `O(n²)`, so the whole function is **`O(n²)`**. When several parts run one after another, you **add** them and keep the biggest.

### Nested loops: multiply; sequential loops: add

```python
# Sequential (one after another): ADD
for x in a: ...     # n
for y in b: ...     # m
# Total: O(n + m)

# Nested (one inside another): MULTIPLY
for x in a:         # n
    for y in b:     # m
        ...
# Total: O(n × m)
```

> **Beginner trap:** if a function takes two different inputs, use two variables. Looping over list `A` (size `n`) and then over list `B` (size `m`) is `O(n + m)`, **not** `O(n)`. Interviewers love this distinction.

---

## 1.7 Space complexity — the memory side

Space complexity works the same way, but counts **extra memory** your algorithm uses (beyond the input itself).

```python
def sum_all(nums):
    total = 0                 # just one extra variable
    for x in nums:
        total += x
    return total
# Space: O(1) — no matter how big nums is, we only added 'total'
```

```python
def double_all(nums):
    result = []               # a new list that grows to size n
    for x in nums:
        result.append(x * 2)
    return result
# Space: O(n) — we allocated an extra list as big as the input
```

**Recursion uses memory too.** Every time a recursive function calls itself, Python remembers where it was — stacking up "unfinished work." So a function that recurses `n` levels deep uses `O(n)` space even if it has no lists. (We'll see this vividly in Part 7.)

A tricky idea handled simply: an algorithm can be `O(1)` space even if it reuses an existing list. "Extra space" means *new* memory, not space that already existed.

---

## 1.8 Algorithmic vs. Pythonic optimization

This distinction trips up beginners, and interviewers test it, so let's be precise. There are two totally different ways to make code faster:

**Algorithmic optimization** — changing the *idea*, so the code's growth rate improves. This is the powerful one. It can make code 1,000x or 1,000,000x faster.

```python
# Before: O(n²) — compare every pair
def has_duplicate_slow(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

# After: O(n) — one pass using a set
def has_duplicate_fast(nums):
    return len(set(nums)) < len(nums)
```

**Pythonic optimization** — keeping the same idea but writing it in a way Python runs faster. These gains are smaller (maybe 2x–50x) and don't change the growth rate.

```python
# Before: a manual loop with append
squares = []
for x in range(1000):
    squares.append(x * x)

# After: a list comprehension — same idea, less overhead
squares = [x * x for x in range(1000)]
```

**The order matters: fix the algorithm first, style second.**

Why? If your algorithm is `O(n²)` and you micro-optimize the syntax, you might get it 3x faster — but it's *still* `O(n²)` and still dies on large inputs. Fixing the algorithm takes it to `O(n)`, which scales to millions. A 3x gain is irrelevant next to a growth-rate gain.

```python
# This is STILL O(n²) no matter how "clean" you make it:
def still_slow(nums):
    return any(
        nums[i] == nums[j]
        for i in range(len(nums))
        for j in range(i + 1, len(nums))
    )
# Fancy syntax, same exploding algorithm.
```

**Rule of thumb:**
- In interviews, focus on the **algorithm** (the Big O). Clean syntax is a bonus, not the point.
- In real production code, once the algorithm is right, reach for Python's built-ins (`set`, `sorted`, `sum`, comprehensions) — they're written in fast C.

Two more Pythonic wins worth knowing now, because beginners hit both:

```python
# Membership: list vs set
if x in my_list:    # O(n) — scans every item
if x in my_set:     # O(1) — instant, thanks to hashing (Part 6)

# Building a string: += in a loop vs join
s = ""
for word in words:
    s += word       # O(n²) — each += makes a whole new string
s = "".join(words)  # O(n) — build once
```

---

## 1.9 Recap — test yourself

Cover the right column first, then check.

1. **Data structure** → a way of arranging data.
2. **Algorithm** → a step-by-step recipe that turns input into output.
3. **Why complexity instead of a stopwatch?** → A stopwatch measures the machine; complexity measures the *idea*, independent of hardware.
4. **What does Big O describe?** → How work grows as the input grows.
5. **`O(1)`** → constant work regardless of input size.
6. **`O(n)`** → work grows in step with input.
7. **`O(n²)`** → a loop inside a loop; work grows with n × n.
8. **`O(log n)`** → input is halved each step; extremely fast.
9. **Do you keep constants like `2n`?** → No; drop them → `O(n)`.
10. **Two separate loops over the same input** → `O(n)` (added, then constants dropped).
11. **A loop over `A` (size n) then a loop over `B` (size m)** → `O(n + m)`.
12. **Nested loop over two lists of sizes n and m** → `O(n × m)`.
13. **Space complexity of a single accumulator variable** → `O(1)`.
14. **Space used by recursion** → grows with recursion depth.
15. **Algorithmic vs Pythonic** → growth-rate change vs constant-factor change; fix the algorithm first.

---

## 1.10 Tasks (do these before moving on)

These match the `basics/` folder in the repo.

1. **Find max and min in a list** without using `max()` or `min()`.
   Write a function `find_max_min(nums)` that returns both. What is its time complexity?

2. **Compare `append` vs `insert(0, x)`.**
   Time these two snippets on a list built up to 100,000 elements and see which is slower:
   ```python
   # A
   lst = []
   for i in range(100_000):
       lst.append(i)

   # B
   lst = []
   for i in range(100_000):
       lst.insert(0, i)
   ```
   Which is `O(n)` overall, and which is `O(n²)`? Explain why using what you learned.

3. **Analyze this function's complexity** (don't guess — reason it out):
   ```python
   def mystery(nums):
       count = 0
       for x in nums:
           if x in nums:
               count += 1
       return count
   ```
   What's the time complexity, and what's the single change that makes it `O(n)`?

4. **Classify each** as `O(1)`, `O(n)`, `O(n²)`, or `O(log n)`:
   - Reading `nums[-1]`
   - Summing a list with a loop
   - Checking every pair in a list for equality
   - Repeatedly halving a number until it reaches 1

5. **Set up your project (later).** When you get to the code folders, everything from this chapter lives in `basics/`. There's a starter file `max_and_min.py` and `compare_append_insert.py` there — run them.

<details>
<summary>Answers (peek only after trying)</summary>

**1.** Iterate once, tracking the running biggest and smallest → **`O(n)`**, one pass.

**2.** A (`append`) is `O(n)` overall — each append adds to the end in ~1 step. B (`insert(0, i)`) is `O(n²)` — every insert pushes the whole list one slot to the right, so `n` inserts cost `1 + 2 + ... + n ≈ n²/2`.

**3.** `O(n²)`. The `x in nums` check scans the entire list each time (that's `O(n)`), inside a loop that runs `n` times. Fix: turn `nums` into a set once (`lookup = set(nums)`), then `x in lookup` is `O(1)` → total `O(n)`.

**4.** `O(1)`, `O(n)`, `O(n²)`, `O(log n)`.

**5.** Run the files and read the printed timings.
</details>

---

**Next:** [Part 2 — Arrays (Lists)](01-arrays-lists.md)
