# DSA Mastery in Python — From Zero to Interview-Pro

> **A master document for people who want to actually understand Data Structures & Algorithms — not memorize them.**
> Built so you can read it front-to-back once, then rewind any section any time: before an interview, before a contest, or whenever a concept feels fuzzy.

---

## How to use this document

This is **not** a 30-day crash course. There is no schedule. There is one file, organized so you can enter at any point and leave with one solid skill.

**Rules of engagement (these make or break the whole thing):**

1. **Struggle first, read second.** When you hit an exercise or a problem sketch, spend 15–20 minutes trying it *before* reading on. The discomfort is the learning. Reading a solution you didn't earn teaches you almost nothing.
2. **Run every code block.** Python on your machine, in a REPL or a `.py` file. Change inputs. Break it. Code you haven't run is code you don't understand.
3. **Explain it out loud (Feynman pass).** After each chapter, close the file and explain the concept in plain words to an empty chair. Where you stall is exactly where you don't understand it yet.
4. **Use the recap boxes.** Every chapter ends with a one-line-per-concept recap. Cover the rest, read the bold terms, and recall the definition. That's active recall — the single most effective study technique known.
5. **Before an interview:** jump to [Part 9](#part-9--interviews--the-top-150), open the final revision checklist, and skim the pattern library in Part 8. That's the designed "rewind" path.

**Document map**

| Part | What's inside | Read when |
|---|---|---|
| [0](#part-0--foundations--mindset) | Why DSA, AI-era reality, companies, the learning method | First. Always first. |
| [1](#part-1--big-o--algorithm-efficiency) | Big O, complexity, Python's built-in costs | Second |
| [2](#part-2--core-data-structures) | Lists, linked lists, stacks, queues, hashing, strings | Core foundation |
| [3](#part-3--recursion--problem-solving-engine) | Recursion, backtracking, the problem-solving framework | The turning point |
| [4](#part-4--searching--sorting--two-pointers) | Search, all sorts, two pointers, sliding window | Interview gold |
| [5](#part-5--trees--heaps--tries) | Trees, BST, heap/priority queue, trie | Interview gold |
| [6](#part-6--graphs) | BFS, DFS, topo sort, Dijkstra, Union-Find | Interview gold |
| [7](#part-7--dynamic-programming--greedy) | Memoization, tabulation, knapsack, greedy | The hard-problem key |
| [8](#part-8--the-pattern-library) | 25+ named patterns: signal → template → problems | Revise often |
| [9](#part-9--interviews--the-top-150) | Interview process, Top 150 LeetCode list, revision checklist | The night before |

---

---

# Part 0 — Foundations & Mindset

## 0.1 What DSA actually is

Two words, two jobs.

**Data Structure** = a way of *arranging* data so that some operations become cheap.
**Algorithm** = a *procedure*, a finite sequence of instructions, that transforms input into output.

That's it. No mysticism. A data structure is a filing decision; an algorithm is a recipe.

But here's the part nobody tells beginners: **they are never chosen independently.** The data structure you pick *is* the algorithm you enable. Choose a hash map and "find the duplicate" becomes O(1) per lookup. Choose a sorted array and "find the range" becomes a binary search. Choose a heap and "give me the top-K" becomes O(n log k). Choosing the structure is already 70% of solving the problem.

### The core idea of the entire subject

> **Same problem. Different arrangement of data. Wildly different running time.**

Example — *find whether two numbers in a list add up to a target*:

```python
def two_sum_brute(nums, target):
    # Check every pair: n*(n-1)/2 comparisons
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return True
    return False                       # O(n^2)

def two_sum_hash(nums, target):
    seen = set()
    for x in nums:                     # One pass, set lookup is O(1)
        if target - x in seen:
            return True
        seen.add(x)
    return False                       # O(n)
```

Same input, same output, **quadratic vs linear**. On 100,000 numbers: the first runs ~5 billion operations (minutes), the second runs 100,000 (instant). DSA is the study of *why* that gap exists and *how* to create such gaps on demand.

## 0.2 Why DSA matters — the honest version

### Reason 1: It's how software stops being slow

Every system you've ever called "fast" is fast because someone made a structural choice:

| Product feature | DSA underneath |
|---|---|
| Autocomplete in a search bar | Trie / prefix tree |
| "People you may know" | Graph traversal + set intersection |
| GPS route | Dijkstra's / A* shortest path |
| News feed ranking | Heaps (top-K), hash maps (dedup) |
| Load balancer | Queue |
| Undo/redo in an editor | Stack |
| Spell checker | Hash set of words |
| Database indexes | B-Trees (generalized trees) |
| Cache eviction (LRU) | Hash map + doubly linked list |
| Task scheduler / rate limiter | Heap by time, queue by arrival |
| Version control (git merge) | Graphs + content hashing |
| Spam filtering | Naive Bayes over frequency maps |

You cannot optimize what you cannot see. DSA gives you the vocabulary to see *where* the time goes.

### Reason 2: It's the industry's filter — and it's not leaving

Interviewers don't ask DSA because they enjoy watching people sweat. They ask it because it's the **cheapest standardized signal** of:
- Can you break an unfamiliar problem into parts?
- Do you know the cost of the things you write?
- Can you reason about correctness under pressure?
- Do you have depth behind your framework-of-the-month experience?

### Reason 3: It makes you AI-proof (read this carefully — it's Part 0's most important section)

See next section.

## 0.3 DSA in the AI era — the real talk

You're learning this in 2026, when an AI will happily write `two_sum_hash` for you. So why learn it at all? Three honest truths:

### Truth 1: AI can write code, but it can't own your decisions

An AI assistant gives you *an* answer. It doesn't tell you whether that answer is O(n) or O(n²), whether it will melt at 10^6 inputs, whether a heap would beat a sort here, or whether the "clever" solution has a bug at the array boundary. **You are the reviewer, and a reviewer who can't derive the answer can't judge the answer.** Every hallucinated complexity claim slips past someone who doesn't know the material.

### Truth 2: The interview is AI-free by design

Every serious company removed the tool precisely *because* everyone was using it. The written test, the live coding round, the pair-programming session — no copilot in the room. DSA interviews are the last un-automatable skill check. In the AI era the interview bar went *up*, not down.

### Truth 3: AI is the best tutor ever — if you use it correctly

Here is the line between **using AI to learn** and **using AI to skip learning**:

| ✅ AI as TUTOR (does this) | ❌ AI as ANSWER MACHINE (never do this) |
|---|---|
| "Explain *why* this is O(n log n)" | "Write the solution to LeetCode 42" |
| "Give me a hint, not the answer — I've tried sliding window and it fails on `[1,2,1,3]`" | Paste your failed code → accept the fix → move on |
| "Generate 3 variations of this problem with different constraints" | Read the solution, think "makes sense", mark it done |
| "Find the bug in *my* reasoning: I think this loop is O(n), convince me otherwise" | Ask "is my solution optimal?" and trust "yes" |
| "Explain this recursion's call stack frame by frame" | Skim the output, never trace it yourself |

**The 20-minute rule:** struggle with a problem for 20 minutes unaided. Then, and only then, ask an AI for a *hint* (one sentence, no code). Struggle again. If still stuck, ask for the *approach in words* (still no code). Code is the last thing you ever look at — ideally written by you.

### Your AI-era workflow per problem

```
1. Read the problem. Restate it in your own words.
2. Brute force it in your head (or on paper). Name its complexity.
3. Ask: which pattern from Part 8 fits? Why?
4. Implement brute force. It's allowed to be ugly. Get it CORRECT first.
5. Identify the bottleneck (the nested loop? the repeated work?).
6. Ask yourself: what structure makes that bottleneck O(1)?
7. Optimize. Verify on 3 edge cases: empty, size 1, duplicates/overflow.
8. ONLY NOW compare with an editorial/AI — as a peer review, not a source.
9. If your solution differs, understand WHICH is better and why.
10. Next day: solve it again from blank. If you can't, it never counted.
```

**Self-test for whether you're learning or cheating:** *Could you solve a slightly different version of this problem tomorrow, with no memory of today's code?* If no — you memorized, you didn't learn.

## 0.4 Which companies ask DSA, and what they actually ask

Not every company runs the same gauntlet. Know which one you're facing.

### Tier map

| Tier | Examples | DSA weight | Typical difficulty | Rounds |
|---|---|---|---|---|
| **Big Tech / FAANG-tier** | Google, Meta, Amazon, Apple, Microsoft, Netflix, Adobe | Very heavy — 40–60% of hiring decision | Easy → Hard, mostly Medium+ | 3–5 rounds, 45–60 min each, pure DSA |
| **High-growth product** | Stripe, Databricks, Airbnb, Uber, Airbnb, Salesforce, Oracle, SAP | Heavy | Medium → Hard | 3–4 rounds |
| **AI labs & infra** | OpenAI, Anthropic, NVIDIA, scale-ups | Heavy on algorithms + systems | Medium → Hard, some math/probability | 4 rounds |
| **Unicorns / startups (funded)** | Series B–E product startups | Medium — 1–2 DSA rounds plus project deep-dives | Easy → Medium, rarely Hard | 2–3 rounds, practical bent |
| **Product companies (regional)** | Zoho, Swiggy, Flipkart, Zerodha, Razorpay, Byju's-tier | Medium-heavy | Medium | 3–4 rounds |
| **Service / consulting / SI** | TCS, Infosys, Wipro, Cognizant, Accenture | Aptitude-style basics, sometimes OOP | Easy, sometimes MCQ-based | Online assessment first |
| **Banks & fintech (backend)** | JPMorgan, Goldman, finance tech | Medium, sometimes probability/puzzles | Medium | 2–4 rounds |
| **Remote / international** | Anywhere-remote startups | Varies wildly; assume one DSA screen | Easy → Medium | 1–2 rounds |
| **Non-tech employers** | Any company with an engineering org now uses a DSA screen for "SDE" roles | Basic | Easy → Medium | 1 online assessment |

### What each round typically looks like

1. **Online assessment (OA):** 2–3 problems in 60–90 minutes. Usually Easy+Medium. Gate for everything else. Speed matters here — this is why pattern recognition (Part 8) is trained, not just understanding.
2. **Live coding round:** One problem, 30–45 minutes, you talk while typing. They care about: clarifying questions → brute force → optimize → code → test. The *process* is graded, not just the final answer.
3. **Hiring-manager / system round:** DSA appears as "design the data structure for X" (LRU cache, Twitter feed, calendar). That's DSA dressed as design.
4. **Bar-raiser / final:** One hard problem or two mediums, plus behavioral.

### Frequency ranking (what actually shows up, 2026–2028 expectations)

From most to least common:

1. **Hash map / set usage** — appears in some form in *most* problems
2. **Two pointers & sliding window** — the signature modern-screen pattern
3. **Binary search** (including on the answer)
4. **Trees** — traversals, max depth, LCA, validate BST
5. **Graph BFS/DFS** — grids especially (flood fill, islands)
6. **Recursion / backtracking** — subsets, permutations, combinations
7. **Stacks** — monotonic stack, parentheses, daily temperature
8. **Heaps** — top-K, merge K lists, median stream
9. **Dynamic programming** — 1D first, then 2D/grid, then knapsack
10. **Linked lists** — reverse, merge, cycle — classic but fading slightly
11. **Tries, Union-Find, segment trees** — rare, mostly at Big Tech Hard level

**Implication:** Parts 2, 4, 5, 6 are your highest-yield study. Part 7 (DP) is what separates offers from rejections at top companies.

## 0.5 The learning method — how this document is built (and how to read it)

This file uses a fixed structure everywhere so your brain stops re-orienting and starts recognizing.

### The concept block (used for every topic)

```
WHY      → what problem in the world creates this idea (motivation)
WHAT     → the definition in one paragraph
HOW      → mechanics, with a diagram you can trace with your finger
PROS     → what it makes fast
CONS     → what it makes slow or painful
COMPARE  → vs the alternative structure (table)
CODE     → runnable Python, from scratch, no black boxes
COST     → time/space complexity table for every operation
PATTERNS → which interview problems this structure powers
RECAP    → one-line-per-term summary for active recall
```

### Why this order (the science, briefly)

- **Motivation before mechanics.** Your brain stores information better when it knows *why it should care*. The WHY block creates a hook; the HOW block hangs on it.
- **Pros AND cons together.** Learning only advantages creates brittle knowledge — you'll reach for a hash map in a place a sorted array was right. Knowing *when each fails* is the expert skill.
- **Comparison tables.** Knowledge becomes usable only when it's *relational* — "A is faster but B is ordered" is far more retrievable than two isolated fact sheets.
- **Diagram → code → complexity.** Perception order: see it, run it, measure it. Three encodings of the same idea = three ways to remember it.
- **Recap for active recall.** Closing the file and re-deriving beats re-reading by a wide margin.

### Three-pass reading strategy

| Pass | What you do | Time |
|---|---|---|
| **Pass 1 — Orient** | Read WHY/WHAT/COMPARE/RECAP only. Skip code. Build the map. | Fast |
| **Pass 2 — Build** | Read everything, run all code, do the exercises. | Slow |
| **Pass 3 — Prove** | Re-solve the exercises from blank after a 2-day gap. | Test |

Most people only ever do Pass 1 and think they learned. They didn't.

### Schedule-agnostic spaced repetition (this replaces the "30-day plan")

No fixed calendar — instead, a **re-encounter rule**:

```
Learn topic  →  revisit next day  →  revisit after 3 days  →
revisit after 7 days  →  revisit after 14 days  →  monthly until it's boring
```

In practice: every time you open this file, before reading the new part, spend 5 minutes in the recap box of the *previous* part you read. That single habit is worth more than any schedule.

## 0.6 The 7-Step Problem-Solving Framework

This framework is used in every chapter of this document and is exactly what interviewers watch you execute. Learn it once, apply it 150 times.

```
┌──────────────────────────────────────────────────────────────┐
│  STEP 1 — PARROW: Paraphrase. Read aloud constraints.        │
│           Restate the problem in your own words.             │
│           Ask: input size? duplicates? sorted? mutability?    │
│                                                              │
│  STEP 2 — EXAMPLES: Work 2 concrete examples by hand.        │
│           Include edge cases: empty, single element,         │
│           all-equal, max/min values.                         │
│                                                              │
│  STEP 3 — BRUTE FORCE: State the dumbest correct solution    │
│           AND its complexity out loud. (Never skip this —     │
│           it anchors the interviewer and often scores.)       │
│                                                              │
│  STEP 4 — FIND THE BOTTLENECK: Name the expensive line.      │
│           Nested loop? Repeated work? Unsorted scan?         │
│           Scanning what you just sorted?                     │
│                                                              │
│  STEP 5 — MAP TO A PATTERN: Ask "what does this bottleneck   │
│           need?" → lookup? order? nearest? prefix sums?       │
│           → choose structure from Part 8's decision tree.     │
│                                                              │
│  STEP 6 — DRY RUN, THEN CODE: Trace your new approach on     │
│           the Step-2 example FIRST. Then implement.           │
│                                                              │
│  STEP 7 — TEST & MEASURE: empty / one / duplicates / max.    │
│           State final complexity. Say what you'd change       │
│           for 10^7 inputs.                                   │
└──────────────────────────────────────────────────────────────┘
```

### The bottleneck → structure decision tree (memorize this)

```
Need FAST lookup / dedup / "have I seen this?"     → dict / set
Need ORDER and NEIGHBORS of range [lo, hi]         → sorted array + binary search
Need FIRST / LATEST / UNPROCESSED in order          → queue (BFS), deque
Need MOST RECENT / UNDO / BALANCE / nesting        → stack
Need "largest/smallest K of stream"                → heap (heapq)
Need PARENT-CHILD / HIERARCHY / PREFIX             → tree / trie
Need CONNECTEDness / DISJOINT groups                → Union-Find
Need ALL CONNECTIONS / PATHS                        → graph (adj list)
Need EXHAUST ALL CHOICES (subsets, perms, paths)    → backtracking
Need REPEATED SUBPROBLEMS (count ways, min cost)    → memoization / DP
NEED ORDERED + fast insert/delete anywhere          → linked list (rarely)
REPEATED "next greater / span / brackets"           → stack (monotonic)
OVERLAPPING RANGES / PREFIX AGGREGATES              → prefix sums
```

This one table is the spine of Part 8 and the cheat-sheet you'll review before any interview.

---

---

# Part 1 — Big O & Algorithm Efficiency

## 1.1 WHY — what problem creates complexity theory?

A programmer says "my code is fast." Fast compared to what? On what input? On a laptop or a server? Without a *unit of speed that doesn't depend on hardware*, you can't compare solutions at all.

Big O is that unit. It answers one question:

> **As the input grows, how does the work grow?**

Hardware differences are a constant factor — a 3 GHz machine is ~2x a 1.5 GHz machine. Growth *rate* is not a constant factor: O(n²) on 1,000,000 items does **1,000,000,000,000** operations while O(n) does **1,000,000**. No hardware fixes a million-fold gap. Big O measures the part that matters.

## 1.2 WHAT — Big O notation, precisely

`O(f(n))` = "the running time grows **at most as fast as** f(n), ignoring constants."

- `O(n)` — doubling input roughly doubles time.
- `O(n²)` — doubling input roughly *quadruples* time.
- `O(log n)` — doubling input adds a *fixed* amount of time.
- `O(1)` — time doesn't depend on input size at all.

### The six rates that matter (memorize the shapes)

```
 Time
  │                                          ╱ O(2^n)   explodes
  │                                        ╱
  │                                      ╱   ╱ O(n^2)  n=1000 → 1e6
  │                                    ╱   ╱
  │                                ╱   ╱  ╱ O(n log n) n=1000 → ~1e4
  │                            ╱   ╱  ╱
  │                        ╱  ╱  ╱  ╱ O(n)       n=1000 → 1e3
  │                  ▁▁▁▁▁▁▁▁▁▁▁▁╱
  │        ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁╱ O(log n)      n=1000 → 10
  │▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ O(1)         n=1000 → 1
  └──────────────────────────────────────── n (input size)
```

| Name | Notation | n = 10³ | n = 10⁶ | Intuition |
|---|---|---|---|---|
| Constant | `O(1)` | 1 | 1 | Hash lookup, array index |
| Logarithmic | `O(log n)` | 10 | 20 | Binary search |
| Linear | `O(n)` | 1,000 | 1,000,000 | Single loop |
| Linearithmic | `O(n log n)` | ~10,000 | ~20,000,000 | Good comparison sort |
| Quadratic | `O(n²)` | 1,000,000 | 10¹² | Nested loops |
| Exponential | `O(2ⁿ)` | 10³⁰¹ | ∞ (unusable) | All subsets of n items |
| Factorial | `O(n!)` | ∞ | ∞ | All permutations of n items |

**Rule of thumb for feasibility:** a modern machine does roughly **10⁸ operations per second**.
- n = 100 → O(n²) is fine (10⁴ ops)
- n = 10⁵ → O(n²) is 10¹⁰, **too slow** (needs O(n log n) or better)
- n = 10⁶ → O(n log n) is required; O(n²) impossible
- n = 10⁷ → must be O(n) or O(n log n) with small constants

**This is why reading constraints first (Step 1 of the framework) solves half the problem:**

| Max n given in the problem | Required complexity |
|---|---|
| n ≤ 10–15 | O(2ⁿ) or O(n!) — brute force / backtracking |
| n ≤ 100–500 | O(n³) — sometimes DP over pairs |
| n ≤ 10,000 | O(n²) — DP over intervals, 2D grid |
| n ≤ 10⁵–10⁶ | O(n log n) — sorting, heap, binary search |
| n ≤ 10⁸+ | O(n) — one pass, two pointers, hash map |

## 1.3 HOW — computing Big O by hand

### The 5 rules

1. **Drop constants.** `3n` and `n/2` are both `O(n)`. Code:
   ```python
   for a in A:          # n
       print(a)
   for b in B:          # n
       print(b)
   # Total: 2n  →  O(n)   (NOT O(2n))
   ```
2. **Drop lower-order terms.** `n² + 100n + 5000` → `O(n²)`. The n² term wins for large n; the rest is noise.
3. **Different inputs = different variables.** The most common beginner mistake:
   ```python
   def f(A, B):                 # A has n elements, B has m elements
       for a in A:              # O(n)
           print(a)
       for b in B:              # O(m)
           print(b)
       # O(n + m)  — NOT O(n), NOT O(2n)
   ```
4. **Nested loops multiply, sequential loops add.**
   ```python
   for a in A:            # n
       for b in B:        # m  (runs n times)
           work()         # n*m
   # O(n * m); if m == n: O(n²)
   ```
5. **Watch what shrinks the input.** A loop that halves its remaining work is logarithmic:
   ```python
   i = 1
   while i < n:     # i: 1, 2, 4, 8, ...  → doubles each round
       i *= 2       # O(log n) rounds
   ```

### Worked examples (trace these with your finger)

```python
# (a) O(1) — index-based access
def get_middle(lst):
    return lst[len(lst) // 2]

# (b) O(n) — single pass
def total(lst):
    s = 0
    for x in lst:
        s += x
    return s

# (c) O(n²) — every pair
def has_duplicate_pair(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                return True
    return False

# (d) O(n) — inner loop shrinks (i advances, not resets!)
def adjacent_duplicates(lst):        # ← this one fools people
    for i in range(len(lst) - 1):
        if lst[i] == lst[i + 1]:
            return True
    return False
    # range() re-evaluates, but j doesn't exist — ONE loop. O(n)

# (e) O(log n) — divide and conquer
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            lo = mid + 1          # remaining size halves
        else:
            hi = mid - 1
    return -1

# (f) O(n log n) — sort dominates
def solve(lst):
    lst.sort()                # O(n log n)
    for x in lst:             # O(n)
        pass
    # O(n log n) + O(n) → O(n log n)

# (g) O(2^n) — every subset
def subsets(nums):
    if not nums:
        return [[]]
    without = subsets(nums[1:])       # includes element 0 or not...
    with_el = [[nums[0]] + s for s in without]
    return without + with_el
```

### The recurrence trick (for recursive code)

Count calls, then solve:

```python
def f(n):
    if n <= 1: return
    f(n - 1)      # one smaller call
    f(n - 1)      # one smaller call
```
`T(n) = 2·T(n-1) + O(1)` → doubles each level → **O(2ⁿ)**.

```python
def g(n):
    if n <= 1: return
    g(n // 2)     # halves
    g(n // 2)
```
`T(n) = 2·T(n/2) + O(1)` → log n levels × 2 work each → **O(n)**.

```python
def h(n):
    if n <= 1: return
    for _ in range(n): pass   # O(n) at this level
    h(n // 2)
```
`T(n) = T(n/2) + O(n)` → n + n/2 + n/4 + ... = **2n → O(n)**.

(Geometric series rule: `n + n/2 + n/4 + ... ≤ 2n`. This one pattern explains most divide-and-conquer costs.)

## 1.4 Best, average, worst, amortized

Reporting only worst case is honest but incomplete. Three lenses:

| Case | Question | Example (linear search for x) |
|---|---|---|
| **Best** | Happiest input | x is first element → `O(1)` |
| **Average** | Typical input, x uniformly random | x found halfway → `O(n)` |
| **Worst** | Meanest input | x absent or last → `O(n)` |

Convention: **Big O = worst case, Ω = best case, Θ = tight bound.** Interviews expect `O(...)` with worst case; say "average case is..." when it differs meaningfully (e.g., hash tables, quicksort).

### Amortized analysis — the O(1) that isn't always O(1)

`list.append` in Python: occasionally the internal array is full and must be **copied** to a bigger one — that copy is O(n). Yet we call append O(1). Why?

```
append #1      → array size 4  → O(1)
append #2,3,4  → O(1) each
append #5      → COPY 4 items → O(n) ← expensive
append #6,7,8  → O(1) each
append #9      → COPY 8 items → O(n) ← expensive
```

Over n appends, total copies = `1 + 2 + 4 + 8 + ... + n/2 < n`.
Total work ≈ n (appends) + n (all copies) = **2n → amortized O(1)**.

**Amortized** = average cost *per operation over a sequence of operations*, even though individual operations may spike. This is a crucial interview concept (often asked directly: "what's the amortized complexity of dynamic array insertion?").

Python's list growth factor is **~1.125–2x** depending on version (CPython over-allocates geometrically, CPython 3.11+ grows by ~12.5% for small lists and more for large) — geometric growth is what guarantees amortized O(1). A naive "grow by 1" implementation would be amortized **O(n²)**.

## 1.5 Space complexity

Count **extra** memory beyond the input, as a function of n.

```python
def sum_list(lst):            # O(1) space — one accumulator
    s = 0
    for x in lst: s += x
    return s

def copy_list(lst):           # O(n) space — new list of n items
    return list(lst)

def nested(n):                # O(n²) space if you allocate the grid
    grid = [[0]*n for _ in range(n)]
    return grid
```

### Recursive space = depth of the call stack

```python
def fact(n):                  # O(n) space: n frames live at once
    if n <= 1: return 1
    return n * fact(n - 1)
```
At the deepest point, `fact(n)`, `fact(n-1)`, ..., `fact(1)` are all **paused on the stack** → O(n) frames.

```python
def fib(n, a=0, b=1):         # O(1) space! Tail-recursive form
    if n == 0: return a
    return fib(n - 1, b, a + b)
```
Python doesn't do tail-call optimization, so this still grows the stack — but the *logical* algorithm uses O(1). (Know the distinction: some interviewers will test whether you know Python specifically doesn't optimize tail calls → raises `RecursionError`.)

**Infinite recursion check:**
```python
import sys
sys.setrecursionlimit(10**6)  # only postpones the problem; recursion
                              # depth ~ n will still crash at large n
```
**Practical rule:** if n can exceed ~10³ and your recursion is O(n) deep, convert to iteration (Part 3, §3.6 shows how).

## 1.6 Python's built-in complexity table (know this cold)

| Operation | list | dict | set | `collections.deque` | `sorted()` |
|---|---|---|---|---|---|
| Access by index `x[i]` | **O(1)** | ❌ | ❌ | O(n)¹ | — |
| Search `x in s` | O(n) | **O(1)** avg | **O(1)** avg | O(n) | — |
| Insert at end `append` | **O(1)** amortized | O(1) avg | O(1) avg | O(1) | — |
| Insert at front | **O(n)** | — | — | **O(1)** | — |
| Insert at middle | O(n) | — | — | O(n) | — |
| Delete arbitrary | O(n) | O(1) avg | O(1) avg | O(n) | — |
| Delete last | **O(1)** | — | — | O(1) amortized | — |
| Find min / max | O(n) | O(n) | O(n) | O(n) | — |
| Iterate all | O(n) | O(n) | O(n) | O(n) | — |
| Length `len()` | O(1) | O(1) | O(1) | O(1) | — |

¹ deque supports O(1) indexing at both *ends*; middle indexing walks.

**Hidden gems to memorize:**
- `x in set` / `x in dict` → **O(1)** vs `x in list` → **O(n)**. This single fact solves dozens of interview problems.
- `heapq.heappush/heappop` → O(log n). `heapq.nlargest(k, xs)` → O(n log k).
- `bisect.bisect_left` → O(log n) on a sorted list, O(n) on `list.insert` though!
- `list.pop()` from the **end** → O(1); from index 0 → O(n).
- `str.join(list)` → O(total characters). Concatenating with `+=` in a loop → O(n²). **Always `join`.**
- `collections.Counter` → O(n) construction, O(1) lookups.
- `dict` preserves insertion order (Python 3.7+ language guarantee) — this enables the **LRU cache** trick without extra code.

## 1.7 Algorithmic vs Pythonic optimization — the distinction that matters

Two different kinds of "make it faster":

- **Algorithmic:** change the *math* of the solution (nested loop → hash map). Gains are **asymptotic**: 1000x, 1,000,000x.
- **Pythonic:** change the *implementation* while keeping the algorithm (for-loop → comprehension, `append` → `join`). Gains are **constant factors**: 2x–50x.

### Order of operations: algorithm first, always

```python
# ❌ ALGORITHMICALLY O(n²) — no Python trick saves this
def has_dup_brute(nums):
    return any(nums[i] == nums[j]
               for i in range(len(nums)) for j in range(i+1, len(nums)))

# ✅ ALGORITHMICALLY O(n) — the win is the structure, not the syntax
def has_dup_fast(nums):
    return len(set(nums)) < len(nums)
```

The second version wins by *orders of magnitude* — not because `set` is written in C (that's the Pythonic part, maybe 10x), but because the algorithm changed from comparing pairs to hashing once.

### Common Pythonic wins (constant factors — apply *after* the algorithm is right)

```python
# 1) Membership testing: list → set
if x in my_list: ...        # O(n)
if x in my_set: ...         # O(1)          ← often worth calling "algorithmic"

# 2) String building: += loop → join
s = ""
for word in words: s += word   # O(total²) due to reallocation
s = "".join(words)             # O(total)  ← big win

# 3) Loop → comprehension / builtin
squares = [x*x for x in range(n)]        # ~2-4x faster than for+append
total   = sum(lst)                        # C loop under the hood
exists  = any(pred(x) for x in lst)       # short-circuits

# 4) Local variable binding inside loops
append = result.append                    # attribute lookup hoisted
for x in data: append(x)

# 5) Avoid work inside the loop that's constant outside it
for x in lst:
    result.append(len(lst))      # ❌ recalculated every iteration
n = len(lst)
for x in lst:
    result.append(n)             # ✅

# 6) Iterators over materialized lists when you only need one pass
map(str, nums)                   # lazy generator — no big intermediate list
it = iter(lst); next(it)         # instead of lst[0] if you'll iterate anyway
```

### When Pythonic micro-optimization actually matters

Only when the algorithm is already optimal **and** the constant is huge (inner-loop over 10⁷ items, competitive programming with tight time limits, hot paths in services). In interviews: **never spend time on it** — state the complexity and write clear code. If an interviewer says "this times out," the fix is almost always algorithmic, not stylistic.

### The trap in the other direction

`sorted()` is O(n log n) written in highly optimized C (Timsort). Your hand-written merge sort is also O(n log n) but ~10–50x slower in pure Python. **In production code, always use `sorted()`/`.sort()`.** You implement sorting algorithms *to understand them* (Part 4), not to ship them. Same for `dict`, `set`, `heapq`, `bisect`, `deque` — Python's standard library is your algorithm toolbox; reaching for it *is* the professional move.

## 1.8 COST — complexity quick card

| You wrote... | Complexity | Faster alternative |
|---|---|---|
| Nested loop over all pairs | O(n²) | hash set (O(n)) or sort + two pointers (O(n log n)) |
| Linear scan in a loop | O(n²) | build a `dict` once → O(n) |
| `list.insert(0, x)` in a loop | O(n²) | `deque.appendleft` → O(n) |
| `+=` string in a loop | O(n²) | `"".join` → O(n) |
| `x in sorted(list)` | O(n) | `bisect` → O(log n) |
| Sorting just to dedupe | O(n log n) | `set` → O(n) |
| Recursion depth n on n=10⁵ | crash | iteration or `deque` |
| `min()` repeatedly in a loop | O(n²) | `heapq` → O(n log n) total |

## 1.9 RECAP — active recall test

Cover the answers and define each term:

1. **Big O** — _?_ (growth rate upper bound, constants dropped)
2. **Why drop constants** — _?_ (they're hardware-dependent; growth rate isn't)
3. **Two different input arrays A, B** — complexity of processing both — _?_ (O(n + m))
4. **Nested loop where inner iterates the whole array** — _?_ (O(n²))
5. **Binary search complexity and why** — _?_ (O(log n); input halves each step)
6. **Amortized O(1) — explain with list.append** — _?_ (rare O(n) copy spread over many appends; geometric growth ⇒ total copies < n)
7. **Space complexity of recursion** — _?_ (O(depth of call stack))
8. **`x in list` vs `x in set`** — _?_ (O(n) vs O(1) average)
9. **Algorithmic vs Pythonic optimization** — _?_ (changes growth rate vs changes constant factor)
10. **n ≤ 15 implies what complexity is acceptable** — _?_ (O(2ⁿ)/O(n!) brute force is fine)
11. **Build-a-dict-then-lookup pattern replaces what** — _?_ (replaces nested search, O(n²) → O(n))
12. **Fastest way to concatenate many strings** — _?_ (`"".join`)

**Exercises (do them — they're the lesson):**

1. Write and time (use `time.perf_counter()`) two solutions for "find if any pair sums to k" on n = 2,000. Confirm the ratio matches theory.
2. What's the complexity of:
   ```python
   def f(n):
       i = 0
       while i < n:
           i += 1
       for _ in range(n):
           for _ in range(n):
               pass
   ```
3. Implement a function that grows a list by exactly 1 slot each time it's full, and count total copies for n = 1000. Compare with Python's real list. What do you conclude about growth strategy?
4. For each, state whether an algorithmic or Pythonic fix is needed: (a) building HTML by `+=`, (b) checking overlap of two unsorted arrays, (c) counting word frequencies.

<details><summary>Solutions</summary>

2. O(n) + O(n²) = O(n²).
3. Growth-by-1 total copies = 1+2+...+n ≈ n²/2 → O(n²) amortized. Geometric growth gives < n total → O(1) amortized.
4. (a) Pythonic (`join`). (b) Algorithmic (set intersection → O(n+m)). (c) Algorithmic (`Counter`/dict is a structural change from nested counting).
</details>

---

---

---

# Part 2 — Core Data Structures

---

## 2.1 Python Lists (Dynamic Arrays)

### WHY

You need a sequence of things where you know the position of every element. Random access, ordered iteration, compact memory. Every language has this; Python calls it `list`. But Python's list is a **dynamic array** — it has an array's strengths *and* array's weaknesses, and most beginners never learn where those boundaries are.

### WHAT

A `list` is a **contiguous block of memory holding pointers to objects**, plus a length. The block is over-allocated (grows geometrically) so appends are cheap — that's the "dynamic" part.

```
list object                 pointer array (contiguous memory)
┌────────┐     ┌───┬───┬───┬───┬───┬───┬───┐
│ size=4 │────▶│ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │   ← capacity 7, size 4
└────────┘     └─┬─┴─┬─┴─┬─┴─┬─┴───┴───┴───┘
                 │   │   │   │
                 ▼   ▼   ▼   ▼
                "a"  42  [ ] True    ← actual objects (any type)
```

- **Index access `lst[i]`** = jump to slot i → **O(1)**. This is the array's superpower.
- **Insert/delete at position i** = shift everything after i → **O(n)**.
- **append** = write at the end → **O(1) amortized** (geometric growth, Part 1 §1.4).

### HOW — operations traced

```python
nums = [10, 20, 30, 40]

# ACCESS — O(1)
nums[0]          # 10
nums[-1]         # 40   (negative = from the end: index i means len+i)

# SEARCH — O(n)   (must inspect elements one by one)
30 in nums       # True
nums.index(30)   # 2    (ValueError if absent)

# INSERT — O(n) because everything after shifts
nums.insert(1, 15)     # [10, 15, 20, 30, 40]   insert BEFORE index 1
nums.append(50)        # [10, 15, 20, 30, 40, 50]  end insert, O(1)

# DELETE — O(n)
nums.pop()             # removes and returns LAST, O(1)  → [10, 15, 20, 30, 40]
nums.pop(0)            # removes index 0, O(n) → [15, 20, 30, 40]
del nums[1]            # remove index 1, O(n)  → [15, 30, 40]
nums.remove(30)        # remove FIRST occurrence by VALUE, O(n) search + O(n) shift

# REVERSE — O(n)
nums.reverse()         # in-place, returns None
nums2 = nums[::-1]     # new reversed copy, O(n), also a trick for "copy"

# SORT — O(n log n)
nums.sort()            # in-place, returns None
sorted(nums)           # returns NEW sorted list, original untouched
```

### Manual implementations (the interview versions)

```python
# ---- Reverse a list manually (no [::-1], no .reverse()) ----
def reverse_list(lst):
    i, j = 0, len(lst) - 1
    while i < j:                     # two pointers closing in
        lst[i], lst[j] = lst[j], lst[i]
        i += 1; j -= 1
    # O(n) time, O(1) space — in-place

# ---- Remove duplicates from a SORTED list in place ----
def remove_dups_sorted(lst):
    if not lst: return 0
    write = 1                        # where the next unique goes
    for read in range(1, len(lst)):
        if lst[read] != lst[write - 1]:
            lst[write] = lst[read]
            write += 1
    del lst[write:]                  # truncate tail
    # O(n) time, O(1) extra space

# ---- Insert into a SORTED list keeping order ----
import bisect
def insert_sorted(lst, val):
    bisect.insort(lst, val)          # O(log n) search + O(n) shift
```

### `copy()` vs `[:]` vs `list()` vs `deepcopy` — the copying trap

```python
a = [[1, 2], [3, 4]]

b = a            # ❌ ALIAS: same object. b[0][0] = 99 also changes a.
c = a[:]         # ✅ SHALLOW copy: new outer list, SAME inner objects
d = a.copy()     # ✅ same as [:]  — shallow
e = list(a)      # ✅ same as [:]  — shallow
import copy
f = copy.deepcopy(a)   # ✅✅ DEEP copy: recursively clones everything
```

```
a = [[1,2],[3,4]]          b = a               c = a[:]

list_a ──┐                 list_a/b (ONE)       list_a ─┐   list_c ─┐
         ▼                      │                       │           │
       [0]──────────►[1,2]      ▼                       ▼           ▼
       [1]──────────►[3,4]    same internals          [0]────────►[1,2]  ← same inner lists!
                                                 [1]────────►[3,4]
```

**Rule:** shallow copy protects you from `append`/`remove`/`sort` on the outer list, but **mutations to elements leak through**. Nested data → `deepcopy`.

**`copy()` vs `[:]`** — functionally identical for lists. `[:]` is idiomatic and works on any sequence (`str`, `tuple`); `.copy()` only on objects that define it. For dicts/sets use `.copy()`; for "any sequence" use `[:]`.

### Slicing — deep but quick

```python
lst[start:stop:step]     # start inclusive, stop exclusive, step stride
lst[2:5]                 # indices 2,3,4
lst[:3]                  # first 3
lst[-3:]                 # last 3
lst[::2]                 # every other element
lst[::-1]                # full reverse (also: the copy-then-reverse trick)
lst[10:3]                # EMPTY — Python clamps ranges, never errors
lst[::0]                 # ValueError: slice step cannot be zero
```
Every slice builds a **new list** → **O(k)** time & space for k elements. `lst[::2]` on 10⁷ items allocates 5·10⁶ — be mindful.

### Complexity summary card

| Operation | Complexity | Notes |
|---|---|---|
| `lst[i]`, `lst[-i]` | **O(1)** | the reason arrays exist |
| `len(lst)` | O(1) | stored, not counted |
| `x in lst` | O(n) | unordered scan |
| `lst.append(x)` | O(1) amortized | occasional O(n) copy |
| `lst.insert(0, x)` / `pop(0)` | **O(n)** | shifts all elements |
| `lst.pop()` (end) | O(1) | |
| `lst.remove(x)` | O(n) search + O(n) shift | |
| `lst.sort()`, `sorted()` | O(n log n) | Timsort |
| `lst * k` (repeat) | O(n·k) | new list |
| slice `lst[a:b]` | O(b-a) | new list |
| iterate | O(n) | |

### PROS / CONS

**Pros:** O(1) random access; cache-friendly (contiguous → CPU prefetch works); compact memory; rich built-in methods; fantastic for iteration.

**Cons:** insert/delete in the middle is O(n); storage is contiguous so huge lists cause resizes; over-allocation wastes memory; storing *objects* (not primitives) means a pointer array — cache friendliness is partial in Python specifically.

### COMPARE — when arrays beat linked structures (and vice versa)

| Scenario | Winner | Why |
|---|---|---|
| Read by index, iterate in order | **list** | O(1) access, contiguous cache lines |
| "Get the 5000th element" | **list** | linked list needs 5000 hops, O(n) |
| Append at end (most common) | **list** | amortized O(1), tiny constants |
| Insert/delete at the head repeatedly | **deque** / linked list | list shifts everything, O(n) |
| Insert/delete at a known node | **linked list** | O(1) once you hold the node |
| Memory overhead per element | **list** | linked list stores 1–2 extra pointers/node + object overhead |
| Unknown/dynamic size, frequent splicing | **linked list** | no shifting, no resizes |
| Binary search | **list** | needs indexing; linked list's binary search is O(n) |

**Use arrays (lists) in real code about 95% of the time.** Linked lists in Python are almost never worth it in production (the object overhead kills the theoretical advantage) — you learn them for **interviews** (pointer manipulation is a classic test) and for understanding how things like `deque` work under the hood.

### PATTERNS this powers
Two pointers on arrays, sliding window, prefix sums, in-place rotation, Dutch national flag, Kadane's algorithm, merge of sorted arrays — Parts 4 and 8.

### RECAP
- **list** = dynamic array → index O(1), insert-middle O(n), append O(1) amortized
- **`x in list`** = O(n) → use a set instead when possible
- **shallow copy** (`[:]`, `.copy()`, `list()`) shares inner objects; **deepcopy** doesn't
- **slice** always allocates; `[::-1]` reverses and copies
- **aliasing** (`b = a`) is the #1 list bug — two names, one object
- **pop()/append() at the end** O(1); **pop(0)/insert(0,)** O(n) → use `deque`

---

## 2.2 Linked Lists

### WHY

Arrays have two structural weaknesses: (1) inserting at the front or middle costs O(n) because elements must shift, (2) a fixed contiguous block means resizing copies everything. A structure that trades **random access** for **cheap local edits** solves both. That structure is the linked list — and more importantly, it's the purest way to learn *pointer manipulation*, the skill every interview's "reverse the list" question is really testing.

### WHAT

A sequence of **nodes**, each holding **data + a reference (pointer) to the next node**. No contiguous block, no index — you reach element k by walking from the head, k hops.

```
 Singly linked list:
 ┌──────┬────┐   ┌──────┬────┐   ┌──────┬────┐
 │  10  │ ──┼──▶│  20  │ ──┼──▶│  30  │None│
 └──────┴────┘   └──────┴────┘   └──────┴────┘
  head ▶

 Doubly linked list:
        ┌──────┬────┬─────┐
        │  10  │None│  ──┼──▶  ...
        └──────┴────┴─────┘
              ▲    │
            ──┼────┘
   ... ──▶┌──────┬────┬────┐
          │  30  │ ◀──┤next│
          └──────┴────┴────┘
              prev
```

### The Node structure — Python

```python
class Node:
    """One link in the chain. The whole data structure is just this + a head."""
    def __init__(self, data, next=None, prev=None):
        self.data = data      # the payload (anything)
        self.next = next      # reference to next Node (or None)
        self.prev = prev      # only used in doubly linked lists

# Creating and connecting nodes by hand:
a = Node(10)
b = Node(20)
c = Node(30)
a.next = b          # 10 ──▶ 20
b.next = c          # 20 ──▶ 30 ──▶ None
head = a            # entry point to the whole list
```

**Key insight:** there is no "list object" beyond `head`. The list *is* the chain of nodes. Lose `head`, lose the list (the nodes still exist in memory → leak, until GC — Python's garbage collector reclaims them, but you've lost access).

### The Singly vs Doubly decision

| | Singly | Doubly |
|---|---|---|
| Per node | `data`, `next` | `data`, `next`, `prev` |
| Memory | less | ~2x pointer overhead |
| Traverse forward | ✅ | ✅ |
| Traverse backward | ❌ (need recursion or a stack) | ✅ O(1) |
| Delete a node given only that node | ❌ must find the *previous* node first | ✅ O(1) via `node.prev` |
| Interview usage | reverse, merge, cycle — most classics | LRU cache, "delete node in O(1)" |

**Convert Singly → Doubly:**
```python
def to_doubly(head):
    prev = None
    cur = head
    while cur:
        cur.prev = prev       # link backwards
        prev = cur            # advance both
        cur = cur.next
    return prev               # old tail becomes new tail (or return head again)
    # O(n) time, O(1) space — the classic single-pass two-pointer walk
```

**Convert Doubly → Singly:** drop all `prev` links.
```python
def to_singly(head):
    cur = head
    while cur:
        cur.prev = None       # sever backwards links
        if cur.next:
            cur.next.prev = None   # (or just never read prev again)
        cur = cur.next
    return head
    # O(n) — if you only need forward traversal, you can ignore prev entirely
    # and return head unchanged. Deleting becomes O(n) though.
```

### Core operations — traced step by step

```python
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    # ---- PREPEND — O(1) ----
    def push_front(self, data):
        node = Node(data, next=self.head)   # new node points at old head
        self.head = node                    # head points at new node
        self.size += 1

    #     before:  head ─▶ [20] ─▶ None
    #     after:   head ─▶ [10] ─▶ [20] ─▶ None

    # ---- APPEND — O(n) without a tail pointer, O(1) with one ----
    def push_back(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            cur = self.head                 # walk to the last node
            while cur.next:
                cur = cur.next
            cur.next = node
        self.size += 1

    # ---- DELETE first occurrence of value — O(n) ----
    def delete(self, key):
        # Case 1: head itself is the target
        if self.head and self.head.data == key:
            self.head = self.head.next      # head skips over it
            self.size -= 1
            return True
        # Case 2: walk with a trailing pointer so we know the PREV node
        cur = self.head
        while cur and cur.next:
            if cur.next.data == key:
                cur.next = cur.next.next    # bypass: prev → next.next
                self.size -= 1
                return True
            cur = cur.next
        return False
        #     cur.next = cur.next.next
        #     [A] ─▶ [B] ─▶ [C]   delete B
        #     [A] ──────────▶ [C]   B is orphaned; GC reclaims it

    # ---- SEARCH — O(n) ----
    def find(self, key):
        cur = self.head
        while cur:
            if cur.data == key: return True
            cur = cur.next
        return False

    # ---- TRAVERSE (the pattern behind every linked-list solution) ----
    def to_list(self):
        out, cur = [], self.head
        while cur:
            out.append(cur.data)
            cur = cur.next        # THE line: advance one hop
        return out
```

**The universal traversal skeleton** — memorize this; every linked-list problem is a variation:
```python
cur = head
while cur:
    # ... do something with cur ...
    cur = cur.next
```

### THE interview classics (each one is this skeleton + a trick)

```python
# ---- 1) REVERSE a singly linked list — O(n) time, O(1) space ----
def reverse(head):
    prev = None
    cur = head
    while cur:
        nxt = cur.next        # 1) save the rest of the list BEFORE breaking it
        cur.next = prev       # 2) flip the arrow backwards
        prev = cur            # 3) move prev up
        cur = nxt             # 4) move cur up
    return prev               # prev is the new head

    # trace with 10 → 20 → 30 → None:
    # step0: prev=None  cur=10  10.next=None      (20,30 still reachable via nxt)
    # step1: prev=10    cur=20  20.next=10
    # step2: prev=20    cur=30  30.next=20
    # step3: cur=None → return 30   result: 30 → 20 → 10 → None

# ---- 2) Detect cycle — Floyd's Tortoise & Hare — O(n) time, O(1) space ----
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next              # 1 step
        fast = fast.next.next         # 2 steps
        if slow is fast:
            return True               # they met → cycle exists
    return False                       # fast fell off the end → no cycle

def cycle_start(head):                 # extension: WHERE does it start?
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            break
    else:
        return None                    # no cycle
    slow = head                        # reset one pointer to head
    while slow is not fast:            # BOTH advance exactly 1 step now
        slow = slow.next               #   (not 2! the two-step move was only
        fast = fast.next               #    for the meeting phase)
    return slow                        # they meet exactly at the cycle entry

# ---- 3) Middle of the list (slow/fast again) ----
def middle_node(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow                        # for even length: 2nd middle (LC 876 convention)

# ---- 4) Merge two sorted lists — O(n+m) ----
def merge_two(l1, l2):
    dummy = Node(0)                    # sentinel: avoids all "empty list?" branches
    tail = dummy
    while l1 and l2:
        if l1.data <= l2.data:
            tail.next, l1 = l1, l1.next
        else:
            tail.next, l2 = l2, l2.next
        tail = tail.next
    tail.next = l1 or l2               # append whichever has leftovers
    return dummy.next

# ---- 5) Remove Nth node from end — one pass ----
def remove_nth(head, n):
    dummy = Node(0, next=head)
    fast = slow = dummy
    for _ in range(n + 1):             # fast runs n+1 ahead
        fast = fast.next
    while fast:                        # when fast hits end, slow is just BEFORE target
        fast, slow = fast.next, slow.next
    slow.next = slow.next.next         # skip the target
    return dummy.next
```

### The `dummy` (sentinel) node trick

Half of all linked-list bugs come from handling "the head might change / might be empty." A dummy node in front solves it once:
```python
dummy = Node(0); dummy.next = head
# ... manipulate as if head can never change ...
return dummy.next     # real head at the end
```
**Use it whenever you might modify the head.** It eliminates 4 edge cases with 2 lines.

### PROS / CONS

**Pros:**
- Insert/delete at front → **O(1)** (no shifting)
- Insert/delete *at a known node* → O(1) for doubly linked (O(n) to find it, but with a node reference you're done)
- No fixed size, no resizing copies
- Teaches pointer reasoning — the transferable interview skill

**Cons:**
- **No random access** — getting element k is O(n). Cannot binary search.
- **Memory overhead**: every node stores an extra reference (and `prev` in doubly), plus Python object header (~56 bytes/node!). A Python linked list of ints uses ~10x the memory of a `list`.
- **Cache hostility**: nodes scatter across heap → pointer chasing defeats CPU prefetch. Empirically a linked list is *slower than a list* for plain iteration despite identical O(n).
- Extra code complexity (null/None checks, broken links on bugs)

### COMPARE — the canonical table

| Operation | Array (list) | Singly LL | Doubly LL | deque |
|---|---|---|---|---|
| Access by index k | **O(1)** | O(k) | O(k) | O(min(k, n-k)) |
| Search by value | O(n) | O(n) | O(n) | O(n) |
| Insert/delete at head | O(n) | **O(1)** | **O(1)** | **O(1)** |
| Insert/delete at tail | **O(1)** am. | O(n)¹ | **O(1)** with tail ptr | **O(1)** |
| Insert/delete at known node | O(n) shift | O(n) find prev | **O(1)** | O(n) |
| Reverse | O(n) in-place | O(n) 3-pointer | O(n) swap | O(n) |
| Memory per element | low | +1 ptr | +2 ptrs | array block |
| Cache behavior | excellent | poor | poor | good |

¹ unless you keep a tail pointer — then O(1).

### PATTERNS
Reverse (in-place, recursive), detect cycle + find start, middle (slow/fast), merge K lists (with heap), reorder list, copy list with random pointer, LRU cache (doubly LL + dict), flatten multilevel lists, add-two-numbers as digit chains.

### RECAP
- Node = `data` + `next` (+ `prev` if doubly); the list is just the `head` pointer
- **Traversal skeleton:** `cur = head; while cur: ...; cur = cur.next`
- **Reverse:** save `next`, flip `next`, advance `prev` and `cur` — O(n)/O(1)
- **Slow/fast:** cycle detection, cycle start, middle — all O(n)/O(1)
- **dummy node** kills head-handling edge cases
- Find prev before delete in singly lists; doubly gives O(1) delete-with-node
- Python linked lists lose to lists in practice — use them to *learn pointer skills*, not in production

---

---

## 2.3 Stack (LIFO)

### WHY

Some problems have a natural shape: **the most recent thing matters most**. Undo history, browser back-button, matching parentheses, expression evaluation, DFS, "what's the smallest bracket group nested inside this one", function calls themselves. Any time the answer depends on *what happened last*, you need a structure that only talks to its top — pushing everything else to O(1).

### WHAT

A **stack** is a Last-In-First-Out (LIFO) collection. Think of a stack of plates: you put a plate on top, you take from the top. You never pull a plate from the middle.

```
   push ▶  ┌─────┐  ◀ pop (LIFO: last in, first out)
           │  E  │  ◀ peek/top (read without removing)
           ├─────┤
           │  D  │
           ├─────┤
           │  C  │
           ├─────┤
           │  B  │
           ├─────┤
           │  A  │  ◀ bottom
           └─────┘
```

### Operations

| Op | Name | Effect | Complexity |
|---|---|---|---|
| `push(x)` | put on top | adds to top | O(1) |
| `pop()` | remove top | removes & returns top | O(1) |
| `peek()` / `top()` | read top | returns top, no remove | O(1) |
| `is_empty()` | test | | O(1) |
| `size()` | count | | O(1) |

That's the entire interface. **The restriction is the feature** — you *can't* access the middle, which is exactly what makes stack-based algorithms provably simple.

### Implementation 1 — using a Python list

```python
class StackList:
    def __init__(self):
        self.items = []

    def push(self, x):  self.items.append(x)      # end-append = O(1) amortized ✅
    def pop(self):
        if self.is_empty(): raise IndexError("pop from empty stack")
        return self.items.pop()                   # end-pop = O(1) ✅
    def peek(self):
        if self.is_empty(): raise IndexError("peek from empty stack")
        return self.items[-1]                     # O(1) ✅
    def is_empty(self): return not self.items
    def size(self):     return len(self.items)
```

**Why `append`/`pop()` are correct here:** both operate on the **end** → O(1) amortized. The classic mistake is using index 0:
```python
# ❌ WRONG end — O(n) per op makes stack ops O(n)
self.items.insert(0, x)   # shifts everything
self.items.pop(0)         # shifts everything
```
**Rule: a list used as a stack must only ever touch the end.** (`collections.deque` works too, and is O(1) at *both* ends — but for stack duty, list is perfectly fine and slightly faster.)

### Implementation 2 — using a Linked List

```python
class StackLL:
    def __init__(self):
        self.top = None        # head IS the top — never traverse to reach it
        self._size = 0

    def push(self, x):
        self.top = Node(x, next=self.top)   # new node points to old top
        self._size += 1                     # O(1)

    def pop(self):
        if not self.top: raise IndexError("empty")
        data = self.top.data
        self.top = self.top.next            # top slides down one node
        self._size -= 1                     # O(1)
        return data

    def peek(self):
        if not self.top: raise IndexError("empty")
        return self.top.data                # O(1)

    def is_empty(self): return self.top is None
    def size(self):     return self._size
```

**Why head = top, not head = bottom?** If the head were the bottom, every push would walk the whole list → O(n). Putting the top at the head makes all three ops O(1). This is the one design decision that matters.

| | List stack | Linked-list stack |
|---|---|---|
| push/pop/peek | O(1) amortized | O(1) **worst case** |
| Memory | contiguous, over-allocated, efficient | node + pointer overhead, scattered |
| Empty check / size | trivial | explicit bookkeeping |
| Python practice | idiomatic (`s.append`, `s.pop`) | interview demonstration |

### The recursive power of stacks: expression evaluation

```python
def is_valid_parens(s: str) -> bool:
    """The canonical stack problem (LeetCode 20)."""
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for ch in s:
        if ch in "([{":
            stack.append(ch)               # push every opener
        else:                              # ch is a closer
            if not stack or stack[-1] != pairs[ch]:
                return False               # closer matches nothing / wrong opener
            stack.pop()                    # matched — remove the opener
    return not stack                       # stack must be empty at the end

# trace: "{[()]}"
# ch={ → stack=['{']
# ch=[ → stack=['{','[']
# ch=( → stack=['{','[','(']
# ch=) → top '(' matches ')' → pop → stack=['{','[']
# ch=] → top '[' matches ']' → pop → stack=['{']
# ch=} → top '{' matches '}' → pop → stack=[]  → True ✅
```

**Why a stack and not a counter?** Because *order matters*: `([)]` has balanced counts but is invalid — you need to verify the most recent opener is the right one. That's the LIFO requirement.

### PROS / CONS
**Pros:** O(1) ops; trivially correct for nesting/order problems; the backbone of recursion, DFS, undo, parsing.
**Cons:** no random access; no early removal of arbitrary items (need extra structure); can overflow (deep recursion = implicit stack overflow — Python's `RecursionError`).

### RECAP
- **Stack = LIFO**, ops only at top, all O(1)
- List implementation: **only touch the end** (`append`/`pop`/`[-1]`), else it becomes O(n)
- Linked-list implementation: **head = top** so push/pop are O(1)
- Stack is the *default answer* for: nesting/matching, "next/previous greater", monotonic order, DFS, expression parsing, undo

---

## 2.4 Queue (FIFO)

### WHY

Some problems demand **fairness and order of arrival**: print jobs, task scheduling, BFS (level order), request handling, producers feeding consumers. If you process the *oldest* pending item first — and a stack would process the *newest* — you need a queue. The data structure you choose here literally decides whether your traversal is BFS or DFS.

### WHAT

A **queue** is First-In-First-Out (FIFO): like a real queue at a counter — first person to arrive is first served.

```
 enqueue (rear) ▶  ┌───┬───┬───┬───┐  ▶ dequeue (front)
                   │ D │ C │ B │ A │
                   └───┴───┴───┴───┘
                    rear             front
        A arrived first → A leaves first (FIFO)
```

### Operations

| Op | Name | End | Complexity |
|---|---|---|---|
| `enqueue(x)` / `append(x)` | add | rear | O(1) |
| `dequeue()` / `popleft()` | remove | front | O(1) with deque; **O(n) with list!** |
| `peek()` / `front()` | read | front | O(1) |
| `is_empty()`, `size()` | | | O(1) |

### Implementation 1 — naive Python list (and why it fails)

```python
class BadQueue:
    def __init__(self): self.items = []
    def enqueue(self, x): self.items.append(x)      # O(1) ✅
    def dequeue(self):    return self.items.pop(0)   # O(n) ❌ — shifts all n items!
```
`pop(0)` must move every remaining element one slot left. A loop of n enqueues/dequeues becomes **O(n²)** total. This is *the* classic queue mistake.

### Implementation 2 — `collections.deque` (the right answer)

```python
from collections import deque

q = deque()
q.append(1)          # enqueue at rear     O(1)
q.append(2)
q.popleft()          # dequeue from front  O(1)  → returns 1
q[0]                 # peek front          O(1)
len(q)               # size                O(1)
```
`deque` = **double-ended queue**, a block-linked list of fixed-size arrays. O(1) at *both* ends, no shifting. It's the Swiss-army knife: works as stack (`append`/`pop`) *and* queue (`append`/`popleft`).

### Implementation 3 — Circular Queue (ring buffer)

**The concept:** in a plain array-based queue, `front` only moves forward and every dequeue wastes the slot behind it — the array fills up even though it's mostly empty. A **circular queue** wraps the end back to the beginning, reusing those slots.

```
 Normal array queue (after dequeues, slots 0-2 are WASTED):
 [ ____ | C | D | E | ____ | ____ ]   front=3 rear=4

 Circular queue (rear wraps to index 0):
 index:   0   1   2   3   4
        [ E | _ | _ | C | D ]
               ▲           ▲
             rear(1)     front(3)
 rear+1 = 5 → wraps to 5 % 5 = 0 → slot 0 is reusable ✅
```

**Difference from a normal queue:**
- Normal array queue: O(1) dequeue *conceptually*, but array slots leak, or you shift (O(n)).
- Circular: fixed capacity, both pointers advance with `% capacity` → true O(1) both ends, zero wasted slots, zero shifting.

```python
class CircularQueue:
    def __init__(self, capacity):
        self.cap = capacity
        self.data = [None] * capacity
        self.front = 0          # index of the next item OUT
        self.rear = 0           # index of the next slot IN
        self.count = 0          # needed to tell "empty" from "full"
                               # (both would have front == rear otherwise)

    def enqueue(self, x):
        if self.count == self.cap:
            raise OverflowError("queue is full")
        self.data[self.rear] = x
        self.rear = (self.rear + 1) % self.cap   # ← THE wrap-around
        self.count += 1                            # O(1)

    def dequeue(self):
        if self.count == 0:
            raise IndexError("queue is empty")
        x = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self.cap   # ← front also wraps
        self.count -= 1                            # O(1)
        return x

    def is_empty(self): return self.count == 0
    def is_full(self):  return self.count == self.cap
    def size(self):     return self.count
```

**Three ways to distinguish empty from full** (know all three; each appears in interviews):
1. **Count variable** (above) — simplest.
2. **Keep one slot unused** — full when `(rear+1) % cap == front`. No count needed.
3. **Store size and capacity separately.**

**Circular queue is a direct implementation of** fixed-size buffers: network packet rings, audio/video streaming buffers, logging rings, clock/calendar slots.

### BFS — the reason queues exist in interviews

```python
from collections import deque

def bfs(graph, start):
    visited = {start}
    order = []
    q = deque([start])              # seed the queue
    while q:
        node = q.popleft()           # ← FIFO: oldest first = level order
        order.append(node)
        for nxt in graph[node]:
            if nxt not in visited:
                visited.add(nxt)     # mark WHEN ENQUEUED (not when dequeued)
                q.append(nxt)
    return order
```
**DFS uses a stack** (or recursion); **BFS uses a queue**. Same skeleton, one line different, completely different traversal — this single fact appears in dozens of interview problems (shortest path in unweighted grid, level order, islands, word ladder).

### PROS / CONS
**Pros:** fair/ordered processing; O(1) enqueue/dequeue with deque; BFS backbone; natural decoupling of producer and consumer.
**Cons:** list implementation is O(n) per dequeue (trap); no random access; plain array queues waste slots without wrap-around; circular queues have fixed capacity (or need resizing logic).

### COMPARE — Stack vs Queue vs Deque

| | Stack (LIFO) | Queue (FIFO) | Deque (both ends) |
|---|---|---|---|
| Order | last in, first out | first in, first out | flexible |
| Ops at | top only | front + rear | both ends |
| Traverse → | **DFS**, recursion | **BFS**, levels | sliding window, monotonic |
| Python | `list` (`append`/`pop`) | `deque` (`append`/`popleft`) | `deque` (`appendleft` too) |
| Classic use | parentheses, undo, parsing, monotonic stack | task scheduling, BFS, rate limiting | LRU, K-sliding-window max, front+back processing |

### `collections.deque` — full operation card

```python
from collections import deque
d = deque([2, 3])
d.append(4)        # [2, 3, 4]      rear add        O(1)
d.appendleft(1)    # [1, 2, 3, 4]   FRONT add       O(1)  ← list can't do this fast
d.pop()            # [1, 2, 3]      rear remove     O(1)
d.popleft()        # [2, 3]         FRONT remove    O(1)  ← list's O(n) spot
d.rotate(1)        # [3, 2]         rotates right (leftmost goes to right)  O(k)
d[0], d[-1]        # front/back peek O(1)
del d[1]           # middle delete   O(n)
x in d             # membership      O(n)
```
**Also:** `maxlen` argument creates a **fixed-size ring buffer** — oldest elements auto-evict. That's a one-line sliding-window-max container:
```python
d = deque(maxlen=3)   # never longer than 3; appending evicts oldest
```

### RECAP
- **Queue = FIFO**; enqueue rear, dequeue front
- **`list.pop(0)` is O(n)** → never use lists as queues → use `collections.deque`
- **Circular queue:** `front`/`rear` advance with `% capacity` → O(1) both ends, no wasted slots; needs count (or a spare slot) to distinguish empty/full
- **Queue → BFS; stack → DFS.** The one-line difference that defines traversal
- `deque` does everything: stack ops, queue ops, `appendleft`, `rotate`, `maxlen` ring buffer

---

## 2.5 Hashing, Dictionaries & Sets

### WHY

The single most-used structure in real code and interviews. Its purpose is one sentence: **turn "search" into "compute".**

Searching an unsorted list costs O(n) because the only way to find x is to *look at things until you find it*. A hash table computes a **memory address directly from the key** — you jump straight to where x *should* be, no scanning. Average **O(1)** search, insert, and delete. Nothing else in CS gets you that for unordered data.

Ask: how would you count word frequencies, find duplicates, check "have I seen the complement", group anagrams, build a cache, deduplicate a feed — without a hash map? You'd be stuck in nested loops. This structure *is* modern software.

### WHAT — how a hash table stores and retrieves

```
        KEY                 HASH FUNCTION               BUCKET ARRAY
   "apple" ────▶  hash("apple") = 0b101101... ──▶  % 8 = 5
                            │
                            ▼
   ┌────┬────┬────┬────┬────┬─────────────┬────┬────┐
   │ 0  │ 1  │ 2  │ 3  │ 4  │ 5          │ 6  │ 7  │
   └────┴────┴────┴────┴────┴─────┬──────┴────┴────┘
                                  │
                     ┌────────────┴────────────┐
                     │ key="apple" val=3       │  ← linked list (bucket chain)
                     │   ↓                     │
                     │ key="grape" val=1       │
                     └─────────────────────────┘

 RETRIEVAL of d["apple"]:
   1. hash("apple") → index 5           (O(1) computation)
   2. go to bucket 5                    (O(1) array access)
   3. compare keys in the chain         (O(1) avg if chain is short)
   → No scan of the other 7 buckets. Ever.
```

**The three-step promise:** hash → index → chain. All three are fast *if the chains stay short* — and keeping them short is the whole engineering problem (load factor, resizing, collision handling).

### Collisions — why they happen and how they're fixed

A collision = **two different keys produce the same index**. With finite buckets and infinite possible keys, collisions are *mathematically guaranteed* (pigeonhole principle). Two main remedies:

**1. Separate chaining (what CPython dict/set uses):** each bucket holds a linked list (actually a compact array) of all entries that hash there. Lookup walks that chain.

```python
# Minimal hash table demonstrating chaining:
class HashMap:
    def __init__(self, capacity=8):
        self.cap = capacity
        self.buckets = [[] for _ in range(capacity)]   # each bucket = a chain (list)
        self.size = 0

    def _index(self, key):
        return hash(key) % self.cap                     # hash → bucket position

    def put(self, key, value):
        i = self._index(key)
        bucket = self.buckets[i]
        for j in range(0, len(bucket), 2):              # scan THIS chain only
            if bucket[j] == key:
                bucket[j + 1] = value                   # update existing
                return
        bucket.append(key); bucket.append(value)        # append to chain
        self.size += 1
        if self.size / self.cap > 0.75:                 # load factor exceeded
            self._resize()                              # grow & rehash everything

    def get(self, key):
        bucket = self.buckets[self._index(key)]
        for j in range(0, len(bucket), 2):
            if bucket[j] == key:
                return bucket[j + 1]
        raise KeyError(key)

    def _resize(self):
        old = self.buckets
        self.cap *= 2
        self.buckets = [[] for _ in range(self.cap)]
        self.size = 0
        for b in old:                                   # re-insert all pairs
            for j in range(0, len(b), 2):
                self.put(b[j], b[j + 1])
```

**2. Open addressing:** no chains — a colliding key probes forward to the next free slot.
- *Linear probing:* try `h+1, h+2, ...` → fast but causes clusters
- *Quadratic probing:* try `h+1, h+4, h+9, ...`
- *Double hashing:* use a second hash to decide the probe step (best distribution)

```
Open addressing insert of key2 colliding at slot 5:
 [0][1][2][3][4][5=key1][6=key2←probed][7]
                        ↑ collision → next free slot
```
Deletion in open addressing needs **tombstones** (deleted markers) so probe chains don't break — a real interview follow-up question.

| | Separate chaining | Open addressing |
|---|---|---|
| Load factor | can exceed 1 (chains grow) | must stay < 1 (or ≤0.7) |
| Deletion | trivial | needs tombstones |
| Memory | extra pointer per node | denser, pointer-free |
| Cache | poor (pointer chasing) | good (contiguous) |
| Used by | CPython dict/set, Java HashMap (tree-ifies long chains) | Python `set` (initially compact dict, effectively open-ish), Redis |

**3. Load factor & resizing:** `load = items / buckets`. Keep it below ~0.75; when exceeded, **double the bucket count and rehash every key** (O(n) but amortized O(1) per insert, same math as dynamic arrays). This is why `dict` never degrades: chains stay short, average lookup stays O(1).

### Python `dict` and `set` — how they work internally

**Hashability rules — memorize:**
```python
# ✅ HASHABLE (usable as dict key / set member) — immutable:
d = {}     # 1, 3.14, "abc", (1,2), frozenset({1,2}), True, None, complex

# ❌ UNHASHABLE — mutable containers:
d = {}
d[[1,2]] = 1     # TypeError: unhashable type: 'list'
d[{1,2}] = 1     # TypeError: unhashable type: 'set'
d[{}]   = 1      # TypeError: unhashable type: 'dict'
```
**Why:** a key's hash must never change while it's stored. A list can be mutated → its hash would change → the table would lose track of it. Python forbids it at the type level.

**`hash()` — Python's hash function:**
```python
hash(42)          # 42  (small ints hash to themselves)
hash("abc")       # some large int, deterministic per run (PYTHONHASHSEED)
hash((1, 2))      # combiner of element hashes
hash(1.5)         # derived from the float's bits
# hash(x) == hash(y) whenever x == y   ← REQUIRED by the dict contract
# equal → same hash (necessary); same hash → equal (NOT required)
```
- Built-in hashes are **not cryptographic** — deliberately randomized per process (`PYTHONHASHSEED`) to prevent collision-flooding attacks (someone sending many keys that all hash to the same bucket could make your server O(n) per lookup — hash randomization makes this attacker-proof).
- If you write your own class as a dict key:
  ```python
  class Player:
      def __init__(self, name): self.name = name
      def __eq__(self, other): return self.name == other.name
      def __hash__(self):      return hash(self.name)
      # MUST override BOTH — default hash is identity-based, default __eq__ is identity
  ```
  **Contract:** equal objects → equal hashes. Violating it makes your object silently invisible in dicts.

**Key uniqueness & set uniqueness:**
- Dict keys are unique **by value** (`==` + equal hash): `{"a":1, "a":2}` → `{"a":2}` (second wins).
- Set elements unique by value: `set([1,1,2])` → `{1,2}`.
- Uniqueness is checked *within a bucket only* — that's why hashing must be fast.

**The dict ↔ set relationship:** `set` is literally a dict with no values (CPython stores only keys). Everything about hash tables applies to both. `collections.Counter` is a dict subclass.

### Frequency counting patterns — the #1 interview application

```python
# ---- 1) Count occurrences of each element ----
from collections import Counter, defaultdict
freq = Counter([1, 2, 2, 3, 3, 3])       # {1:1, 2:2, 3:3}   O(n)
freq = {}
for x in nums:                             # manual version (know it for interviews)
    freq[x] = freq.get(x, 0) + 1           # get() avoids KeyError

# ---- 2) Most frequent element ----
most_common = Counter(nums).most_common(1)[0]     # (value, count)
# or with a heap for top-K frequent (Part 5):
import heapq
top3 = heapq.nlargest(3, freq.items(), key=lambda kv: kv[1])

# ---- 3) Character / word frequencies ----
char_count = Counter("mississippi")        # {'m':1,'i':4,'s':4,'p':2}
word_count = Counter(text.split())         # word → count in O(total words)

# ---- 4) Group by a key (anagrams, dates, categories) ----
groups = defaultdict(list)
for w in words:
    groups[tuple(sorted(w))].append(w)     # key = canonical form → list of matches

# ---- 5) First non-repeating character (ordered uniqueness) ----
def first_unique(s):
    count = Counter(s)
    for i, ch in enumerate(s):
        if count[ch] == 1: return i
    return -1

# ---- 6) Two-sum via complement lookup ----
def two_sum(nums, target):
    seen = {}                              # value → index
    for i, x in enumerate(nums):
        if target - x in seen:             # O(1) "have I seen the complement?"
            return [seen[target - x], i]
        seen[x] = i
    return []

# ---- 7) Detect duplicates ----
def has_dup(nums): return len(set(nums)) < len(nums)     # O(n) one-liner

# ---- 8) Anagram check (two frequency maps, or one decrementing map) ----
def is_anagram(a, b):
    if len(a) != len(b): return False
    cnt = Counter(a)
    for ch in b:
        cnt[ch] -= 1
        if cnt[ch] < 0: return False
    return all(v == 0 for v in cnt.values())
```

**The transformation pattern — replace a nested loop with a dict:**
```
BEFORE (O(n²)):                 AFTER (O(n)):
for i in range(n):              seen = {}
  for j in range(n):            for x in nums:
    if a[i] == b[j]:              if x in seen: ...
                                  seen[x] = ...
```
If your inner loop is *searching* something you computed earlier → **cache it in a dict/set**. This single move converts dozens of O(n²) solutions to O(n).

### Common use cases (with structure choice)

| Use case | Structure | Why |
|---|---|---|
| Duplicate detection | `set` | membership O(1) |
| Fast lookup by key | `dict` | O(1) get/set |
| Membership test "seen before?" | `set` | O(1), no values needed |
| Counting / frequency | `dict` / `Counter` | accumulate in one pass |
| Grouping items by category | `defaultdict(list)` | auto-creates buckets |
| Caching / memoization | `dict` | key → computed result |
| Two-sum complement | `dict` (value→index) or `set` | one-pass lookup |
| Set operations (union, intersect diff) | `set` | built-in `|`, `&`, `-` with O(min(n,m)) |
| Ordered unique sequence | `dict` (3.7+ order) or `set` + list | insertion-ordered |
| Remove duplicates preserving order | `dict.fromkeys(lst)` | O(n), keeps first-seen order |

### PROS / CONS

**Pros:** O(1) average search/insert/delete *without* ordering; set operations are near-instant; makes "n² → n" conversions possible; foundational to caches, indexes, dedup, counting, graphs (adjacency maps), DP memo tables.

**Cons:**
- **Average, not worst.** Pathological inputs (all keys same hash) degrade to O(n); Python mitigates with hash randomization + internal checks.
- **No ordering** (plain dict in older semantics; 3.7+ preserves *insertion* order — but not sorted order). Need sorted → `sorted(d)` (O(n log n)).
- **No range queries** — "keys between 5 and 10" requires sorting or a tree.
- **Memory hungry** — dicts/sets have big per-table overhead; small collections are cheaper as lists.
- **Mutable keys forbidden** — no lists/dicts as keys (use `tuple`).

### COMPARE — dict/set vs list vs sorted array

| Need | Best choice | Complexity | Why not the others |
|---|---|---|---|
| Find x in unordered collection | **set/dict** | O(1) avg | list = O(n) scan |
| Find x in sorted collection | sorted list + `bisect` | O(log n) | set loses ordering |
| "All elements unique?" | `set` | O(n) | nested loop O(n²) |
| Frequency of each element | `dict`/`Counter` | O(n) | sorting then counting = O(n log n) |
| Range query [lo, hi] | sorted array + bisect | O(log n) + output | dict has no order |
| Tiny n (≤ ~8) | list | constants win | dict overhead dominates |
| Iterate in insertion order | dict (3.7+) / list | O(1) per item | set is unordered-ish |
| Union/intersect of two groups | `set` | O(n+m) | lists = O(n·m) |

### RECAP
- **Hashing = search becomes compute:** `hash(key) % buckets` → O(1) average
- **Collisions are guaranteed** → chaining (bucket lists, CPython) or open addressing (probing, tombstones)
- **Load factor ~0.75 → resize (double + rehash),** amortized O(1)
- **Hashable = immutable types** (int, str, tuple, frozenset); custom classes must define `__eq__` + `__hash__` consistently
- `hash(x) == hash(y)` whenever `x == y`; same hash does NOT imply equal
- **Frequency counting** (`Counter`, `get(x,0)+1`) and **complement lookup** (two-sum) are the two killer interview patterns
- **dict ↔ set:** same structure; set = dict without values
- No ordering, no range queries → that's what sorted arrays/trees are for

---

## 2.6 Strings (as first-class interview material)

### WHY

Strings *look* like text problems but are usually **array problems wearing a costume** — or **hash-map problems** (frequency), or **two-pointer problems** (palindromes, reversing). They show up constantly because they're easy for interviewers to state and brutally easy to get subtly wrong (indices, Unicode, mutation — Python strings are immutable!).

### WHAT

A string is an **immutable sequence of characters**. Immutability matters: `s[i] = 'a'` raises `TypeError`; every "modification" allocates a new string → building strings by concatenation in a loop is O(n²).

```python
s = "algorithm"
s[0]            # 'a'          indexing, O(1)
s[-1]           # 'm'          negative indexing
s[2:5]          # 'go'         slicing → new string, O(k)
len(s)          # 9            O(1)
'a' in s        # True         O(n) but C-optimized
s.lower()       # new string
s.split(",")    # split into list of parts
"".join(parts)  # the O(total) way to rebuild
```

### The string patterns that recur everywhere

```python
# 1) Build with join, never += (O(n) vs O(n²))
out = []
for ch in s:
    out.append(transform(ch))
result = "".join(out)

# 2) Frequency map of characters
from collections import Counter
cnt = Counter(s)                      # {char: count}

# 3) Two pointers on a string (palindrome check) — O(n)/O(1)
def is_palindrome(s):
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]: return False
        i += 1; j -= 1
    return True

# 4) Sliding window on a string (longest substring without repeats) — O(n)
def longest_unique(s):
    last, best, left = {}, 0, 0
    for right, ch in enumerate(s):
        if ch in last and last[ch] >= left:
            left = last[ch] + 1       # jump left past the previous occurrence
        last[ch] = right
        best = max(best, right - left + 1)
    return best

# 5) Character ↔ number tricks
ord('a')          # 97      ASCII/Unicode code
chr(97)           # 'a'
ord(ch) - ord('a')  # 0..25  → use an array of 26 counts (often faster than dict)
[0]*26            # fixed alphabet bucket array — the "counting sort on letters" trick
```

### Comparison: string techniques

| Task | Naive | Optimized | Complexity |
|---|---|---|---|
| Concatenate n pieces | `+=` in loop | `"".join` | O(n²) → O(n) |
| Count characters | nested loop | `Counter` / `[0]*26` | O(n²) → O(n) |
| Palindrome | build reversed copy + compare | two pointers | O(n) space → O(1) |
| Check substring | manual nested scan | `in` (mix of algorithms) | don't hand-roll |
| Anagram check | sort both + compare O(n log n) | decrement frequency map | → O(n) |
| First unique char | repeated `s.count()` O(n²) | one `Counter` pass | → O(n) |

### RECAP
- Strings are **immutable sequences** → `join` for building, never `+=` in loops
- Treat them like arrays: **two pointers, sliding window, frequency maps**
- `ord()`/`chr()` convert letters to 0–25 indices for fixed-size count arrays
- `Counter(s)` for character frequencies — the anagram/unique/frequency family all starts here

---

---

---

# Part 3 — Recursion & Problem-Solving Engine

## 3.1 Introduction to Recursion

### WHY

Some problems are most naturally stated in terms of *themselves*: compute n! from (n-1)!, check a tree by checking subtrees, find a path by extending a shorter path. Writing these iteratively means manually simulating what the computer already does for free — maintaining your own stack of "where was I". Recursion lets you **delegate the rest of the work to the language's call stack** and focus only on the one step you're responsible for right now.

It's also the mental training ground for trees, graphs, divide-and-conquer, and dynamic programming. If recursion feels shaky, every part after this one feels shaky.

### WHAT

A **recursive function** is a function that calls itself on a *smaller* input, with two mandatory components:

1. **Base case** — the smallest input the function can answer *directly*, without recursing. Stops the descent.
2. **Recursive case** — the function reduces the problem and calls itself, trusting the smaller call to do the rest.

```
recursion = TRUST
            ├── I answer the trivial part
            └── I trust the same function on a smaller piece
```

### HOW — anatomy, traced

```python
def factorial(n):
    # ┌─ BASE CASE: no recursion, direct answer
    if n <= 1:
        return 1
    # └─ REDUCTION: smaller, simpler call
    return n * factorial(n - 1)
```

**Trace of `factorial(4)` — watch the call stack:**

```
factorial(4)                        depth 0   waiting for factorial(3)
  └─ factorial(3)                    depth 1   waiting for factorial(2)
       └─ factorial(2)               depth 2   waiting for factorial(1)
            └─ factorial(1)          depth 3   BASE CASE → returns 1
            ◀──────────────────── 2 * 1 = 2       (unwinding begins)
       ◀──────────────────── 3 * 2 = 6
  ◀──────────────────────── 4 * 6 = 24
return 24

Call stack during the deepest point:
┌───────────────────────┐
│ factorial(4) : 4 * _  │  ← paused, multiplier 4 saved
├───────────────────────┤
│ factorial(3) : 3 * _  │  ← paused, multiplier 3 saved
├───────────────────────┤
│ factorial(2) : 2 * _  │  ← paused, multiplier 2 saved
├───────────────────────┤
│ factorial(1) → 1      │  ← currently executing (top of stack)
└───────────────────────┘
Each level holds its own local variables (n, and the pending * operation).
```

**Two phases:** the **descending phase** (unwinding the problem into smaller pieces until the base case) and the **returning phase** (composing answers back up). Most recursion bugs are one of: missing base case (infinite descent → `RecursionError`), wrong base case (stops too early/late), or the recursive call not actually *smaller*.

### The three questions to ask of every recursive function

1. **What is the base case?** (When do I answer without recursing?)
2. **Is each recursive call strictly smaller/simpler?** (Progress guarantee — else infinite recursion.)
3. **Can I trust the recursive call's answer?** (State what it guarantees: "returns the factorial of its argument.")

### More classic traces

```python
# ---- Fibonacci — the canonical example AND the canonical warning ----
def fib(n):
    if n <= 1: return n
    return fib(n - 1) + fib(n - 2)

# fib(5) call tree — COUNT THE NODES:
#                                 fib(5)
#                              /           \
#                         fib(4)           fib(3)
#                       /      \          /     \
#                   fib(3)    fib(2)   fib(2)   fib(1)
#                  /    \      /   \     /   \
#              fib(2) fib(1) fib(1) fib(0) fib(1) fib(0)
#               /   \
#           fib(1) fib(0)
#
# Nodes: 15 for n=5. In general ~ O(1.618^n) = O(2^n) — EXPONENTIAL.
# Why: fib(3) computed TWICE, fib(2) THREE times... repeated work!
# Fix in Part 7: memoization → O(n). (This example IS the motivation for DP.)

# ---- Reverse a string — reduce by one character ----
def reverse(s):
    if len(s) <= 1:                 # base case
        return s
    return reverse(s[1:]) + s[0]    # trust: reverse of tail + head at the end
# reverse("abc") = reverse("bc") + "a"
#                = (reverse("c") + "b") + "a"
#                = ("c" + "b") + "a" = "cba"

# ---- Sum of digits ----
def digit_sum(n):
    if n < 10: return n             # single digit is its own sum
    return n % 10 + digit_sum(n // 10)   # last digit + sum of the rest

# ---- Print all elements (structure of every tree/graph traversal) ----
def traverse(node):
    if node is None: return         # base case: nothing to process
    print(node.data)                # process this node
    for child in node.children:
        traverse(child)             # trust children to handle themselves
```

### Recursion vs Iteration

| | Recursion | Iteration |
|---|---|---|
| State maintained by | call stack (automatic) | your own variables |
| Code clarity for tree/nested problems | **excellent** — mirrors problem structure | often clumsy (manual stack) |
| Memory | O(depth) stack frames | O(1) extra (or explicit stack O(depth)) |
| Speed | frame push/pop overhead ~2–4x slower | faster |
| Limits | `RecursionError` ~1000 default in Python (`sys.setrecursionlimit` can raise but risks segfault) | no depth limit |
| Tail calls | Python does **NOT** optimize them (even correct tail recursion blows the stack) | n/a |
| Debugging | stack traces show the descent | simple line-by-line |

**When to use which:**
- **Use recursion** for: trees, graphs (DFS), backtracking, divide-and-conquer, problems whose definition is self-referential (fibonacci, parentheses generation, nested structures), when depth is provably small (log n or √n or ≤ ~10 for combinations).
- **Use iteration** for: simple loops, linear processes, depth can reach 10⁵+, hot inner loops, or when the interviewers ask explicitly ("do it without recursion" is a common follow-up — it tests whether you understood the algorithm vs the syntax).

**Converting recursive → iterative (the general method):**
```
1. Identify what the call stack is holding: each frame = local vars + "where I was".
2. Replace frames with an EXPLICIT stack (list) of those states.
3. Simulate: pop state → do what the frame would do → push new states.

def dfs_recursive(node):
    if not node: return
    process(node)
    for c in node.children: dfs_recursive(c)

def dfs_iterative(node):                 # same algorithm, manual stack
    if not node: return
    stack = [node]
    while stack:
        node = stack.pop()               # "enter frame"
        process(node)
        for c in reversed(node.children):  # reversed → same visit order as recursion
            stack.append(c)              # "schedule frame"
```
For **tail-recursive** functions the conversion is trivial — replace the recursive call with a `while` loop and its parameters with variables (Part 1 §1.5 `fib_iter` example). Master this: "convert it to iteration" is a standard interview follow-up and it *proves* you know what the stack was doing.

### PROS / CONS of recursion
**Pros:** expressiveness for self-similar problems; automatic backtracking state management; the foundation of trees/graphs/DP; elegant solutions that interviewers expect to see.
**Cons:** stack depth limits; slower than loops; hard to debug deep chains; exponential blowup if overlapping subproblems aren't memoized (fib!); easy to write infinite recursion with a wrong base case.

### RECAP
- Recursion = **base case + smaller recursive call + trust**
- Trace the stack: descending phase builds pending operations, base case triggers the returning phase
- **fib's tree repeats work → O(2ⁿ)** — this exact problem motivates memoization (Part 7)
- Recursion is **O(depth) memory**; Python caps depth ~1000, no tail-call optimization
- Convert to iteration with an **explicit stack**; tail recursion → `while` loop with parameter variables

---

## 3.2 Backtracking — recursion with a decision process

### WHY

A huge family of problems asks you to **enumerate or search among combinations of choices**: all subsets, all permutations, all valid parentheses strings, all ways to place queens, all paths through a maze, word search, Sudoku. Brute-force over all possibilities is exponential — but *naive* brute force wastes enormous time on prefixes that can never lead to an answer. Backtracking = brute force + **prune early and undo cleanly**.

### WHAT

The universal template — **choose → explore → unchoose**:

```python
def backtrack(state, choices):
    if GOAL(state):                 # 1. base case: record/accept the solution
        record(state); return
    for c in choices:               # 2. enumerate choices at THIS level
        if not PROMISING(c, state): # 3. PRUNE: skip hopeless branches early
            continue
        make_choice(state, c)       # 4. CHOOSE
        backtrack(state, ...)       # 5. EXPLORE deeper (same function)
        undo_choice(state, c)       # 6. UNCHOOSE ← restores state for sibling
```

**Why step 6 exists:** the loop continues to the next choice — if state weren't restored, choice 2 would run with choice 1's leftovers. The undo is what lets one `state` object serve every branch. **Forgetting to undo is the #1 backtracking bug** (produces duplicated or corrupted results).

```python
# THE template in full: Subsets (LeetCode 78) — every element in or out
def subsets(nums):
    result, path = [], []
    def dfs(start):
        result.append(path[:])           # record current state (copy!)
        for i in range(start, len(nums)):  # start → avoid permutations of same set
            path.append(nums[i])         #   CHOOSE
            dfs(i + 1)                   #   EXPLORE (next index, not next value)
            path.pop()                   #   UNCHOOSE  ← the backbone
    dfs(0)
    return result

# subsets([1,2,3]):
#   []                          ← recorded at entry
#     [1] → [1,2] → [1,2,3]
#               ↘ [1,3]
#        [2] → [2,3]
#        [3]
# 8 results = 2^3 (each element in/out) — exponential is INHERENT here
```

**The four variations you must recognize:**
```python
# (a) Subsets — all combinations:   dfs(i + 1)   → 2^n results
# (b) Permutations — order matters: mark used[], dfs() any unused → n! results
def permute(nums):
    res, path, used = [], [], [False]*len(nums)
    def dfs():
        if len(path) == len(nums):
            res.append(path[:]); return
        for i in range(len(nums)):
            if used[i]: continue
            used[i] = True; path.append(nums[i])
            dfs()
            path.pop(); used[i] = False       # undo BOTH changes
    dfs(); return res

# (c) Combinations of size k — start = i+1, stop when len(path)==k
# (d) Paths in a grid/maze — choose among neighbors, mark visited to avoid cycles
```

### The complexity truth about backtracking

Output size *forces* exponential time: subsets of n = 2ⁿ, permutations = n!. No cleverness removes that — if the problem asks for all of them, O(output) is optimal. What backtracking buys you is **not redoing dead work**: pruning a branch at depth 3 saves its entire subtree. State the complexity honestly in interviews: *"O(2ⁿ) in the worst case because there are 2ⁿ subsets, but pruning cuts the effective tree significantly on constrained inputs."*

### RECAP
- Backtracking = **choose → explore → unchoose**, with pruning
- **Undo is mandatory** — it restores state for sibling branches
- `start` index parameter = "don't re-permute the same combination"
- **Output-size lower bounds:** subsets 2ⁿ, permutations n!, combinations C(n,k) — complexity can't beat the answer's size
- Recognize: subset / permutation / combination / grid-path / constraint-satisfaction (N-Queens, Sudoku)

---

## 3.3 Problem-Solving with DSA — the integration layer

### WHY this is the actual skill

You now own ~15 structures and algorithms. Interview problems don't announce which one to use. The difference between "knows DSA" and "solves problems" is a **reliable method for choosing** — which is why this section exists before Part 4's algorithms: to wire the pieces into one workflow.

### HOW the pieces map to problem types

| The problem smells like... | Reach for... | Example problems |
|---|---|---|
| "Find a pair/subarray with a property" | hash map/set, two pointers | two-sum, subarray sum = k |
| "Longest/shortest contiguous segment" | sliding window | longest substring w/o repeats |
| "Find in a sorted structure efficiently" | binary search (or on answer) | search rotated array, koko eating |
| "Order matters / process pending items" | queue → BFS | level order, shortest path grid |
| "Most recent / balanced / nested / span" | stack, monotonic stack | valid parens, daily temperatures |
| "Top K / running median / merge streams" | heap | kth largest, merge k lists |
| "Group / count / dedupe / seen before" | dict / set | anagram groups, happy number |
| "Hierarchy, decision chain, contains-prefix" | tree / trie | max depth, word search II |
| "Connections between things, reachability" | graph + BFS/DFS | courses, islands, word ladder |
| "All combinations that satisfy constraints" | backtracking | subsets, N-Queens |
| "Count ways / min cost with repeated subproblems" | DP | climb stairs, coin change |
| "Repeatedly need min/max, input streamed" | heap | task scheduler, reorganize string |
| "Sorted + insert/delete + range queries" | (rare in Python) balanced tree / sortedcontainers | range sum queries |

### The full walkthrough — applying the 7-step framework to a real problem

**Problem:** *Given an array of integers, find the length of the longest subarray whose elements sum to at most `k`.*

```python
# STEP 1 — PARROW: array of ints (can be negative?), target sum ≤ k, want MAX LENGTH.
#            n up to 10^5? → need O(n) or O(n log n).

# STEP 2 — EXAMPLES:
#   [1, 2, 3], k=5 → [1,2] len 2
#   [2, -1, 2], k=3 → [2,-1,2] len 3   (negative! → shrinking window alone may fail*)
#   [], k=0 → 0 ; [5], k=4 → 0

# STEP 3 — BRUTE FORCE: all O(n²) subarrays, sum each → O(n³), or precompute
#   prefix sums → O(n²). Fine to state. Bottleneck: checking every pair (i, j).

# STEP 4 — BOTTLENECK: re-summing subarrays from scratch; every (i,j) pair.

# STEP 5 — PATTERN MAP: "longest subarray with constraint" → SLIDING WINDOW.
#   Maintain window [left..right], running sum. Extend right; when sum > k,
#   shrink from left. One pointer moves n steps each → O(n).
#   *Negatives break "shrink until valid" for SUM windows → note for later
#   (prefix sum + monotonic deque would be the hard version).

# STEP 6 — DRY RUN on [1,2,3], k=5:
#   r=0 sum=1 ok          best=1
#   r=1 sum=3 ok          best=2
#   r=2 sum=6 >5 → shrink l=1 sum=4 ok   best=2   → answer 2 ✓

# STEP 7 — CODE:
def longest_subarray_at_most_k(nums, k):
    left = best = cur = 0
    for right, x in enumerate(nums):
        cur += x                                  # extend
        while cur > k and left <= right:          # shrink until valid
            cur -= nums[left]
            left += 1
        best = max(best, right - left + 1)
    return best
    # O(n): each pointer visits each index at most once
    # TEST: empty→0, single too big→0, all negatives→n, exact k→included
```

**Notice what the framework did:** it converted "find the longest subarray" (vague) into "maintain a valid window with two pointers" (concrete) via one question: *what's my bottleneck and what structure fixes it?*

### Breaking complex problems into smaller problems — three decomposition moves

1. **Reduce to a known subproblem:** "validate BST" → "every node obeys bounds" + "left subtree valid" + "right subtree valid" (recursion over smaller subtrees).
2. **Split into phases:** "median of stream" → "store data" (two heaps) + "answer query" (peek). Design the *storage* first, algorithm second.
3. **Solve a weaker version:** "longest increasing subsequence" → first find length for arrays of 3 elements by brute force → notice the pattern → generalize. This "small-n manual solve" technique frequently *reveals* the recurrence that DP needs.

### RECAP
- The mapping table above is a **lookup index of your entire toolkit** — review it until the instinct is automatic
- Always state brute force + its complexity first (Step 3), then attack the bottleneck (Step 4)
- **Negative numbers break sum-based shrinking windows** — know which window invariants survive which input properties
- Decompose: known-subproblem / phased design / solve-small-n-then-generalize

---

## 3.4 DSA in interviews

### WHY it matters (the meta-view)

Interviewers evaluate four things, in this order of weight:
1. **Communication** — did you clarify before coding? Are you narrating?
2. **Approach** — did you derive the solution, or recall it? Brute force stated → bottleneck named → optimal chosen is a *derivation*.
3. **Correctness** — did it run on first try? Did you test edge cases yourself?
4. **Complexity** — did you state time/space unprompted at the end?

A **correct optimal solution delivered silently** often scores lower than a **brute-force → optimal conversation delivered clearly.** That's not unfair — the job is working with humans on ambiguous problems.

### Common problem families (expect one from each)

| Family | Signature phrasing | Go-to pattern |
|---|---|---|
| Array/pair finding | "return indices of two numbers that..." | hash map / two pointers |
| Contiguous segment | "longest/shortest subarray where..." | sliding window / Kadane |
| Search | "find x / find min in sorted-ish data" | binary search or on answer |
| Ordering & dependencies | "can all tasks finish / in what order" | topological sort |
| Structure design | "design a cache / queue with min" | combine structures (LRU, min-stack) |
| Sequences & counts | "number of ways / minimum cost" | DP |
| Combinatorial listing | "return all subsets/permutations/..." | backtracking |
| Hierarchy | "height / path / ancestor / validate" | tree recursion |
| Connectivity | "how many groups / shortest path / reachable" | Union-Find / BFS |
| Repeated pattern | "longest repeating / anagram windows" | frequency map + window |

### Approaching an unknown problem systematically (spoken script)

```
1. "Let me restate this to make sure I got it..."        ← clarifying
2. "Can the input be empty? Duplicates? Negative numbers? How large is n?"
3. "The brute force would be to ____. That's O(___) — too slow for n = ___."
4. "The bottleneck is ___. What if I used ___? That makes that step O(1)..."
5. "Let me trace that on a small example before coding."  ← DRY RUN (scores big)
6. [code while narrating the plan, not every keystroke]
7. "Let me test: empty input, single element, all duplicates, and the max case."
8. "Final complexity is O(___) time and O(___) space."
```
Silence is the most common failure mode. **Talk through steps 1–5 even if you later struggle with code** — the interviewer now knows your thinking process, and hints become conversation rather than rescue.

### Complexity awareness while solving (not just after)

- **Check constraints FIRST** (Part 1 table): n ≤ 15 → backtracking; n ≤ 10⁵ → O(n log n); n ≤ 10⁶ → O(n).
- **Name the cost as you write:** "this membership test is O(1) because it's a set", "this nested loop makes it quadratic — I'll need a map".
- **Space counts too:** "I'm trading O(n) memory for O(n) time — with n ≤ 10⁵ that's fine."

### RECAP
- Interviews grade **communication > approach > correctness > complexity** — narrate the framework
- Always deliver: restate → constraints → brute force + complexity → bottleneck → optimal → dry run → code → test → state complexity
- Constraints dictate the allowed complexity — read them before designing

---

## 3.5 DSA in real-world projects

### WHY (beyond interviews)

Every performance bug in production is a DSA bug wearing a disguise: an O(n²) loop that melts when data grows 10x, a list `in` check inside another loop, a cache that never evicts, a feed that re-sorts the whole database per request. Knowing DSA is what lets you **profile, recognize, and fix** those — rather than "add more servers" to a quadratic algorithm.

### Practical applications by domain

| Domain | The DSA reality |
|---|---|
| **Search** | Autocomplete → trie (prefix traversal). Web search ranking → heaps (top-K scores), inverted indexes → dict of term → posting lists |
| **Caching** | LRU cache → dict (O(1) lookup) + doubly linked list (O(1) eviction order) — *the* classic interview-to-production structure. Redis uses dict + linked list exactly this way. TTL caches → heap by expiry time |
| **Data processing** | Deduplicate a stream → set. Aggregate logs → `Counter`/`defaultdict`. Join two datasets → hash join (dict) or sort-merge. Group records → `groupby` after sort |
| **Task management** | Job queues → queue (FIFO fairness) or heap (priority/deadline). Rate limiting → deque of timestamps. Scheduling with priorities → heap. Cron "next run time" → heap |
| **Databases** | Indexes → B-trees (balanced search trees: ordered range queries in O(log n)). Query planner picks join order. `ORDER BY` on 10⁶ rows → Timsort on pre-allocated buffer |
| **Networking** | Packet buffering → circular queue (ring buffer, fixed memory). Load balancing → queue + least-connections. DNS caching → dict with TTL |
| **Version control / file systems** | git: commits form a **graph** (DAG); branches = refs; merge = graph traversal. Directories: hash map (name → inode) |
| **Recommendation / social** | "Friends of friends" → graph BFS at depth 2. Similarity → set intersection. Feed ranking → heap over scored candidates |
| **Compilers / parsing** | Expression evaluation → stack. Symbol tables → dict. AST → tree. Type checking → recursive tree walk |
| **Games / pathfinding** | Grid movement → BFS (unweighted), Dijkstra/A* (weighted). Maze generation → backtracking. Undo systems → stack |
| **Machine learning (your era)** | Nearest neighbors → similarity search structures. Token frequency → dict/Counter (that's literally a language model's counts). Batch scheduling → heap. Embedding dedup → set of hashes. Even transformers' attention is matrix ops where cache strategy matters for latency |

### A concrete mini-build: an LRU cache (structures combined)

```python
from collections import OrderedDict

class LRUCache:
    """Least Recently Used cache — the interview staple that IS production code.
    dict gives O(1) lookup; OrderedDict gives O(1) move-to-end for recency."""
    def __init__(self, capacity: int):
        self.cap = capacity
        self.data = OrderedDict()

    def get(self, key):
        if key not in self.data:
            return -1
        self.data.move_to_end(key)        # this access makes key "recent"
        return self.data[key]             # O(1) total

    def put(self, key, value):
        if key in self.data:
            self.data.move_to_end(key)
        self.data[key] = value
        if len(self.data) > self.cap:
            self.data.popitem(last=False)  # evict OLDEST (front) — O(1)
        # O(1) total

# Why this matters: any bounded cache in any service needs eviction.
# The DSA insight — two structures covering each other's weakness — is the lesson.
```

### RECAP
- Production performance bugs are almost always **hidden complexity bugs** — DSA is your diagnostic lens
- **trie** = search/autocomplete; **heap** = scheduling/top-K; **queue/deque** = buffers/rate limits; **dict/set** = dedup/join/cache; **graph** = dependencies/version control; **LRU** = dict + doubly linked list combined
- Design pattern: **combine two structures so each covers the other's weakness**

---

---

---

# Part 4 — Searching, Sorting & Two Pointers

## 4.1 Searching Algorithms

### WHY

Search is the most fundamental query: *does X exist? where?* The difference between searching blindly (look at everything) and searching structurally (exploit an invariant like "sortedness") is the difference between O(n) and O(log n) — and binary search is the single highest return-on-investment algorithm to master: 30 lines of care for a technique that appears in some form in nearly every interview.

### Linear Search — WHY/WHAT

**What:** look at each element, one by one, until you find it or run out. Works on **any** collection — sorted or not, list or linked list.

```python
def linear_search(arr, target):
    for i in range(len(arr)):      # examine elements in order
        if arr[i] == target:
            return i               # found: return position
    return -1                      # not found
    # Time:  O(n) best/worst (best O(1) if first element matches)
    # Space: O(1)
```

**When it's the right choice:** unsorted data (nothing else *can* be faster without preprocessing), tiny inputs (n ≤ ~50 — the setup cost of sorting or hashing exceeds the scan), linked lists (no indexing anyway), or one-off searches where you'll never search again.

**Variants you'll use:** `x in list` (Python's built-in linear scan, C-speed), `list.index(x)`, `min`/`max` scans.

### Binary Search — WHY/WHAT/HOW

**The problem it solves:** linear search wastes the fact that your data is *sorted*. If the array is sorted, after checking the middle element you can **eliminate half the remaining array** — then half again, then half again.

**Preconditions (all required):**
1. Data is **sorted** (ascending or descending — consistent order)
2. Access by index is **O(1)** (arrays yes, linked lists no — even though sorted!)
3. You can define a **target condition** on the sorted order

**The invariant (the sentence that prevents off-by-one bugs forever):**

> **The answer, if it exists, always lies inside `[lo, hi]`.** Every iteration must shrink that range while preserving the invariant.

```python
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1          # search space = [lo, hi] inclusive
    while lo <= hi:                   # ← invariant: answer ∈ [lo, hi] if present
        mid = lo + (hi - lo) // 2     # ← avoids overflow in languages with int32
                                      #   (Python ints are unbounded, but form the habit)
        if arr[mid] == target:
            return mid                # found
        elif arr[mid] < target:
            lo = mid + 1              # target is in the RIGHT half (arr is ascending)
        else:
            hi = mid - 1              # target is in the LEFT half
    return -1                         # lo > hi → empty range → not present
```

**Trace — `binary_search([2, 5, 8, 12, 16, 23, 38, 56, 72, 91], target=23)`:**

```
step 1:  lo=0  hi=9  mid=4   arr[4]=16  16 < 23 → lo = 5        [5..........9]
step 2:  lo=5  hi=9  mid=7   arr[7]=56  56 > 23 → hi = 6        [5.....6....9]
step 3:  lo=5  hi=6  mid=5   arr[5]=23  23 = 23 → return 5 ✅

10 elements → found in 3 comparisons; worst case for n elements = ⌈log₂(n)⌉ = 4.
1,000,000 elements → ~20 comparisons.
```

**Complexity:**
- **Time:** O(log n) — the array *halves* each step: n → n/2 → n/4 → ... → 1 takes log₂n steps.
- **Space:** O(1) iterative. Recursive version: O(log n) stack frames.

### The four binary search shapes (know all of them — interviews test the variants)

```python
# ── SHAPE 1: exact position of target (classic, above) ──

# ── SHAPE 2: lower bound — FIRST index where arr[i] >= target (insertion point) ──
def lower_bound(arr, target):
    lo, hi = 0, len(arr)              # hi = n (one past end — allows "insert at end")
    while lo < hi:                    # ← strict <, NOT <=
        mid = lo + (hi - lo) // 2
        if arr[mid] < target:
            lo = mid + 1              # mid is too small, discard it AND left
        else:
            hi = mid                  # mid might be the answer, keep it
    return lo                         # lo == hi == first index satisfying condition
    # Returns len(arr) if all elements < target — never out of range. Very robust.

# ── SHAPE 3: upper bound — FIRST index where arr[i] > target ──
def upper_bound(arr, target):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] <= target:
            lo = mid + 1
        else:
            hi = mid
    return lo

# ── SHAPE 4: BINARY SEARCH ON ANSWER — no searchable array at all ──
# "Find the MINIMUM value x such that check(x) is true"
def binary_search_answer(lo, hi, check):
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if check(mid):        # mid works → try smaller (we want minimum)
            hi = mid
        else:                 # mid fails → must go bigger
            lo = mid + 1
    return lo                 # smallest working value
    # Requires: check(x) must be MONOTONIC — false...false true...true
    # Example: "koko eats bananas in min hours h?" → check(h) = "can finish in h?"
    #          as h grows, finishing gets easier → monotonic → binary search works
```

**Shape 1 vs 2/3:** exact-match returns -1 when absent; lower/upper bounds *always* return a valid index (the position where the value would be inserted) — that makes them safer and more useful. Python's `bisect.bisect_left` **is** Shape 2, in C:
```python
import bisect
bisect.bisect_left(arr, target)   # lower_bound — O(log n)
bisect.bisect_right(arr, target)  # upper_bound
bisect.insort(arr, x)             # insert preserving order — but O(n) insert!
```

### Binary search on the answer — the hard-problem unlock

Problems phrased *"what is the minimum/maximum X such that..."* where X is a **number, not an array index** — the search space is the *value range*, verified by a greedy `check()`:

```python
# LeetCode 875: Koko eating bananas. Min speed to finish within h hours?
def min_eating_speed(piles, h):
    def can_finish(speed):                 # monotonic: faster → fewer hours
        return sum((p + speed - 1) // speed for p in piles) <= h
    lo, hi = 1, max(piles)                 # search the VALUE range [1, max]
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if can_finish(mid):
            hi = mid        # works → try slower
        else:
            lo = mid + 1    # too slow → go faster
    return lo
    # O(n log M): check() is O(n), called O(log M) times, M = value range
    # Without binary search: O(n * M) brute force over speeds — hopeless
```

**The pattern checklist for "search on answer":**
1. Is the question asking **min/max of a value**? (speed, capacity, distance, days, k)
2. Can I write `check(x)` = "is x feasible?" in O(n)-ish?
3. Is `check` **monotonic**? (if x works, does x+1 also work?) → yes = binary search valid

### Linear vs Binary — the comparison table

| | Linear Search | Binary Search |
|---|---|---|
| Prerequisite | none | **sorted** + index access |
| Time (worst) | O(n) | **O(log n)** |
| Time (best) | O(1) (first match) | O(1) (middle match) |
| Time (avg) | O(n) | O(log n) |
| Space | O(1) | O(1) iterative / O(log n) recursive |
| Works on linked list | ✅ | technically no (O(n) mid access) |
| n = 10⁶ comparisons | ~10⁶ | **~20** |
| Preprocessing cost | 0 | sort: O(n log n) — worth it if searching ≥ O(log n) times |

**When sorting first pays off:** one sort (O(n log n)) then k binary searches (O(k log n)) beats k linear scans (O(k·n)) as soon as `n log n < k·n`, i.e., **k > log n**. A handful of searches on a big array → sort first.

### RECAP
- **Linear:** O(n), no prerequisites, right for unsorted/tiny/one-off
- **Binary:** O(log n), needs sorted + indexable, built on one invariant — *answer stays in [lo, hi]*
- `lo + (hi-lo)//2` for mid; `while lo <= hi` for exact match, `while lo < hi` for bounds
- **lower/upper bound** always return valid positions — use them instead of exact-match when absence is common
- **Search on answer:** min/max value + monotonic `check(x)` → binary search over the value range
- Python: `bisect.bisect_left` is lower bound, already written in C

---

## 4.2 Sorting Algorithms

### WHY

Sorting is **the** preprocessing step: sorted data unlocks binary search, two pointers, merge logic, greedy choice, and dedup detection. Roughly 25% of all interview problems either sort directly or need the *concept* of ordering. You learn the classic algorithms not to reimplement them (never in production — `sorted()` is Timsort in C, faster than anything you'll write in Python) but because each teaches a structural idea that gets reused: partitioning (quicksort), merging (mergesort), incremental building (insertion sort), and selection (heapsort / selection sort).

### Introduction — the ground rules

A **comparison sort** orders elements by pairwise comparison → theoretical floor **O(n log n)** (any comparison-based sort must distinguish n! orderings; log₂(n!) ≈ n log n). Going faster requires non-comparison tricks (counting/radix sort, O(n) on bounded keys). **Stability** = equal elements keep their original relative order — critical when sorting by one key while preserving another (sort tuples by score, names stay alphabetical within equal scores).

| Algorithm | Best | Average | Worst | Space | Stable? | In-place? | Core idea |
|---|---|---|---|---|---|---|---|
| Bubble | O(n) | O(n²) | O(n²) | O(1) | ✅ | ✅ | swap adjacent out-of-order pairs |
| Selection | O(n²) | O(n²) | O(n²) | O(1) | ❌ | ✅ | select min, place at front |
| Insertion | O(n) | O(n²) | O(n²) | O(1) | ✅ | ✅ | grow sorted prefix, insert next |
| Merge | O(n log n) | O(n log n) | O(n log n) | O(n) | ✅ | ❌ | divide, sort halves, merge |
| Quick | O(n log n) | O(n log n) | O(n²) | O(log n) | ❌ | ✅ | partition around pivot |
| Heap | O(n log n) | O(n log n) | O(n log n) | O(1) | ❌ | ✅ | heapify, repeatedly extract max |
| Counting | O(n+k) | O(n+k) | O(n+k) | O(k) | ✅ | ❌ | count key occurrences |
| Radix | O(d(n+k)) | O(d(n+k)) | O(d(n+k)) | O(n+k) | ✅ | ❌ | digit-by-digit counting |
| **Timsort** (Python) | O(n) | O(n log n) | O(n log n) | O(n) | ✅ | ❌ | merge + insertion on runs |

### Bubble Sort — the teaching baseline

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):                 # each pass pushes the next-largest to the end
        swapped = False
        for j in range(n - 1 - i):         # −i: last i positions are already sorted
            if arr[j] > arr[j + 1]:        # compare ADJACENT pair
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:                    # optimization: no swaps → already sorted
            break                          # gives O(n) best case
    return arr
    # Pass 1: [5,3,8,1] → [3,5,1,8]  (8 bubbled to the end)
    # Pass 2:        → [3,1,5,8]
    # Pass 3:        → [1,3,5,8]  done
    # O(n²) comparisons/swaps worst & avg, O(n) best (with swapped flag), O(1) space, stable
```
**Lesson it teaches:** the "adjacent swap propagates extremes to their home" mechanic, and the early-exit optimization (best case O(n)).

### Selection Sort — the teaching baseline

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):                 # fill position i
        min_idx = i
        for j in range(i + 1, n):          # scan the UNSORTED suffix for the minimum
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]   # swap it into place
    return arr
    # [64, 25, 12, 22] → min=12 swap→[12,25,64,22] → min=22 swap→[12,22,64,25] → ...
    # ALWAYS O(n²) even on sorted input (no early exit possible — must scan for min)
    # Fewest swaps: exactly n−1 → useful when writes are expensive (flash memory)
    # Not stable: the swap can jump an element over equal ones. O(1) space.
```
**Lesson it teaches:** "select the extreme of the unsorted region, place it, shrink the region" — this exact logic reappears as **heap sort** (selection with a heap = O(n log n)).

### Insertion Sort — the teaching baseline (and hidden production hero)

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):           # arr[0..i-1] is SORTED prefix (invariant)
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:     # shift larger elements right
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key                   # place key in its hole
    return arr
    # [12, 11, 13, 5, 6]
    #  i=1: key=11 → shift 12 → [11,12,13,5,6]
    #  i=2: 13 stays → [11,12,13,5,6]
    #  i=3: key=5 → shift 13,12,11 → [5,11,12,13,6]
    #  i=4: key=6 → shift 13,12,11 → [5,6,11,12,13]
    # Best O(n) — already-sorted input never enters the while loop
    # In-place, O(1) space, STABLE, adaptive → excellent for nearly-sorted data
```
**Why it matters beyond teaching:** real libraries (including Timsort) fall back to insertion sort for small or nearly-sorted runs because its constants are tiny and it's O(n) on sorted input. **Nearly-sorted data → insertion sort beats quicksort.** Also the go-to for *streaming* data: keep a sorted list, insert each new item O(n) but with minuscule constants.

### Merge Sort — divide and conquer, guaranteed O(n log n)

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left  = merge_sort(arr[:mid])          # DIVIDE: sort left half
    right = merge_sort(arr[mid:])          #        sort right half
    return merge(left, right)              # COMBINE: two sorted halves → one sorted

def merge(a, b):                           # both already sorted — linear merge
    res, i, j = [], 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:                   # <= keeps it STABLE
            res.append(a[i]); i += 1
        else:
            res.append(b[j]); j += 1
    res.extend(a[i:]); res.extend(b[j:])   # leftovers (at most one non-empty)
    return res
    # [38,27,43,3] → split → [38,27],[43,3] → [27,38],[3,43] → [3,27,38,43]
    # O(n log n) ALWAYS (splits log n levels × O(n) merge work each)
    # NOT in-place: O(n) extra space. STABLE. Predictable performance.
    # Recurrence: T(n) = 2T(n/2) + O(n) → O(n log n)  ← Part 1 §1.3(f)
```
**Lesson it teaches:** *merge two sorted things in linear time.* This reappears in: merging K sorted lists (heap + merge), external sorting, counting inversions, interval merging, and "sorted array" two-pointer problems.

### Quick Sort — partition, then recurse

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lo    = [x for x in arr if x <  pivot]   # Pythonic partition (readable version)
    mid   = [x for x in arr if x == pivot]
    hi    = [x for x in arr if x >  pivot]
    return quick_sort(lo) + mid + quick_sort(hi)
    # Better avg: O(n log n) with tiny constants, cache-friendly, in-place possible
    # Worst: O(n²) if pivots are always extreme (already-sorted input + naive pivot)
    # NOT stable (in-place versions). Space: O(log n) stack avg, O(n) worst.
    # Real implementations: random pivot or median-of-three → worst case vanishes
```
**Lesson it teaches:** **partitioning** — one pass that splits data around a pivot into `<` and `>` groups, putting the pivot in its final place. Partition logic is reused in: quickselect (kth smallest, O(n) avg), Dutch national flag, 3-way partition, and Lomuto/Hoare interview follow-ups.

### Heap Sort (know it exists): build a max-heap from the array O(n), repeatedly extract max → O(n log n) worst-case, O(1) space, not stable. Best of both bubble's in-place and merge's guaranteed bound — but poor cache locality, so quicksort usually wins in practice. Details in Part 5's heap section.

### Python Built-in Sorting

```python
nums = [5, 2, 9, 1]
sorted(nums)      # NEW sorted list — original untouched; works on ANY iterable
nums.sort()       # IN-PLACE — modifies, returns None
nums = sorted(nums, reverse=True)   # descending

# Key functions — the power tool:
words = ["banana", "pie", "apple"]
sorted(words, key=len)                          # sort by length
sorted(words, key=str.lower)                    # case-insensitive
sorted(words, key=lambda w: w.count('a'))       # custom criterion
sorted(students, key=lambda s: (-s.gpa, s.name))  # multi-key: gpa desc, name asc
# ↑ this replaces writing a custom comparator — in Python, key functions ARE sorting

# Sorting while keeping index association (argsort — a numpy concept in pure Python):
indexed = sorted(range(len(nums)), key=lambda i: nums[i])
```

**`sorted()` vs `.sort()` — the difference table:**

| | `sorted(iterable)` | `list.sort()` |
|---|---|---|
| Returns | **new** list | `None` (in-place!) |
| Works on | any iterable: tuple, dict, string, generator | lists only |
| Original | untouched | modified |
| Memory | O(n) extra | O(1) extra |
| Use when | you need to keep the original / sort a non-list | you own the list and don't need it |
| Example gotcha | `x = nums.sort()` → `x is None` ← classic bug | |

**Built-in vs manual — the honest comparison:**

| | `sorted()` (Timsort) | Your bubble/insertion/merge in Python |
|---|---|---|
| Time constant | C speed, ~10–50x faster | interpreted loop overhead |
| Adaptive | ✅ O(n) on sorted runs | insertion O(n), bubble with flag O(n) |
| Stable | ✅ | insertion/bubble/merge yes, quick/selection no |
| Memory | O(n) | merge O(n), quick/bubble O(1) |
| Interviews | use it AFTER solving the algorithmic problem | you must be able to WRITE one |
| Verdict | always, in real code | for understanding + assessments |

**Interview protocol:** if the problem isn't *about* sorting, `sorted()` is the right move and interviewers expect it. If it IS about sorting (implement merge sort, find first bad version, sort by custom rules) — write it. Knowing *when* to just call `sorted()` is itself a sign of maturity.

### Time complexity comparison — best/average/worst

| Algorithm | Best | Average | Worst | Note |
|---|---|---|---|---|
| Linear search | O(1) | O(n) | O(n) | unsorted data |
| Binary search | O(1) | O(log n) | O(log n) | sorted data |
| Bubble sort | O(n) | O(n²) | O(n²) | O(n) if no-swap exit |
| Selection sort | O(n²) | O(n²) | O(n²) | never better than n² |
| Insertion sort | O(n) | O(n²) | O(n²) | great when nearly sorted |
| Merge sort | O(n log n) | O(n log n) | O(n log n) | guaranteed, stable |
| Quick sort | O(n log n) | O(n log n) | **O(n²)** | fast avg, bad pivots hurt |
| Heap sort | O(n log n) | O(n log n) | O(n log n) | in-place, not stable |
| Timsort (`sorted`) | O(n) | O(n log n) | O(n log n) | what Python actually runs |

**The `n log n` intuition:** each of the log n "levels" does O(n) total work — merge sorts halves (levels are explicit), quicksort partitions shrink the problem (levels amortize), heaps sift down log n per element. Any structure that *splits or sinks* log n times per element gives n log n.

### RECAP
- Comparison sorts **cannot beat O(n log n)** — information-theoretic limit
- **Bubble/selection/insertion:** O(n²), teach mechanics; insertion is the one that survives in real libraries (adaptive, stable, O(n) on sorted data)
- **Merge:** guaranteed n log n, stable, O(n) space — merge-two-sorted-lists is the reusable trick
- **Quick:** fastest constants, partition idea, O(n²) worst without good pivots
- **`sorted()` returns new, `.sort()` returns None** (in-place) — classic bug source
- **`key=` functions replace custom comparators**; `sorted(nums, key=..., reverse=True)` covers most needs
- Use built-ins in real code; hand-write algorithms only when the problem asks

---

## 4.3 Two Pointers

### WHY

Nested loops over a pair of indices are the default O(n²) reflex. But when the array is **sorted** (or you can sort it), or when you're scanning from **both ends toward a middle goal**, two pointers walk toward each other (or in tandem) and settle the whole problem in **one O(n) pass** — because every movement of a pointer is permanent, nothing is revisited.

### WHAT / HOW

Two pointers = maintain two indices with a **moving rule derived from the problem's condition**, advance them monotonically, never reset. The rule replaces the inner loop.

**Pattern A — opposite ends, converging (sorted data):**
```python
# LeetCode 167: Two Sum II — sorted array, find pair summing to target
def two_sum_sorted(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        cur = arr[lo] + arr[hi]
        if cur == target:
            return [lo, hi]
        if cur < target:
            lo += 1          # sum too small → need bigger values → move left up
        else:
            hi -= 1          # sum too large → need smaller values → move right down
    return []                # O(n) time, O(1) space — replaces the O(n²) pair loop
    # WHY it's correct: each step eliminates one element's worth of pairs;
    # a matched pair can't be missed because we only move when the sum says to.
```

**Pattern B — same direction, fast/slow (aka "runner"):**
```python
# Remove duplicates in sorted array — fast explores, slow writes
def remove_dups(nums):
    if not nums: return 0
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1
```

**Pattern C — shrink from one side (linked list / arrays):**
```python
# Container With Most Water (LC 11): two ends, move the SHORTER side inward
def max_area(h):
    lo, hi, best = 0, len(h) - 1, 0
    while lo < hi:
        best = max(best, min(h[lo], h[hi]) * (hi - lo))
        if h[lo] < h[hi]: lo += 1      # only moving the shorter side can improve
        else:             hi -= 1
    return best
```

**Classic family:** two-sum (sorted), three-sum (fix i + two pointers), container with most water, valid palindrome, remove-dups-in-place, merge sorted arrays, reverse vowels, partition array (Dutch flag uses three pointers).

```python
# Three Sum — the O(n²) that two pointers makes respectable
def three_sum(nums):
    nums.sort()                                   # O(n log n) — enables the pointers
    res = []
    for i in range(len(nums) - 2):                # fix the FIRST element
        if i > 0 and nums[i] == nums[i-1]: continue   # skip duplicate anchors
        lo, hi = i + 1, len(nums) - 1             # two pointers on the REST
        while lo < hi:
            s = nums[i] + nums[lo] + nums[hi]
            if s == 0:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1; hi -= 1
                while lo < hi and nums[lo] == nums[lo-1]: lo += 1   # skip dup pairs
            elif s < 0: lo += 1
            else:       hi -= 1
    return res                                     # O(n²) total: n anchors × O(n) scan
```

### RECAP
- Two pointers replaces pair-nested loops when the movement rule is **monotonic** (indices only advance)
- **Sorted array → opposite-ends convergence**; same-direction → runner/dedup patterns
- Correctness argument = "each move eliminates a whole class of pairs without losing the answer"
- Sorting first (O(n log n)) buys an O(n²) → O(n²)→ actually O(n) or O(n²) scan — three-sum becomes O(n²) instead of O(n³)

---

## 4.4 Sliding Window

### WHY

A special family of problems asks about **contiguous subarrays/substrings with a property** ("longest with ≤ k distinct", "minimum covering all characters", "sum ≤ k"). Trying every start/end pair is O(n²) — but notice: consecutive windows **overlap almost entirely**. Re-summing from scratch throws away information you already had. A sliding window keeps a running summary (sum, counts, set) and adjusts it **incrementally** as the edges move — every element enters the window exactly once and leaves exactly once → **O(n)**.

### WHAT — the two shapes

**Fixed size k:** always exactly k elements.
```python
# Max sum of any window of size k — O(n)
def max_window_sum(nums, k):
    window = sum(nums[:k])          # build first window once: O(k)
    best = window
    for i in range(k, len(nums)):   # slide: add new, drop old
        window += nums[i] - nums[i - k]   # O(1) adjustment instead of O(k) re-sum
        best = max(best, window)
    return best
```

**Variable size:** window grows/shrinks based on a validity condition.
```python
# LeetCode 3: longest substring WITHOUT repeating characters — O(n)
def length_of_longest_substring(s):
    last_seen, best, left = {}, 0, 0
    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1   # invalid → jump left PAST the previous ch
        last_seen[ch] = right
        best = max(best, right - left + 1)
    return best

# The generic shrink loop (used in 90% of variable windows):
#   for right in range(n):
#       add nums[right] to window state
#       while state is INVALID:       ← while, NOT if (may need multiple shrinks)
#           remove nums[left] from state
#           left += 1
#       record answer (window is valid now)
```

### The invariant — what keeps it correct

> **The window is always valid at the bottom of the loop** (after the while-shrink). Answers are recorded only in valid states.

```python
# LeetCode 209: minimum-length subarray with sum ≥ target
def min_subarray_len(target, nums):
    left = cur = 0
    best = float('inf')
    for right, x in enumerate(nums):
        cur += x                                  # GROW
        while cur >= target:                      # SHRINK while still satisfying
            best = min(best, right - left + 1)
            cur -= nums[left]
            left += 1                             # smallest window ending at right found
    return best if best != float('inf') else 0
    # Each index enters once (right loop) and leaves once (left loop) → O(n)
```

### Window-state toolkit (what to keep inside the window)

| Condition in problem | Window state |
|---|---|
| Sum / average constraint | running `int` sum |
| "k distinct characters" | `Counter` + `len(counter)` |
| "all characters of pattern present" | countdown of unsatisfied chars |
| Max/min in window | `deque` monotonic (Part 5) or heap |
| "no repeats" | `set` of current members (or last-index map) |

### When sliding window does NOT apply (know the boundary!)

- **Unsorted array + negatives + "sum exactly k"** → shrinking logic breaks (adding a negative makes sums non-monotonic) → use **prefix sums + hashmap** instead.
- Problem asks about **non-contiguous** elements → it's a set/dict problem, not a window.
- Constraint depends on the *middle* of the window, not its edges → probably two pointers or DP.

### RECAP
- Sliding window = **contiguous subarray + overlapping consecutive windows + incremental state** → O(n)
- Fixed window: build once, `+= in, -= out`. Variable window: `add right → while invalid: shrink left → record`
- **`while`, not `if`,** when shrinking (multiple elements may need removal)
- Window state: sum / Counter / set depending on the constraint
- Breaks on non-contiguous asks and negative-poisoned sums → prefix-sum hashmap instead

---

---

---

# Part 5 — Trees, Heaps & Tries

## 5.1 Binary Trees & BSTs

### WHY

Trees are the data structure of **hierarchy** — and hierarchy is everywhere: file systems, DOM, organization charts, ASTs, decision processes, family trees, and crucially, **search with sorted structure**: a binary search tree with balanced height gives O(log n) search/insert/delete *while keeping elements ordered* (which hash maps can't). Every database index, JSON parser, and compiler front-end you touch runs on trees. In interviews, trees are the most common *structure-specific* topic — almost every interview has at least one tree question.

### WHAT

```
 Node terminology (memorize these — interviewers use them):
                 ┌─────── 15 ◀──── ROOT (no parent, entry point)
                /    \
           ┌── 10     20 ──┐      ◀ internal nodes
          /   \      /    \
        6      14  17     25      ◀ LEAVES (no children, degree 0)
       / \                            ◀ EDGE (connection parent→child)
      3   7
                                  ◀ HEIGHT: longest path node→leaf
                                     leaf height = 0 (or 1, say which!)
                                     height(10) = 2, height(15) = 3
                                  ◀ DEPTH: path from ROOT to node
                                     depth(3) = 2, depth(15) = 0
                                  ◀ DEGREE: number of children of a node

 Binary tree    : every node has ≤ 2 children (left, right)
 Full binary    : every node has 0 or 2 children
 Complete       : all levels filled except possibly last, LEFT-aligned
 Perfect       : all leaves same depth, all full
 Balanced       : height = O(log n) — |height(L) − height(R)| ≤ 1 per node
 BST invariant  : LEFT subtree < node < RIGHT subtree  (ALL nodes, not just children!)
```

**The BST invariant is global:** every node in the left subtree is smaller than the root, *not just the direct child*. This is what makes log-time search possible — each comparison kills a whole subtree.

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### The recursive worldview — trees ARE recursion

Every tree problem is: **handle this node + recurse on children**. The tree's own shape gives you the base case (a leaf's children are `None`).

```python
# ── The 4 traversals (know all — they're one skeleton with moved print) ──

def inorder(root):        # LEFT → NODE → RIGHT  ★ produces sorted order in a BST
    if not root: return
    inorder(root.left)
    print(root.val)       # ← the visit sits BETWEEN the two recursions
    inorder(root.right)

def preorder(root):       # NODE → LEFT → RIGHT   (use: copy tree, serialize, prefix)
    if not root: return
    print(root.val)
    preorder(root.left)
    preorder(root.right)

def postorder(root):       # LEFT → RIGHT → NODE  (use: delete, compute aggregates)
    if not root: return
    postorder(root.left)
    postorder(root.right)
    print(root.val)

def levelorder(root):      # BFS — uses a QUEUE (see Part 6 connection)
    if not root: return []
    res, q = [], deque([root])
    while q:
        node = q.popleft()
        res.append(node.val)
        if node.left:  q.append(node.left)
        if node.right: q.append(node.right)
    return res

# Trace on:      1
#               / \
#              2   3
#             / \
#            4   5
# inorder:   4 2 5 1 3      preorder: 1 2 4 5 3      postorder: 4 5 2 3 1
# levelorder: 1 2 3 4 5
```

**Why the three differ:** they're the same exploration with a different *moment of processing* the node — before descending left, after left returns, or after both subtrees finish. Memorize by the middle word: **N**LR / L**N**R / LR**N**.

### Iterative traversals (the follow-up interview: "without recursion")

```python
def inorder_iter(root):
    res, stack, cur = [], [], root
    while stack or cur:
        while cur:                 # go as far LEFT as possible
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()          # no more left → process this node
        res.append(cur.val)
        cur = cur.right            # then explore right subtree
    return res
    # The explicit stack replaces the call stack — same O(n)/O(h) bounds
```

### The core tree problems (with complexity)

```python
# 1) MAX DEPTH — the "hello world" of tree recursion — O(n)/O(h)
def max_depth(root):
    if not root: return 0                       # base: empty tree has depth 0
    return 1 + max(max_depth(root.left),        # my depth = 1 + deepest child
                   max_depth(root.right))

# 2) VALIDATE BST — the "did you understand the invariant" test — O(n)/O(h)
def is_valid_bst(root, lo=float('-inf'), hi=float('inf')):
    if not root: return True
    if not (lo < root.val < hi): return False   # THIS node's bounds
    return (is_valid_bst(root.left, lo, root.val) and    # left subtree: all < node
            is_valid_bst(root.right, root.val, hi))      # right: all > node
    # ★ The bounds-passing trick is the key insight: the constraint is inherited
    # down the WHOLE subtree, not checked only against the direct parent.
    # Common bug: checking only root.left.val < root.val — fails on deep violations:
    #        5
    #       / \
    #      1   6        ← 6 > 5 ✓ ... but
    #         / \
    #        4   7      ← 4 is in RIGHT subtree of 5 but < 5 → INVALID
    #   Local check passes, global invariant violated. Bounds catch it.

# 3) SAME TREE / SYMMETRIC — O(n)
def is_same(p, q):
    if not p or not q: return p is q             # both None → True; one None → False
    return (p.val == q.val and
            is_same(p.left, q.left) and
            is_same(p.right, q.right))

# 4) LOWEST COMMON ANCESTOR (BST version) — O(h) — walk down once
def lca_bst(root, p, q):
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left          # both smaller → ancestor is left
        elif p.val > root.val and q.val > root.val:
            root = root.right         # both bigger → ancestor is right
        else:
            return root               # split point (or one is root) → LCA found
    # General binary tree version: postorder — if left returns node and right
    # returns node → that's the split. If only one side → bubble it up.

# 5) LEVEL ORDER WITH LEVELS (grouped) — O(n)
def level_groups(root):
    if not root: return []
    res, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):           # ← freeze current width = one level
            node = q.popleft()
            level.append(node.val)
            if node.left:  q.append(node.left)
            if node.right: q.append(node.right)
        res.append(level)
    return res

# 6) PATH SUM / MAX PATH — the hard family
def has_path_sum(root, target):           # any root→leaf path equals target
    if not root: return False
    if not root.left and not root.right:
        return target == root.val
    return (has_path_sum(root.left, target - root.val) or
            has_path_sum(root.right, target - root.val))
    # max_path_sum variant (LC 124): postorder returning "best downward gain"
    # while updating a global "best through this node" — classic hard problem.
```

**Complexity of every recursive tree algorithm:**
- **Time:** O(n) — each node visited a constant number of times.
- **Space:** O(h) = O(log n) for a balanced tree, **O(n) worst case** (degenerate chain = linked list → recursion depth n → `RecursionError` risk).

### Binary Search Tree — insertion, deletion, search

```python
class BST:
    def __init__(self):
        self.root = None

    # INSERT — O(h): walk down, place at the empty spot — O(log n) if balanced
    def insert(self, val):
        def _ins(node, v):
            if not node: return TreeNode(v)        # found the empty parent slot
            if v < node.val:  node.left = _ins(node.left, v)
            elif v > node.val: node.right = _ins(node.right, v)
            return node                            # duplicates: ignore (or count)
        self.root = _ins(self.root, val)

    # SEARCH — O(h) — the binary-search-on-a-tree walk
    def search(self, val):
        node = self.root
        while node:
            if val == node.val: return True
            node = node.left if val < node.val else node.right
        return False

    # DELETE — the trickiest standard operation — O(h)
    def delete(self, val):
        def _del(node, v):
            if not node: return None
            if v < node.val:
                node.left = _del(node.left, v)
            elif v > node.val:
                node.right = _del(node.right, v)
            else:                                 # found it — 3 cases
                if not node.left:  return node.right       # (a) no left child
                if not node.right: return node.left        # (b) no right child
                # (c) TWO children: replace with INORDER SUCCESSOR
                #      (smallest node in right subtree), then delete that successor
                succ = node.right
                while succ.left: succ = succ.left
                node.val = succ.val                # copy successor's value up
                node.right = _del(node.right, succ.val)    # remove successor's old spot
            return node
        self.root = _del(self.root, val)
```

**Why the inorder successor for two-child deletion?** Inorder traversal is *sorted* — the successor is the **smallest value larger than the deleted node**, so swapping it in preserves the BST invariant for both subtrees. (The inorder *predecessor* works too — pick one and be consistent.)

### The balance problem — why plain BSTs fail

Insert sorted input `1,2,3,4,5` into a plain BST → a right-leaning chain:
```
1 → 2 → 3 → 4 → 5     ← BST degenerated into a linked list! O(n) search
```
Height = n, so every O(h) operation becomes O(n). **Solutions:** self-balancing trees (AVL, Red-Black — rotate to keep height O(log n)), or **don't insert sequentially** / shuffle input. In Python you'd use `bisect` on a list, or `sortedcontainers`, rather than hand-rolling AVL — but **know that the problem exists**; it's a favorite follow-up: *"what's the worst case for BST search and how do you fix it?"* → rotations / balanced variants.

### PROS / CONS of trees

**Pros:** O(log n) search/insert/delete **with ordering** (BST balanced); natural for hierarchy; traversals give sorted/inorder/level semantics; recursive solutions are clean; bounded shape enables proofs.
**Cons:** unbalanced → O(n); pointer-heavy, cache-unfriendly; more implementation complexity than hash maps; O(h) recursion space — deep trees risk stack overflow.

### COMPARE

| | BST (balanced) | Hash map | Sorted array + bisect |
|---|---|---|---|
| Search | O(log n) | **O(1)** avg | O(log n) |
| Insert/delete | O(log n) | O(1) avg | O(n) shift |
| **Range query** `[lo,hi]` | **O(log n + k)** | ❌ impossible | O(log n + k) |
| Ordered iteration | **O(n) in order** | insertion order only | O(n) sorted |
| Predecessor/successor | **O(log n)** | ❌ | O(1) neighbors + O(log n) search |
| Memory | node overhead | table overhead | compact |
| Worst case | O(log n) with balancing | O(n) degenerate | O(log n) |

**Rule of thumb:** need ordering/ranges/predecessor → tree family. Need pure lookup → hash map. Sorted array + bisect covers most Python needs.

### RECAP
- Tree = nodes with ≤ 2 children; **BST invariant is global**: left-subtree-all-smaller < node < right-subtree-all-larger
- **Inorder on BST = sorted output**; preorder = copy/serialize; postorder = aggregate/delete; levelorder = queue BFS
- Recursive template: `if not node: return base` + process + recurse children → **O(n) time, O(h) space**
- Validate BST with **inherited bounds** (lo, hi), not parent comparison
- Delete with two children → swap in **inorder successor**
- Unbalanced BST degrades to O(n) → balanced variants / why hash maps exist

---

## 5.2 Heaps & Priority Queues

### WHY

Queues process in *arrival* order and stacks in *recent* order — but often you need **"the biggest/smallest thing next"**: task schedulers run the most urgent job, "top K recommendations" needs the K highest scores, Dijkstra always expands the closest unexplored node, "median of a stream" needs both ends' extremes. A full sort every time is O(n log n) *per query*; a heap delivers the extreme in **O(1)** and maintains order on insert in **O(log n)** — the sweet spot when you repeatedly need the min/max but not full sorted order.

### WHAT — the structure

A **binary heap** is a **complete binary tree** (all levels full, last level left-packed) that satisfies the **heap property**:
- **Max-heap:** every parent ≥ its children → root is the maximum
- **Min-heap:** every parent ≤ its children → root is the minimum

```
Min-heap:              NOT a heap (parent < child violated):

      1                     1
    /   \                 /   \
   3     5               7     2      ← 7 > 2? OK at top...
  / \   /               / \
 8   4 9               9   6          ← but where's the ORDER?
                                       Heap ≠ sorted! Only the ROOT is
complete tree:                guaranteed extreme. Siblings unordered.
every slot filled left→right.
```

**Key insight — heaps don't give you sorted order**, only the extreme. That's not a limitation; it's the design. Sorting everything when you only need the top is wasted work.

**Storage: array indexing (no pointers needed):**
```
Tree:            1
                / \
               3   5
              / \  /
             8  4 9

Array:  [1, 3, 5, 8, 4, 9]
index:   0  1  2  3  4  5

parent(i) = (i-1)//2        child(i) = 2i+1, 2i+2
        i=3 (val 8): parent = (3-1)//2 = 1 → val 3 ✅
        i=1 (val 3): children 3,4 → 8, 4 ✅
```
A complete tree fits perfectly in an array with zero wasted slots — *this* is why heaps are arrays in every language.

### The two heap operations (trace them once, you'll never forget)

```python
# PUSH (up-heap / bubble up): append at the end, then swap with parent while smaller
#  push 0 into [1,3,5,8,4,9]:
#  step 1: append → [1,3,5,8,4,9,0]   (0 at index 6, position of next free slot)
#  step 2: parent(6)=(6-1)//2=5 → 9 > 0 → SWAP → [1,3,5,8,4,0,9]
#  step 3: parent(5)=2 → 5 > 0 → SWAP → [1,3,0,8,4,5,9]
#  step 4: parent(2)=0 → 1 > 0 → SWAP → [0,3,1,8,4,5,9]
#  step 5: parent(0) → none → DONE          ↑ O(log n) swaps, height of tree

# POP (down-heap / sift down): move LAST element to root, sink it
#  pop min from [0,3,1,8,4,5,9]:
#  step 1: save root=0 (answer), move 9 to root → [9,3,1,8,4,5]
#  step 2: children of 0: 3,1 → min child 1 < 9 → SWAP → [1,3,9,8,4,5]
#  step 3: children of 2 (index of 9): 4,5 → values 4,5 → min 4 < 9 → SWAP
#          → [1,3,4,8,5,9]
#  step 4: index 4 has no children → DONE. return 0.
#  O(log n) swaps.
```

### Python's `heapq` (min-heap, in-place on a list)

```python
import heapq

heap = []
heapq.heappush(heap, 5)      # insert         O(log n)
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)
heapq.heappop(heap)          # → 1 (minimum)  O(log n)
heap[0]                      # peek min        O(1)
len(heap)                    #                O(1)

# Build a heap from an existing list: O(n) — NOT O(n log n)!
heap = [7, 2, 5, 3, 9]
heapq.heapify(heap)          # sift-down all internal nodes at once

# Top-K / N-largest helpers (heap internally):
heapq.nlargest(3, nums)      # → 3 biggest     O(n log k)
heapq.nsmallest(3, nums)     # → 3 smallest    O(n log k)

# MAX-heap trick (Python's heapq is min-only):
# push NEGATIVE values, or push (priority, item) tuples and remember
# the comparison is tuple-lexicographic:
maxh = [-x for x in nums]                 # negate
# or for objects: heapq.heappush(h, (-score, name))
```

**The idiomatic heap entry is a tuple:** `heapq.heappush(h, (priority, item))` — tuples compare element-wise, so priority orders the heap and the item breaks ties. Remember the tuple's first field drives everything.

### The five interview problems that ARE heaps

```python
# 1) KTH LARGEST (LC 215) — min-heap of size k: O(n log k)
def find_kth_largest(nums, k):
    heap = []
    for x in nums:
        heapq.heappush(heap, x)
        if len(heap) > k:
            heapq.heappop(heap)        # evict smallest of the top-k
    return heap[0]                     # smallest among the k largest = kth largest
    # Alternative: heapify all (O(n)) then pop k times: O(n + k log n)

# 2) TOP-K FREQUENT (LC 347) — freq map + heap
def top_k_frequent(nums, k):
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)   # O(n + k log n)
    # bucket-sort version: buckets[freq] = [items] → O(n), also worth knowing

# 3) MERGE K SORTED LISTS (LC 23) — THE heap problem
def merge_k_lists(lists):
    heap = [(l[0], i, 0) for i, l in enumerate(lists) if l]  # (value, list#, idx)
    heapq.heapify(heap)
    out = []
    while heap:
        val, li, idx = heapq.heappop(heap)
        out.append(val)
        if idx + 1 < len(lists[li]):
            heapq.heappush(heap, (lists[li][idx + 1], li, idx + 1))
    return out
    # O(N log k): N total elements, heap holds ≤ k heads
    # ★ why tuple? (val, list#, idx): values may TIE — without list# Python
    #   would compare list objects and crash (or compare nodes — TypeError)

# 4) K CLOSEST POINTS (LC 973) — same shape: push (dist, point), keep k, pop farthest
# 5) REORGANIZE STRING / TASK SCHEDULER — (count, char) heap: always use the
#    most-frequent-still-legal character; proves greedy with heap is optimal
```

### PROS / CONS
**Pros:** O(1) min/max; O(log n) insert/delete; O(n) heapify; O(n log k) top-K beats full sort when k ≪ n; array-backed (compact, cache-friendly); streams — handles data you haven't seen yet, which a pre-sorted array can't.
**Cons:** no O(1) search for arbitrary values (that's not its job); no ordered iteration (pop them all = sort, O(n log n)); min-only in Python (negate for max); duplicates allowed (careful with tie-breaking).

### COMPARE — heap vs sorted array vs BST vs queue

| Need | Best structure | Complexity | Note |
|---|---|---|---|
| Repeated min/max extraction | **heap** | O(1) peek, O(log n) pop | sorted array pop(0) = O(n) shift |
| Top-K of a static array | heap or sort | O(n log k) vs O(n log n) | heap wins when k small |
| Top-K of a *stream* | **heap** | O(n log k) | sort impossible (data still arriving) |
| Everything sorted | `sorted()` | O(n log n) | heap pop-all is the same cost, worse constants |
| Random lookup by key | dict | O(1) | heap can't |
| Ordered + extremes + ranges | BST / sorted list | O(log n) | heap gives extremes only |
| Strict FIFO fairness | queue | O(1) | heap is priority, not arrival order |

### RECAP
- Heap = **complete binary tree in an array**; parent `(i-1)//2`, children `2i+1`, `2i+2`
- **Only the root is guaranteed extreme** — siblings unordered, not fully sorted
- push/pop = **O(log n)** bubble/sink; **heapify = O(n)**
- Python: `heapq` (min-heap, in-place), max = negate or `(-prio, item)` tuples
- Tuple entries `(priority, ..., tiebreaker)` prevent comparison crashes
- Job families: **kth largest, top-k frequent, merge k lists, k closest, scheduling**

---

## 5.3 Tries (Prefix Trees)

### WHY

A family of problems revolves around **prefixes**: autocomplete ("what words start with 'app'?"), spell checking, word games (Boggle, Wordle validation), IP routing, longest common prefix. A hash map can check exact-word membership in O(1) — but it *cannot* enumerate "everything starting with pre" without checking every key (O(total keys)). A structure indexed **character by character** shares storage among words with common prefixes and turns prefix questions into simple tree walks.

### WHAT

A **trie** (from "reTRIEval", try-ee) is a tree where each node represents one character of the prefix; the path from the root *is* the string.

```
Words stored: "car", "card", "care", "dog"

                 [root]
        ┌──── c ────┐          ┌──── d ────┐
        │           │          │           │
       (c)         (d)        (d)         (o)
        │           │          │           │
        a           a*         o           g*
        │           │          │
        r*          r*         g*
        │           │          │
        d*          e*         (…)

  * = end-of-word marker (this node completes a real word)
  "car" path: root→c→a→r*       "card": continues r*→d*
  "ca" alone is NOT a word (no * on the 'a' node) but IS a valid prefix.
```

```python
class TrieNode:
    def __init__(self):
        self.children = {}          # char → TrieNode  (dict keeps it sparse)
        self.is_end = False         # marks complete words

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # INSERT "car" — O(length of word)
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()   # build the missing path
            node = node.children[ch]             # walk down one character
        node.is_end = True                        # the last node completes a word

    # SEARCH exact word — O(length of word) — independent of how many words stored!
    def search(self, word):
        node = self._walk(word)
        return node is not None and node.is_end   # must END a word, not just pass through
        # search "ca": walk succeeds but 'a'.is_end is False → False ✅

    # PREFIX check (starts_with) — O(length of prefix)
    def starts_with(self, prefix):
        return self._walk(prefix) is not None     # path exists = prefix exists

    def _walk(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return None                        # path dead-ends → no such prefix
            node = node.children[ch]
        return node

    # AUTOCOMPLETE — list all words with a given prefix
    def autocomplete(self, prefix):
        node = self._walk(prefix)
        if not node: return []
        out = []
        def dfs(n, path):                          # explore everything below
            if n.is_end: out.append(path)
            for ch, nxt in n.children.items():
                dfs(nxt, path + ch)
        dfs(node, prefix)
        return out
        # collects the whole SUBTREE under the prefix — exactly the answer set
```

### Complexity (the trie's selling point)

| Operation | Trie | Hash map | Sorted array |
|---|---|---|---|
| Insert word | O(L) | O(L) | O(n log n + L) |
| Exact search | O(L) | O(L) avg | O(log n · L) |
| Prefix search | **O(L)** | **O(total keys)** ❌ | O(log n · L + output) |
| List all with prefix | O(L + output) | O(N) scan | O(log n + output) |
| Find common prefix of set | walk shared path — O(longest) | impossible directly | sort + compare neighbors |

L = length of the query word, N = total characters across all keys. **Trie cost depends only on query length, never on collection size** — that's the point.

### PROS / CONS
**Pros:** prefix operations in O(L); shares storage for common prefixes (space-efficient for prefix-heavy sets); ordered traversal possible (sort children); predictable (no hashing, no collisions — a natural answer when someone asks "what if all keys collide?"); supports lexicographic range queries.
**Cons:** **memory-hungry in Python** — a dict per node (~100+ bytes overhead each) can dwarf the data (26-slot arrays are worse for sparse alphabets); slow constant factors from Python object overhead; overkill for exact-match-only lookups (dict wins); better alternatives exist for static dictionaries (DAWG/DAFSA, radix trees) — but those are beyond interview scope.

### When interviewers ask for a trie
Word search II (board + dictionary), autocomplete design, replace words (shortest prefix match), XOR/max-prefix bit variants (binary trie), phone directory, word breaks with dictionary. **Signal:** the problem gives you a *dictionary* and asks about *prefixes* or *sharing*.

### RECAP
- Trie = tree keyed by characters; path = string; `is_end` distinguishes words from prefixes
- Insert/search/prefix = **O(L)**, independent of dictionary size
- Autocomplete = DFS over the subtree below the prefix node
- Solves **prefix** queries that hash maps fundamentally can't
- Memory cost per node is high in Python — reach for it only when prefixes are the actual requirement

---

---

---

# Part 6 — Graphs

## 6.1 WHY graphs exist

Trees couldn't handle one thing: **cycles and many-to-many relationships**. A file system is a tree; the *web* is not — page A links to B links to C links back to A. Social connections, road networks, dependencies, state machines, version control, recommendation chains — everything real is a graph. Whenever the problem says "connected," "reachable," "shortest path," "dependencies," "groups of things that link together," or "can I get from X to Y," you're holding a graph.

And there's one algorithm skeleton underneath about **70% of graph interview problems**: BFS/DFS with a visited set. Master that once, and dozens of problems collapse into small variations.

## 6.2 WHAT — vocabulary

```
Graph G = (V, E)      V = vertices (nodes), E = edges (connections)

Directed (digraph):  A→B but maybe no B→A      Undirected: A—B both ways
Weighted:            edges have cost (distances, prices)
                     A ──5── B
Cyclic:              contains cycles            Acyclic (DAG): no cycles
                     (a path returning to start)  (dependencies, schedules)

      Undirected            Directed (DAG)           Weighted
        A—B                  A ──▶ B                  A ──3──▶ B
        |  |                 ▲    ▼                    \       ▲
        C—D                  E ◀──┘                    2▶C ──1──┘

Degrees: undirected → deg(A) = # neighbors
         directed   → in-degree / out-degree
Path: sequence of vertices connected by edges (no repeats = simple path)
Connected: a path exists between every pair (undirected)
```

## 6.3 Representations — choose BEFORE writing code

| | **Adjacency list** | **Adjacency matrix** |
|---|---|---|
| Storage | `dict: node → list of neighbors` | 2D array `n × n` |
| Space | **O(V + E)** | **O(V²)** |
| "Is A–B an edge?" | O(deg(A)) or O(1) with set | **O(1)** |
| Iterate neighbors of v | **O(deg(v))** | O(V) — must scan full row |
| Sparse graph (E ≈ V) | ✅ ideal | wasteful |
| Dense graph (E ≈ V²) | lists bloat | ✅ ideal |
| Adding an edge | O(1) append | O(1) write |
| Best for | **interviews, always** (most graphs are sparse) | dense, repeated edge-existence queries, Floyd–Warshall, grid-as-graph shortcuts |

**Python defaults for interviews:**
```python
from collections import defaultdict, deque

# 1) UNWEIGHTED — adjacency list
graph = defaultdict(list)
graph['A'].append('B'); graph['B'].append('A')     # undirected: add BOTH directions

# 2) WEIGHTED — list of (neighbor, weight) tuples
graph = {'A': [('B', 5), ('C', 1)], 'B': [('A', 5)], 'C': [('A', 1)]}

# 3) FROM EDGE LIST (very common input format in problems)
edges = [(0,1), (1,2), (2,0)]
graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)          # only if undirected

# 4) IMPLICIT GRIDS (number of islands, flooded areas) — no graph built at all!
#    grid[r][c]'s neighbors = 4 (or 8) adjacent cells — index arithmetic IS the edges
def neighbors(r, c, rows, cols):
    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            yield nr, nc
```
**Rule:** in interviews, start every problem by stating "I'll use an adjacency list — O(V+E) space, O(deg) neighbor iteration" — that alone signals competence.

## 6.4 BFS — breadth-first search (the queue traversal)

**Use when:** shortest path in an **unweighted** graph (fewest edges), level-by-level exploration, "is it reachable", bipartite checking, dependency level ordering.

```python
def bfs(graph, start):
    visited = {start}                 # ★ mark WHEN ENQUEUED (prevents double-queue)
    order = []
    q = deque([start])
    while q:
        node = q.popleft()            # FIFO → explores neighbors of x BEFORE grandchildren
        order.append(node)
        for nxt in graph[node]:
            if nxt not in visited:
                visited.add(nxt)
                q.append(nxt)
    return order
    # Time  O(V + E): every vertex enqueued once, every edge scanned once
    # Space O(V): visited + queue

# SHORTEST PATH (unweighted) — BFS level = distance. THE reason to use BFS.
def shortest_path(graph, start, goal):
    q = deque([(start, [start])])              # (node, path-so-far)
    visited = {start}
    while q:
        node, path = q.popleft()
        if node == goal:
            return path                        # first time reached = fewest edges
        for nxt in graph[node]:
            if nxt not in visited:
                visited.add(nxt)
                q.append((nxt, path + [nxt]))
    return None
    # Correct because all edges weigh 1: level k of BFS = exactly k edges from start.
    # (Weighted? → Dijkstra, below. This is the single most-tested distinction.)
```

**The grid BFS pattern (flood fill / islands / shortest path in maze):**
```python
def num_islands(grid):
    if not grid: return 0
    rows, cols = len(grid), len(grid[0])
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':              # unvisited land
                count += 1
                grid[r][c] = '0'               # mark IMMEDIATELY (or use visited set)
                q = deque([(r, c)])
                while q:
                    cr, cc = q.popleft()
                    for nr, nc in ((cr+1,cc),(cr-1,cc),(cr,cc+1),(cr,cc-1)):
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                            grid[nr][nc] = '0' # mark on ENQUEUE to avoid duplicates
                            q.append((nr, nc))
    return count
    # O(rows × cols): each cell enters the queue at most once
    # ★ DFS one-liner alternative exists — but BFS gives shortest distance for free
```

## 6.5 DFS — depth-first search (the stack/recursion traversal)

**Use when:** connectivity, cycle detection, topological sort, path *existence* (not shortest), exhaustive search, connected components, maze generation, any "explore everything reachable" with less memory than BFS at depth.

```python
# RECURSIVE (most common form — the call stack IS the stack)
def dfs(node, visited):
    visited.add(node)
    for nxt in graph[node]:
        if nxt not in visited:
            dfs(nxt, visited)

# ITERATIVE (explicit stack) — avoids RecursionError on deep graphs
def dfs_iter(start, graph):
    visited, stack, order = set(), [start], []
    while stack:
        node = stack.pop()           # LIFO → depth first
        if node in visited: continue
        visited.add(node)
        order.append(node)
        for nxt in graph[node]:      # reversed() if you need recursion's exact order
            if nxt not in visited:
                stack.append(nxt)
    return order
    # Time O(V + E), Space O(V)
```

**When to mark visited — enqueue (BFS) vs pop (DFS):** marking at *push* time prevents the same node entering the stack twice (could blow up to exponential). Marking at *pop* is also correct but with wasted pushes. **Interview-safe default: mark when you push/enqueue.**

### Cycle detection — follow-up that separates candidates

```python
# UNDIRECTED cycle: DFS with parent tracking (can't just use "visited”)
def has_cycle_undirected(n, edges):
    g = defaultdict(list)
    for u, v in edges: g[u].append(v); g[v].append(u)
    visited = set()
    def dfs(u, parent):
        visited.add(u)
        for v in g[u]:
            if v not in visited:
                if dfs(v, u): return True
            elif v != parent:          # neighbor already visited and NOT my parent
                return True            # → we've looped back = cycle
        return False
    return any(dfs(s, -1) for s in range(n) if s not in visited)

# DIRECTED cycle: 3-color DFS (white/gray/black) — "gray" = on current path
def has_cycle_directed(n, edges):
    g = defaultdict(list)
    for u, v in edges: g[u].append(v)
    color = {}                          # 0 unvisited, 1 on-stack(gray), 2 done(black)
    def dfs(u):
        color[u] = 1
        for v in g[u]:
            if color.get(v, 0) == 1: return True    # back-edge to on-stack node = cycle
            if color.get(v, 0) == 0 and dfs(v): return True
        color[u] = 2
        return False
    return any(dfs(u) for u in range(n) if color.get(u, 0) == 0)
    # In undirected graphs "neighbor is visited" often just means "my parent came back"
    # — that's why undirected needs the parent parameter and directed needs colors.
```

### BFS vs DFS — the comparison that decides your traversal

| | BFS | DFS |
|---|---|---|
| Data structure | **queue** (FIFO) | **stack / recursion** (LIFO) |
| Explores | all of depth k before depth k+1 | one path to the bottom, then backtracks |
| Shortest unweighted path | ✅ **guaranteed** | ❌ finds *a* path, not shortest |
| Memory | O(width) — can be huge on wide graphs | O(depth) — can be huge on deep graphs |
| Cycle detection | yes (visited) | yes (+ colors/parent) |
| Topological sort | ✅ (Kahn's, natural) | ✅ (post-order, less intuitive) |
| Typical problems | shortest path, level order, bipartite, nearest | connected components, cycle, topo, path existence, mazes |
| Complete traversal cost | O(V + E) both | O(V + E) both |

## 6.6 Topological sort (DAG only)

**The problem:** order tasks so every dependency comes before its dependent. Only defined on **directed acyclic graphs** — a cycle means the requirements are circular and impossible (that's why "course schedule" problems combine topo sort with cycle detection).

```python
# KAHN'S ALGORITHM — BFS on in-degrees (the interview default)
def topo_sort(n, edges):
    g = defaultdict(list)
    indeg = [0] * n
    for u, v in edges:                 # edge u → v means u BEFORE v
        g[u].append(v)
        indeg[v] += 1
    q = deque([i for i in range(n) if indeg[i] == 0])   # start with no-dependency tasks
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in g[u]:
            indeg[v] -= 1              # u done → one less dependency for v
            if indeg[v] == 0:
                q.append(v)            # v now unblocked
    if len(order) != n:
        return None                    # ← cycle exists (some tasks never unblocked)
    return order
    # O(V + E). The "len(order) != n → cycle" check is the cycle-detection bonus.

# DFS version: append node to FRONT after exploring children (reverse post-order)
def topo_dfs(n, edges):
    g = defaultdict(list)
    for u, v in edges: g[u].append(v)
    visited, order, on_stack = set(), [], set()
    def dfs(u):
        visited.add(u); on_stack.add(u)
        for v in g[u]:
            if v in on_stack: return False     # back edge → cycle
            if v not in visited and not dfs(v): return False
        on_stack.discard(u)
        order.append(u)                        # post-order...
        return True
    for u in range(n):
        if u not in visited and not dfs(u): return None
    return order[::-1]                         # ...reversed = topological order
```

**You need topological sort when:** prerequisites/courses, build systems, task scheduling with dependencies, resolving import orders, "alien dictionary" (order given as pairwise comparisons), "course schedule II" return order.

## 6.7 Dijkstra — shortest path on WEIGHTED graphs (no negative weights)

**The setup:** BFS gives shortest paths only when all edges weigh 1. With varied weights, a "further" node might reach the goal cheaper via a better edge — BFS's level order lies. Dijkstra fixes this with a **greedy rule: always finalize the closest unvisited node** (a min-heap provides that node).

```python
import heapq

def dijkstra(graph, start):
    """graph: node → [(neighbor, weight), ...]"""
    dist = {start: 0}
    heap = [(0, start)]                       # (distance-so-far, node)
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist.get(u, float('inf')):
            continue                          # STALE entry — already found shorter path
        for v, w in graph[u]:
            nd = d + w
            if nd < dist.get(v, float('inf')):
                dist[v] = nd                  # RELAXATION: cheaper route found
                heapq.heappush(heap, (nd, v))
    return dist
    # O((V + E) log V) with binary heap. Each edge relaxed at most once per
    # improvement; stale pops skipped by the dist check above.
    # ★ "lazy deletion" (skip stale heap entries) is the Python-idiomatic form —
    #   much simpler than an indexed decrease-key, same complexity.

# Path reconstruction: keep a parent map alongside dist
#   parent[v] = u whenever dist[v] improves → walk parent from goal to start
```

**The one critical rule:** **Dijkstra fails with negative edge weights.** A later "negative shortcut" can invalidate an already-finalized node. Negative weights → **Bellman–Ford** (O(V·E), also detects negative cycles) — that's the comparison question interviewers love: *"why not Dijkstra here?"*

**Relaxation is the whole algorithm:** `if dist[u] + w < dist[v]: update v`. Every shortest-path algorithm (Dijkstra, Bellman-Ford, Floyd-Warshall, SPFA) is a different *order and strategy* of applying that one line.

| | BFS | Dijkstra | Bellman-Ford | Floyd-Warshall |
|---|---|---|---|---|
| Weights | all = 1 | non-negative | any (detects neg cycles) | any, all pairs |
| Time | O(V+E) | O((V+E) log V) | O(V·E) | O(V³) |
| Question | fewest edges | shortest from **one** source | shortest, negative OK | shortest **all pairs** |

## 6.8 Union-Find (Disjoint Set Union)

**Why:** some questions aren't about *paths* but about **grouping**: "how many connected components", "are these two nodes already connected", "merge these groups". Re-running BFS per query is O(Q·(V+E)). Union-Find answers connectivity in **near-O(1)** per operation — amortized **α(V)** (inverse Ackermann — grows so slowly it's ≤ 4 for any practical V; effectively constant).

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))     # each node its own group
        self.rank = [0] * n              # heuristic: keep trees short
        self.count = n                   # number of disjoint components

    def find(self, x):                   # which group is x in?
        # PATH COMPRESSION: every node on the way points straight to the root
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]   # halve the height
            x = self.parent[x]
        return x
        # (or the clean recursive form:)
        # if self.parent[x] != x: self.parent[x] = self.find(self.parent[x])
        # return self.parent[x]

    def union(self, a, b):               # merge groups; return True if actually merged
        ra, rb = self.find(a), self.find(b)
        if ra == rb: return False        # already connected → nothing to do
        # UNION BY RANK: attach shorter tree under taller → depth stays tiny
        if self.rank[ra] < self.rank[rb]: ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]: self.rank[ra] += 1
        self.count -= 1
        return True

    def connected(self, a, b):
        return self.find(a) == self.find(b)
```

**Why both optimizations matter:** path compression (flattens on query) + union by rank (keeps trees short) together give amortized α(n) ≈ constant. With only one, it's O(log n) — still fine, but the *pair* is the textbook result and a common explanation question.

**The classic applications:**
```python
# 1) Number of provinces / connected components:
uf = UnionFind(n)
for u, v in edges: uf.union(u, v)
components = uf.count                      # O(n + E·α)

# 2) Redundant connection (find the edge that creates a cycle):
for u, v in edges:
    if not uf.union(u, v): return [u, v]   # first union that FAILS = the extra edge

# 3) Accounts merge, graph validity, friends-of-friends, Kruskal's MST:
#    sort edges by weight, add each if it connects different components
def kruskal(n, edges):                     # Minimum Spanning Tree
    uf, mst, total = UnionFind(n), [], 0
    for w, u, v in sorted(edges):          # greedy: cheapest edge first
        if uf.union(u, v):
            mst.append((u, v, w)); total += w
    return mst, total
    # O(E log E) — sorting dominates. Union-Find makes each check ~O(1).
```

**When Union-Find beats BFS:** repeated connectivity queries (dynamic edges being *added*), incremental grouping, "redundant connection", Kruskal's MST. **When BFS beats Union-Find:** you need the actual path or distances.

## 6.9 Choosing the right graph algorithm (the decision card)

```
Problem says "shortest" + UNWEIGHTED           → BFS
Problem says "shortest" + WEIGHTED (≥0)        → Dijkstra (+ heap)
Problem says "shortest" + negative weights     → Bellman-Ford
Problem says "all pairs shortest"              → Floyd-Warshall O(V³)
Problem says "order / prerequisites / schedule"→ Topological sort (Kahn's)
Problem says "groups / connected / redundant"  → Union-Find
Problem says "is X reachable / explore / fill" → BFS or DFS
Problem says "count paths / enumerate all"     → DFS + backtracking
Problem says "cycle exists?"                   → DFS with colors/parent
Problem says "dependencies"                    → build graph + topo sort
Input is a GRID/BOARD                          → implicit graph, BFS/DFS on cells
Problem is "minimum spanning tree"             → Kruskal (sort + Union-Find)
```

**Framework recap for graph problems:**
1. Explicit or implicit? (edge list / adjacency dict / grid)
2. Directed or undirected? Weighted or not?
3. Which question is being asked? (path? order? groups? count?)
4. → decision card above.
5. State complexity: **almost everything is O(V + E)** — memorize that sentence.

## 6.10 RECAP — Part 6
- Graph = V + E; **adjacency list O(V+E) is the interview default**; matrix only for dense/edge-queries
- **BFS = queue = levels = unweighted shortest path**; **DFS = stack = depth = exhaustive/structural work**
- Mark visited **on enqueue/push** to avoid duplicates; grids are implicit graphs
- **Topo sort (Kahn's):** zero-indegree queue; `len(order) < n` ⟹ cycle
- **Dijkstra:** heap of `(dist, node)` + relaxation + **skip stale pops**; never with negative weights
- **Union-Find:** path compression + union by rank → amortized constant; for *connectivity/grouping*, not paths
- Everything costs **O(V + E)** (Dijkstra O((V+E) log V), Floyd-Warshall O(V³))

---

---

---

# Part 7 — Dynamic Programming & Greedy

## 7.1 WHY DP exists — the fib warning from Part 3, resolved

Remember `fib(n)` calling `fib(n-1)` and `fib(n-2)`? The call tree **recomputed the same subproblems exponentially many times** — `fib(2)` evaluated 3 times for n=5, and the pattern explodes as O(1.618ⁿ).

**Dynamic Programming** is the discipline of fixing exactly that: when a problem has

1. **Overlapping subproblems** — the same smaller problem appears again and again, *and*
2. **Optimal substructure** — the optimal answer is built from optimal answers to smaller pieces,

then **compute each subproblem once and store the answer.** That's it. DP = recursion + a memory table. The exponential becomes linear.

- Recursion answers: *"what's the answer, defined in terms of smaller versions of itself?"*
- Memoization answers: *"have I already computed this smaller version?"*
- DP answers: *"in what order should I compute them so each is ready when needed?"*

Three terms, one idea: **never do the same work twice.**

| Technique | What it is | Direction |
|---|---|---|
| **Naive recursion** | recompute everything | top, exponential |
| **Memoization** | recursion + cache dict | top-down (as needed) |
| **Tabulation** | fill a table bottom-up, loop | bottom-up (iterative) |
| **Space optimization** | keep only the rows the recurrence touches | bottom-up, O(1)–O(k) space |

## 7.2 The evolution, step by step — Climbing Stairs (LC 70)

*You climb 1 or 2 steps at a time. How many distinct ways to reach the top of n stairs?*

```python
# ── STAGE 1: plain recursion (correct, EXPONENTIAL) ──
def climb_naive(n):
    if n <= 2: return n               # base: 1 way for 1 step, 2 ways for 2
    return climb_naive(n - 1) + climb_naive(n - 2)
    # Why: to be at step n, your LAST move was either from n-1 or from n-2.
    #       ways(n) = ways(n-1) + ways(n-2)
    # T(n) = T(n-1) + T(n-2) + O(1) → O(1.618ⁿ) — hopeless beyond ~35

# ── STAGE 2: TOP-DOWN MEMOIZATION (recursion + cache) → O(n) ──
def climb_memo(n, memo=None):
    if memo is None: memo = {}
    if n <= 2: return n
    if n not in memo:                          # ← the entire trick
        memo[n] = climb_memo(n - 1, memo) + climb_memo(n - 2, memo)
    return memo[n]
    # Each n computed AT MOST ONCE → n entries → O(n) time, O(n) space (stack+cache)

# ── STAGE 3: BOTTOM-UP TABULATION (loop, no recursion) → O(n) ──
def climb_tab(n):
    if n <= 2: return n
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2                     # base cases written into the table
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]       # recurrence = the SAME line as recursion
    return dp[n]
    # Builds answers for 3,4,...,n in order — each value ready before it's needed.
    # No call stack → no RecursionError at large n.

# ── STAGE 4: SPACE OPTIMIZATION → O(1) space ──
def climb_opt(n):
    if n <= 2: return n
    prev2, prev1 = 1, 2                     # dp[i-2], dp[i-1]
    for _ in range(3, n + 1):
        prev2, prev1 = prev1, prev1 + prev2 # slide the window of 2 forward
    return prev1
    # dp[i] only depends on dp[i-1], dp[i-2] → only 2 variables needed.
    # ★ The recurrence tells you the space: how many previous slots does
    #   dp[i] read? That's how many you keep. Never guess — read it off.
```

**The pattern across all four:** the **recurrence** (`ways(n) = ways(n-1) + ways(n-2)`) never changes. What changes is only *how you avoid recomputing it*. That's why every DP problem follows the same 5-step recipe:

```
┌─────────────────────────────────────────────────────────────────┐
│  1. DEFINITION:  What does dp[i] (or dp[i][j]) MEAN, in         │
│                  one English sentence? (never "the answer")     │
│  2. BASE CASES:  What values are directly known?                │
│  3. RECURRENCE:  dp[i] = f(smaller dp entries) — the equation  │
│  4. ORDER:       which direction fills so every f() is ready?   │
│  5. ANSWER:      which cell is it? (sometimes dp[n-1],          │
│                  sometimes max over all cells)                 │
└─────────────────────────────────────────────────────────────────┘
```

## 7.3 The DP zoo — 1D patterns with worked problems

### (A) Linear 1D — each state reads a few previous states

```python
# HOUSE ROBBER (LC 198): max loot, can't rob two adjacent houses
# dp[i] = max money considering houses[0..i]
# recurrence: either skip house i (dp[i-1]) or rob it (dp[i-2] + val[i])
def rob(nums):
    incl = excl = 0                        # incl = best ending WITH last house robbed
    for x in nums:
        incl, excl = excl + x, max(excl, incl)
    return max(incl, excl)
    # O(n)/O(1). Pattern signature: "adjacent constraint → two running totals"

# MIN COST CLIMBING STAIRS: cost per step, pay cost[i] to leave step i
def min_cost(cost):
    a, b = 0, 0                            # dp[i-1], dp[i] built right-to-left-ish
    for i in range(len(cost) - 1, -1, -1):
        a, b = b, cost[i] + min(a, b)      # pay cost[i] then cheapest exit
    return b

# DELETION DISTANCE / EDIT DISTANCE → see (C) 2D
```

### (B) Knapsack family — "include this item or not" (the most reusable shape)

```python
# 0/1 KNAPSACK: capacity W, items (weight w[i], value v[i]), each used ONCE
def knapsack(weights, values, W):
    dp = [0] * (W + 1)                     # dp[c] = best value with capacity c
    for i in range(len(weights)):
        w, v = weights[i]
        for c in range(W, w - 1, -1):      # ★ BACKWARD: each item used once
            dp[c] = max(dp[c], dp[c - w] + v)
    return dp[W]
    # Forward iteration would reuse the same item (that's UNBOUNDED knapsack!).
    # Backward vs forward = 0/1 vs unbounded — the single most-tested detail.
    # O(n·W) time, O(W) space. Pseudo-polynomial (W is a VALUE, not a count).

# UNBOUNDED KNAPSACK (coins — unlimited reuse of each coin):
# COIN CHANGE (LC 322): fewest coins summing to amount
def coin_change(coins, amount):
    dp = [0] + [float('inf')] * amount     # dp[a] = min coins for amount a
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], dp[a - c] + 1)   # last coin is c
    return dp[amount] if dp[amount] != float('inf') else -1
    # O(amount × len(coins)). ★ Forward iteration here = reuse allowed = correct.

# PARTITION EQUAL SUBSET SUM (LC 416) — knapsack as yes/no reachability:
def can_partition(nums):
    total = sum(nums)
    if total % 2: return False
    target = total // 2
    reachable = {0}
    for x in nums:
        reachable = reachable | {s + x for s in reachable if s + x <= target}
    return target in reachable             # O(n × total/2) — set-based version
```

### (C) 2D grid DP — state reads neighbors

```python
# UNIQUE PATHS (LC 62): robot top-left → bottom-right, only right/down
def unique_paths(m, n):
    dp = [1] * n                           # first row: 1 way each (only from left)
    for _ in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]             # from above (itself, old) + left (dp[j-1])
    return dp[n - 1]
    # recurrence: dp[r][c] = dp[r-1][c] + dp[r][c-1]  (arrived from top or left)

# MIN PATH SUM (LC 64): same shape, + grid values, min instead of +
def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0]*n for _ in range(m)]
    dp[0][0] = grid[0][0]
    for r in range(m):
        for c in range(n):
            if r == c == 0: continue
            above = dp[r-1][c] if r else float('inf')
            left  = dp[r][c-1] if c else float('inf')
            dp[r][c] = grid[r][c] + min(above, left)
    return dp[-1][-1]

# LONGEST COMMON SUBSEQUENCE (LC 1143) — THE 2D template
def lcs(a, b):
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]   # extra row/col = empty-string bases
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1      # both matched → diagonal + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])   # drop a[i-1] or b[j-1]
    return dp[m][n]
    # EDIT DISTANCE is the same grid with +1 costs instead of max...
    # "Two strings?" → build this i×j grid. Family: LCS, edit distance,
    # distinct subsequences, interleavings, wildcard matching.
```

### (D) Sequences & subarrays

```python
# KADANE'S ALGORITHM (LC 53) — max subarray sum — the elegant O(n)/O(1)
def max_subarray(nums):
    best = cur = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)              # extend, or start fresh at x
        best = max(best, cur)
    return best
    # dp[i] = max subarray ENDING at i = max(nums[i], dp[i-1] + nums[i])
    # ★ "ending at i" framing is what makes Kadane linear — the key DP move

