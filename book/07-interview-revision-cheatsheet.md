# Part 8 — The Last-Minute Interview Revision

*One document to read the night before (and the hour before) an interview. It compresses every part of this book into the facts, tricks, and answers you need to recall fast. Nothing new here — just everything, sharpened.*

**How to use this:** skim the tables first (they're the core). Then read the Q&A out loud, covering the answers. Any question you can't answer in two sentences is a topic to reopen in the full chapter.

---

## 8.1 The 30-second complexity recall

| Big O | Name | Grows like | You'll see it in |
|---|---|---|---|
| `O(1)` | Constant | Flat | Index access, hash lookup |
| `O(log n)` | Logarithmic | Halves | Binary search |
| `O(n)` | Linear | Straight | One loop / one pass |
| `O(n log n)` | Linearithmic | Slightly above linear | Good sorting |
| `O(n²)` | Quadratic | Steep | Nested loops over same data |
| `O(2ⁿ)` | Exponential | Doubles per item | All subsets |
| `O(n!)` | Factorial | Explodes | All permutations |

**Memory hook:** *1, log, n, n log n, n², 2ⁿ, n!* — say it in that order.

**Feasibility from the constraints:**
- `n ≤ 15` → `O(2ⁿ)` / `O(n!)` is fine.
- `n ≤ 500` → `O(n³)` ok.
- `n ≤ 5,000` → `O(n²)` ok.
- `n ≤ 10⁵–10⁶` → need `O(n log n)` or better.
- `n ≥ 10⁷` → need `O(n)` or `O(log n)`.

---

## 8.2 The Python operation cost table (know this cold)

| Operation | Cost | Note |
|---|---|---|
| `lst[i]`, `lst[-1]` | `O(1)` | The array superpower |
| `len(lst)` | `O(1)` | Stored, not counted |
| `lst.append(x)` | `O(1)` amortized | Add at end |
| `lst.pop()` | `O(1)` | Remove from end |
| `lst.insert(0, x)` / `lst.pop(0)` | `O(n)` | Shifts everything — avoid in loops |
| `x in lst` | `O(n)` | Linear scan |
| `lst.sort()` / `sorted()` | `O(n log n)` | Timsort |
| `lst[a:b]` | `O(b-a)` | Makes a new list |
| `x in dict` / `x in set` | `O(1)` avg | The big win |
| `dict[k]`, `dict[k]=v` | `O(1)` avg | — |
| `x in deque` | `O(n)` | Membership is linear |
| `deque.append/pop/appendleft/popleft` | `O(1)` | Both ends fast |
| `deque[i]` (middle) | `O(n)` | — |
| `heappush` / `heappop` | `O(log n)` | Not covered here but worth knowing |
| `"".join(list)` | `O(total)` | Never `+=` in a loop (`O(n²)`) |
| `str += x` in a loop | `O(n²)` | Use `join` |

**Three facts that solve the most problems:**
1. `x in set/dict` is `O(1)` — `x in list` is `O(n)`.
2. `append`/`pop` at the **end** are `O(1)`; at index 0 are `O(n)`.
3. `"".join(parts)` beats `s += part` in a loop.

---

## 8.3 Which structure do I need? (decision box)

```
Need fast lookup / "have I seen this?"          → dict or set
Need to count things                            → dict / Counter
Need items sorted / in order                    → sort (sorted)
Need most-recent-first (undo, nesting, match)   → stack  (list append/pop)
Need oldest-first (levels, scheduling, BFS)     → queue  (deque append/popleft)
Need access by position                          → list / array
Need cheap insert/remove at the ends             → deque / linked list
Need to search sorted data fast                  → binary search
Need to split into smaller copies of itself      → recursion
```

**The single best optimization move:** find the slow inner loop (usually a repeated *search*) and replace it with a `set`/`dict` lookup. `O(n²) → O(n)`.

---

## 8.4 Rapid revision by topic

### Big O
- Measure **growth**, not seconds. Drop constants and lower terms.
- Sequential loops **add**; nested loops **multiply**.
- Two different inputs → two variables: `O(n + m)` or `O(n × m)`.
- Halving each step → `O(log n)`.
- Recursion costs `O(depth)` space.
- `append` is `O(1)` **amortized** (rare resizes averaged out).
- **Algorithmic** fix (change the idea) beats **Pythonic** fix (change the syntax) — always fix the algorithm first.

### Arrays (lists)
- `O(1)` index access; `O(n)` insert/delete at front or middle.
- `b = a` does **NOT** copy; use `a[:]`, `a.copy()`, `list(a)`.
- Shallow copy shares nested items; `copy.deepcopy` doesn't.
- A slice makes a **new** list (`O(k)`).
- Reverse in place with two pointers (`O(n)` time, `O(1)` space).
- Use `deque` when you insert/remove at the front.

### Linked lists
- Node = `data` + `next` (+ `prev` if doubly). The list is just the `head`.
- Traverse: `cur = head; while cur: ...; cur = cur.next`.
- Prepend `O(1)`; append `O(n)` without a tail pointer, `O(1)` with one.
- No index access — getting item `k` is `O(k)`.
- **Reverse:** save `next`, flip `next`, advance `prev`/`cur`.
- **Slow/fast pointers:** find middle, detect cycle.
- **Dummy node** removes "head might change" edge cases.
- Python reality: lists usually beat linked lists in practice.

### Stacks & queues
- Stack = LIFO (add/remove at top); Queue = FIFO (add rear, remove front).
- List stack: `append` + `pop()` — **end only**.
- Linked stack: head = top.
- Queue with a list = trap (`pop(0)` is `O(n)`). Use `deque`: `append` + `popleft`.
- Circular queue: advance pointers with `% capacity`; track `count` to tell full vs empty.
- Stack → nesting/matching, undo, monotonic "next greater".
- Queue → BFS, level order, scheduling.

### Searching & sorting
- Linear search `O(n)` — any list. Binary search `O(log n)` — **sorted only**.
- Bubble/selection/insertion sorts are `O(n²)`; bubble & insertion have `O(n)` best case; selection never beats `O(n²)`.
- Binary search: `low <= high`, `mid = (low+high)//2`, then `mid ± 1`.
- `sorted(x)` returns a new list; `x.sort()` is in place (returns `None`).
- Use the `key=` argument to sort by a custom rule.
- Real code: always `sorted`/`.sort`.

### Hashing (dicts & sets)
- Turns search into compute: `hash(key) % slots` → `O(1)` average.
- Collisions: **chaining** (lists per slot) or **open addressing** (probe).
- Load factor ~0.75 → resize & rehash → amortized `O(1)`.
- Hashable = immutable (`int`, `str`, `tuple`). No `list`/`dict`/`set` keys.
- `hash(a) == hash(b)` whenever `a == b` (not the reverse).
- Frequency counting: `freq[x] = freq.get(x, 0) + 1` or `Counter`.
- Duplicate check: `len(set(x)) < len(x)`.
- Two Sum: store seen values, look up the complement in `O(1)`.
- Limits: no ordering, no range queries.

### Recursion
- Two parts: **base case** + **smaller recursive case**. Trust the recursion.
- The **call stack** grows with depth → `O(depth)` space; Python's limit is ~1000.
- No base case → `RecursionError`.
- Naive Fibonacci is `O(2ⁿ)` (repeated work); memoization makes it `O(n)`.
- Recursion → iteration: use a loop, or an explicit stack.
- Use recursion for self-similar/nested problems; iteration for deep or simple ones.

---

## 8.5 Interview tricks & gotchas (the traps that cost points)

1. **`b = a` is not a copy.** Interviewers watch for this. Say "I'll take a copy" and write `a[:]`.
2. **`pop(0)` / `insert(0, x)` in a loop = `O(n²)`.** Use `append`/`pop()` or `deque`.
3. **Building strings with `+=` in a loop is `O(n²)`.** Use `"".join`.
4. **`x in list` in a loop is `O(n²)`.** Build a `set` once.
5. **Binary search needs sorted data** — always confirm or sort first.
6. **Off-by-one in binary search.** Use `while low <= high` and `mid ± 1`.
7. **`.sort()` returns `None`.** Don't assign it.
8. **Mutating a list while iterating it** skips elements. Iterate a copy.
9. **`range` upper bound is exclusive.** `range(n)` is `0..n-1`.
10. **Integer division `//` vs `/`.** Index math needs `//`.
11. **Empty input first.** `if not nums: return ...` before touching `[0]`.
12. **Deleting the head** in a linked list — handle it (or use a dummy node).
13. **Forgetting to advance** in a linked-list traversal → infinite loop.
14. **Two separate inputs = two variables** (`n + m`, not `2n`).
15. **State the complexity out loud** at the end — it's graded.
16. **`deque` has no `.peek()`** — use `q[0]`.
17. **A `set` has no order** — don't rely on it.
18. **Recursion depth can crash** — know when to convert to iteration.
19. **Return early** where possible; it simplifies reasoning and code.
20. **Clarify constraints before coding** — it tells you which complexity is allowed.

---

## 8.6 Core patterns, as templates

### 1. Hash lookup — "have I seen this?"
```python
seen = set()
for x in nums:
    if x in seen:
        return True        # or handle the duplicate/pair
    seen.add(x)
```

### 2. Frequency counting
```python
from collections import Counter
counts = Counter(items)                 # one pass
# manual: counts[x] = counts.get(x, 0) + 1
```

### 3. Two Sum (complement lookup)
```python
seen = {}
for i, x in enumerate(nums):
    if target - x in seen:
        return [seen[target - x], i]
    seen[x] = i
```

### 4. Two pointers
```python
i, j = 0, len(nums) - 1
while i < j:
    # compare nums[i], nums[j]; move one pointer inward
    i += 1          # or j -= 1 depending on the comparison
```

### 5. Sliding window (longest/shortest subarray)
```python
left = best = 0
window = {}                     # or a running sum
for right, x in enumerate(nums):
    # add x to window
    while <window invalid>:
        # remove nums[left] from window; left += 1
        left += 1
    best = max(best, right - left + 1)
```

### 6. Binary search (on a sorted list)
```python
low, high = 0, len(nums) - 1
while low <= high:
    mid = (low + high) // 2
    if nums[mid] == target: return mid
    elif nums[mid] < target: low = mid + 1
    else: high = mid - 1
return -1
```

### 7. Monotonic stack (next greater element)
```python
result = [-1] * len(nums)
stack = []                      # indices, values decreasing
for i, x in enumerate(nums):
    while stack and nums[stack[-1]] < x:
        result[stack.pop()] = x
    stack.append(i)
```

### 8. Recursion template
```python
def solve(problem):
    if <base case>:
        return <direct answer>
    return <combine>(solve(<smaller problem>))
```

---

## 8.7 Classic problems — approach + complexity

| Problem | Approach | Time |
|---|---|---|
| Two Sum | Hash map of value → index | `O(n)` |
| Contains Duplicate | Set | `O(n)` |
| Valid Parentheses | Stack | `O(n)` |
| Merge Two Sorted Lists | Two pointers | `O(n + m)` |
| Reverse Linked List | Three pointers | `O(n)` |
| Linked List Cycle | Slow/fast pointers | `O(n)` |
| Middle of Linked List | Slow/fast pointers | `O(n)` |
| Binary Search | Halve the range | `O(log n)` |
| Search Insert Position | Binary search | `O(log n)` |
| Merge Sorted Array | Two pointers | `O(n + m)` |
| Remove Duplicates (sorted) | Read/write pointers | `O(n)` |
| Move Zeroes | Two pointers | `O(n)` |
| Valid Anagram | Frequency count | `O(n)` |
| First Unique Character | Frequency count | `O(n)` |
| Group Anagrams | Dict keyed by sorted word | `O(n k log k)` |
| Longest Substring w/o Repeat | Sliding window + set/dict | `O(n)` |
| Max Subarray (Kadane) | Running best | `O(n)` |
| Next Greater Element | Monotonic stack | `O(n)` |
| Factorial / Fibonacci | Recursion (+ memo) | `O(n)` |
| Reverse String | Two pointers / recursion | `O(n)` |

---

## 8.8 Q&A — the questions you'll actually be asked

Answers are kept to what you'd *say*. Cover the right side and test yourself.

### Big O & efficiency

1. **What does Big O measure?** → How the work grows as input grows; ignores hardware and constants.
2. **Why drop constants?** → They depend on hardware; growth rate doesn't.
3. **Difference between `O(n)` and `O(n log n)`?** → `n log n` has an extra logarithmic factor (typically from sorting/divide-conquer); slightly worse, both fine at scale.
4. **Complexity of a loop inside a loop?** → `O(n²)` if both iterate `n`.
5. **Two separate input arrays, processed one after another?** → `O(n + m)`.
6. **What is amortized `O(1)`?** → Expensive steps are rare; averaged over many operations the cost is constant (e.g., `list.append`).
7. **Space complexity of recursion?** → `O(depth)` — one stack frame per level.
8. **Best vs worst case — which do you report?** → Worst case by default; mention best/average when relevant.
9. **Algorithmic vs Pythonic optimization?** → Algorithmic changes the growth rate; Pythonic changes constant factors. Fix the algorithm first.

### Arrays & lists

10. **Why is list index access `O(1)` but insert `O(n)`?** → Contiguous memory gives instant indexing; inserting shifts later elements.
11. **How do you copy a list safely?** → `a[:]`, `a.copy()`, or `list(a)`. `b = a` just aliases.
12. **Shallow vs deep copy?** → Shallow shares nested objects; `deepcopy` clones them recursively.
13. **Reverse a list in place?** → Two pointers swapping from the ends, `O(n)`/`O(1)`.
14. **Why does `x in list` cost `O(n)`?** → It scans element by element.
15. **How to make membership fast?** → Put the data in a `set`.
16. **Does slicing copy?** → Yes, a new list of size `k` → `O(k)`.

### Linked lists

17. **Array vs linked list?** → Array: `O(1)` index, bad middle insert. Linked list: cheap end insert/remove, no index access.
18. **How do you traverse a linked list?** → `cur = head; while cur: ...; cur = cur.next`.
19. **How do you reverse a singly linked list?** → Three pointers: save `next`, flip `next` to `prev`, advance both; return `prev` as new head. `O(n)`/`O(1)`.
20. **How do you detect a cycle?** → Slow/fast pointers; if they meet, there's a cycle.
21. **How do you find the middle?** → Slow/fast pointers; when fast ends, slow is at the middle.
22. **Why a dummy node?** → Removes special cases when the head might change.
23. **Why are Python linked lists often slower than lists?** → Per-node object overhead and scattered memory.

### Stacks & queues

24. **Stack vs queue?** → Stack LIFO (top only); queue FIFO (add rear, remove front).
25. **How do you implement a stack in Python?** → List with `append`/`pop()` (end only), or a linked list with head as top.
26. **Why not implement a queue with a list?** → `pop(0)` shifts everything → `O(n)` per dequeue. Use `deque`.
27. **What's a circular queue and why?** → A fixed array where pointers wrap with `% capacity`; avoids wasted slots and shifting.
28. **When is a stack the answer?** → Nesting/matching, undo, monotonic "next greater", DFS.
29. **When is a queue the answer?** → BFS/level order, scheduling, fairness by arrival.

### Searching & sorting

30. **Linear vs binary search?** → Linear `O(n)` any list; binary `O(log n)` but **needs sorted data**.
31. **Condition for binary search?** → The data must be sorted.
32. **Name three `O(n²)` sorts.** → Bubble, selection, insertion.
33. **Which `O(n²)` sort is fastest on nearly-sorted data?** → Insertion sort (best case `O(n)`).
34. **Which sort has the best best-case?** → Bubble and insertion both `O(n)` on sorted input.
35. **Which sort is fastest overall in Python?** → `sorted()`/`.sort()` (Timsort, `O(n log n)`, fast C).
36. **`sorted()` vs `.sort()`?** → `sorted()` returns a new list; `.sort()` sorts in place and returns `None`.
37. **How do you sort by a custom rule?** → `sorted(items, key=...)`, e.g. `key=len` or `key=lambda p: p[1]`.

### Hashing

38. **How does a hash table achieve `O(1)`?** → `hash(key)` computes the slot directly; no scanning.
39. **What is a collision and how is it handled?** → Two keys map to one slot; handle by chaining or open addressing.
40. **What is the load factor?** → Items ÷ slots; keep it low (~0.75), else resize and rehash.
41. **What can be a dict key?** → Any immutable, hashable object (int, str, tuple). Never a list or dict.
42. **Why can't a list be a key?** → It's mutable; its hash could change after insertion.
43. **Relationship between `dict` and `set`?** → A set is a dict with keys only.
44. **How do you count frequencies?** → `freq[x] = freq.get(x, 0) + 1` or `collections.Counter`.
45. **How do you check for duplicates?** → `len(set(x)) < len(x)`.
46. **Two Sum in `O(n)`?** → Store seen values; check `target - x` in the map.
47. **Two things hash tables can't do?** → Ordered iteration and range queries.

### Recursion

48. **What is recursion?** → A function solving a problem by calling itself on a smaller version.
49. **Two required parts?** → Base case and a smaller recursive case.
50. **What happens without a base case?** → Infinite recursion → `RecursionError` (stack overflow).
51. **What's the call stack?** → The stack of paused calls; grows with recursion depth.
52. **Why is naive Fibonacci slow?** → It recomputes the same subproblems → `O(2ⁿ)`.
53. **How do you fix it?** → Memoization (cache results) → `O(n)`.
54. **Recursion vs iteration?** → Recursion is elegant for self-similar/nested problems but uses `O(depth)` memory; iteration is safer for deep/simple loops.
55. **Convert recursion to iteration?** → Use a loop (for tail-like recursion) or an explicit stack.

### Problem solving & interviews

56. **First step on any problem?** → Restate it and clarify constraints.
57. **Why state brute force first?** → It shows understanding and gives a baseline complexity to improve.
58. **How do you choose a data structure?** → Identify the bottleneck (often repeated search) and pick the structure that makes it cheap.
59. **What should you always say at the end?** → The time and space complexity.
60. **Name edge cases to always check.** → Empty, single element, duplicates, negatives, all-equal, max-size input.

---

## 8.9 The edge-case checklist (run this before saying "done")

- [ ] Empty input (`[]`, `""`, `None`)?
- [ ] One element?
- [ ] Two elements?
- [ ] All elements equal?
- [ ] Already sorted / reverse sorted?
- [ ] Duplicates present?
- [ ] Negatives / zero / large numbers?
- [ ] Target not present?
- [ ] Result at the very start or very end?
- [ ] Did I handle the head/first index?

---

## 8.10 How to behave in the interview (the process is graded)

1. **Restate** the problem and **ask about constraints** (input size? sorted? duplicates?).
2. **Give a small example** and confirm the expected output.
3. **State a brute-force solution + its complexity** out loud.
4. **Identify the bottleneck** ("this inner search is `O(n)`").
5. **Propose the better structure** and why.
6. **Dry-run on your example**, then **write the code**.
7. **Test edge cases** using the checklist above.
8. **State final time and space complexity.**
9. If asked "can you do better?" — go back to the bottleneck.

**Do:** think out loud, ask clarifying questions, write clean names, test.
**Don't:** jump straight to code, stay silent, claim `O(1)` without justification, ignore edge cases.

---

## 8.11 One-screen memory dump (read this 10 minutes before)

```
Complexity order:  1  <  log n  <  n  <  n log n  <  n²  <  2ⁿ  <  n!
Sequential add, nested multiply.
Different inputs → different variables.

list:    index O(1) | append/pop() O(1) | insert(0)/pop(0) O(n) | x in O(n)
dict/set: lookup/insert O(1) avg | keys immutable | set = dict of keys
deque:   both ends O(1) | middle O(n) | queue = append + popleft
stack:   append + pop (end only) | LIFO | nesting, undo, next-greater
queue:   FIFO | levels/BFS | never list.pop(0)

Search:  linear O(n) any | binary O(log n) needs SORTED
Sorts:   bubble/selection/insertion O(n²) | sorted()/sort() O(n log n) USE THIS
Copy:    b = a is NOT a copy | a[:] / a.copy() / list(a)
String:  "".join(parts), never += in a loop

Hash:    hash(key) % slots → O(1) | collisions: chaining / probing
Freq:    freq.get(x, 0) + 1  or  Counter
2-sum:   seen = {} ; if target-x in seen
Dup:     len(set(x)) < len(x)

Recursion: base case + smaller call | O(depth) space | memoize repeats
Fibo:    naive O(2ⁿ) → memo O(n) → iterative O(n)/O(1)

Always:  restate → brute force → bottleneck → structure → code → test → state complexity
```

---

**Previous:** [Part 7 — Recursion & Problem Solving](06-recursion-and-problem-solving.md) · **Back to:** [Book index](README.md)
