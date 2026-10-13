"""
queue/circular_queue.py  —  Part 4

A fixed-size circular queue (ring buffer). When front/rear reach the end,
they wrap back to index 0 using the modulo operator, so no slots are wasted.
"""


class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.front = 0        # index of the next item OUT
        self.rear = 0         # index where the next item goes IN
        self.count = 0        # needed to tell "full" from "empty"

    def enqueue(self, x):
        if self.is_full():
            raise OverflowError("queue is full")
        self.data[self.rear] = x
        self.rear = (self.rear + 1) % self.capacity   # wrap around
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("queue is empty")
        value = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self.capacity  # wrap around
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


if __name__ == "__main__":
    q = CircularQueue(3)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print("full?          :", q.is_full())      # True
    print("dequeue        :", q.dequeue())       # 1
    q.enqueue(4)                                  # reuses the freed slot
    print("dequeue        :", q.dequeue())       # 2
    print("dequeue        :", q.dequeue())       # 3
    print("dequeue        :", q.dequeue())       # 4
    print("empty?         :", q.is_empty())      # True