# LONGEST INCREASING SUBSEQUENCE (LC 300) — O(n log n) with patience sorting
import bisect
def length_of_lis(nums):
    tails = []                             # tails[k] = smallest tail of LIS of length k+1
    for x in nums:
        i = bisect.bisect_left(tails, x)   # first tail ≥ x
        if i == len(tails): tails.append(x)
        else: tails[i] = x                 # replace: better (smaller) tail
    return len(tails)
    # O(n log n) vs O(n²) DP. tails isn't the actual LIS (need parent pointers),
    # but its LENGTH is the answer — worth knowing as the optimal version.
```

## 7.4 Greedy algorithms — when local best IS global best

### WHY / WHAT

**Greedy** = at each step, take the locally optimal choice, never reconsider. No tables, no recursion — just a rule and a loop. It's *tempting* because it's simple, and **dangerous** because it's only correct under specific conditions:

> Greedy works iff the problem has **greedy choice property** (a local optimum leads to a global optimum) + **optimal substructure**. There's no mechanical test — you must **prove or find a counterexample**.

**How to know a greedy is safe (heuristics for interviews):**
1. **Exchange argument:** "if an optimal solution differs from my greedy pick, I can swap my pick in without making it worse" — say this out loud; it *is* the proof.
2. The problem asks for **minimum count / maximum sum** with **no interdependencies** between choices.
3. Sorting first makes choices obviously safe (interval scheduling, boat rescue).
4. **Test against DP:** if you can DP it, DP it — DP is always correct; greedy is only sometimes.

### The classic greedy problems (each is a template)

```python
# 1) ACTIVITY / INTERVAL SELECTION: max non-overlapping meetings
def max_activities(intervals):
    intervals.sort(key=lambda x: x[1])      # sort by END time ← the greedy key
    count, last_end = 0, float('-inf')
    for s, e in intervals:
        if s >= last_end:                   # fits after everything chosen so far
            count += 1
            last_end = e
    return count                            # O(n log n) — optimal
    # WHY end-time? Finishing earliest leaves the MOST room for later activities.
    # Proof sketch (exchange): swap any optimal pick with the earliest-ending
    # meeting that starts before it → still valid, never fewer choices remain.

