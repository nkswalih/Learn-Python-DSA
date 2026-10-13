# Searching & Sorting — Complexity Table

Keep this handy for revision.

| Algorithm | Best | Average | Worst | Space | Stable? | Notes |
|---|---|---|---|---|---|---|
| Linear search | O(1) | O(n) | O(n) | O(1) | — | Works on any list |
| Binary search | O(1) | O(log n) | O(log n) | O(1) | — | **Requires sorted data** |
| Bubble sort | O(n) | O(n²) | O(n²) | O(1) | Yes | Early-exit gives O(n) best case |
| Selection sort | O(n²) | O(n²) | O(n²) | O(1) | No | Always n²; few swaps |
| Insertion sort | O(n) | O(n²) | O(n²) | O(1) | Yes | Fast on nearly-sorted data |
| Python `sorted`/`.sort` | O(n) | O(n log n) | O(n log n) | O(n) | Yes | Timsort — use this in real code |

## Reading it

- **Best case:** the friendliest possible input.
- **Average case:** a typical random input.
- **Worst case:** the meanest input. Interviews expect this unless stated otherwise.
- **Stable:** equal items keep their original relative order.

## Scale intuition

A modern machine does on the order of 10^8 simple operations per second.

| n | O(n log n) | O(n²) |
|---:|---:|---:|
| 1,000 | ~10,000 ops (instant) | 1,000,000 ops (instant) |
| 100,000 | ~1.7 million ops (instant) | 10 billion ops (~100 s — too slow) |
| 1,000,000 | ~20 million ops (fast) | 10^12 ops (hours — impossible) |

**Conclusion:** never use O(n²) sorting on large data. Use `sorted()`/`.sort()`.
