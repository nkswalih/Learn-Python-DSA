# Part 2 — Arrays (Lists)

*Arrays are the most fundamental data structure in all of computing. In Python, an array is called a `list`. This chapter is about what a list really is under the hood, what each operation costs, and how to use it without accidentally writing slow code.*

---

## 2.1 What is an array?

An **array** is a row of items stored **side by side in memory**, in order, where each item sits at a numbered position called an **index**.

```
 Index:   0      1      2      3      4
        ┌──────┬──────┬──────┬──────┬──────┐
 Value: │  10  │  20  │  30  │  40  │  50  │
        └──────┴──────┴──────┴──────┴──────┘
```

Two facts follow from "stored side by side," and they explain almost everything:

1. **You can jump to any position instantly.** To get index 3, the computer computes where index 3 lives and goes straight there. It does *not* walk past items 0, 1, 2. This is `O(1)` access — the array's superpower.
2. **Inserting or removing in the middle is expensive.** Because items are packed tightly, if you remove index 1, everything after it has to shift left to close the gap.

```
Remove index 1 (value 20):

 Before:  [10][20][30][40][50]
 After:   [10][30][40][50]        ← 30,40,50 each moved one slot left
```

That shifting is why middle insert/delete is `O(n)`.

---

## 2.2 Python's list is a **dynamic** array

A plain array from older languages has a fixed size — you must say "I want room for 10 items" upfront. Python's list is smarter: it grows automatically as you add items. That's the "dynamic" part.

How does it grow? Python keeps a bit of **extra room** at the end (called the capacity) so it doesn't have to resize on every single append. When the room runs out, it allocates a bigger block and copies everything over.

```
Python list: size = how many items, capacity = how many fit before resizing

  list: size=3, capacity=5
  ┌────┬────┬────┬─────┬─────┐
  │ 10 │ 20 │ 30 │     │     │   ← two empty slots ready for appends
  └────┴────┴────┴─────┴─────┘
    ▲ index 0..2 filled      ▲ spare capacity

  Append 40, 50 → still O(1) each (room available)
  Append 60 → no room! Allocate a bigger block and COPY all 5 → O(n) this once
```

That rare "copy everything" moment is expensive, but it happens so rarely (the block roughly doubles each time) that the **average cost per append is `O(1)`**. This idea is called **amortized `O(1)`** — occasional expensive steps averaged over many cheap ones. You can safely treat `append` as fast.

---

## 2.3 The operations, one by one (with costs)

Let's go through everything you'll actually do with a list. Keep this table handy:

| Operation | Example | Cost | Why |
|---|---|---|---|
| Access by index | `lst[2]` | **`O(1)`** | Jump straight to the position |
| Access from the end | `lst[-1]` | `O(1)` | Counts backward, still one jump |
| Length | `len(lst)` | `O(1)` | Stored, not counted |
| Add to the end | `lst.append(x)` | `O(1)` amortized | Writes in a spare slot |
| Remove from the end | `lst.pop()` | `O(1)` | Nothing to shift |
| Insert at position | `lst.insert(1, x)` | **`O(n)`** | Everything after shifts right |
| Remove at position | `lst.pop(0)` / `del lst[0]` | **`O(n)`** | Everything after shifts left |
| Remove by value | `lst.remove(x)` | `O(n)` | Must search for it first, then shift |
| Search (is x in the list?) | `x in lst` | **`O(n)`** | Checks items one by one |
| Find index of a value | `lst.index(x)` | `O(n)` | Scans until found |
| Reverse | `lst.reverse()` | `O(n)` | Must touch every item |
| Sort | `lst.sort()` | `O(n log n)` | Part 5 |
| Slice | `lst[1:4]` | `O(k)` | Copies `k` items |
| Iterate | `for x in lst` | `O(n)` | Visits each once |

**Memorize the two starred ideas:** index access is instant, and inserting/removing at the **front or middle** is slow because of shifting. Almost every "why is my code slow?" list bug traces back to these.

---

## 2.4 Manipulating a list — insert, delete, search, reverse by hand

In real Python you'd use built-ins for these. But writing them by hand teaches you what's happening and prepares you for interviews, where you're often asked to do it manually.

### Manual insert at an index

```python
def insert_at(lst, index, value):
    """Insert value so it sits at 'index', shifting later items right."""
    lst.append(None)                       # make room at the end
    for i in range(len(lst) - 1, index, -1):
        lst[i] = lst[i - 1]                # shift each item one slot right
    lst[index] = value
    return lst

print(insert_at([10, 20, 30, 40], 2, 25))  # [10, 20, 25, 30, 40]
```

