"""
stack/stack_linked.py  —  Part 4

A stack (LIFO) built on a linked list. The top is the head, so push and pop
are both O(1) — no walking to the other end.
"""


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
        node.next = self.top         # new node points at the old top
        self.top = node              # it becomes the new top
        self._size += 1

    def pop(self):
        if self.top is None:
            raise IndexError("pop from empty stack")
        value = self.top.data
        self.top = self.top.next     # top slides down one node
        self._size -= 1
        return value

    def peek(self):
        if self.top is None:
            raise IndexError("peek from empty stack")
        return self.top.data

    def is_empty(self):
        return self.top is None

    def size(self):
        return self._size


if __name__ == "__main__":
    s = LinkedStack()
    for ch in "abcd":
        s.push(ch)
    print("peek :", s.peek())    # d
    print("pop  :", s.pop())     # d
    print("pop  :", s.pop())     # c
    print("size :", s.size())    # 2
