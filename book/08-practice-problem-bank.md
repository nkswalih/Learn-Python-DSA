# Part 9 — The Practice Problem Bank

*Every topic, real interview-style problems, ordered from warm-up to challenge. Each entry gives you the **prompt**, a **hint**, the **approach**, the **cost**, and **where the working code lives** in the repo. Try the problem before you read the approach — the struggle is where the learning happens.*

**How to use this:** pick a topic you just read, do the problems top to bottom, then run the matching file to compare. The **Challenge** items at the end of each topic have no code — they're yours to solve.

---

## 9.1 Arrays (lists) — the `arrays/` folder

### A1. Two Sum
**Prompt:** Given a list and a target, return the indices of two numbers that add to the target.
**Hint:** You're searching for `target - x`. Make that search instant.
**Approach:** Walk once, storing each value → index in a dict. Before storing `x`, check if `target - x` is already seen.
**Cost:** `O(n)` time, `O(n)` space. **Code:** `arrays/two_sum.py`

### A2. Remove Duplicates from a Sorted Array
**Prompt:** In place, remove duplicates so each value appears once; return the new length.
**Hint:** The list is already sorted — equal values are neighbours. Use one pointer to "write".
**Approach:** `write` marks the end of the unique part; `read` scans. When `nums[read] != nums[write-1]`, copy it forward.
**Cost:** `O(n)` time, `O(1)` space. **Code:** `arrays/remove_duplicates.py`

### A3. Merge Sorted Array
**Prompt:** Merge two sorted lists into one sorted list.
**Hint:** Compare the current fronts; take the smaller.
**Approach:** Two pointers, one per list; append the smaller each step; attach the leftovers.
**Cost:** `O(n + m)` time. **Code:** `arrays/merge_sorted_array.py`

### A4. Rotate Array
**Prompt:** Rotate the list right by `k` steps, in place.
**Hint:** Reversing is your friend.
**Approach:** Reverse the whole list, then reverse the first `k`, then reverse the rest.
**Cost:** `O(n)` time, `O(1)` space. **Code:** `arrays/rotate_array.py`

### A5. Move Zeroes
**Prompt:** Move all zeroes to the end, keeping non-zero order, in place.
**Hint:** Keep a "next write" position.
**Approach:** `write` points where the next non-zero goes; swap it into place as `read` scans.
**Cost:** `O(n)` time, `O(1)` space. **Code:** `arrays/move_zeroes.py`

### A6. Maximum Subarray (Kadane's Algorithm)
**Prompt:** Find the largest sum of any contiguous subarray.
**Hint:** At each step, do you extend the run or restart?
**Approach:** `current = max(x, current + x)`; track the best seen.
**Cost:** `O(n)` time, `O(1)` space. **Code:** `arrays/max_subarray.py`

### A7. Product of Array Except Self
**Prompt:** Each index gets the product of every other element — no division, in `O(n)`.
**Hint:** Two passes: products to the left, then products to the right.
**Approach:** A forward pass fills left-products; a backward pass multiplies in right-products.
**Cost:** `O(n)` time, `O(n)` space (the output). **Code:** `arrays/product_except_self.py`

### A8. Majority Element (Boyer-Moore Voting)
**Prompt:** Find the value that appears more than `n/2` times.
**Hint:** Cancellation — different votes cancel, matching votes reinforce.
**Approach:** Keep a `candidate` and a `count`; on `count == 0` adopt a new candidate.
**Cost:** `O(n)` time, `O(1)` space. **Code:** `arrays/majority_element.py`

### A9. Range Sum Query
**Prompt:** Answer "sum of `nums[lo..hi]`" many times, fast.
**Hint:** Precompute cumulative sums once.
**Approach:** `prefix[i] = sum of first i`; then `sum(lo..hi) = prefix[hi+1] - prefix[lo]`.
**Cost:** `O(n)` setup, `O(1)` per query. **Code:** `arrays/prefix_sums.py`

**Challenges (no code):** Best Time to Buy & Sell Stock · Container With Most Water · 3Sum · Sort Colors (Dutch flag)

---

## 9.2 Linked lists — the `linked_list/` folder

