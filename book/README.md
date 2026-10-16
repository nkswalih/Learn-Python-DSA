# DSA From Scratch
### A beginner's guide to Data Structures & Algorithms in Python

> This book assumes you can write a `for` loop and a function — and almost nothing else.
> If you've never solved a DSA problem before, you are exactly who this is for.
> We build every idea from the ground up, with pictures, runnable code, and zero hand-waving.

---

## Who this is for

You, if any of these sound like you:

- "I can write basic Python but freeze when I see a 'find the duplicate' problem."
- "I've heard terms like Big O, hash map, and recursion but they don't really click."
- "I keep copying solutions I don't understand and forgetting them a day later."

You do **not** need advanced math. You do **not** need to have finished a computer science degree. You need patience and the willingness to type code and run it.

---

## How to read this book (please actually do these)

A mentor's warning: **reading this like a novel will not work.** DSA is a skill, like swimming. Watching someone swim is not swimming.

1. **Type every code block yourself.** Do not copy-paste. Your fingers learning the syntax matters.
2. **Run it.** Change the numbers. Break it on purpose. Watch what happens. Code you haven't run is code you don't understand.
3. **Do the tasks at the end of each chapter before moving on.** They are short, and they are the real lesson.
4. **When stuck, sit with it for 15 minutes before looking anything up.** That discomfort is literally your brain building the skill.
5. **Explain it out loud to an empty chair when you finish a chapter.** Wherever your explanation gets vague is exactly where you don't understand yet.

---

## The map

Read in order the first time. After that, jump to whatever you need.

| Chapter | What you'll learn | You'll be able to... |
|---|---|---|
| [Part 1 — Core Concepts & Big O](00-core-concepts-and-big-o.md) | What DSA is, Python's built-in structures, and how to measure code speed | Reason about how fast your code is |
| [Part 2 — Arrays (Lists)](01-arrays-lists.md) | Python lists as dynamic arrays, inserting, deleting, slicing, copying | Manipulate lists like a pro and know their costs |
| [Part 3 — Linked Lists](02-linked-lists.md) | Nodes, pointers, singly vs doubly linked lists | Build and traverse a linked list from scratch |
| [Part 4 — Stacks & Queues](03-stacks-and-queues.md) | LIFO and FIFO, circular queues, `deque` | Pick the right structure for order-sensitive problems |
| [Part 5 — Searching & Sorting](04-searching-and-sorting.md) | Linear & binary search, bubble/selection/insertion sort | Search and sort data and compare the trade-offs |
| [Part 6 — Hashing, Sets & Dicts](05-hashing-sets-and-dicts.md) | Hash tables, collisions, frequency counting | Turn slow O(n²) code into fast O(n) code |
| [Part 7 — Recursion & Problem Solving](06-recursion-and-problem-solving.md) | Recursion, the call stack, and how to think through problems | Solve problems you've never seen before |
| [Part 8 — Last-Minute Interview Revision](07-interview-revision-cheatsheet.md) | Everything compressed: cost tables, tricks, patterns, 60 Q&A | Revise the whole book fast before an interview |
| [Part 9 — Practice Problem Bank](08-practice-problem-bank.md) | Every topic, real interview problems with hints, approaches, and challenges | Drill any topic from warm-up to challenge |

---

## How to run the code

You only need Python installed (version 3.8 or newer; any recent version is fine).

```bash
# Run a file
python myprogram.py

# Or open an interactive Python shell (great for quick experiments)
python
>>> 2 + 3
5
```

Every chapter has matching runnable code in the **repo folders** (see the main project `README.md`). Read a chapter, then open its folder and run the files.

---

## A note on tone

This book explains *why* before *how*, and *how* before *code*. It will not pad pages with filler. If a sentence isn't helping you understand or helping you do, it doesn't belong here.

Let's begin.