# 2) JUMP GAME (LC 55): can you reach the last index? — track reachable frontier
def can_jump(nums):
    farthest = 0
    for i in range(len(nums)):
        if i > farthest: return False       # stuck before reaching i
        farthest = max(farthest, i + nums[i])
    return True                             # O(n)

# 3) GAS STATION (LC 134): one full circuit possible?
def can_complete_circuit(gas, cost):
    total = start = tank = 0
    for i in range(len(gas)):
        total += gas[i] - cost[i]           # net for whole circuit
        tank += gas[i] - cost[i]
        if tank < 0:                        # can't even reach station i+1
            start, tank = i + 1, 0          # restart AFTER the failure point
    return start if total >= 0 else -1      # O(n); existence proof via total ≥ 0

# 4) ASSIGN COOKIES / BOATS / MINIMUM PLATFORMS — sort both sides, greedy match
def find_content_children(g, s):            # children greed factors, cookie sizes
    g.sort(); s.sort()
    child = cookie = 0
    while child < len(g) and cookie < len(s):
        if s[cookie] >= g[child]: child += 1   # smallest cookie that satisfies
        cookie += 1                             # always advance cookie
    return child                                # O(n log n)

# 5) HUFFMAN-style / priority tasks → heap greedy (Task Scheduler, reorganize string)
```

### Greedy vs DP — the comparison interviewers probe

| | Greedy | Dynamic Programming |
|---|---|---|
| Decision | local best now, **never revisits** | considers all valid choices via subproblems |
| Correctness | **needs proof** (exchange argument) | guaranteed by construction (exhaustive over states) |
| Speed | usually O(n) or O(n log n) (sorting) | often O(n²), O(nW), O(n²) — slower |
| Code | tiny, one loop | table + recurrence |
| Risk | **silently wrong** on off-spec inputs | hard to be wrong if recurrence is right |
| Coin change (1,5,10,25 US coins) | ✅ greedy optimal (canonical system) | also works |
| Coin change (coins = 1,3,4; target 6) | ❌ greedy takes 4+1+1 = 3 coins; **optimal is 3+3 = 2** | ✅ DP gives 2 |
| Interval scheduling (sort by end) | ✅ provably optimal | overkill |
| Knapsack 0/1 | ❌ counterexample exists | ✅ required |
| "Whenever unsure" | state the counterexample | **default to DP** |

**The safe interview script:** "A greedy choice of X seems right because ___. Let me check a counterexample: if input is [___], greedy would pick ___ but optimal is ___. It fails there / it holds. To be safe I'll use DP, which is guaranteed." Showing you *tested* greedy before trusting it scores highly.

## 7.5 Choosing between recursion / greedy / DP / backtracking

```
Problem needs ALL valid options listed          → backtracking (Part 3)
Problem asks count/min/max + repeated subprobs  → DP (5-step recipe)
Problem asks min/max and a provably safe local
  rule exists (sort + pick)                     → greedy (verify first!)
