# Part 4 — Stacks & Queues

*Two of the simplest structures in computing, and two of the most used. They differ in one idea: **which end you take from**. Get that idea right and a huge family of problems becomes easy.*

---

## 4.1 Stack — Last In, First Out (LIFO)

### The idea

A **stack** is a collection where you add and remove items **only at one end**, called the **top**. The last item you put in is the first one you take out. That's **LIFO: Last In, First Out**.

**Everyday analogy — a stack of plates.** You put a clean plate on top. When you need a plate, you take the top one. You never pull a plate from the middle. The last plate placed is the first plate taken.

```
        ▲ push (add here)
        │
     ┌─────┐
     │  D  │  ← top  (the only place you add or remove)
     ├─────┤
     │  C  │
     ├─────┤
     │  B  │
     ├─────┤
     │  A  │  ← bottom
     └─────┘
        │
        ▼ pop (remove from the same end)
```

Where do you meet stacks in real life (and in software)?

- **The Undo button** in an editor — the most recent action is undone first.
- **The browser Back button** — you go back to the most recent page first.
- **Function calls** — Python itself uses a stack to remember where to return after a function finishes (Part 7).
- **Matching brackets** in code — the most recently opened bracket must close first.

### The operations

| Operation | What it does | Cost |
|---|---|---|
| `push(x)` | add `x` on top | `O(1)` |
| `pop()` | remove and return the top item | `O(1)` |
| `peek()` (or `top()`) | look at the top without removing | `O(1)` |
| `is_empty()` | is the stack empty? | `O(1)` |
| `size()` | how many items? | `O(1)` |

That's the entire interface. The *restriction* — you can only touch the top — is the feature. It's what makes stacks simple and their algorithms provably correct.

### Stack #1: using a Python list

Because `append` and `pop` (from the end) are both `O(1)`, a Python list makes a perfect stack — as long as you **only ever touch the end**.

```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)          # add to the END — O(1)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()       # remove from the END — O(1)

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]         # look at the last item — O(1)

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
```

```python
s = Stack()
s.push("a")
s.push("b")
s.push("c")
print(s.peek())    # "c"
print(s.pop())     # "c"
print(s.pop())     # "b"
print(s.size())    # 1
```

> **The classic mistake:** using the *wrong end* of the list.
> ```python
> self.items.insert(0, x)   # ❌ O(n) — shifts everything right
> self.items.pop(0)         # ❌ O(n) — shifts everything left
> ```
> A list works as a stack **only if you use `append` and `pop()` at the end**. Touch index 0 and every operation becomes `O(n)`.

### Stack #2: using a linked list

If you built a linked list in Part 3, a stack is a natural fit: make the **head the top**. Then push and pop are both `O(1)` because they only touch the front.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedStack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, x):
        node = Node(x)
        node.next = self.top     # new node points at the old top
        self.top = node          # it becomes the new top
        self._size += 1          # O(1)

    def pop(self):
        if self.top is None:
            raise IndexError("pop from empty stack")
        value = self.top.data
        self.top = self.top.next # top slides down one node
        self._size -= 1          # O(1)
        return value

    def peek(self):
        if self.top is None:
            raise IndexError("peek from empty stack")
        return self.top.data

    def is_empty(self):
        return self.top is None

    def size(self):
        return self._size
```

**The one design decision that matters:** put the **top at the head**. If the head were the bottom, every push would have to walk the whole list (`O(n)`). Head = top keeps everything `O(1)`.

### When to reach for a stack

Any time the answer depends on **the most recent thing**:

- Matching brackets / parentheses.
- Undo/redo.
- Reversing something.
- Checking nested structures.
- Finding "the next bigger number" (we'll do this below).
- Depth-first search (Part 7 territory).

---

## 4.2 Queue — First In, First Out (FIFO)

### The idea

A **queue** is a collection where you add at one end (the **rear**) and remove from the other end (the **front**). The first item in is the first one out. That's **FIFO: First In, First Out**.

**Everyday analogy — a line at a coffee shop.** The first person to join the line is the first served. New people join at the back. You don't serve the most recent arrival first.

```
  enqueue (join at rear)                     dequeue (leave from front)
        ──────────▶  ┌────┬────┬────┬────┐  ──────────▶
                     │ D  │ C  │ B  │ A  │
                     └────┴────┴────┴────┘
                      rear              front
                   (A arrived first → A leaves first)
```

Where do queues show up?

- **Print jobs** — first document sent is printed first.
- **Task schedulers** — requests handled in order of arrival.
- **Breadth-first search (BFS)** — explore things level by level.
- **Customer support / message queues** — fair, first-come-first-served processing.

### The operations

| Operation | What it does | End | Cost |
|---|---|---|---|
| `enqueue(x)` | add `x` | rear | `O(1)` |
| `dequeue()` | remove and return the front item | front | `O(1)` with `deque`; **`O(n)` with a list!** |
| `peek()` / `front()` | look at the front | front | `O(1)` |
| `is_empty()`, `size()` | | | `O(1)` |

### Queue #1: the naive list version (and why it's a trap)

```python
class BadQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, x):
        self.items.append(x)          # O(1) — add at the end ✅

    def dequeue(self):
        return self.items.pop(0)      # ❌ O(n) — removes index 0, shifts everything!
