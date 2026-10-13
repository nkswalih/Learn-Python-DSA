# Part 3 — Linked Lists

*Arrays store items side by side, which makes indexing fast but inserting in the middle slow. A linked list trades away fast indexing to make inserting and removing cheap. More importantly, it's the cleanest way to learn how "pointers" (references) work — a skill every interview tests.*

---

## 3.1 The problem linked lists solve

Recall the array's weakness: removing the first item forces every other item to shift one slot left — `O(n)`.

```
Array: [10][20][30][40]
Remove 10 → every item shifts:  [20][30][40]
```

What if items weren't packed together? What if each item simply *knew where the next one is*? Then removing the first item would be a single step: just change where the list starts.

```
[10] → [20] → [30] → [40]
Remove 10 by making [20] the new start:

[20] → [30] → [40]        (one step — nothing shifted!)
```

That's the whole idea. A **linked list** is a chain of items where each item holds its value **and a reference to the next item**.

---

## 3.2 What a linked list is

A linked list is a sequence of **nodes**. Each node contains:

- **data** — the value it holds,
- **a reference** (pointer) to the **next** node.

The list is accessed through a single starting point called the **head**. The last node's next reference points to `None` (nothing), which marks the end.

```
 S I N G L Y   L I N K E D   L I S T

  head
   │
   ▼
 ┌──────────┬──────┐     ┌──────────┬──────┐     ┌──────────┬──────┐
 │ data: 10 │ next │────▶│ data: 20 │ next │────▶│ data: 30 │ next │────▶ None
 └──────────┴──────┘     └──────────┴──────┘     └──────────┴──────┘
```

Compare with an array:

```
 A R R A Y   (stored side by side)
 ┌──────┬──────┬──────┐
 │  10  │  20  │  30  │
 └──────┴──────┴──────┘
```

**The key idea:** there is no single "list object" holding everything. The list *is* the chain of nodes, and you only need to remember the head to reach them all. Follow `next` from the head, and you eventually reach every node.

---

## 3.3 The Node — building block of a linked list

A node is just a tiny container. Let's write it in Python:

```python
class Node:
    def __init__(self, data):
        self.data = data       # the value this node holds
        self.next = None       # reference to the next node (None = end)
```

That's the whole thing. Two fields: a value and a pointer.

### Creating and connecting nodes by hand

This is the single most important exercise for understanding linked lists. Do it line by line:

```python
# Step 1: create three separate nodes
a = Node(10)
b = Node(20)
c = Node(30)

# At this point they are NOT connected:
#   [10]      [20]      [30]

# Step 2: connect them with 'next' references
a.next = b        # 10 → 20
b.next = c        # 20 → 30   (30.next is still None → end)

# Now we have:
#   [10] → [20] → [30] → None

# Step 3: remember the head so we can find the chain later
head = a

# Step 4: walk the chain to prove it works
cur = head
while cur is not None:
    print(cur.data)     # prints 10, 20, 30
    cur = cur.next      # move to the next node
```

**The traversal pattern.** That `while` loop is the heartbeat of linked lists. Almost every linked-list algorithm is this loop with something added inside.

```python
cur = head
while cur is not None:      # (you'll often see: while cur:)
    # do something with cur.data
    cur = cur.next
```

**Why `cur = cur.next` matters:** if you forget to advance, you loop forever on the first node. This one line is the difference between working code and an infinite loop.

---

## 3.4 Singly vs. Doubly linked lists

So far each node only points **forward**. That's a **singly linked list** — and it has a limitation: you can't easily go backward.

A **doubly linked list** gives each node an extra reference to the **previous** node.

```
 D O U B L Y   L I N K E D   L I S T

        ┌──────────┬──────┬──────┐      ┌──────────┬──────┬──────┐
 None ◀─┤  prev    │ 10   │ next ├─────▶│  prev    │ 20   │ next ├──▶ None
        └──────────┴──────┴──────┘◀─────┴──────────┴──────┴──────┘
                       (next)                (prev)
```

```python
class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None       # reference to the next node
        self.prev = None       # reference to the previous node
```

### The decision table

| | Singly linked | Doubly linked |
|---|---|---|
| Each node stores | `data`, `next` | `data`, `next`, `prev` |
| Memory per node | less | more (one extra reference) |
| Move forward | ✅ | ✅ |
| Move backward | ❌ (must restart from head) | ✅ easy |
| Delete a known node | ❌ need the node before it | ✅ use `prev` |
| Typical uses | reverse, detect cycle, merge | browser back/forward, LRU cache |

**Rule of thumb:** use a singly linked list unless you specifically need to move backward or delete nodes you already hold. Doubly costs memory for that flexibility.

---

## 3.5 Building a singly linked list (class)

