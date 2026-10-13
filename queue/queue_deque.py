"""
queue/queue_deque.py  —  Part 4

The right way to build a queue in Python: collections.deque.
O(1) operations at BOTH ends — works as a queue AND as a stack.
"""

from collections import deque


class DequeQueue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, x):
        self.items.append(x)             # add at the rear — O(1)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.popleft()      # remove from the front — O(1)

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    # --- queue (FIFO) ---
    q = DequeQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print("queue dequeues:", [q.dequeue() for _ in range(3)])   # [1, 2, 3]

    # --- stack (LIFO) using the same deque type ---
    s = deque()
    for x in [1, 2, 3]:
        s.append(x)
    print("stack pops    :", [s.pop() for _ in range(3)])       # [3, 2, 1]
