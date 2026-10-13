"""
linked_list/doubly_linked_list.py  —  Part 3

A doubly linked list: each node points forward (next) AND backward (prev).
This enables easy backward traversal and O(1) appends via a tail pointer.
"""


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

    # ---- add to the front — O(1) ----
    def prepend(self, data):
        node = DoublyNode(data)
        node.next = self.head
        if self.head is not None:
            self.head.prev = node        # old head points back
        self.head = node
        if self.tail is None:            # first node
            self.tail = node
        self.size += 1

    # ---- add to the end — O(1) thanks to tail ----
    def append(self, data):
        node = DoublyNode(data)
        if self.tail is None:            # empty list
            self.head = self.tail = node
        else:
            node.prev = self.tail        # new node points back
            self.tail.next = node        # old tail points forward
            self.tail = node
        self.size += 1

    # ---- traverse forward ----
    def to_list(self):
        out = []
        cur = self.head
        while cur is not None:
            out.append(cur.data)
            cur = cur.next
        return out

    # ---- traverse backward (a singly list cannot do this) ----
    def to_list_reverse(self):
        out = []
        cur = self.tail
        while cur is not None:
            out.append(cur.data)
            cur = cur.prev
        return out


if __name__ == "__main__":
    d = DoublyLinkedList()
    d.append(10)
    d.append(20)
    d.append(30)
    d.prepend(5)                 # 5 -> 10 -> 20 -> 30

    print("forward :", d.to_list())          # [5, 10, 20, 30]
    print("backward:", d.to_list_reverse())  # [30, 20, 10, 5]
    print("size    :", d.size)