Problem is a search on a structure              → BFS/DFS (Part 6)
Subproblems DON'T overlap (distinct branches)   → plain recursion is fine (divide & conquer)
```

**DP problem type signals:**
- "number of ways to..." → count DP (sum of sub-ways)
- "minimum/maximum cost or effort" → min/max DP
- "longest/shortest subsequence/subarray" → sequence DP
- "can we partition/reach/target sum" → boolean reachability DP
- **two strings / two sequences side by side** → 2D LCS-shaped grid
- constraints n ≤ 1000 → O(n²) DP; n ≤ 100 → O(n³) or 2D; W ≤ 10⁴ → knapsack O(nW)

## 7.6 RECAP — Part 7
- DP = **overlapping subproblems + optimal substructure** → compute each state once
- **Four stages:** naive recursion → memoization → tabulation → space optimization — *the recurrence never changes*
- **5-step recipe:** define `dp[i]` in English → base cases → recurrence → fill order → which cell is the answer
- **0/1 knapsack iterates backward, unbounded iterates forward** — the classic trap
- **Kadane** = "dp[i] = best ending at i" framing; LIS = O(n log n) with bisect on tails
- **Greedy:** needs an exchange-argument proof; test with a counterexample; when in doubt DP wins because it's always correct
- Read space complexity **off the recurrence** (how many previous states are read)

---

---

---

# Part 8 — The Pattern Library

> This is the "tricks" layer. Every interview problem you'll ever see is a **signal** (words in the prompt) → **pattern** (a named technique) → **template** (a skeleton you've practiced). You don't solve problems by genius; you solve them by recognizing which of ~25 patterns you're standing in.

## 8.1 The master decision tree (review before every mock)

```
READ THE PROBLEM → identify the SIGNAL → pick the pattern