### L1. Reverse a Linked List
**Prompt:** Reverse the chain, return the new head.
**Hint:** Three pointers: `prev`, `cur`, `next`.
**Approach:** Save `next`, flip `cur.next` to `prev`, advance both.
**Cost:** `O(n)` time, `O(1)` space. **Code:** `linked_list/singly_linked_list.py` (`reverse`)

### L2. Middle of the Linked List
**Prompt:** Return the middle node.
**Hint:** A pointer moving twice as fast finishes in half the time.
**Approach:** `slow` moves 1, `fast` moves 2; when `fast` ends, `slow` is the middle.
**Cost:** `O(n)` time, `O(1)` space. **Code:** `linked_list/middle_node.py`

### L3. Detect a Cycle (and its start)
**Prompt:** Does the list loop? If so, where does the loop begin?
**Hint:** Floyd's tortoise and hare.
**Approach:** If slow and fast meet, there's a cycle. Reset one to the head and step both by 1 — they meet at the start.
**Cost:** `O(n)` time, `O(1)` space. **Code:** `linked_list/detect_cycle.py`

### L4. Merge Two Sorted Lists
**Prompt:** Splice two sorted lists into one sorted list.
**Hint:** A dummy node removes the "empty result" edge case.
**Approach:** Dummy + tail; pick the smaller front each step; attach leftovers.
**Cost:** `O(n + m)` time, `O(1)` space. **Code:** `linked_list/merge_two_lists.py`

### L5. Remove the N-th Node From the End
**Prompt:** Remove the n-th node from the end in **one** pass.
**Hint:** Keep two pointers `n + 1` apart.
**Approach:** Advance `fast` by `n + 1`, then move both until `fast` falls off; `slow` is just before the target.
**Cost:** `O(n)` time, `O(1)` space. **Code:** `linked_list/remove_nth_from_end.py`

### L6. Full Doubly Linked List
**Prompt:** Implement insert-at-index (front, middle, back), delete by index/value, get/set, search, reverse.
**Hint:** Four links to update on a middle insert; use `prev` to delete in `O(1)` given the node.
**Approach:** See the chapter. Keep a `tail` for `O(1)` appends and walk from the nearer end.
**Cost:** end ops `O(1)`; index ops `O(n)`. **Code:** `linked_list/doubly_linked_list.py`

**Challenges (no code):** Palindrome Linked List · Reorder List · Add Two Numbers · Flatten a Multilevel List · LRU Cache (dict + doubly linked list)

---

## 9.3 Stacks & Queues — the `stack/` and `queue/` folders

### S1. Valid Parentheses
**Prompt:** Are `()[]{}` balanced and correctly nested?
**Hint:** The most recent opener must match the next closer.
**Approach:** Push openers; on a closer, pop and check the pair.
**Cost:** `O(n)` time, `O(n)` space. **Code:** `stack/stack_list.py` (see chapter examples)

### S2. Min Stack
**Prompt:** A stack that also returns its minimum in `O(1)`.
**Hint:** A second stack of "smallest so far".
**Approach:** Every push also records the running minimum.
**Cost:** all ops `O(1)`. **Code:** `stack/min_stack.py`

### S3. Evaluate Postfix (RPN)
**Prompt:** Evaluate `["2","1","+","3","*"]` → `9`.
**Hint:** Operators come after their operands.
**Approach:** Numbers push; an operator pops two, applies, pushes the result.
**Cost:** `O(n)` time. **Code:** `stack/postfix_evaluation.py`

### S4. Sort a Stack
**Prompt:** Sort a stack using only stack operations.
**Hint:** Use a second stack as "sorted so far".
**Approach:** Pop `value`; move larger items back temporarily; place `value` in order.
**Cost:** `O(n²)` time, `O(n)` space. **Code:** `stack/sort_stack.py`

### Q1. Queue Using Two Stacks
**Prompt:** Build a FIFO queue from two LIFO stacks.
**Hint:** Pour one stack into the other to reverse order.
**Approach:** `in` stack receives; `out` stack serves; pour when empty.
**Cost:** amortized `O(1)`. **Code:** `queue/queue_using_stacks.py`

### Q2. Sliding Window Maximum
**Prompt:** For every window of size `k`, report the max.
**Hint:** A deque of candidate indices in decreasing value order.
**Approach:** Drop out-of-window indices from the front; drop smaller values from the back; front is the max.
**Cost:** `O(n)` time. **Code:** `queue/sliding_window_max.py`

