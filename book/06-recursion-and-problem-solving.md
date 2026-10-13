# Part 7 — Recursion & Problem Solving

*Recursion is the idea that a function can call itself to solve a smaller version of the same problem. It looks strange the first time, then becomes the most natural way to think about many problems. This chapter ends by tying everything together: how to look at a problem you've never seen and choose the right tool.*

---

## 7.1 What is recursion?

**Recursion** is when a function solves a problem by calling **itself** on a *smaller* version of the problem.

That sounds like it could loop forever — and it would, if not for one crucial ingredient: a **base case**, the point where the function stops recursing and returns a direct answer.

**Real-world analogy — Russian nesting dolls.** To count all the dolls, you open one, and inside is *another, smaller* set of dolls with the same problem: "count these." You keep opening until you reach the tiny solid doll that can't be opened. That tiny doll is the base case.

Two parts, always:

1. **Base case** — the smallest case, answered directly, no recursion. *Stops the descent.*
2. **Recursive case** — do one small piece of work, then call the function on a *smaller* input and trust it to finish the job.

> **The mental shift: TRUST.** You don't trace every step in your head. You answer the trivial case, and you trust your own function to correctly solve the smaller version. That trust is what makes recursion click.

---

## 7.2 A first recursive function

Let's compute a factorial: `5! = 5 × 4 × 3 × 2 × 1 = 120`.

Notice the pattern: `5! = 5 × 4!`. And `4! = 4 × 3!`. Each factorial is built from a smaller factorial. That's recursion begging to happen.

```python
def factorial(n):
    if n <= 1:              # BASE CASE: 1! and 0! are both 1
        return 1
    return n * factorial(n - 1)   # RECURSIVE CASE: n × (n-1)!
```

Call `factorial(4)` and in your head trace it like this:

```
factorial(4)                 waiting for factorial(3)
  └─ factorial(3)            waiting for factorial(2)
       └─ factorial(2)       waiting for factorial(1)
            └─ factorial(1)  BASE CASE → returns 1
            ← returns 2 * 1 = 2
       ← returns 3 * 2 = 6
  ← returns 4 * 6 = 24
final answer: 24
```

Two phases: **going down** (breaking the problem into smaller pieces until the base case), and **coming back up** (combining the answers). Every recursion has both.

---

## 7.3 The call stack — where recursion actually lives

To understand recursion properly, you need to know about the **call stack**. It's how the computer remembers where to return after a function finishes.

When a function calls another, the caller is *paused* and remembered on a stack. When the called function finishes, the computer pops the stack and resumes the caller.

Trace `factorial(3)` and watch the stack. Each "frame" is one paused call:

```
Step 1: Python enters factorial(3)
   ┌──────────────────┐
   │ factorial(3)      │  n=3, waiting for factorial(2)
   └──────────────────┘

Step 2: enters factorial(2)
   ┌──────────────────┐
   │ factorial(2)      │  n=2, waiting for factorial(1)
   ├──────────────────┤
   │ factorial(3)      │  n=3, still waiting
   └──────────────────┘

Step 3: enters factorial(1) → base case → returns 1, its frame is popped
   ┌──────────────────┐
   │ factorial(2)      │  now gets 1, returns 2×1 = 2 → popped
   ├──────────────────┤
   │ factorial(3)      │  still waiting
   └──────────────────┘

Step 4: factorial(3) gets 2, returns 3×2 = 6 → popped
   (stack empty → done)
```

**Why this matters:**

- The stack **grows with the depth** of the recursion. Deep recursion uses a lot of memory.
- Python has a **limit** (about 1,000 frames by default). Recursing tens of thousands of levels deep raises `RecursionError` — the stack is full.
- If you forget the base case, the recursion never stops going down → stack overflow → `RecursionError`.

```python
# This crashes with RecursionError — no base case!
def countdown(n):
    print(n)
    countdown(n - 1)     # ❌ never stops

# Fixed:
def countdown(n):
    if n == 0:           # ✅ base case stops the descent
        return
    print(n)
    countdown(n - 1)
```

---

## 7.4 Three classic recursive problems, traced

Let's do three you'll see everywhere. For each, find the base case and the smaller problem.

### 1. Factorial

Already done above. Base case: `n <= 1 → 1`. Smaller problem: `(n-1)!`. Complexity: `O(n)` time, and `O(n)` space because the stack grows `n` deep.

### 2. Fibonacci

The Fibonacci sequence: `0, 1, 1, 2, 3, 5, 8, 13, ...` where each number is the sum of the two before it.

```python
def fibonacci(n):
    if n <= 1:                       # base case
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)   # two smaller problems
```