"pair / subarray / subsequence / substring" ─┐
"longest / shortest contiguous" ─────────────┼─▶ sliding window / two pointers
"sorted array / O(n) or O(n log n)" ─────────┘
"find target in sorted / min-max of something" ─▶ binary search (or on answer)
"two things move toward each other" ──────────▶ two pointers
"frequency / count / group / seen before" ────▶ hash map / set
"stack of nested / matching / next greater" ──▶ stack / monotonic stack
"top K / running extreme / merge streams" ────▶ heap
"level by level / shortest unweighted path" ──▶ queue (BFS)
"deepest / exhaustive / all combinations" ────▶ DFS / backtracking
"order of tasks / dependencies" ──────────────▶ topological sort
"connected groups / dynamic connectivity" ────▶ Union-Find
"shortest path weighted" ─────────────────────▶ Dijkstra
"number of ways / min cost / repeated work" ─▶ dynamic programming
"prefixes / autocomplete" ────────────────────▶ trie
"arrange / reverse / in-place structure" ─────▶ linked list pointers
"grid / matrix / island" ─────────────────────▶ implicit graph BFS/DFS
"permutations / subsets / puzzles" ───────────▶ backtracking
"most frequent / Kth" ────────────────────────▶ Counter + heap/buckets
"prefix sums / subarray = k" ─────────────────▶ prefix sum + hashmap
"all intervals / merge / cover" ──────────────▶ sort + sweep
```

## 8.2 The pattern catalog

Each pattern: **SIGNAL** (what to notice in the prompt) → **WHY it works** → **TEMPLATE** → **PROBLEMS** (names to practice from the Top 150).

---

### P1 — Counter / Frequency Map
**SIGNAL:** "count occurrences", "most frequent", "anagram", "group words", "first unique", "isomorphic", "subarray sums equal" with word/char data.
**WHY:** a dict turns every "scan the collection again" (O(n)) into O(1); grouping is one pass into `defaultdict(list)`.
```python
freq = Counter(nums)                    # build: O(n)
groups = defaultdict(list)
for x in items: groups[key(x)].append(x)  # group: O(n)
```
**PROBLEMS:** Two Sum, Valid Anagram, Group Anagrams, Top K Frequent, Longest Consecutive, First Unique Character.

---

### P2 — Two Pointers (converging, sorted)
**SIGNAL:** sorted array + pair/target; "return indices"; palindrome checks; "merge in place".
**WHY:** monotonic movement eliminates whole classes of pairs per step; O(n) replaces O(n²).
```python
lo, hi = 0, len(arr) - 1
while lo < hi:
    cur = arr[lo] + arr[hi]
    if cur == target: handle; lo += 1; hi -= 1
    elif cur < target: lo += 1
    else: hi -= 1