**Challenges (no code):** Next Greater Element (monotonic stack) · Daily Temperatures · Implement Stack Using Queues · Largest Rectangle in Histogram

---

## 9.4 Searching & Sorting — the `search_sort/` folder

### B1. Binary Search
**Prompt:** Find a target's index in a sorted list.
**Hint:** `while low <= high`, then `mid ± 1`.
**Approach:** Halve the range each step.
**Cost:** `O(log n)` time. **Code:** `search_sort/binary_search.py`

### B2. First & Last Position of a Target
**Prompt:** Return `[first, last]` index of a target in sorted (possibly repeated) data.
**Hint:** Binary search twice, keeping searching one side on a hit.
**Approach:** One search squeezes left, one squeezes right.
**Cost:** `O(log n)` time. **Code:** `search_sort/first_last_position.py`

### B3. Search in a Rotated Sorted Array
**Prompt:** Sorted then rotated; find the target in `O(log n)`.
**Hint:** At any `mid`, one half is still sorted.
**Approach:** Identify the sorted half; check if the target lies in it; discard the other.
**Cost:** `O(log n)` time. **Code:** `search_sort/search_rotated.py`

### B4. Merge Sort
**Prompt:** Sort by divide and conquer.
**Hint:** Sort halves, then merge two sorted runs.
**Approach:** Recurse on halves; linear merge.
**Cost:** `O(n log n)` always, `O(n)` space. **Code:** `search_sort/merge_sort.py`

### B5. Quick Sort
**Prompt:** Sort by partitioning around a pivot.
**Hint:** Everything smaller left, larger right, then recurse.
**Approach:** Lomuto partition with a middle pivot (avoids the sorted-input worst case).
**Cost:** average `O(n log n)`, worst `O(n²)`. **Code:** `search_sort/quick_sort.py`

### B6. The `O(n²)` Sorts
**Prompt:** Implement bubble, selection, and insertion sort.
**Hint:** Insertion sort is the fast one on nearly-sorted data.
**Approach:** See files.
**Cost:** `O(n²)` (best `O(n)` for bubble/insertion). **Code:** `bubble_sort.py`, `selection_sort.py`, `insertion_sort.py`, `compare_runtime.py`

**Challenges (no code):** Find Peak Element · K-th Largest Element · Count Inversions · Sort Colors · Median of Two Sorted Arrays

---

## 9.5 Hashing, Sets & Dicts — the `hashing/` folder

### H1. Character Frequency
**Prompt:** Count each character in a string.
**Hint:** `freq.get(ch, 0) + 1`.
**Approach:** One pass with a dict.
**Cost:** `O(n)` time. **Code:** `hashing/hash_utils.py`

### H2. First Non-Repeating Character
**Prompt:** Find the first character that appears once.
**Hint:** Count first, then scan in order.
**Approach:** `Counter`, then first char with count 1.
**Cost:** `O(n)` time. **Code:** `hashing/first_non_repeating.py`

### H3. Contains Duplicate
**Prompt:** Any value repeated?
**Hint:** A set forgets duplicates.
**Approach:** `len(set(x)) < len(x)`.
**Cost:** `O(n)` time. **Code:** `hashing/hash_utils.py`

### H4. Group Anagrams
**Prompt:** Group words that are anagrams.
**Hint:** Anagrams share a sorted signature.
**Approach:** Dict keyed by `"".join(sorted(word))`.
**Cost:** `O(n · k log k)`. **Code:** `hashing/group_anagrams.py`

### H5. Subarray Sum Equals K
**Prompt:** Count contiguous subarrays summing to `k`.
**Hint:** Running sum + how often each prefix sum was seen.
**Approach:** If `running - k` was seen, those subarrays count.
**Cost:** `O(n)` time, `O(n)` space. **Code:** `hashing/subarray_sum_k.py`

### H6. Longest Consecutive Sequence
**Prompt:** Length of the longest run of consecutive integers.
**Hint:** Only start counting where `n - 1` is absent.
**Approach:** Set + walk runs from their start.
**Cost:** `O(n)` time. **Code:** `hashing/longest_consecutive.py`

**Challenges (no code):** Top K Frequent Elements · Isomorphic Strings · Word Pattern · LRU Cache · Substring Without Repeating Characters (sliding window)