Trace the shifting for `[10, 20, 30, 40]`, inserting `25` at index 2 (going backward so we don't overwrite data we still need):

```
[10, 20, 30, 40, None]      append room
[10, 20, 30, 30, 40]        move index 3 → 4
[10, 20, 25, 30, 40]        place 25 at index 2
```

Backward shifting is the key trick — always move from the end toward the target, never the other way.

### Manual delete at an index

```python
def delete_at(lst, index):
    """Remove the item at 'index', shifting later items left."""
    for i in range(index, len(lst) - 1):
        lst[i] = lst[i + 1]                # pull each item one slot left
    lst.pop()                              # drop the now-duplicate last item
    return lst

print(delete_at([10, 20, 30, 40], 1))      # [10, 30, 40]
```

### Manual search

```python
def manual_search(lst, target):
    """Return the index of target, or -1 if not present."""
    for i in range(len(lst)):
        if lst[i] == target:
            return i                       # found — stop early
    return -1

print(manual_search([10, 20, 30], 30))     # 2
print(manual_search([10, 20, 30], 99))     # -1
```

### Manual reverse (this is a classic interview question)

```python
def reverse_in_place(lst):
    """Reverse using two pointers that walk toward each other."""
    i, j = 0, len(lst) - 1
    while i < j:
        lst[i], lst[j] = lst[j], lst[i]   # swap the two ends
        i += 1
        j -= 1
    return lst

print(reverse_in_place([1, 2, 3, 4, 5]))   # [5, 4, 3, 2, 1]
```

```
[1, 2, 3, 4, 5]
 ↑           ↑        swap 1 and 5  → [5,2,3,4,1]
    ↑     ↑           swap 2 and 4  → [5,4,3,2,1]
       ↑              pointers meet (i >= j) → stop
```

**Why two pointers?** Because we only need to swap `n/2` pairs. One pass, `O(n)` time, and **`O(1)` extra space** — we never build a new list. That "in-place" quality is often the point of the interview question.

---

## 2.5 Slicing — grabbing sub-lists

Slicing extracts a piece of a list. The syntax is `lst[start:stop:step]`:

```python
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

nums[2:5]      # [2, 3, 4]          start at 2, stop BEFORE 5
nums[:3]       # [0, 1, 2]          first three (start defaults to 0)
nums[7:]       # [7, 8, 9]          from 7 to the end
nums[-3:]      # [7, 8, 9]          last three
nums[::2]      # [0, 2, 4, 6, 8]    every 2nd item
nums[::-1]     # [9, 8, 7, ...]     reversed
```

**Two things beginners should know:**

1. **`stop` is exclusive.** `nums[2:5]` gives indices 2, 3, 4 — *not* 5. Think "start at 2, stop *just before* 5."
2. **Slicing never crashes on out-of-range.** `nums[5:100]` just gives `[5, 6, 7, 8, 9]`. Python clamps to the ends.

A slice **creates a new list** and copies the items, so it costs `O(k)` time and space for `k` items. Slicing out a huge chunk inside a loop can quietly eat memory and time — use it deliberately.

---

## 2.6 Copying lists — the #1 beginner trap

This causes more bugs than any other list topic. Read it twice.

```python
a = [1, 2, 3]

b = a            # ❌ NOT a copy! 'b' is another name for the SAME list.
b.append(4)
print(a)         # [1, 2, 3, 4]  — a changed too!
```

Why? In Python, `b = a` doesn't copy the list — it copies the *reference* (the "address") of the one list. Now both names point to the same list. Change it through one name, it changes for the other.

```
a = [1,2,3]
b = a

  a ──┐
      ├──▶  [1, 2, 3]     (one list, two names)
  b ──┘
```

To actually copy, use one of these:

```python
a = [1, 2, 3]

b = a[:]          # slice copy — new list
c = a.copy()      # same thing, clearer name
d = list(a)       # also a copy
```

This is a **shallow copy**: it makes a new outer list, but if the items are themselves lists, the inner lists are still shared. Watch:

```python
a = [[1, 2], [3, 4]]
b = a[:]                # shallow copy
b.append([9, 9])        # affects only b — new outer list
print(a)                # [[1, 2], [3, 4]]  ✅ a is safe

b[0][0] = 99            # but THIS reaches into a shared inner list!
print(a)                # [[99, 2], [3, 4]]  ❌ a changed too!
```

When a copy's contents are nested, use a **deep copy**:

```python
import copy
b = copy.deepcopy(a)    # recursively copies everything — fully independent
```

### `copy()` vs `[:]` — which to use?

They behave identically on lists. Use whichever reads better:

- `a.copy()` — clear intent, works on dicts and sets too.
- `a[:]` — idiomatic for lists and works on any sequence (strings, tuples).

**Rule of the chapter:** if you mean "a separate list," always write a copy explicitly. Never rely on `b = a`.

---

## 2.7 When arrays beat linked structures

We'll meet **linked lists** in Part 3, but you can already guess the trade-off. Here's the honest comparison:

| Situation | Winner | Why |
|---|---|---|
| Grab item #5000 | **Array (list)** | Instant (`O(1)`) vs a linked list's 5000 hops |
| Read items in order, one by one | **Array** | Memory is packed together — the CPU loves it |
| Add to the **end** a lot | **Array** | `append` is amortized `O(1)` |
| Add/remove at the **front** or middle | **Linked list** | No shifting, but see the caveat below |
| Binary search | **Array** | Needs instant indexing; impossible on a linked list |
| Almost everything in Python | **Array (list)** | See below |

**The practical truth:** in Python, use lists about 95% of the time. Linked lists have real advantages on paper, but in Python every node is a heavy object with overhead, so a hand-written linked list is usually *slower and larger* than a list even when the theory says it should win. You'll learn linked lists for interviews and for understanding — not because you'll reach for them in everyday Python.

Where arrays/lists shine, in one sentence: **when you mostly read by position and walk through items in order.** That's most programs.

---

## 2.8 Common beginner mistakes

1. **Thinking `b = a` copies a list.** It doesn't. Use `a[:]`, `a.copy()`, or `list(a)`.
2. **Using `insert(0, x)` or `pop(0)` in a loop.** Each is `O(n)`, so the loop is `O(n²)`. Use `append`/`pop()` at the end, or a `deque` (Part 4).
3. **Forgetting that `stop` in a slice is exclusive.** `nums[2:5]` is 3 items, not 4.
4. **Confusing `remove(x)` (removes by *value*) with `pop(i)` (removes by *index*).**
5. **Mutating a list while looping over it.** This skips items. Loop over a copy, or build a new list.
6. **Assuming `in` is fast.** `x in lst` is `O(n)`. If you check membership a lot, use a `set`.

---

## 2.9 Recap — test yourself

1. **Array** → items stored side by side, reached by index.
2. **`lst[i]` cost** → `O(1)` — jump straight there.
3. **`insert`/`pop` at the front cost** → `O(n)` — everything shifts.
4. **`append`/`pop()` at the end cost** → `O(1)` amortized.
5. **Why is `append` only "amortized"?** → It occasionally triggers a full copy when capacity runs out, but that's rare and averaged out.
6. **`x in lst` cost** → `O(n)` scan.
7. **Reverse a list in place** → two pointers from the ends, swap inward, `O(n)` time, `O(1)` space.
8. **Does `b = a` copy?** → No — two names, one list.
9. **How do you really copy a list?** → `a[:]`, `a.copy()`, or `list(a)`.
10. **Shallow vs deep copy** → shallow shares nested items; `deepcopy` copies everything.
11. **Does a slice copy?** → Yes — new list, `O(k)` cost.
12. **When do arrays beat linked lists?** → Reading by index and iterating in order.

---

## 2.10 Tasks (the `arrays/` folder)

1. **Implement insert at a given index** (by hand, no `list.insert`).
   `def insert_at(lst, index, value)` — shift items right, place the value.

2. **Implement delete at a given index** (by hand, no `list.pop(index)`).

3. **Reverse a list manually** (no `[::-1]`, no `.reverse`) using two pointers.

4. **Count how many times a value appears** using a single pass (no `.count`).

5. **Check if a list is a palindrome** (reads the same both ways) using two pointers.

6. **LeetCode-style problems** (in `arrays/`):
   - **Two Sum** — find two numbers that add to a target (uses a dict).
   - **Merge Sorted Array** — merge two already-sorted lists into one sorted list.
   - **Remove Duplicates** — from a sorted list, remove duplicates in place.

7. **Reusable helper file:** build `arrays/array_utils.py` containing your insert, delete, reverse, and search functions, so you can import and reuse them.

<details>
<summary>Hint for "Remove Duplicates (sorted)"</summary>

Use two pointers: one slow pointer `write` marking where the next unique value goes, one fast pointer `read` scanning ahead. When `lst[read]` differs from the last written value, copy it to `lst[write]` and advance `write`. This is `O(n)` and needs no extra space.
</details>

---

**Previous:** [Part 1 — Core Concepts & Big O](00-core-concepts-and-big-o.md) · **Next:** [Part 3 — Linked Lists](02-linked-lists.md)