Let's trace `fibonacci(4)`:

```
                       fib(4)
                    /          \
               fib(3)           fib(2)
              /      \          /     \
          fib(2)   fib(1)   fib(1)   fib(0)
          /    \
      fib(1) fib(0)

Count the boxes: 9 calls for just n = 4.
```

**The problem with this version:** it redoes work! `fib(2)` is computed **twice**, `fib(1)` **three** times. The number of calls roughly doubles with each increase in `n` → it's `O(2ⁿ)`, which explodes. `fibonacci(40)` would take minutes.

**The fix** (used in dynamic programming) is **memoization**: remember answers you've already computed.

```python
def fibonacci_fast(n, memo=None):
    if memo is None:
        memo = {}
    if n <= 1:
        return n
    if n in memo:              # already computed? reuse it — O(1)
        return memo[n]
    memo[n] = fibonacci_fast(n - 1, memo) + fibonacci_fast(n - 2, memo)
    return memo[n]
# Now O(n) time instead of O(2ⁿ).
```

The naive Fibonacci is the classic example that *motivates* memoization — good to know it exists now.

### 3. Reverse a string recursively

Recursion can solve it without loops: the reverse of a string is "the reverse of everything after the first character, then the first character on the end."

```python
def reverse_string(s):
    if len(s) <= 1:              # base case: empty or one character
        return s
    return reverse_string(s[1:]) + s[0]   # reverse the tail, then add the front
```

Trace `reverse_string("abc")`:

```
reverse("abc") = reverse("bc") + "a"
reverse("bc")  = reverse("c")  + "b"
reverse("c")   = "c"                       ← base case
= ("c" + "b") + "a" = "cba" ✅
```

---

## 7.5 Recursion vs. iteration

Every recursion can also be written with a loop. So which should you use?

| | Recursion | Iteration (loops) |
|---|---|---|
| State held by | the call stack (automatic) | your own variables |
| Best for | naturally self-similar problems (trees, nested structures, divide & conquer) | simple, linear repetition |
| Memory | grows with depth (`O(depth)`) | usually `O(1)` extra |
| Speed | a bit slower (each call has overhead) | faster |
| Risk | stack overflow if too deep | none from depth |
| Readability | elegant for nested problems | clearer for simple ones |

**When to use recursion:**
- The problem is naturally defined in terms of itself (factorial, Fibonacci, "reverse the rest").
- You're working with nested or tree-like structures (folders inside folders, menus inside menus).
- You're splitting a problem in half repeatedly (divide and conquer).
- The recursion depth will stay safely small (a few hundred or less).

**When to use iteration:**
- Simple, one-pass repetition.
- The depth could get very large (thousands+) — Python's stack limit means deep recursion *crashes*.
- You want maximum speed and minimum memory.

**Converting recursion to iteration** — the general idea: recursion uses a hidden stack, so an iterative version uses an **explicit** stack (a list) to remember the same things. For simple tail-style recursions (where the recursive call is the very last thing), you can convert to a plain loop.

```python
# Recursive factorial
def factorial_rec(n):
    if n <= 1:
        return 1
    return n * factorial_rec(n - 1)

# Iterative factorial — no stack risk
def factorial_iter(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
```

Same answer, `O(1)` extra space, no chance of a stack overflow. **In interviews, "now do it without recursion" is a very common follow-up** — knowing both proves you understand what the recursion was really doing.

---

## 7.6 Problem solving — putting all of DSA together

Here's the moment this whole book has been building toward. You now own:

- **Big O** — to judge if a solution is fast enough.
- **Lists/arrays** — ordered storage with instant indexing.
- **Linked lists** — cheap inserts/removals.
- **Stacks & queues** — when order-of-processing matters.
- **Searching & sorting** — find and order data.
- **Hashing (dicts/sets)** — instant lookups and counting.
- **Recursion** — solving self-similar problems.

A hard problem is usually just these pieces combined. The skill is **choosing** the right piece. Here's a reliable method.

### The 5-step problem-solving method

Use this on *every* problem — in practice, in interviews, always:

```
STEP 1 — Understand.
    Restate the problem in your own words. What is the input? The output?
    Ask about the constraints: how big can the input be? Sorted? Duplicates?

STEP 2 — Work small examples by hand.
    Take a tiny example (3-4 items) and solve it manually. Include edge cases:
    empty input, one item, all the same. This reveals the pattern.

STEP 3 — Write the slow-but-correct solution first.
    Nested loops are fine. Don't optimize yet — get something CORRECT.

STEP 4 — Find the bottleneck.
    Which line does the most work? Usually the inner loop searching for
    something. Name it out loud.

STEP 5 — Swap in the right structure.
    "The inner loop is searching" → use a dict/set (Part 6).
    "It keeps the most recent item" → use a stack.
    "It processes oldest first" → use a queue.
    "The data must stay ordered" → sort it.
    "I need the smallest/largest repeatedly" → a sorted list or heap.
    "The problem repeats itself" → recursion.
```