Now let's wrap the chain in a class so it feels like a real data structure you can `append` to, search, and traverse. Read the comments — each method is small.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    # ---- ADD TO THE FRONT — O(1) ----
    def prepend(self, data):
        node = Node(data)
        node.next = self.head     # new node points at the old first node
        self.head = node          # head now points at the new node
        self.size += 1

    #     Before:  head → [20] → [30] → None
    #     After:   head → [10] → [20] → [30] → None

    # ---- ADD TO THE END — O(n) without a tail pointer ----
    def append(self, data):
        node = Node(data)
        if self.head is None:           # empty list: new node is the head
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:  # walk to the last node
                cur = cur.next
            cur.next = node              # attach the new node at the end
        self.size += 1

    # ---- SEARCH — O(n) ----
    def find(self, target):
        cur = self.head
        while cur is not None:
            if cur.data == target:
                return True
            cur = cur.next
        return False

    # ---- DELETE first occurrence of a value — O(n) ----
    def delete(self, target):
        if self.head is None:
            return False

        # Case A: the head itself holds the target
        if self.head.data == target:
            self.head = self.head.next      # head skips over it
            self.size -= 1
            return True

        # Case B: walk with a trailing pointer so we know the PREVIOUS node
        cur = self.head
        while cur.next is not None:
            if cur.next.data == target:
                cur.next = cur.next.next    # jump over the target node
                self.size -= 1
                return True
            cur = cur.next
        return False

    # ---- TRAVERSE ----
    def to_list(self):
        result = []
        cur = self.head
        while cur is not None:
            result.append(cur.data)
            cur = cur.next
        return result
```

Try it:

```python
lst = SinglyLinkedList()
lst.prepend(30)
lst.prepend(20)
lst.prepend(10)          # list is now 10 → 20 → 30
print(lst.to_list())     # [10, 20, 30]

lst.append(40)           # 10 → 20 → 30 → 40
lst.delete(20)           # 10 → 30 → 40
print(lst.find(30))      # True
print(lst.to_list())     # [10, 30, 40]
```

### Deleting is the tricky one — understand `cur.next = cur.next.next`

To remove a node, you can't just "delete" it. You reach the node *before* it and point its `next` past the target:

```
Before:  [10] → [20] → [30] → [40]      delete 30
You are here: cur = [20]                 cur.next is [30], cur.next.next is [40]

cur.next = cur.next.next  →  [10] → [20] → [40]     [30] is now unlinked
```

The node `[30]` still exists in memory for a moment, but nothing points to it, so Python's garbage collector reclaims it. **That's why singly linked lists can't delete a node given only that node — you need the one before it** to reroute the pointer. A doubly linked list avoids this because `prev` gives you the node before directly.

---

## 3.6 Building a doubly linked list (class)

Same idea, plus backward links. The extra `prev` references must be maintained carefully — that's the only real added difficulty.

```python
class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # ---- ADD TO THE FRONT — O(1) ----
    def prepend(self, data):
        node = DoublyNode(data)
        node.next = self.head
        if self.head is not None:
            self.head.prev = node      # old head points back to new node
        self.head = node
        if self.tail is None:          # first node added
            self.tail = node
        self.size += 1

    # ---- ADD TO THE END — O(1) thanks to the tail pointer ----
    def append(self, data):
        node = DoublyNode(data)
        if self.tail is None:          # empty list
            self.head = self.tail = node
        else:
            node.prev = self.tail      # new node points back
            self.tail.next = node      # old tail points forward
            self.tail = node           # tail moves to the new node
        self.size += 1

    # ---- TRAVERSE FORWARD ----
    def to_list(self):
        result, cur = [], self.head
        while cur is not None:
            result.append(cur.data)
            cur = cur.next
        return result

    # ---- TRAVERSE BACKWARD (impossible with a singly linked list!) ----
    def to_list_reverse(self):
        result, cur = [], self.tail
        while cur is not None:
            result.append(cur.data)
            cur = cur.prev
        return result
```

```python
d = DoublyLinkedList()
d.append(10)
d.append(20)
d.append(30)
print(d.to_list())          # [10, 20, 30]
print(d.to_list_reverse())  # [30, 20, 10]   ← backward walk works!
```

**Why keep a `tail` pointer?** Without it, `append` has to walk from the head to the end every time (`O(n)`). With `tail`, appending is one step (`O(1)`). Small detail, big difference.

**The invariant to protect:** in a doubly linked list, whenever `node.next` is set, the target's `prev` should point back (when the target exists). Break that and backward traversal silently goes wrong.

---

## 3.7 Converting between singly and doubly linked lists

You may be asked to convert one into the other. Both conversions are a single forward walk — a great exercise in managing references.

### Singly → Doubly

Walk forward; at each node, set its `prev` to the node you just came from.

```python
def to_doubly(head):
    prev = None
    cur = head
    while cur is not None:
        cur.prev = prev        # remember where we came from
        prev = cur             # this node becomes the 'previous' for the next
        cur = cur.next
    return head                # head is unchanged
```

Trace on `10 → 20 → 30`:

```
cur=10  prev=None → 10.prev = None   prev=10
cur=20             → 20.prev = 10    prev=20
cur=30             → 30.prev = 20    prev=30
cur=None → done
```

### Doubly → Singly

Just stop using `prev`. You *could* set every `prev` to `None` to free that memory:

```python
def to_singly(head):
    cur = head
    while cur is not None:
        cur.prev = None        # drop the backward links
        cur = cur.next
    return head