```
**PROBLEMS:** Two Sum II, Valid Palindrome, Container With Most Water, Three Sum, Trapping Rain Water.

---

### P3 — Sliding Window (contiguous)
**SIGNAL:** "longest/shortest subarray/substring with property"; at most/at least k; characters covering pattern.
**WHY:** consecutive windows overlap → incremental add/remove keeps state fresh; each element enters/leaves once → O(n).
```python
left = 0; state = init()
for right, x in enumerate(nums):
    add(x)
    while INVALID: remove(nums[left]); left += 1
    record(state)
```
**PROBLEMS:** Longest Substring Without Repeating, Minimum Window Substring, Longest Subarray with Sum ≤ K, Permutation in String, Max Consecutive Ones III.

**Variant — fixed window:** `window += in - out` one line per step.

---

### P4 — Prefix Sum (+ hashmap of counts)
**SIGNAL:** "subarray sums to k"; cumulative sums; "equilibrium"; difference arrays.
**WHY:** `prefix[j] - prefix[i]` gives any subarray sum in O(1); storing seen prefixes converts "find i<j with sum k" into one hashmap lookup.
```python
prefix, count = 0, {0: 1}
for x in nums:
    prefix += x
    count += prefix.get(prefix - k, 0)   # subarrays ENDING here with sum k
```
**PROBLEMS:** Subarray Sum Equals K, Continuous Subarray Sum, Find Pivot Index, Maximum Subarray (Kadane as prefix thinking).

---

### P5 — Binary Search (on sorted array)
**SIGNAL:** "sorted", O(log n) requested, "first/last occurrence", search space halving.
**WHY:** invariant — answer stays in [lo, hi] while halving.
```python
lo, hi = 0, len(arr) - 1
while lo <= hi:
    mid = lo + (hi - lo) // 2
    if check(mid): ...   # see Part 4 for all 4 shapes