---

## 9.6 Recursion — the `recursion/` folder

### R1. Factorial
**Prompt:** `n! = n × (n-1)!`, with `0! = 1`.
**Hint:** Base case first.
**Approach:** Direct recursion.
**Cost:** `O(n)` time, `O(n)` stack. **Code:** `recursion/factorial.py`

### R2. Fibonacci (memoized)
**Prompt:** The n-th Fibonacci number, fast.
**Hint:** Naive recursion repeats itself — cache it.
**Approach:** `lru_cache`/dict memo turns `O(2ⁿ)` into `O(n)`.
**Cost:** `O(n)`. **Code:** `recursion/fibonacci.py`

### R3. Palindrome Check
**Prompt:** Is a string a palindrome?
**Hint:** First char vs last char, then recurse inward.
**Approach:** Compare ends, recurse on the slice.
**Cost:** `O(n)`. **Code:** `recursion/palindrome.py`

### R4. Reverse a String (recursively)
**Prompt:** Reverse a string with recursion.
**Hint:** Last char first.
**Approach:** `s[-1] + reverse(s[:-1])`.
**Cost:** `O(n²)` naively; `O(n)` with a helper index. **Code:** `recursion/reverse_string.py`

### R5. Tower of Hanoi
**Prompt:** Move `n` disks between pegs, never larger on smaller.
**Hint:** Move `n-1` aside, move the biggest, move them back.
**Approach:** Classic 3-step recursion.
**Cost:** `O(2ⁿ)`. **Code:** `recursion/tower_of_hanoi.py`

### R6. Sum of Digits
**Prompt:** Add all digits of a number.
**Hint:** Last digit plus the rest.
**Approach:** `n % 10 + sum_digits(n // 10)`.
**Cost:** `O(d)`. **Code:** `recursion/sum_digits.py`

### R7. Fast Power
**Prompt:** Compute `base^exp` in `O(log exp)`.
**Hint:** `x^n = x^(n/2) · x^(n/2)`.
**Approach:** Halve the exponent each recursion.
**Cost:** `O(log n)`. **Code:** `recursion/power.py`

### R8. Generate Subsets (Power Set)
**Prompt:** List every subset of a list.
**Hint:** Each element is in or out — branch twice.
**Approach:** Backtracking with an explicit undo.
**Cost:** `O(2ⁿ)`. **Code:** `recursion/generate_subsets.py`

**Challenges (no code):** Permutations · Combinations · Generate Parentheses · Climbing Stairs · N-Queens · Word Search

---

## 9.7 The pattern map — which problem uses which trick

| If the problem says… | Reach for… | Topic |
|---|---|---|
| "two numbers add to…" | hash map (complement) | Hashing |
| "duplicate? / seen before?" | set | Hashing |
| "count of each…" | dict / `Counter` | Hashing |
| "contiguous subarray sums to…" | prefix sum + dict | Hashing |
| "sorted, find in log time" | binary search | Searching |
| "rotate / reverse in place" | two pointers / reversal | Arrays |
| "longest / smallest window" | sliding window | Arrays |
| "balanced brackets / nesting / undo" | stack | Stacks |
| "levels / BFS / fairness" | queue | Queues |
| "next greater / span" | monotonic stack | Stacks |
| "best window / running max" | deque | Queues |
| "linked chain / pointers" | linked list, slow/fast | Linked lists |
| "sorted lists, merge" | two pointers + dummy node | Linked lists |
| "try all combinations" | backtracking (recursion) | Recursion |
| "big repeats / overlapping subproblems" | memoization | Recursion |

---

## 9.8 How to grind these properly

1. **Read the prompt. Don't look at the approach yet.** Attempt it for 15 minutes.
2. If stuck, read only the **Hint**. Try again.
3. Still stuck? Read the **Approach**, then close the page and code it from memory.
4. **Run the matching file** and compare — but only after you've written your own.
5. Come back in 3 days and redo it cold. That's the real test.

Consistency beats intensity: **2–3 problems a day** with full understanding is worth more than 20 skimmed.

---

**Previous:** [Part 8 — Last-Minute Interview Revision](07-interview-revision-cheatsheet.md) · **Back to:** [Book index](README.md)