```

If the program never reads `prev` again, you can also leave them alone and simply treat the list as singly linked (forward traversal still works). Converting is mostly about updating references — there's no data to move.

---

## 3.8 Linked list vs. array — the honest comparison

| Operation | Array (list) | Linked list |
|---|---|---|
| Get item at index `k` | **`O(1)`** | `O(k)` — must walk `k` nodes |
| Search for a value | `O(n)` | `O(n)` |
| Insert/delete at the **front** | `O(n)` (shift) | **`O(1)`** |
| Insert/delete at the **end** | `O(1)` amortized | `O(1)` if you keep a `tail` pointer |
| Insert/delete at a **known node** | `O(n)` shift | `O(1)` (doubly) |
| Memory per element | compact | extra reference(s) per node |
| Works with binary search | ✅ | ❌ |

**Advantages of linked lists:** cheap inserts/removes at the ends; no resizing; no shifting; great for lists that grow and shrink a lot.

**Limitations:** no instant indexing; extra memory per node; harder to get right (dangling references, endless loops); and in Python specifically, the per-node object overhead often makes them *slower* than plain lists in practice.

**So why learn them?** Two reasons: (1) interviewers use them to test whether you truly understand references and edge cases, and (2) many real structures — like the `deque` from Part 4 and an LRU cache — are built from the same ideas.

---

## 3.9 Common beginner mistakes

1. **Forgetting to advance `cur`.** `cur = cur.next` must be inside the loop, or you spin forever.
2. **Losing the head.** If you overwrite `head` without saving it, you can lose the way back to the list.
3. **Null-checking too late.** Always check `if self.head is None` (empty list) *before* touching `.next`.
4. **Breaking the chain during deletion.** Save what comes next before you reroute pointers.
5. **Forgetting to update `prev` in a doubly linked list.** Forward traversal works; backward silently breaks.
6. **Assuming `head` always stays the first node.** Inserting at the front or deleting the head *moves* the head.

A handy trick for that last one is the **dummy (sentinel) node**: create a throwaway node pointing at the head, do all your work treating `dummy.next` as the list, and return `dummy.next` at the end. It removes special cases like "the head might change." Example:

```python
def delete_first(head, target):
    dummy = Node(0)
    dummy.next = head
    cur = dummy
    while cur.next is not None:
        if cur.next.data == target:
            cur.next = cur.next.next    # works even if the target IS the head
            break
        cur = cur.next
    return dummy.next                   # the real (possibly new) head
```

---

## 3.10 Recap — test yourself

1. **Linked list** → a chain of nodes, each holding data + a reference to the next.
2. **Head** → the entry point; lose it and you lose the list.
3. **Node fields** → `data` and `next` (and `prev` if doubly).
4. **Traversal pattern** → `cur = head; while cur: ...; cur = cur.next`.
5. **Singly vs doubly** → doubly adds `prev`; enables backward moves and easy node deletion.
6. **Prepend cost** → `O(1)`.
7. **Append cost** → `O(n)` without a tail pointer, `O(1)` with one.
8. **Why can't singly delete a node given only that node?** → You need the previous node to reroute the pointer.
9. **Convert singly → doubly** → walk forward, set each `prev` to the previous node.
10. **Convert doubly → singly** → ignore/clear `prev`.
11. **Index access cost** → `O(k)` — no instant jumping.
12. **Dummy node** → a fake node in front that removes head-changing edge cases.

---

## 3.11 Tasks (the `linked_list/` folder)

1. **Create and connect nodes by hand** (no class) — build `10 → 20 → 30` and print it.
2. **Implement a basic singly linked list** with `prepend`, `append`, `find`, `delete`, and `to_list`.
3. **Implement a basic doubly linked list** with `prepend`, `append`, and both forward and backward traversal.
4. **Traverse a linked list** and print every value (both classes).
5. **Insert a node at a given position** in the singly linked list.
6. **Reverse a singly linked list** (the classic interview question). It's the traversal pattern with three pointers: `prev`, `cur`, `next`:
   ```python
   def reverse(head):
       prev = None
       cur = head
       while cur is not None:
           nxt = cur.next     # save the rest before breaking the link
           cur.next = prev    # flip the arrow backward
           prev = cur         # move prev forward
           cur = nxt          # move cur forward
       return prev            # prev is the new head
   ```
   Trace it by hand on `10 → 20 → 30` until you can explain every step.
7. **Convert** a singly linked list into a doubly linked list, then back — reusing the helper functions above.
8. **Challenge:** find the **middle** node using two pointers (a "slow" pointer moving one step and a "fast" pointer moving two). When `fast` reaches the end, `slow` is at the middle. This slow/fast trick also detects cycles — worth learning now.

---

**Previous:** [Part 2 — Arrays (Lists)](01-arrays-lists.md) · **Next:** [Part 4 — Stacks & Queues](03-stacks-and-queues.md)