```
**PROBLEMS:** Binary Search, Search in Rotated Sorted Array, Find First and Last Position, Search 2D Matrix, Koko Eating Bananas, Median of Two Sorted Arrays.

---

### P6 — Binary Search on the Answer
**SIGNAL:** "minimum/maximum X such that condition holds"; speed/capacity/days/distance problems; feasibility language ("can it be done within...").
**WHY:** feasibility is monotonic — if x works, x+1 works → the boundary is findable by halving the *value* range.
```python
def feasible(x) -> bool: ...   # greedy/check in O(n)
lo, hi = min_possible, max_possible
while lo < hi:
    mid = (lo + hi) // 2
    if feasible(mid): hi = mid
    else: lo = mid + 1
return lo
```
**PROBLEMS:** Koko Eating Bananas, Capacity to Ship Packages, Split Array Largest Sum, Minimized Max of Divided, Magnetic Force Between Balls.

---

### P7 — Monotonic Stack (next greater / spans)
**SIGNAL:** "next greater element", "daily temperatures", "stock span", "largest rectangle in histogram", bracket nesting with positions, "walls/histogram".
**WHY:** a stack keeping values in decreasing order answers "what's the first bigger thing to my right/left" the moment a violation pops — every element pushed/popped once → O(n).
```python
stack = []                      # indices, values decreasing
for i in range(n):
    while stack and nums[stack[-1]] < nums[i]:
        idx = stack.pop()                  # nums[i] is the NEXT GREATER of idx
        answer[idx] = i - idx              # span / distance
    stack.append(i)
# leftover stack elements → no greater element to the right (answer 0 / -1)
```
**PROBLEMS:** Next Greater Element I/II, Daily Temperatures, Stock Span, Largest Rectangle in Histogram, Trapping Rain Water (two-stack/pointer cousin).

---

### P8 — Stack for parsing / undo
**SIGNAL:** nested structures, "valid parentheses", expression evaluation, "decode string", RLE, path simplification.
**WHY:** nesting is inherently LIFO — the most recent unmatched opener must be checked first.
```python
stack = []
for token in tokens:
    if is_opener(token): stack.append(token)
    elif is_closer(token):
        if stack and matches(stack[-1], token): stack.pop()
        else: return invalid
return not stack
```
**PROBLEMS:** Valid Parentheses, Decode String, Basic Calculator II, Simplify Path, Remove K Digits (stack + greedy).

---

### P9 — Heap / Top-K
**SIGNAL:** "Kth largest/smallest", "top K frequent", "merge K lists", "closest points", "median from stream", scheduling by priority.
**WHY:** heap maintains extremes in O(log n) without full sorting; size-k heap is O(n log k) and stream-safe.
```python
h = []
for x in stream:
    heapq.heappush(h, x)
    if len(h) > k: heapq.heappop(h)        # keep best k only
# h[0] = kth best (smallest among the k largest)
```
**PROBLEMS:** Kth Largest Element, Top K Frequent Elements, Merge K Sorted Lists, K Closest Points, Find Median from Data Stream, Task Scheduler.

---

### P10 — BFS on unweighted graph/grid
**SIGNAL:** "shortest path" + no weights / unit steps; "level order"; "nearest"; "is it reachable"; "rotting oranges" (time/levels).
**WHY:** FIFO explores strictly by distance-from-source; first reach = fewest edges.
```python
q = deque([start]); visited = {start}; level = 0
while q:
    for _ in range(len(q)):          # freeze width = one level
        u = q.popleft()
        if target(u): return level
        for v in neighbors(u):
            if v not in visited: visited.add(v); q.append(v)
    level += 1
```
**PROBLEMS:** Number of Islands, Rotting Oranges, Word Ladder, 01 Matrix, Open the Lock, Level Order Traversal, Course Schedule (via topo).

---

### P11 — DFS / backtracking (exhaustive)
**SIGNAL:** "all subsets/permutations/combinations", "restore/arrange", N-Queens, Sudoku, path enumeration, word search.
**WHY:** explores the full decision tree with clean undo; pruning cuts dead branches.
```python
def dfs(state, start):
    if GOAL(state): record(state[:]); return
    for choice in options(state, start):
        if not promising(choice): continue
        make(choice, state); dfs(state, ...); undo(choice, state)
```
**PROBLEMS:** Subsets, Permutations, Combination Sum I/II, N-Queens, Word Search, Palindrome Partitioning, Letter Combinations.

---

### P12 — Grid DFS (flood fill / islands)
**SIGNAL:** "number of islands", "fill region", "connected cells", "max area of island", "surrounded regions".
**WHY:** grids are implicit graphs; DFS marks the whole component in one recursion → O(rows·cols).
```python
def sink(r, c):
    if out_of_bounds(r, c) or grid[r][c] != LAND: return
    grid[r][c] = VISITED               # mark NOW
    for dr, dc in dirs: sink(r+dr, c+dc)
```
**PROBLEMS:** Number of Islands, Max Area of Island, Surrounded Regions, Flood Fill, Friends of Appropriate Ages (grid cousin), Pacific Atlantic Water Flow.

---

### P13 — Topological Sort
**SIGNAL:** "prerequisites", "order tasks", "dependency", "course schedule", "alien dictionary".
**WHY:** Kahn's zero-indegree queue emits tasks only when all deps are done; leftover nodes = cycle.
```python
indeg = [...]; q = deque(zero-indeg nodes); order = []
while q:
    u = q.popleft(); order.append(u)
    for v in g[u]:
        indeg[v] -= 1
        if indeg[v] == 0: q.append(v)
return order if len(order) == n else []     # [] = cycle → impossible
```
**PROBLEMS:** Course Schedule I/II, Alien Dictionary, Sequence Reconstruction, Parallel Courses.

---

### P14 — Union-Find
**SIGNAL:** "number of connected components", "redundant connection", "are they connected", "merge accounts", dynamic edge additions, Kruskal's MST.
**WHY:** union/find amortized ~constant; avoids rerunning BFS per query.
```python
uf = UnionFind(n)
for a, b in edges:
    uf.union(a, b)
    # first failed union = redundant edge; uf.count = components
```
**PROBLEMS:** Number of Provinces, Redundant Connection, Accounts Merge, Graph Valid Tree, Similar String Groups.

---

### P15 — Dijkstra (weighted shortest)
**SIGNAL:** "shortest path" + weights (cost, time, probability); "cheapest route with k stops" (variant: bounded hops → BFS-like layers).
**WHY:** greedy finalize-closest-node + relaxation gives correct distances for non-negative weights.
```python
dist = {start: 0}; h = [(0, start)]
while h:
    d, u = heappop(h)
    if d > dist[u]: continue                # stale skip
    for v, w in g[u]:
        if d + w < dist[v]:
            dist[v] = d + w; heappush(h, (d + w, v))
```
**PROBLEMS:** Network Delay Time, Cheapest Flights Within K Stops, Path With Minimum Effort, Swim in Rising Water.

---

### P16 — Kadane (max subarray)
**SIGNAL:** "maximum sum subarray/contiguous"; circular variant flagged.
**WHY:** dp[i] = best ending at i → extend or restart; O(n)/O(1).
```python
cur = best = nums[0]
for x in nums[1:]:
    cur = max(x, cur + x); best = max(best, cur)
```
**PROBLEMS:** Maximum Subarray, Maximum Sum Circular Subarray, Best Time to Buy/Sell Stock (same skeleton with min-so-far).

---

### P17 — Linear DP (climb/rob/house)
**SIGNAL:** "ways to climb", "rob houses with adjacency rule", "decode ways", steps with 1/2 costs.
**WHY:** dp[i] reads a constant-size window of previous states.
```python
dp = base_cases
for i in range(k, n + 1):
    dp[i] = combine(dp[i-1], dp[i-2], ...)   # read recurrence off the story
```
**PROBLEMS:** Climbing Stairs, House Robber I/II, Decode Ways, Min Cost Climbing Stairs, Delete and Earn.

---

### P18 — Knapsack / subset-sum DP
**SIGNAL:** "partition into two equal sums", "target sum with +/-", "coin change", "capacity/value" language.
**WHY:** boolean/value reachability table over (item, capacity); backward iteration for 0/1.
```python
dp = [False] * (target + 1); dp[0] = True
for x in nums:                          # 0/1: iterate BACKWARD
    for s in range(target, x - 1, -1):
        dp[s] = dp[s] or dp[s - x]
```
**PROBLEMS:** Partition Equal Subset Sum, Target Sum, Coin Change, Combination Sum IV, Last Stone Weight II.

---

### P19 — 2D sequence DP (LCS / edit distance)
**SIGNAL:** **two strings/arrays side by side**; "longest common...", "delete/insert/replace to transform", "distinct subsequences".
**WHY:** dp[i][j] = best answer for prefixes a[:i], b[:j]; match → diagonal+1, else max of drop-left/drop-right.
```python
dp = [[0]*(n+1) for _ in range(m+1)]
for i in range(1, m+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i-1][j-1]+1 if a[i-1]==b[j-1] else max(dp[i-1][j], dp[i][j-1])
```
**PROBLEMS:** Longest Common Subsequence, Edit Distance, Distinct Subsequences, Longest Palindromic Subsequence, Interleaving String.

---

### P20 — Grid DP
**SIGNAL:** "paths in a grid", "min cost path", "triangle", "unique paths with obstacles/dungeon".
**WHY:** cell state depends only on top/left (or neighbors) → bottom-up fill.
```python
dp[0][0] = base
for r in range(m):
    for c in range(n):
        dp[r][c] = cost + min(dp[r-1][c], dp[r][c-1])
```
**PROBLEMS:** Unique Paths I/II, Minimum Path Sum, Triangle, Dungeon Game, Maximal Square.

---

### P21 — Greedy with sorting
**SIGNAL:** "maximum number of activities/meetings/boats"; "minimum platforms"; "assign cookies"; interval covering.
**WHY:** sorting by the right key (usually end time) makes local choices provably safe — state the exchange argument.
```python
items.sort(key=lambda x: x[1])   # sort by END
chosen_end = -inf
for item in items:
    if item.start >= chosen_end:
        take(item); chosen_end = item.end
```
**PROBLEMS:** Non-overlapping Intervals, Minimum Number of Arrows, Meeting Rooms II, Assign Cookies, Gas Station, Jump Game I/II.

---

### P22 — Intervals: merge / sweep line
**SIGNAL:** "merge overlapping", "insert interval", "cover all points", "minimum number of rooms" (overlap counting).
**WHY:** sort by start; one pass merges (or a ±1 event counter sweeps all boundaries).
```python
# merge:
intervals.sort(key=lambda x: x[0])
out = [intervals[0]]
for s, e in intervals[1:]:
    if s <= out[-1][1]: out[-1][1] = max(out[-1][1], e)
    else: out.append([s, e])
# count max overlap (rooms):
events = sorted([(s,1) for s,e in iv] + [(e,-1) for s,e in iv])
# running sum of +1/-1 → peak = answer
```
**PROBLEMS:** Merge Intervals, Insert Interval, Meeting Rooms II, Interval List Intersections, Minimum Interval to Include Each Query.

---

### P23 — Trie (prefix-heavy dictionary problems)
**SIGNAL:** dictionary given + asks about prefixes/autocomplete/word board searches/replace words with shortest prefix.
**WHY:** character-by-character paths share prefixes; search cost = query length only.
```python
node = root
for ch in word:
    node = node.children.setdefault(ch, TrieNode())
node.is_end = True
```
**PROBLEMS:** Implement Trie, Word Search II, Replace Words, Design Add and Search Words, Maximum XOR of Two Numbers (binary trie variant).

---

### P24 — Two pointers on linked lists (slow/fast)
**SIGNAL:** linked list + "middle", "cycle", "reverse", "reorder", "remove nth from end".
**WHY:** without random access, index math becomes pointer races; O(n)/O(1) everywhere.
```python
slow = fast = head
while fast and fast.next:
    slow = slow.next; fast = fast.next.next
