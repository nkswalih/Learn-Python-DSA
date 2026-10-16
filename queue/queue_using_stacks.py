"""
queue/queue_using_stacks.py  —  Part 4 problem (LeetCode 232)

Build a FIFO queue using only two stacks.

Trick: an "in" stack receives pushes; when we need to dequeue, we pour the
"in" stack into an "out" stack (which reverses the order). Each element moves
at most once, so every operation is amortized O(1).
"""


class QueueUsingStacks:
    def __init__(self):
        self.stack_in = []            # receives new items
        self.stack_out = []           # serves old items

    def enqueue(self, x):
        self.stack_in.append(x)       # push onto the back

    def dequeue(self):
        if not self.stack_out:
            while self.stack_in:      # reverse into the out stack
                self.stack_out.append(self.stack_in.pop())
        if not self.stack_out:
            raise IndexError("dequeue from empty queue")
        return self.stack_out.pop()

    def peek(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        if not self.stack_out:
            raise IndexError("peek from empty queue")
        return self.stack_out[-1]

    def is_empty(self):
        return not self.stack_in and not self.stack_out


if __name__ == "__main__":
    q = QueueUsingStacks()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print("peek    :", q.peek())     # 1
    print("dequeue :", q.dequeue())  # 1
    print("dequeue :", q.dequeue())  # 2
    q.enqueue(4)
    print("dequeue :", q.dequeue())  # 3
    print("dequeue :", q.dequeue())  # 4
    print("empty?  :", q.is_empty()) # True
