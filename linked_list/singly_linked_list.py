"""
linked_list/singly_linked_list.py  —  Part 3

A basic singly linked list: each node points to the next.
Operations: prepend, append, find, delete, insert_at, reverse, to_list.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    # ---- add to the front — O(1) ----
    def prepend(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.size += 1

    # ---- add to the end — O(n) without a tail pointer ----
    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
        self.size += 1

    # ---- search — O(n) ----
    def find(self, target):
        cur = self.head
        while cur is not None:
            if cur.data == target:
                return True
            cur = cur.next
        return False

    # ---- delete first occurrence of a value — O(n) ----
    def delete(self, target):
        if self.head is None:
            return False
        if self.head.data == target:           # target is the head
            self.head = self.head.next
            self.size -= 1
            return True
        cur = self.head
        while cur.next is not None:
            if cur.next.data == target:
                cur.next = cur.next.next       # jump over the target
                self.size -= 1
                return True
            cur = cur.next
        return False

    # ---- insert at a position — O(n) ----
    def insert_at(self, index, data):
        if index <= 0:                          # insert at the front
            self.prepend(data)
            return
        cur = self.head
        for _ in range(index - 1):
            if cur is None:
                raise IndexError("index out of range")
            cur = cur.next
        if cur is None:
            raise IndexError("index out of range")
        node = Node(data)
        node.next = cur.next
        cur.next = node
        self.size += 1

    # ---- reverse in place — O(n) time, O(1) space ----
    def reverse(self):
        prev = None
        cur = self.head
        while cur is not None:
            nxt = cur.next          # save the rest
            cur.next = prev         # flip the arrow
            prev = cur              # move prev forward
            cur = nxt               # move cur forward
        self.head = prev            # prev is the new head

    # ---- traverse into a Python list ----
    def to_list(self):
        out = []
        cur = self.head
        while cur is not None:
            out.append(cur.data)
            cur = cur.next
        return out


if __name__ == "__main__":
    lst = SinglyLinkedList()
    lst.prepend(30)
    lst.prepend(20)
    lst.prepend(10)              # 10 -> 20 -> 30
    print("after prepends :", lst.to_list())

    lst.append(40)               # 10 -> 20 -> 30 -> 40
    print("after append   :", lst.to_list())

    lst.insert_at(2, 25)         # 10 -> 20 -> 25 -> 30 -> 40
    print("after insert@2 :", lst.to_list())

    lst.delete(20)               # 10 -> 25 -> 30 -> 40
    print("after delete 20:", lst.to_list())

    print("find 30        :", lst.find(30))

    lst.reverse()                # 40 -> 30 -> 25 -> 10
    print("after reverse  :", lst.to_list())
    print("size           :", lst.size)
