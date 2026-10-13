"""
queue/queue_list.py  —  Part 4

A queue (FIFO) built on a Python list.

NOTE: this is shown to demonstrate WHY lists make bad queues.
list.pop(0) is O(n) because everything shifts left.
Use collections.deque (queue_deque.py) in real code.
"""


class ListQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, x):
        self.items.append(x)             # add at the rear — O(1)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)         # remove from the front — O(n)! (trap)

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    q = ListQueue()
    q.enqueue("first")
    q.enqueue("second")
    q.enqueue("third")

    print("peek    :", q.peek())      # first
    print("dequeue :", q.dequeue())   # first  (FIFO)
    print("dequeue :", q.dequeue())   # second
    print("size    :", q.size())      # 1
    print()
    print("Reminder: pop(0) is O(n). See queue_deque.py for the fast version.")