```

`pop(0)` has to slide every remaining item one slot left. Do `n` enqueues and `n` dequeues and you've done roughly `n²` work. **This is the single most common beginner performance trap with queues.**

The fix is to remove from the *front* without shifting. That's exactly what a `deque` does — and what a circular queue does manually.

---

## 4.3 Circular Queue

### The problem a circular queue solves

Imagine a queue using a fixed-size array, where `front` and `rear` only ever move forward:

```
Start empty, capacity 5:
[ _ ][ _ ][ _ ][ _ ][ _ ]
  front/rear = 0

After a few enqueues and dequeues:
[ _ ][ _ ][ C ][ D ][ E ]
             ▲         ▲
           front     rear

Items 0 and 1 are now WASTED — front already moved past them.
Add more and you hit the end even though there's empty space at the start!
```

A **circular queue** fixes this by **wrapping around**: when `rear` reaches the end, it loops back to index 0 using the modulo operator (`%`). The array behaves like a circle.

```
        index 0 ─── index 1
       /                       \
   index 4                    index 2
       \                       /
            index 3

  rear advances: 0 → 1 → 2 → 3 → 4 → 0 → 1 ...  (wraps!)
```

### Difference from a normal queue

| | Normal array queue | Circular queue |
|---|---|---|
| Wasted slots | Yes (front leaves gaps behind) | No — slots are reused |
| Dequeue cost | `O(1)` imagined, but wastes space (or `O(n)` to shift) | True `O(1)`, no shifting |
| Capacity | Grows/shifts awkwardly | Fixed size, wraps around |
| Used in | simple cases | audio buffers, network packet rings, schedulers |

### Implementing a circular queue

The trick is that both `front` and `rear` advance with `(index + 1) % capacity`. We also keep a `count` so we can tell "empty" from "full" (they look the same otherwise, since both would have `front == rear`).

```python
class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.front = 0        # index of the next item to come OUT
        self.rear = 0         # index where the next item goes IN
        self.count = 0        # how many items are stored

    def enqueue(self, x):
        if self.is_full():
            raise OverflowError("queue is full")
        self.data[self.rear] = x
        self.rear = (self.rear + 1) % self.capacity   # ← the wrap-around
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("queue is empty")
        value = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self.capacity  # ← front wraps too
        self.count -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("queue is empty")
        return self.data[self.front]

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.capacity

    def size(self):
        return self.count
```

```python
q = CircularQueue(3)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())   # 1
q.enqueue(4)         # reuses the freed slot — no overflow!
print(q.dequeue())   # 2
print(q.dequeue())   # 3
print(q.dequeue())   # 4
```

**The wrap-around line `(index + 1) % capacity`** is the entire trick. `%` gives the remainder: `(4 + 1) % 5 = 0`, so from index 4 you go back to 0. Learn to recognize it — it appears in many "circular"/"ring" problems.

> **Why the `count` variable?** Without it, an empty queue and a full queue both have `front == rear`, so you can't tell them apart. Alternatives include keeping one slot permanently unused or tracking size separately — all three approaches appear in interviews.

---

## 4.4 `collections.deque` — the right tool for queues

Python ships with a ready-made double-ended queue called **`deque`** (pronounced "deck"), and it's almost always what you should use for a queue. "Deque" stands for **d**ouble-**e**nded **que**ue: it supports fast `O(1)` operations at **both ends**.

```python
from collections import deque

q = deque()

# Add
q.append(1)         # add to the right (rear)   — O(1)
q.appendleft(0)     # add to the left (front)   — O(1)

# Remove
q.pop()             # remove from the right     — O(1)
q.popleft()         # remove from the left      — O(1)

# Look
q[0]                # peek front
q[-1]               # peek rear
len(q)              # size
```

### Using a `deque` as a queue

```python
from collections import deque

q = deque()
q.append("first")        # enqueue at the rear
q.append("second")
q.append("third")

print(q.popleft())       # "first"  — dequeue from the front (FIFO)
print(q.popleft())       # "second"
```

### Using a `deque` as a stack

The same object works as a stack — just remove from the same end you added to:

```python
from collections import deque

s = deque()
s.append("a")
s.append("b")
s.append("c")

print(s.pop())           # "c"  — LIFO
print(s.pop())           # "b"
```

### The full operation card

| Method | Effect | Cost |
|---|---|---|
| `append(x)` | add to the right end | `O(1)` |
| `appendleft(x)` | add to the left end | `O(1)` |
| `pop()` | remove from the right end | `O(1)` |
| `popleft()` | remove from the left end | `O(1)` |
| `q[0]`, `q[-1]` | peek either end | `O(1)` |
| `q[i]` (middle) | access in the middle | `O(n)` |

**Naming pattern to remember:** `append`/`pop` handle the **right** end; `appendleft`/`popleft` handle the **left** end. A queue uses `append` + `popleft`. A stack uses `append` + `pop`.

---

## 4.5 LIFO vs FIFO — see the difference in one example

This tiny example is the clearest way to feel the difference. Same input, different structure:

```python
from collections import deque