### The structure-choosing cheat sheet

When you're stuck, ask what the problem *needs*:

| The problem needs... | Reach for... |
|---|---|
| Fast lookup / "have I seen this?" | `dict` or `set` |
| To count things | `dict` / `Counter` |
| Items in order | sort (`sorted`) |
| Most recent item first | stack (list: `append`/`pop`) |
| Oldest item first | queue (`deque`: `append`/`popleft`) |
| Access by position | list/array |
| Cheap insert/remove at the ends | linked list / `deque` |
| To split a problem into smaller copies | recursion |
| Fast search in ordered data | binary search |

### A full worked example

**Problem:** *Given a list of numbers, find the first element that appears more than once.*

**Step 1 — Understand.** Input: a list. Output: the first repeated value (or "none"). Can the list be empty? Yes. 

**Step 2 — Small example.** `[3, 1, 4, 1, 5]` → 1 repeats first → answer `1`. Example with no repeats: `[1, 2, 3]` → none.

**Step 3 — Slow solution.** Compare every pair:

```python
def first_duplicate_slow(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return nums[i]
    return None
# O(n²) — too slow for large inputs.
```

**Step 4 — Bottleneck.** The inner loop scans everything to check "have I seen this value before?"

**Step 5 — Swap in the right structure.** "Have I seen this?" → a **set**.

```python
def first_duplicate_fast(nums):
    seen = set()
    for x in nums:
        if x in seen:        # O(1) check
            return x
        seen.add(x)
    return None
# O(n) — one pass → many times faster.
```

That's the whole game: recognize the bottleneck, pick the structure that fixes it. You've just seen the single most valuable move in all of DSA.

### Breaking a big problem into smaller ones

Three techniques that always work:

1. **Reduce to something you already know.** "Is this word an anagram?" → "do these two words have the same letter counts?" → frequency counting (Part 6).
2. **Split into phases.** "Find the most common word" → phase 1: count all words; phase 2: pick the biggest count. Do one phase at a time.
3. **Solve a smaller version first.** Can't see the pattern for a list of 100? Solve it for a list of 3 by hand. The pattern usually appears.

---

## 7.7 DSA in interviews — what to expect and how to behave

### Why companies ask DSA

Interviews use DSA because it's a cheap, fair test of how you think: can you break down a new problem, reason about efficiency, and write correct code under a little pressure? These are the everyday skills of the job, compressed into 45 minutes.

### The types of problems you'll see

In rough order of how often they appear:

1. **Hash map / set problems** — counting, duplicates, lookups. (`Two Sum` is the classic.)
2. **Two pointers / sliding window** — a pair or a sub-range of an array/string.
3. **Sorting and searching** — including binary search.
4. **Stack / queue problems** — matching, order of processing.
5. **Linked list manipulation** — reverse, find middle, detect a cycle.
6. **Recursion** — factorial-style, Fibonacci-style, and "solve the rest."
7. **String problems** — often arrays or hash maps in disguise.

### How to approach a problem in an interview (the same 5 steps, said out loud)

Interviewers grade your **process**, not just the final code. So narrate:

1. "Let me restate the problem and check the constraints."
2. "Here's a small example; here's what I expect."
3. "The simple solution is nested loops, which is `O(n²)`. Let me see if I can do better."
4. "The bottleneck is the repeated search — a hash set would make that `O(1)`."
5. "Now I'll write it." (Then test on the edge cases.)

**Always state the complexity** of your solution at the end, and mention the space it uses. `"This is O(n) time and O(n) space."` Interviewers love hearing that sentence.

### Measuring your own solutions

Before you call a solution done, ask:

- **Time:** how does the work grow with input? Can I name the Big O?
- **Space:** what extra memory did I use? Lists, dicts, and recursion depth all count.
- **Edge cases:** empty input, one item, duplicates, negatives, very large input — does it still work?

---

## 7.8 DSA in real-world projects

DSA isn't only for interviews. Here's where these exact ideas run in real software:

| Real-world feature | Data structure / algorithm |
|---|---|
| Search box autocomplete | Trie (a prefix tree) |
| Undo / redo | Stack |
| "People you may know" | Graph traversal + set intersection |
| GPS shortest route | Graph shortest-path (Dijkstra) |
| Detecting spam / unique visitors | Hash set |
| Caching a slow computation | Dict (memoization) — the Fibonacci fix above! |
| Print queue / job scheduler | Queue |
| Ranking a feed, "top 10" | Sorting / heap |
| Finding duplicates in a big dataset | Set |
| Matching brackets in a code editor | Stack |
| Grouping log entries by type | Dict |
| Loading the most-recent items first (a "recent files" list) | Deque |

**Examples, briefly:**

- **Search:** autocomplete uses a prefix tree so typing "ap" instantly finds "apple". The dict in this book already does a simpler version — keying by prefix instead of the whole string.
- **Caching:** the memoized Fibonacci showed the core idea of caching: store a result by its key so you never compute it twice. That's how real caches work, just at a larger scale.
- **Data processing:** counting word frequencies (dict), removing duplicates (set), grouping records (dict) — the frequency patterns from Part 6 are used constantly in data work.
- **Task management:** a scheduler that handles tasks in arrival order is a queue; an "undo recent change" feature is a stack.

The lesson: the tools in this book show up everywhere. Recognizing which one fits is the skill you've been building the whole time.

---

## 7.9 Recap — test yourself

1. **Recursion** → a function that solves a problem by calling itself on a smaller version.
2. **Two required parts** → a base case and a smaller recursive case.
3. **Base case** → the smallest case, answered directly; stops the descent.
4. **Call stack** → where each paused recursive call is remembered; grows with depth.
5. **What happens without a base case?** → infinite recursion → `RecursionError`.
6. **Factorial base case** → `n <= 1 → 1`.
7. **Why is naive Fibonacci slow?** → it recomputes the same subproblems (`O(2ⁿ)`); memoization fixes it to `O(n)`.
8. **Reverse a string recursively** → `reverse(s[1:]) + s[0]`.
9. **Recursion's memory cost** → `O(depth)`.
10. **When to avoid recursion** → very deep / large inputs (Python's stack limit).
11. **Converting recursion to iteration** → use a loop, or an explicit stack.
12. **First step of problem solving** → understand and restate the problem.
13. **The key optimization move** → find the bottleneck (often a repeated search) and swap in the right structure.
14. **What does a hash set fix?** → slow "have I seen this?" lookups.
15. **What to always state in an interview** → the time and space complexity.

---

## 7.10 Tasks (the `recursion/` folder)

1. **Write recursive functions with proper base cases:**
   - `factorial(n)` — factorial of a number.
   - `sum_list(nums)` — sum of a list (base case: empty list → 0).
   - `count_down(n)` — print from `n` down to 1.

2. **Factorial using recursion** (then write the iterative version and compare).

3. **Generate Fibonacci numbers**
   - Write the naive recursive version.
   - Add memoization and confirm it's fast.
   - Write the iterative version (`a, b = 0, 1` loop).

4. **Reverse a string using recursion.**

5. **Reverse a list using recursion** (or a number's digits).

6. **Check if a string is a palindrome using recursion** (compare the ends, recurse inward).

7. **Solve a basic problem using the right structure** — for each, choose a structure and justify it:
   - Count how many times each word appears → `dict` / `Counter`.
   - Check if a string is a valid sequence of brackets → stack.
   - Find the largest number in a list → a single pass.
   - Reverse a list → two pointers.

8. **Analyze complexity** of each solution you wrote above. Write down time and space for each.

9. **Real-world mini-project:** build a tiny "undo" system for a text editor:
   - Store the history of edits in a stack.
   - Undo pops the last edit.
   - (Queue bonus) Build a "print queue" that handles jobs in order using `deque`.

---

## Where to go next

You've covered the full beginner foundation: efficiency, arrays, linked lists, stacks, queues, searching, sorting, hashing, and recursion. From here, the natural next steps (each builds directly on this book) are:

- **Trees and binary search trees** — hierarchical data (folders, menus, databases).
- **Heaps / priority queues** — always get the smallest or largest item fast.
- **Graphs** — connections and paths (social networks, maps, dependencies).
- **Dynamic programming** — solving hard problems by reusing smaller answers (the memoized Fibonacci is your first taste).
- **Two pointers & sliding window** — a family of array/string techniques built on everything here.

But you don't need those yet. Master what's in this book first — solve the tasks, do the LeetCode problems in each folder, and re-derive each idea from scratch after a few days. **That is how the knowledge sticks.**

You started this book unable to solve small problems. If you've done the work, you can now look at an unfamiliar problem, find its bottleneck, and reach for the right structure. That is the actual skill. Everything else is detail.

---

**Previous:** [Part 6 — Hashing, Sets & Dictionaries](05-hashing-sets-and-dicts.md)
