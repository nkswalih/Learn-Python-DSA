"""
linked_list/singly_linked_list.py  —  Part 3

A FULL singly linked list. Each node points only forward (next).

Operations included:
    prepend, append                 add at front / back          O(1) / O(n)
    insert_at(index)                add at front / middle / back O(n)
    delete_at(index)                remove by position           O(n)
    delete_value(value)             remove first matching value  O(n)
    get(index) / set_at(index)      read / update by index       O(n)
    index_of(value) / contains      search                       O(n)
    pop_front / pop_back            remove ends                  O(1) / O(n)
    reverse()                       reverse in place              O(n)
    to_list, clear, __len__         helpers                      O(n) / O(1)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    # =========================================================
    #  ADD
    # =========================================================

    def prepend(self, data):
        """Add at the front — O(1)."""
        node = Node(data)
        node.next = self.head
        self.head = node
        self.size += 1

    def append(self, data):
        """Add at the back — O(n) (no tail pointer in a singly list)."""
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
        self.size += 1

    def insert_at(self, index, data):
        """Insert at any position: front (0), middle, or end (size). O(n)."""
        if index < 0 or index > self.size:
            raise IndexError("insert_at index out of range")
        if index == 0:
            self.prepend(data)
            return
        cur = self.head
        for _ in range(index - 1):            # stop at the node BEFORE the gap
            cur = cur.next
        node = Node(data)
        node.next = cur.next
        cur.next = node
        self.size += 1

    # =========================================================
    #  REMOVE
    # =========================================================

    def delete_value(self, value):
        """Remove the first node holding value. O(n)."""
        if self.head is None:
            return False
        if self.head.data == value:
            self.head = self.head.next
            self.size -= 1
            return True
        cur = self.head
        while cur.next is not None:
            if cur.next.data == value:
                cur.next = cur.next.next      # jump over the target
                self.size -= 1
                return True
            cur = cur.next
        return False

    def delete_at(self, index):
        """Remove the node at a position. O(n)."""
        if index < 0 or index >= self.size:
            raise IndexError("delete_at index out of range")
        if index == 0:
            return self.pop_front()
        cur = self.head
        for _ in range(index - 1):            # node before the target
            cur = cur.next
        removed = cur.next.data
        cur.next = cur.next.next
        self.size -= 1
        return removed

    def pop_front(self):
        """Remove and return the front item. O(1)."""
        if self.head is None:
            raise IndexError("pop_front from empty list")
        value = self.head.data
        self.head = self.head.next
        self.size -= 1
        return value

    def pop_back(self):
        """Remove and return the back item. O(n) — must walk to the end."""
        if self.head is None:
            raise IndexError("pop_back from empty list")
        if self.head.next is None:            # only one node
            value = self.head.data
            self.head = None
            self.size -= 1
            return value
        cur = self.head
        while cur.next.next is not None:      # stop at the second-to-last node
            cur = cur.next
        value = cur.next.data
        cur.next = None
        self.size -= 1
        return value

    # =========================================================
    #  READ / SEARCH
    # =========================================================

    def get(self, index):
        """Read the value at an index. O(n)."""
        if index < 0 or index >= self.size:
            raise IndexError("get index out of range")
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur.data

    def set_at(self, index, value):
        """Update the value at an index. O(n)."""
        if index < 0 or index >= self.size:
            raise IndexError("set_at index out of range")
        cur = self.head
        for _ in range(index):
            cur = cur.next
        cur.data = value

    def index_of(self, value):
        """Return the index of the first matching value, or -1. O(n)."""
        cur = self.head
        i = 0
        while cur is not None:
            if cur.data == value:
                return i
            cur = cur.next
            i += 1
        return -1

    def contains(self, value):
        """True if value is present. O(n)."""
        return self.index_of(value) != -1

    # =========================================================
    #  OTHER OPERATIONS
    # =========================================================

    def reverse(self):
        """Reverse in place with three pointers. O(n) time, O(1) space."""
        prev = None
        cur = self.head
        while cur is not None:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def to_list(self):
        out = []
        cur = self.head
        while cur is not None:
            out.append(cur.data)
            cur = cur.next
        return out

    def clear(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def __repr__(self):
        return " -> ".join(str(x) for x in self.to_list())


if __name__ == "__main__":
    lst = SinglyLinkedList()
    for v in [10, 20, 30]:
        lst.append(v)
    lst.prepend(5)                        # 5 -> 10 -> 20 -> 30
    print("after adds    :", lst)

    lst.insert_at(0, 1)                   # front
    lst.insert_at(2, 7)                   # middle
    lst.insert_at(len(lst), 99)           # end
    print("after inserts :", lst)

    print("get(2)        :", lst.get(2))
    print("index_of(20)  :", lst.index_of(20))
    lst.set_at(0, 100)
    print("after set_at  :", lst)

    print("pop_front     :", lst.pop_front())
    print("pop_back      :", lst.pop_back())
    print("after pops    :", lst)

    print("delete_at(1)  :", lst.delete_at(1))
    print("delete 99?    :", lst.delete_value(99))
    print("after deletes :", lst)

    lst.reverse()
    print("reversed      :", lst)
    print("length        :", len(lst))