items = [1, 2, 3, 4]

# Stack (LIFO): add and remove at the right end
stack = deque()
for x in items:
    stack.append(x)          # push
print("Stack pops:", [stack.pop() for _ in range(4)])
# → [4, 3, 2, 1]   — last in, first out

# Queue (FIFO): add at the right, remove at the left
queue = deque()
for x in items:
    queue.append(x)          # enqueue
print("Queue dequeues:", [queue.popleft() for _ in range(4)])
# → [1, 2, 3, 4]   — first in, first out
```

**One line of difference (`pop` vs `popleft`), completely different order of processing.** In Part 7 you'll see this same line decide whether a graph traversal is depth-first or breadth-first.

---

## 4.6 The classic stack problem: matching brackets

Let's apply a stack to a real, famous problem (it's LeetCode 20). Given a string of brackets like `"([{}])"`, decide if every opening bracket has a matching closing bracket **in the right order**.

Why does order matter? `"([)]"` has the right *counts* but is still invalid — the `[` opens before the `(` but closes after it, which is illegal.

**The insight:** the most recently opened bracket must be the first to close — that's LIFO, which is a stack.

```python
def is_valid_parentheses(s):
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for ch in s:
        if ch in "([{":
            stack.append(ch)                       # remember an opener
        else:
            if not stack or stack[-1] != pairs[ch]:
                return False                       # nothing to match, or wrong match
            stack.pop()                            # matched — remove the opener
    return len(stack) == 0                          # all openers must be closed
```

Trace `"([{}])"`:

```
(  → stack: [ ( ]
[  → stack: [ ( [ ]
{  → stack: [ ( [ { ]
}  → top { matches } → pop → [ ( [ ]
]  → top [ matches ] → pop → [ ( ]
)  → top ( matches ) → pop → [ ]
end → stack empty → True ✅
```

A counter wouldn't work here — you'd lose the *order*. The stack keeps the order for free.

---

## 4.7 Common beginner mistakes

1. **Using `list.pop(0)` for a queue.** It's `O(n)`; use `deque.popleft()`.
2. **Using the wrong end of a list as a stack.** Only `append`/`pop()` at the end are `O(1)`.
3. **Forgetting the empty check before `pop`/`peek`.** Popping an empty stack should raise a clear error, not crash cryptically.
4. **Trying to peek a `deque` with `q.peek()`.** There's no such method — use `q[0]` (front) or `q[-1]` (rear).
5. **Mixing up `append`/`appendleft`.** `append` = right, `appendleft` = left.
6. **In a circular queue, forgetting the `% capacity` on `rear`.** Without it, `rear` runs off the end of the array.

---

## 4.8 Recap — test yourself

1. **Stack** → LIFO; add and remove at the top.
2. **Stack real-life example** → undo history, browser back, plates.
3. **Queue** → FIFO; add at the rear, remove from the front.
4. **Queue real-life example** → coffee line, print jobs, task scheduling.
5. **Stack with a list** → `append` + `pop()` (end only).
6. **Stack with a linked list** → top = head.
7. **Queue with a list** → bad, because `pop(0)` is `O(n)`.
8. **Queue with `deque`** → `append` + `popleft`, both `O(1)`.
9. **Circular queue trick** → advance pointers with `% capacity`.
10. **Why track `count` in a circular queue?** → To tell full from empty (both have `front == rear`).
11. **`deque` as a stack** → `append` + `pop`.
12. **`deque` as a queue** → `append` + `popleft`.
13. **Which is LIFO?** → Stack. **Which is FIFO?** → Queue.
14. **Best structure for "match nested brackets"?** → Stack.

---

## 4.9 Tasks (the `stack/` and `queue/` folders)

1. **Implement a stack using a list** (push, pop, peek, is_empty, size).
2. **Implement a stack using a linked list.**
3. **Implement a queue using a list** — then *measure* why it's slow — and **reimplement it with `deque`**.
4. **Implement a circular queue** with `enqueue`, `dequeue`, `is_full`, `is_empty`.
5. **Use `deque` for both a stack and a queue**, and print to confirm the LIFO/FIFO difference.
6. **LeetCode: Valid Parentheses** — the bracket solution above. Do it from scratch.
7. **LeetCode: Next Greater Element** — for each item, find the next item to its right that is larger. A **monotonic stack** solves it in `O(n)`:
   ```python
   def next_greater(nums):
       result = [-1] * len(nums)
       stack = []                       # holds indices, values kept decreasing
       for i, x in enumerate(nums):
           while stack and nums[stack[-1]] < x:
               result[stack.pop()] = x  # x is the next greater for that index
           stack.append(i)
       return result
   ```
   Trace it on `[2, 1, 3]` by hand until it clicks.
8. **Export reusable classes.** Put your `Stack` and `Queue` classes in their folders so you can import them in later chapters.

---

**Previous:** [Part 3 — Linked Lists](02-linked-lists.md) · **Next:** [Part 5 — Searching & Sorting](04-searching-and-sorting.md)