# slow = middle / cycle meeting point
```
**PROBLEMS:** Linked List Cycle, Middle of the List, Reorder List, Remove Nth Node, Reverse Linked List, Merge Two Sorted Lists, Palindrome Linked List.

---

### P25 — Bit manipulation
**SIGNAL:** "single number among pairs", "power of two", counting bits, XOR language, subset-by-bits.
**WHY:** XOR cancels pairs (`a^a=0`), `x & (x-1)` clears lowest set bit — O(1) tricks no loop can match.
```python
x ^ x = 0 ; x ^ 0 = x          # dedupe pairs
x & (x - 1)                    # remove lowest 1-bit (count bits / power-of-2 test)
1 << n                         # 2^n ; (x >> k) & 1 = k-th bit
# single number: reduce(nums, xor)
```
**PROBLEMS:** Single Number, Number of 1 Bits, Power of Two, Missing Number, Sum of Two Integers, Counting Bits, Subsets (bitmask enumeration).

---

### P26 — Simulation / design (structures combined)
**SIGNAL:** "design a data structure with X operations", LRU, iterator, matrix rotation, string compression, calendar booking.
**WHY:** interviews test whether you can *compose* known structures to meet stated operation costs.
```python
# e.g. LRU = dict + OrderedDict ; min-stack = two stacks or (value, min) stack pairs
# rolling buffer = deque(maxlen=k) ; schedule = heap + dict
```
**PROBLEMS:** LRU Cache, Min Stack, Moving Average, Logger Rate Limiter, Design Parking System, Insert Delete GetRandom O(1).

---

## 8.3 The "what structure should I pick?" table (Part 0's tree, now with practice)

| If the problem needs... | Use | Complexity you get |
|---|---|---|
| O(1) lookup / dedup / counts | `dict` / `set` | avg O(1) |
| Ordered data + O(log n) search | sort + `bisect` | O(log n) |
| Top-K / extremes from stream | `heapq` | O(log n)/op |
| Fair ordering / BFS | `deque` as queue | O(1)/op |
| Nesting / next-greater / spans | `list` as stack | O(1)/op |
| Prefix matching | trie | O(L) |
| Grouping / connectivity | Union-Find | ~O(1)/op |
| All combinations | backtracking | O(output) |
| Repeated subproblems | DP table | O(#states × #choices) |
| Shortest unweighted path | BFS | O(V+E) |

## 8.4 The pattern-trigger phrase list (memorize these trigger words)

| Problem words | Your immediate response |
|---|---|
| "longest substring where..." | sliding window |
| "sorted array, find pair/insert" | two pointers / bisect |
| "minimum X such that feasible" | binary search on answer |
| "next greater / nested / span" | monotonic stack |
| "Kth / top K / median stream" | heap |
| "shortest path, unweighted" | BFS |
| "prerequisites / order" | topological sort |
| "groups / components / redundant" | Union-Find |
| "number of ways / min cost" | DP (write the 5-step recipe) |
| "all subsets / permutations" | backtracking |
| "island / fill / grid path" | grid DFS/BFS |
| "count / most / group by" | Counter |
| "subarray sum equals k" | prefix sum + hashmap |
| "common between two strings" | 2D LCS-shaped DP |
| "single number / bit" | XOR tricks |

## 8.5 RECAP — Part 8
- You don't solve by inspiration — you solve by **signal → pattern → template**
- **25 patterns**, each with a signal phrase, a one-why, and a skeleton you should be able to write in 90 seconds
- Review the decision tree (§8.1) and trigger phrases (§8.4) before every mock interview — they compress the whole document into one page

---

---

---

# Part 9 — Interviews & the Top 150

## 9.1 The interview, decoded

### What happens in a 45-minute live round (minute by minute)

```
00:00–05:00   Problem read + your clarifying questions
              (they're watching: do you ask about constraints, edge cases, scale?)
05:00–10:00   Brute force stated WITH complexity → bottleneck named → proposed approach
              (this is 40% of your score; do it BEFORE touching the keyboard)
10:00–12:00   Dry run of the approach on a small example
              (candidates who skip this get lost in code 5 minutes later)
12:00–30:00   Coding. Narrate intent, not keystrokes.
              "Now I'm building the frequency map..." not "f-o-r space..."
30:00–36:00   Test: empty, single, duplicates, max size. Fix bugs yourself.
36:00–42:00   Complexity statement + follow-ups ("what if input is a stream?",
              "can you do it in O(1) space?", "what if it's a graph?")
42:00–45:00   Wrap: recap the final approach in 3 sentences.
```

**Common failure modes (ranked by how often they kill candidates):**
1. **Coding in silence** — interviewer disengages, has no idea what to score.
2. **Jumping to code before an approach** — no brute force, no complexity. Even if the code works, "no demonstrated reasoning" = lean no-hire.
3. **Off-by-one / not testing** — you wrote it, they ask "does it work on `[]`?", you stare. Test *yourself first*.
4. **Freezing on a wrong start** — you picked sliding window, it's wrong, and you keep defending it. **Verbally abandon and pivot:** "this doesn't handle negatives — I'll switch to prefix sums." Interviewers *reward* course correction; they punish stubborn silence.
5. **No complexity at the end** — free points left on the table.

### What is actually scored (the rubric, simplified)

| Dimension | Weight | What "good" looks like |
|---|---|---|
| Problem understanding | high | restates, asks about constraints/edge cases unprompted |
| Approach reasoning | **highest** | brute force → bottleneck → optimal → dry run |
| Code quality | high | clear names, handles None/empty, no dead code |
| Testing | high | finds own bug before interviewer does |
| Complexity analysis | medium | states time & space unprompted at the end |
| Communication | continuous | thinks aloud, responds to hints as collaboration |
| Follow-ups | bonus | handles the "now make it O(1) space" extension |

### The spoken script (memorize this — it structures every round)

```
1. "Let me make sure I understand — I can restate it as ___."
2. "Questions: can the input be empty? Duplicates? What's the typical size of n?"
3. "The brute force is ___, which is O(___). For n = ___ that's too slow."
4. "The bottleneck is ___. My idea is to use ___ because ___. That makes it O(___)."
5. "Let me trace it on a small example first — take [___]. ... looks right."
6. [Code while narrating.]
7. "Let's test: empty input → ___; single element → ___; all duplicates → ___."
8. "Time is O(___), space is O(___). Follow-up: if this were a stream, I'd ___."
```

### Talking while coding — the technique

- **Signposting:** say the *goal* of each block before writing it ("I'll build a prefix sum array first").
- **Silence audit:** if you notice yourself quiet > 45 seconds, say what you're checking.
- **Got stuck?** Say the state: "I'm losing track of the window invariant — let me re-derive it: the window must always be valid, so the while-loop shrinks until..." Narrating recovery *is* the signal they want.
- **Bugs found by them = points lost; bugs found by you = points kept.** Read your own code bottom-up once before declaring done.

## 9.2 How to practice — the protocol that builds skill without assistants

### Per-problem protocol (the "no hints" promise, operationalized)

```
TIMED ATTEMPT (no AI, no peeking — this is the training rep)
├─ 0–2 min:   restate, constraints, edge cases on paper
├─ 2–5 min:   brute force + its complexity, say it out loud
├─ 5–20 min:  struggle for the optimization. Trace examples on paper.
│              Stuck? Ask yourself ONE question: "what does my bottleneck need?"
│              (→ Part 8 decision tree) — then keep trying.
├─ 20 min:    still stuck → read ONLY the pattern name in Part 8 (the SIGNAL line).
│              Close it. Keep trying with that hint.
├─ 30 min:    still stuck → read the approach sketch in the Top 150 list below
│              (still no code). Implement YOURSELF from the sketch.
└─ only after your code passes: compare with editorial/AI output as peer review.

AFTER (same day, 10 minutes)
├─ Write down: pattern name, signal phrase, why brute force failed
└─ Log it: problem #, attempts, time, verdict (seen again in 3 days)

REPRODUCTION (the step 90% of self-learners skip)
├─ 2–3 days later: solve again from BLANK FILE. No peeking.
└─ Can't? It never counted. Reset it in the log. Repeat until clean.
```

**Why reproduction matters (the science, one paragraph):** re-reading a solution produces *familiarity* — the feeling of "I know this" that evaporates under pressure. Re-deriving from nothing produces *retrieval strength* — the actual ability to pull the method out of your head when the timer runs. Every study of skill acquisition says the same thing: **the practice that feels hardest (retrieval, blank-page, spaced gaps) is the one that transfers.** The protocol above is engineered around that: struggle → spaced re-encounter → blank reproduction.

### How to schedule without a schedule (the rewind-friendly method)

No 30-day trap. Use **problem-type rotation + the re-encounter rule**:

```
Day session A:  3 new problems from ONE pattern (same pattern ×3 = you feel the shape)
Day session B:  1 old problem (blank reproduction) + 3 new from the NEXT pattern
Before bed / next open: skim the recap box of the last section you read

Weekly:  one timed 90-minute mock (2 problems: 1 easy+1 medium or 2 medium)
         from a random position in the Top 150 — pick by rolling a group number.
```

**Progression signals** (move on when true, not when bored):
- Easy: < 10 minutes, correct, complexity stated.
- Medium: < 25 minutes, correct with at most one bug you self-fixed.
- Hard: < 40 minutes *or* correct approach identified even if coding runs long.

### Revision modes — three ways to use this file

| Mode | When | What to open |
|---|---|---|
| **Learn** | first time through | full chapters, run all code |
| **Drill** | weekly | Part 8 pattern catalog + your logged weak spots |
| **Rewind** | night before interview | §9.5 checklist, then any chapter whose recap feels fuzzy |
| **Fresh pattern** | hit an unknown problem type | §8.1 decision tree first — it usually names the right chapter |

## 9.3 The AI-era mock loop (using AI without hollowing out your skill)

Allowed uses in *practice* (after the timed attempt, never during):
- **Verification:** "Here's my solution and my claimed O(n). Find the case where it breaks." (Judge, not author.)
- **Variation generator:** "Give me 3 variants of this problem with different constraints" — after you solved the original, variants build generalization.
- **Explain-after:** "Explain why this solution is O(n log n)" — comprehension check on code you already understand structurally.
- **Interviewer simulator:** paste a problem prompt only (no solutions available to you) and have AI ask *you* clarifying questions while you code aloud.

Forbidden: pasting the problem before your 20-minute attempt; accepting code you didn't derive; marking a problem "done" from reading.

## 9.4 Timed mock scoring sheet (self-administered)

```
PROBLEM: ______  GROUP: ______  START: ______  TIME LIMIT: 45 min

[ ] Restated + asked ≥1 constraint question            /5
[ ] Brute force + complexity stated                    /5
[ ] Bottleneck named → correct pattern chosen          /5
[ ] Dry run before coding                              /5
[ ] Code correct on first run                          /10
[ ] Edge cases tested by YOU (empty/single/dup/max)    /5
[ ] Time & space complexity stated unprompted          /5
[ ] Communicated through difficulty without silence    /5
                                                       ───
                                        TOTAL          /45

Score ≥ 36: interview-ready on this pattern. 28–35: drill again.
< 28: re-read the chapter's RECAP, redo the problem blank tomorrow.
```

---

---

## 9.5 The Top 150 Interview LeetCode (2026–2028)

**Curated for the AI era.** Selection logic: (1) frequency at product/Big-Tech companies, (2) each problem teaches a *transferable pattern* rather than a trivia trick, (3) coverage — every pattern in Part 8 has representatives, (4) ordered easy → hard within each pattern group so you climb the same ladder the interview does.

**How to use each row (read this once):**
- **Signal** = the phrase in the prompt that should trigger the pattern.
- **Approach sketch** = *brute force → optimal direction in words.* No code. You write the code — that's the whole point.
- **Why** = what makes it worth your finite hours.
- Difficulty: **E**asy / **M**edium / **H**ard.
- **Rules:** one attempt per problem following §9.2 before looking at anything else. Log results. Reproduce blank in 2–3 days.

---

### Group 1 — Arrays & Hashing (13) · *start here; the foundation of everything*

| # | LeetCode | Lvl | Signal | Approach sketch (brute → optimal) | Why it's on the list |
|---|---|---|---|---|---|
| 1 | 1. Two Sum | E | "indices of two numbers that add up" | check all pairs O(n²) → one pass: store `val→index` in a dict, look up `target−x` | The single most-quoted interview question; teaches complement lookup |
| 2 | 217. Contains Duplicate | E | "any value appears twice" | nested compare O(n²) → `set` size vs list size | Fastest way to feel O(n) vs O(n²) |
| 3 | 242. Valid Anagram | E | "same characters, different order" | sort both O(n log n) → `Counter` decrement O(n) | Frequency-map fundamentals |
| 4 | 49. Group Anagrams | M | "group words that are rearrangements" | all-pairs anagram check O(n·m) → group by sorted-word / char-count key into `defaultdict(list)` | The canonical "key = canonical form" grouping move |
| 5 | 128. Longest Consecutive Sequence | M | "longest run of consecutive ints, O(n)" | sort O(n log n) → set + only start chains at numbers with no predecessor | Set-based cleverness; tests true O(n) thinking |
| 6 | 238. Product of Array Except Self | M | "products without division, no /" | prefix×suffix arrays O(n)/O(n) → single pass with running prefix, output array as suffix storage | Interviewers' favorite "no division" constraint; prefix products |
| 7 | 347. Top K Frequent Elements | M | "K most frequent" | sort by count O(n log n) → `Counter` + size-k min-heap O(n log k); mention bucket-sort O(n) | Heap combo + counting in one; follow-up magnet |
| 8 | 169. Majority Element | E | "appears > n/2 times" | Counter O(n)/O(n) → **Boyer-Moore** cancel-pair voting O(1) space | Elegant algorithm that only works with a proof — pattern jewel |
| 9 | 560. Subarray Sum Equals K | M | "count subarrays with sum exactly k" | all subarrays + resum O(n²) → running prefix + hashmap of prefix counts | Prefix-sum+hash is a top-5 modern signal; hard variant of two-sum thinking |
| 10 | 41. First Missing Positive | H | "smallest positive integer, O(n)/O(1)" | sort / set O(n log n) → cyclic sort: put each value at its index `nums[i]−i`, then scan for mismatch | Hard-looking but pure index-placement logic — great "aha" |
| 11 | 287. Find the Duplicate Number | M | "one repeated number, no modify, O(1) space" | sort / set → treat `nums[i]` as a `next` pointer → **Floyd cycle detection** (Part 2's trick!) | Cross-structure insight: array as linked list |
| 12 | 448. Find All Numbers Disappeared | E | "numbers missing from 1..n in place" | set difference → negate-mark `nums[abs(x)−1]`, then report unmarked | In-place marking technique reused in several mediums |
| 13 | 121. Best Time to Buy and Sell Stock | E | "best single buy-then-sell" | all pairs O(n²) → track min-so-far, max profit at each sale point | Kadane's skeleton disguised as finance — pattern #16 |

---

### Group 2 — Two Pointers (9)

| # | LeetCode | Lvl | Signal | Approach sketch (brute → optimal) | Why it's on the list |
|---|---|---|---|---|---|
| 14 | 125. Valid Palindrome | E | "palindrome ignoring non-alnum" | build cleaned copy → two pointers from both ends, skip junk in place | Warm-up for pointer discipline |
| 15 | 167. Two Sum II (sorted array) | M | "sorted array, indices of pair = target" | all pairs → `lo/hi` converge; move whichever side's sum is wrong | Textbook converging pointers |
| 16 | 15. 3Sum | M | "triplets summing to zero, no dup triplets" | triple loop O(n³) → sort + fix `i` + two pointers, skip duplicates at all 3 positions | The most-cited "sort enables pointers" problem |
| 17 | 11. Container With Most Water | M | "max area between vertical lines" | all pairs → ends inward, always move the **shorter** line (argue why) | Exchange-argument reasoning without knowing it's called that |
| 18 | 42. Trapping Rain Water | H | "how much water is trapped" | brute: per-index max-left/max-right O(n²) → two pointers tracking L/R max in O(1) | Two-pointer mastery badge; also has stack + DP solutions to compare |
| 19 | 88. Merge Sorted Arrays | E | "merge in place, nums1 has room" | append+sort → pointers from the **ends** (fill backward, no overwrite) | Direction awareness — the simplest pointer insight |
| 20 | 26. Remove Duplicates from Sorted Array | E | "in-place, return new length" | extra array → slow-writer/fast-reader pattern | The in-place write-pointer template used by dozens of problems |
| 21 | 75. Sort Colors | M | "sort 0/1/2 in place, one pass" | sort → **Dutch national flag**: three pointers (lo/mid/hi) swapping by value | One-pass 3-way partition — also the quicksort partition idea |
| 22 | 443. String Compression | M | "run-length encode in place" | build new string → read/write pointers over the char array | Pointer writes into a shared buffer; interviewers love the in-place constraint |

---

### Group 3 — Sliding Window (8)

| # | LeetCode | Lvl | Signal | Approach sketch (brute → optimal) | Why it's on the list |
|---|---|---|---|---|---|
| 23 | 3. Longest Substring Without Repeating Characters | M | "longest substring, all unique" | all substrings O(n²) → window + last-seen-index map, jump `left` past repeats | The variable-window gateway problem |
| 24 | 209. Minimum Size Subarray Sum | M | "shortest subarray with sum ≥ target" | all subarrays O(n²) → grow sum, shrink while valid, track min length | Minimal version of the shrink template |
| 25 | 567. Permutation in String | M | "some anagram of s1 appears in s2" | all substrings + sort each → fixed-size window with a `Counter` diff count | Fixed window + match counter — reusable for "permutation in" family |
| 26 | 424. Longest Repeating Character Replacement | M | "longest substring of ≤ k replacements" | all windows → window keeps char counts; valid while `window_len − max_count ≤ k` | The counterintuitive invariant (shrink on violation of a derived condition) |
| 27 | 1004. Max Consecutive Ones III | M | "longest run of 1s allowing k zeros" | all windows → zeros-count in window, `while zeros > k: left++` | Cleanest statement of the add/shrink loop |
| 28 | 904. Fruit Into Baskets | M | "longest subarray with ≤ 2 types" | all windows → at-most-K-distinct window with `k=2` | Teaches the **"at most K" ↔ "exactly K"** transform family |
| 29 | 76. Minimum Window Substring | H | "smallest window containing all chars of pattern" | all windows + validity scan O(n²·m) → window + required-counter with a **satisfied counter** | The hardest standard window; interviews ask it for real |
| 30 | 239. Sliding Window Maximum | H | "max of every size-k window" | rescan each window O(nk) → **monotonic decreasing deque** of indices | Bridges window + stack: the deque trick worth knowing cold |

---

### Group 4 — Binary Search (7)

| # | LeetCode | Lvl | Signal | Approach sketch (brute → optimal) | Why it's on the list |
|---|---|---|---|---|---|
| 31 | 704. Binary Search | E | "sorted array, find target" | linear scan → classic `lo/hi/mid` halving | The skeleton everything else builds on |
| 32 | 34. Find First and Last Position | M | "first/last occurrence of target" | find-any-index then expand → two **bound** searches (lower/upper bound) | Tests whether you know bounds vs exact-match |
| 33 | 74. Search a 2D Matrix | M | "rows sorted, each row > last" | nested scan → treat matrix as virtual sorted array, index mapping; or row-bisect then col-bisect | "Where is the sortedness?" — abstraction practice |
| 34 | 33. Search in Rotated Sorted Array | M | "sorted, but rotated, O(log n)" | linear scan → find pivot + search half; or unified predicate on which side is sorted | Top follow-up after basic binary search |
| 35 | 153. Find Minimum in Rotated Sorted Array | M | "rotated sorted, find min O(log n)" | linear min → compare `mid` vs `hi` to know which half holds the min | Pivot logic distilled to one comparison |
| 36 | 875. Koko Eating Bananas | M | "minimum speed to finish within h hours" | try speeds 1..max O(n·max) → **binary search on the answer** with feasibility check | The gateway to search-on-answer; signal: "min X such that feasible" |
| 37 | 4. Median of Two Sorted Arrays | H | "O(log(m+n)), median of two sorted" | merge to one sorted list O(m+n) → partition at midpoints, binary search the **smaller** array for correct cut | Hardest standard binary search — only after #31–36 are fluent |

---

### Group 5 — Stack & Monotonic Stack (9)

| # | LeetCode | Lvl | Signal | Approach sketch (brute → optimal) | Why it's on the list |
|---|---|---|---|---|---|
| 38 | 20. Valid Parentheses | E | "check bracket matching" | counter fails on `([)]` → stack of openers, pop on match | Stack's raison d'être |
| 39 | 232. Implement Queue using Stacks | E | "implement FIFO with LIFO only" | two stacks; pop flips once when needed → **amortized O(1)** | Amortized reasoning in tiny form |
| 40 | 946. Validate Stack Sequences | M | "could this push/pop order happen?" | simulate blindly → track push index, popping whenever top matches | Stack-as-process simulation; small but clever |
| 41 | 150. Evaluate Reverse Polish Notation | M | "postfix expression" | parse with parser → stack: number push, operator pops two | Expression evaluation core |
| 42 | 394. Decode String | M | `"2[a3[b]]" expand` | naive recursion → stack of (string, repeat) or two parallel stacks | Nested-repetition decoding — stack of contexts |
| 43 | 155. Min Stack | M | "get min in O(1)" | scan for min O(n) → aux stack of (val, min-so-far) or store delta | First "design a structure" classic |
| 44 | 739. Daily Temperatures | M | "days until warmer" | for each day scan forward O(n²) → **monotonic decreasing stack** of indices | Monotonic stack gateway problem |
| 45 | 1249. Minimum Remove to Make Valid Parentheses | M | "delete min brackets to fix" | rebuild with counter tricks → stack of indices to delete + pass over string | Stack of positions (not values) — variant awareness |
| 46 | 84. Largest Rectangle in Histogram | H | "largest rectangle under bars" | for each bar expand left/right O(n²) → **monotonic stack** of indices; each bar's width = span to next smaller | The hardest standard stack problem; same trick powers 85. Maximal Rectangle |

---

### Group 6 — Linked List (9)

| # | LeetCode | Lvl | Signal | Approach sketch (brute → optimal) | Why it's on the list |
|---|---|---|---|---|---|
| 47 | 206. Reverse Linked List | E | "reverse the list" | copy values into array → 3-pointer walk (`prev/cur/nxt`) in place | The single most-asked linked-list problem; do it recursive too |
| 48 | 21. Merge Two Sorted Lists | E | "merge two sorted lists" | append all + sort → two-pointer walk attaching smaller node; `dummy` head | Dummy-node technique gateway |
| 49 | 876. Middle of the Linked List | E | "second middle if even" | count + index → **slow/fast** race | Slow/fast foundation for #51 |
| 50 | 141. Linked List Cycle | E | "does it contain a cycle" | hash set of visited nodes O(n)/O(n) → **tortoise & hare** O(1) space | Floyd's algorithm — cycle detection without memory |
| 51 | 142. Linked List Cycle II | M | "WHERE does the cycle start" | same set trick → reset one pointer to head, walk both at 1 → they meet at entry | The beautiful proof-question; explain the *why* out loud |
| 52 | 19. Remove Nth Node From End | M | "remove nth from the end, one pass" | two passes (count then remove) → fast pointer n ahead, then both walk | One-pass distance-maintenance trick |
| 53 | 143. Reorder List | M | "L0→Ln→L1→Ln−1..." | reverse values in array → split at middle (slow/fast), reverse second half, weave | Combines 3 sub-skills — good integration test |
| 54 | 2. Add Two Numbers | M | "digits stored in reverse, add them" | convert to int (overflow!) → digit-by-digit walk with carry | Pointer math with carry — classic |
| 55 | 23. Merge K Sorted Lists | H | "merge K sorted lists" | repeatedly merge pair O(k·N) / 3-way merge → **min-heap of (val, list, node)** O(N log k) | The heap+list combo problem; tuple tie-breaking lesson |

---

### Group 7 — Trees (13)

| # | LeetCode | Lvl | Signal | Approach sketch (brute → optimal) | Why it's on the list |
|---|---|---|---|---|---|
| 56 | 104. Maximum Depth of Binary Tree | E | "deepest path length" | level-order counting → `1 + max(depth(left), depth(right))` | The recursion template in its purest form |
| 57 | 100. Same Tree | E | "identical shape and values" | serialize both & compare → simultaneous recursion with 3-way base | Base-case discipline (both None / one None / values differ) |
| 58 | 101. Symmetric Tree | E | "mirror of itself" | serialize + reverse compare → recurse (left.left vs right.right) *and* (left.right vs right.left) | Teaches "two recursions per node" pairing |
| 59 | 226. Invert Binary Tree | E | "flip every left/right child" | BFS collect+swap → postorder swap one node at a time | Trivial code, famous meme; often first question of the round |
| 60 | 110. Balanced Binary Tree | E | "height-balanced?" | naive: recompute heights everywhere O(n²) → return height or −1 sentinel (prune on first imbalance) | The "return -1 to signal failure" optimization pattern |
| 61 | 543. Diameter of Binary Tree | E | "longest path between any two nodes" | all-pairs DFS O(n²) → postorder returns height; **global best = left_h + right_h** | First taste of "local return + global answer" — DP-in-trees intro |
| 62 | 102. Binary Tree Level Order Traversal | M | "group nodes by level" | recursion with depth param → **queue BFS** with `for _ in range(len(q))` level freeze | The BFS-level-freeze line used everywhere |
| 63 | 199. Binary Tree Right Side View | M | "what's visible from the right" | recursive by depth (right first) → level-order, take last of each level | Level-order variant; good warm follow-up to #62 |
| 64 | 98. Validate Binary Search Tree | M | "is it a valid BST?" | check only direct children (fails on deep violations!) → **inherited (lo, hi) bounds** | The global-vs-local invariant lesson (Part 5 §5.1) |
| 65 | 236. Lowest Common Ancestor of a Binary Tree | M | "deepest common ancestor" | root-to-node paths via DFS, compare → postorder: if left & right both return nodes → current; bubble up one | The bubble-up return pattern for general trees |
| 66 | 105. Construct Binary Tree from Preorder and Inorder | M | "rebuild tree from traversals" | recursive search each time O(n²) → index map + recurse over slices / index ranges | Divide-and-conquer over traversal arrays; favorite of Big Tech |
| 67 | 124. Binary Tree Maximum Path Sum | H | "max path, any node to any node" | try all paths O(n²) → postorder returns **max gain downward**, updates global with `left+right+self` | The hardest standard tree recursion — capstone of "local return, global answer" |
| 68 | 297. Serialize and Deserialize Binary Tree | H | "encode/decode arbitrary tree" | JSON cheats → pre-order with `#` null markers + iterator; deserialize by consuming tokens | Design + recursion; tests if traversal truly makes sense to you |

---

### Group 8 — Heap / Priority Queue (7)

| # | LeetCode | Lvl | Signal | Approach sketch (brute → optimal) | Why it's on the list |
|---|---|---|---|---|---|
| 69 | 703. Kth Largest Element in a Stream | E | "kth largest of a running stream" | sort everything each call O(n log n) → **size-k min-heap**, evict when larger arrives | The heap invariant in its smallest form |
| 70 | 215. Kth Largest Element in an Array | M | "kth largest, not kth distinct" | full sort O(n log n) → size-k heap O(n log k); mention quickselect O(n) avg | Follow-up magnet: heap vs quickselect vs sort |
| 71 | 973. K Closest Points to Origin | M | "k nearest by distance" | sort by distance → heap of (dist, point) keep k → or nlargest with key | Distance-as-priority; tuple-entry habit |
| 72 | 1046. Last Stone Weight | E | "smash two heaviest repeatedly" | sort each round → max-heap (negate for Python) simulating the smash | Minimal simulation + heap combo |
| 73 | 621. Task Scheduler | M | "min intervals with cooldown n" | simulate timeline with queue → **math**: `max(counts)` gives frame, fill gaps; or heap of (count, next-available) | The rare problem where the optimal answer is a formula — discuss both |
| 74 | 253. Meeting Rooms II | M | "how many rooms concurrently" | sweep naive O(n²) → sort starts/ends two-pointer **or** heap of end-times (assign room, recycle earliest) | Interval+heap crossover; asked constantly |
| 75 | 295. Find Median from Data Stream | H | "median of a running stream" | store all, sort per query → **two heaps**: max-heap lower half + min-heap upper half, rebalance | The definitive "why two heaps" design; balance invariant is the interview |

---

### Group 9 — Backtracking (9)

| # | LeetCode | Lvl | Signal | Approach sketch (brute → optimal) | Why it's on the list |
|---|---|---|---|---|---|
| 76 | 78. Subsets | M | "all subsets" | 2ⁿ via bit mask or loop-copy → **choose/undo** path template | The master template — every other backtracking problem is this with branches |
| 77 | 46. Permutations | M | "all orderings" | same as subsets + `used[]` to allow re-picking → backtrack with used array | Second template: permutations vs subsets difference |
| 78 | 17. Letter Combinations of a Phone Number | M | "digit string → all letter combos" | nested loops impossible for length n → same as subsets over per-digit choices | Easiest on-ramp to the template |
| 79 | 39. Combination Sum | M | "combinations summing to target, reuse allowed" | all subsets + sum check → backtrack with `start` index (reuse = don't advance) | Teaches how `start` semantics change the output family |
| 80 | 40. Combination Sum II | M | "each number used once, no dup combos" | dedupe after the fact → **sort + skip equal siblings** (`if i > start and c[i]==c[i-1]: continue`) | The duplicate-pruning line — high-frequency trick |
| 81 | 22. Generate Parentheses | M | "all valid n-pair strings" | generate all 2²ⁿ strings + filter → track open/close counts, prune when close > open or open > n | Pruning demonstrated: cut impossible branches early |
| 82 | 131. Palindrome Partitioning | M | "partition so every part is a palindrome" | all 2ⁿ partitions + validity check → backtrack with palindrome check at each cut | Backtracking + string-check combination |
| 83 | 79. Word Search | M | "word exists along adjacent path on board" | try every path → DFS with **mark visited, unmark on exit** (grid backtracking) | Bridge from backtracking to graph-on-grid thinking |
| 84 | 51. N-Queens | H | "place n queens, none attacking" | n! placements + validate → backtrack row by row, columns/diagonals as boolean sets | Constraint-satisfaction flagship; the diagonal-set trick matters |

---

### Group 10 — Graphs (13)

| # | LeetCode | Lvl | Signal | Approach sketch (brute → optimal) | Why it's on the list |
|---|---|---|---|---|---|
| 85 | 200. Number of Islands | M | "count connected land masses" | visit every cell repeatedly → DFS/BFS flood, mark on entry, count starts | The grid-DFS gateway; everything else flows from it |
| 86 | 695. Max Area of Island | M | "largest connected region" | count per component with flood fill → return `1 + sum(dfs neighbors)` sizing | Islands variant: recursion returns size |
| 87 | 130. Surrounded Regions | M | "flip captured O-regions" | flip all then unflip valid → **boundary DFS/BFS first**, flip only interior survivors | Inversion of intuition: start from edges |
| 88 | 994. Rotting Oranges | M | "minutes until all fresh rot" | BFS minute-by-minute with multi-source seeds → **all rotten as level-0 queue**, count levels | Multi-source BFS — the "add all sources at once" trick |
| 89 | 542. 01 Matrix | M | "distance to nearest zero" | per-cell scan O(mn·dist) → **multi-source BFS from all zeros** | Same trick as #88; cements multi-source |
| 90 | 207. Course Schedule | M | "can all prerequisites finish?" | build graph, DFS → Kahn's topo sort; cycle ⟹ impossible | Topo sort = cycle detection; the dependency template |
| 91 | 210. Course Schedule II | M | "return a valid order" | DFS post-order list → Kahn's zero-indegree queue | Same with output required — the practical version |
| 92 | 133. Clone Graph | M | "deep-copy an arbitrary graph" | naive copy without links → BFS with `old→new` dict | Graph + hashmap pairing; trivial once seen |
| 93 | 399. Evaluate Division | M | "a/b given equations, answer queries" | per-query DFS → build **weighted directed graph**, one DFS/BFS per query multiplying edge weights | Graph-as-modeling problem; also solvable with Union-Find of (node, weight) — discuss both |
| 94 | 785. Is Graph Bipartite? | M | "2-colorable?" | per-component BFS coloring → alternate colors; conflict ⟹ not bipartite | BFS coloring is a top follow-up pattern |
| 95 | 310. Minimum Height Trees | M | "roots that minimize height" | rebuild from every node O(V²) → **trim leaves layer by layer** (topological peeling) | The "in-degree ≤ 1 leaves" insight — elegant and common |
| 96 | 127. Word Ladder | H | "shortest word-change sequence" | BFS over word list O(N·L²) → precompute wildcard buckets `h*t` so neighbors are O(L) | Word-graph construction + BFS; the adjacency-optimization lesson |
| 97 | 743. Network Delay Time | M | "time for signal to reach all nodes" | run Bellman-Ford O(V·E) → **Dijkstra** with heap, skip stale pops | The standard Dijkstra home |

---

### Group 11 — Greedy & Intervals (9)

| # | LeetCode | Lvl | Signal | Approach sketch (brute → optimal) | Why it's on the list |
|---|---|---|---|---|---|
| 98 | 55. Jump Game | M | "can you reach the end?" | DFS/DP reachability O(n²) → track `farthest` reachable in one pass O(n) | Greedy that feels like DP — the "reachable frontier" idea |
| 99 | 45. Jump Game II | M | "minimum jumps" | BFS levels O(n²) → greedy jump-boundaries (end-of-current-jump window) | Same skeleton, harder invariant — pair it with #98 |
| 100 | 134. Gas Station | M | "one full circuit possible? which start" | try every start O(n²) → single pass: reset start at each deficit; `total ≥ 0` decides existence | The "why the greedy proof works" discussion question |
| 101 | 763. Partition Labels | M | "max partitions so each letter in one part" | repeatedly scan extensions → one pass tracking **last occurrence** of each char, cut when window covers all | Frequency + greedy merge; very popular lately |
| 102 | 435. Non-overlapping Intervals | M | "max size of non-overlapping set" | all subsets O(2ⁿ) → sort by **end time**, count non-overlapping (complement of min removals) | The canonical interval greedy — exchange argument practice |
| 103 | 56. Merge Intervals | M | "merge all overlapping" | pairwise compare O(n²) → sort by start, merge into `out[-1]` | Every "merge ranges" problem (calendar, line sweep) reduces to this |
| 104 | 452. Minimum Number of Arrows to Burst Balloons | M | "min arrows through all balloons" | sort + greedy count: new arrow only when current balloon starts after last arrow's position | Merge-intervals' twin — tests if you understand *why* end-sorting works |
| 105 | 406. Queue Reconstruction by Height | M | "rebuild queue by (h, k)" | brute-force insertion search → **sort tallest-first** (or shortest-first) + insert at index `k` using list splice | Counterintuitive greedy that needs justification — differentiator |
| 106 | 135. Candy | H | "min candies, higher-rated neighbor needs more" | two passes of "give more than neighbor" → **left→right then right→left** max pass | The bidirectional-greedy classic; single-pass attempts always fail |

---

### Group 12 — Strings (10)

| # | LeetCode | Lvl | Signal | Approach sketch (brute → optimal) | Why it's on the list |
|---|---|---|---|---|---|
| 107 | 13. Roman to Integer | E | "roman → int" | if/else per letter → sum with **subtractive rule** (`IV = V − I`) lookahead | Simple loop + rule handling; good warm-up |
| 108 | 14. Longest Common Prefix | E | "common prefix of all words" | compare all pairs → **vertical scan** (char by char) or sort-and-compare first/last only | The O(total) trick: sorting isolates extremes |
| 109 | 58. Length of Last Word | E | "length of last word" | `split()` one-liner → manual `rstrip` + count from the end | Interviewers sometimes ban built-ins — be ready either way |
| 110 | 28. Find the Index of the First Occurrence | E | "substring search, no built-in `find`" | nested scan O(n·m) → **two pointers / KMP** discussion; Python `in` for real code | Easiest place to *discuss* KMP even if you implement simple |
| 111 | 7. Reverse Integer | M | "reverse digits, 32-bit overflow check" | string reverse → arithmetic pop/push + bounds check | Digit math without strings; overflow reasoning |
| 112 | 8. String to Integer (atoi) | M | "parse with whitespace/sign/overflow rules" | built-in parse → one pass with state: skip spaces, optional sign, digits, clamp at INT_MAX | State-machine parsing — mirrors real compiler work |
| 113 | 151. Reverse Words in a String | M | "reverse word order in place-ish" | split + join → two-pointer reverse whole string, then reverse each word | The elegant 3-reverse algorithm — a favorite follow-up |
| 114 | 5. Longest Palindromic Substring | M | "longest palindromic substring" | check all O(n²)/O(n³) → **expand around centers** (2n−1 centers) O(n²); mention Manacher O(n) | Center-expansion technique reused by #115 |
| 115 | 647. Palindromic Substrings | M | "count palindromes" | all substrings + check → expand-around-center count, odd & even | Same technique as #114 with a counter — pair them |
| 116 | 1910. Remove All Occurrences of a Substring | M | "remove substring repeatedly until gone" | `while s.find(...)` rebuild → **stack of chars**, pop when suffix matches | Stack-for-substring-removal; also leads to basic KMP intuition |

---

### Group 13 — Dynamic Programming (23) · *the group that separates offers from rejections*

| # | LeetCode | Lvl | Signal | Approach sketch (brute → optimal) | Why it's on the list |
|---|---|---|---|---|---|
| 117 | 70. Climbing Stairs | E | "ways to climb, 1 or 2 steps" | fib recursion exponential → **memo → table → O(1) variables** (do all 4 stages!) | The DP evolution textbook example |
| 118 | 198. House Robber | M | "max sum, no adjacent picks" | all subsets → `dp[i] = max(dp[i−1], dp[i−2]+a[i])` | The 1D "skip or take" template |
| 119 | 213. House Robber II | M | "houses in a circle" | naive → run linear robber on **two ranges** (exclude first / exclude last), take max | Circle-handling technique: break symmetry into two linear cases |
| 120 | 53. Maximum Subarray | M | "max contiguous sum" | all subarrays O(n²) → **Kadane**: best-ending-here or restart | One of the five patterns you must own perfectly |
| 121 | 152. Maximum Product Subarray | M | "max product subarray" | all subarrays → track **min AND max** (negative flips it) | The "negatives flip extremes" insight — Kadane variant with teeth |
| 122 | 300. Longest Increasing Subsequence | M | "longest strictly increasing" | O(n²) DP (`dp[i]` = LIS ending here) → **patience sorting** with bisect O(n log n) | Both versions asked; great follow-up ladder |
| 123 | 139. Word Break | M | "split string using dictionary words" | all partitions O(2ⁿ) → `dp[i] = any(dp[j] and s[j:i] in dict)` + set lookup | String DP + hashing combo; very frequent |
| 124 | 91. Decode Ways | M | "1→A ... 26→Z, count decodings" | naive recursion on prefix → `dp[i] = ways(i−1) + ways(i−2)` with validity checks on `1–9`, `10–26` | Fibonacci-shape with constraint traps (`0` handling) |
| 125 | 322. Coin Change | M | "min coins for amount" | all combinations / greedy (greedy **fails** on `coins=[1,3,4], target=6`) → bottom-up `dp[a]=min(dp[a−c]+1)` | The problem that proves greedy isn't always safe |
| 126 | 518. Coin Change II | M | "number of combinations for amount" | backtracking → **forward iteration** = unbounded (reuse coins); backward = 0/1 | Forces you to internalize iteration direction semantics |
| 127 | 416. Partition Equal Subset Sum | M | "split into two equal sums" | all subsets O(2ⁿ) → boolean knapsack to `sum/2`; sorted + early prune | 0/1 knapsack in boolean clothing — the most-translated DP form |
| 128 | 494. Target Sum | M | "+/− to reach target" | all 2ⁿ assignments → convert to **subset-sum count**: count subsets summing to `(total+target)/2` | The subset-sum ↔ target-sum reduction — a "spot the equivalence" test |
| 129 | 62. Unique Paths | M | "count right/down paths" | recursion with overlap → `dp[r][c]=dp[r−1][c]+dp[r][c−1]`, compress to 1D | The 2D grid DP gateway |
| 130 | 64. Minimum Path Sum | M | "min-cost path" | Dijkstra over grid (overkill) → DP with top/left min — but if obstacles+weights vary, discuss Dijkstra alternative | Contrast: when graph algorithms and DP collide |
| 131 | 221. Maximal Square | M | "largest 1-filled square" | check all squares O((mn)³) → `dp[r][c] = 1 + min(top, left, topleft)` if cell = 1 | The min-of-three recurrence — classic "spot the sub-square" |
| 132 | 1143. Longest Common Subsequence | M | "LCS of two strings" | exponential recursion → **i×j table**, match → diagonal+1 else max(left, up) | The two-string DP template — powers #133 |
| 133 | 72. Edit Distance | M | "min insert/delete/replace" | recursion on both prefixes → same grid with `min` of three ops + diagonals | The most-cited 2D DP; explain the table cells out loud |
| 134 | 516. Longest Palindromic Subsequence | M | "longest palindromic subsequence" | all subsequences → LCS of `s` with `reverse(s)` OR interval DP `dp[i][j]` | Two ways to the same answer — shows DP modeling choice |
| 135 | 115. Distinct Subsequences | H | "ways s forms t as subsequence" | 2D count DP: match → diagonal + up; else up | Counting DP over two strings — the LCS family's counting branch |
| 136 | 132. Palindrome Partitioning II | H | "min cuts for all-palindrome parts" | try every cut → precompute palindrome table + `dp[i] = min(dp[j]+1)` | Interval/2D hybrid — hard-tier signal |
| 137 | 32. Longest Valid Parentheses | H | "longest valid `(...)` substring" | all substrings + stack check → **stack of indices** (base −1) OR DP on ending-here | Stack and DP both solve it — compare approaches |
| 138 | 10. Regular Expression Matching | H | "`.` and `*` matching" | naive backtracking explodes → 2D DP: `dp[i][j]` prefixes match, `*` = zero-or-more with cases | The hardest standard string DP; thought-experiment gold |
| 139 | 123. Best Time to Buy/Sell Stock III | H | "at most **2** trades" | all sequences O(n²) → 4-state one-pass DP (buy1/sell1/buy2/sell2) | The k-transactions family — hardest common state DP |

*If you finish this group early, three strong bonus DP problems:* **309.** Best Time with Cooldown (three-state machine), **44.** Wildcard Matching (greedy-star or DP), **337.** House Robber III (tree-shaped DP).

---

### Group 14 — Bit Manipulation (4)

| # | LeetCode | Lvl | Signal | Approach sketch (brute → optimal) | Why it's on the list |
|---|---|---|---|---|---|
| 140 | 136. Single Number | E | "every number twice, one once" | Counter / sort → **XOR everything**: `a^a=0`, `a^0=a` | XOR's flagship — one line, needs the explanation |
| 141 | 191. Number of 1 Bits | E | "count set bits" | string convert → `n & (n−1)` loop clears lowest 1 each call | Brian Kernighan's trick — bit-level thinking |
| 142 | 338. Counting Bits | E | "bits for 0..n" | count each independently → `dp[i] = dp[i >> 1] + (i & 1)` (or `i & (i−1)`) | Bit + DP hybrid — the pattern-recognition test |
| 143 | 201. Bitwise AND of Numbers Range | M | "AND of all nums in [lo, hi]" | loop O(n) → shift both right until equal, count shifts, shift back | The "common prefix of bits" insight — pure aha |

---

### Group 15 — Trie (3)

| # | LeetCode | Lvl | Signal | Approach sketch (brute → optimal) | Why it's on the list |
|---|---|---|---|---|---|
| 144 | 208. Implement Trie (Prefix Tree) | M | "insert / search / startsWith" | hash set of all words (can't do prefix efficiently) → node-per-char with `children` dict + `is_end` | Implements the Part 5 structure — one-time rite of passage |
| 145 | 211. Design Add and Search Words Data Structure | M | "words + wildcards `.`" | per-query generation (exponential) → trie + **DFS over wildcard branches** | Trie + backtracking combo; the `.` case is the whole test |
| 146 | 212. Word Search II | H | "all dictionary words on a board" | DFS per word O(words·m·n·L) → **build trie, one DFS carrying the trie node** + prune | The hardest trie problem; shows why trie beats set-per-word |

---

### Group 16 — Design & Simulation (4)

| # | LeetCode | Lvl | Signal | Approach sketch (brute → optimal) | Why it's on the list |
|---|---|---|---|---|---|
| 147 | 146. LRU Cache | M | "get/put in O(1), evict least recent" | list scan for LRU O(n) → **dict + OrderedDict** (or hash + doubly linked list manually) | The structure-combination archetype; asked at an enormous number of companies |
| 148 | 380. Insert Delete GetRandom O(1) | M | "all three ops O(1)" | array+set fails delete → **list + index-map**: swap-delete (move last into hole) | Swap-delete trick appears in shuffle, reservoir sampling, removals |
| 149 | 705. Design HashSet | E | "implement set without built-ins" | list of lists / boolean array → **hash with chaining** (design the table yourself) | Proves you understand Part 2's hashing internals |
| 150 | 622. Design Circular Queue | M | "fixed-capacity FIFO" | shifting array O(n) → **ring buffer** with `front/rear % capacity` | The Part 2 circular-queue chapter, implemented on demand |

---

**Count check:** G1 13 · G2 9 · G3 8 · G4 7 · G5 9 · G6 9 · G7 13 · G8 7 · G9 9 · G10 13 · G11 9 · G12 10 · G13 23 · G14 4 · G15 3 · G16 4 = **150** problems, numbered #1–#150 with no duplicates.

*Non-negotiable core if time is short (the eight that show up most): 1. Two Sum (#1) → 20. Valid Parentheses (#38) → 206. Reverse Linked List (#47) → 104. Maximum Depth (#56) → 200. Number of Islands (#85) → 70. Climbing Stairs (#117) → 322. Coin Change (#125) → 146. LRU Cache (#147). Then work each remaining pattern group in order.*

---

## 9.6 Final revision checklist — open this page the night before / morning of any interview

**Minute 0 — pattern reflex (5 min):**
- [ ] Read §8.1 decision tree once. Read §8.4 trigger phrases once.
- [ ] Recall the 7-step framework (Part 0 §0.6): restate → constraints → brute + complexity → bottleneck → pattern → dry run → code → test → state complexity.

**Minute 5 — complexity reflex (3 min):**
- [ ] Table ops: `list[i]` O(1) · `x in list` O(n) · `x in set` O(1) · `append` O(1) · `pop(0)` O(n) · `deque popleft` O(1) · `sort` O(n log n) · heap push/pop O(log n) · binary search O(log n).
- [ ] n limits: ≤15→backtrack · ≤10³→O(n²) · ≤10⁵→O(n log n) · ≥10⁶→O(n).

**Minute 8 — skeletons you must be able to write cold (10 min, blank paper):**
- [ ] two pointers converging loop
- [ ] sliding window add/shrink (`while invalid`)
- [ ] binary search exact + lower bound
- [ ] monotonic stack (next greater)
- [ ] BFS with level freeze · DFS recursive + iterative
- [ ] reverse linked list · slow/fast
- [ ] tree recursion (depth / validate with bounds)
- [ ] backtrack: choose/explore/undo with `start`
- [ ] heap: push/pop with tuple entries · kth-largest size-k pattern
- [ ] DP: 5-step recipe + coin-change table loop
- [ ] topo sort (Kahn's) · Union-Find with path compression
- [ ] Dijkstra with stale-skip

**Minute 18 — your personal weak list (5 min):**
- [ ] Open your problem log. Redo the 3 most recently *failed* reproductions on paper (pseudo-code is fine).

**Minute 23 — calm (5 min):**
- [ ] One easy problem, timed 10 min, to warm up hands and confidence. Then stop. No new material.

**Day-of reminders:**
1. Talk through every step of the framework out loud — even the brute force.
2. Dry run on an example before coding. Always.
3. Test `[]`, `[1]`, duplicates, max input — before saying "done."
4. Stuck > 5 min → state it aloud, name the bottleneck, revisit the pattern's SIGNAL line.
5. Finish with: *"Time O(__), space O(__)."*

---

## Closing — how this document is meant to be used forever

You read it once front-to-back (Pass 1 + Pass 2). After that it's a **lookup surface**, not a book:

- **Before an interview** → §9.6 checklist → Part 8 → weak chapters' recap boxes.
- **When a problem feels unknown** → §8.1 decision tree → jump to the matching chapter.
- **When you solved something clever** → find which pattern it was (§8.2) and add the problem's name to that pattern's list — you're building *your* signal→pattern index now; that's the real skill.
- **Monthly** → re-run 3 random Top-150 problems blank. If reproduction holds, your DSA is durable. If not, rewind the chapter and rebuild.

**The end state you're aiming for:** you don't recall solutions — you recognize *shapes*. Signal → pattern → skeleton → correct complexity, in seconds, without assistance. That's the entire game, and everything above was built to get you there.

*Now go open LeetCode #1 and start the protocol.*

