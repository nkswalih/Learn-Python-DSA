"""
linked_list/doubly_linked_list.py  —  Part 3

A FULL doubly linked list. Each node has next (forward) and prev (backward).

Operations included:
    prepend, append                 add at front / back          O(1)
    insert_at(index)                add at front / middle / back O(n) to find
    delete_at(index)                remove by position           O(n) to find
    delete_value(value)             remove first matching value  O(n)
    get(index)                      read by index (from nearer end) O(n)
    set_at(index, value)            update by index              O(n)
    search(value)                   index of value, or -1        O(n)
    contains(value)                 membership                   O(n)
    reverse()                       reverse in place              O(n)
    to_list() / to_list_reverse()   traversal both ways          O(n)
    clear()                         empty the list               O(1)
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

    # =========================================================
    #  ADD
    # =========================================================

    def prepend(self, data):
        """Add at the front — O(1)."""
        node = DoublyNode(data)
        node.next = self.head
        if self.head is not None:
            self.head.prev = node
        self.head = node
        if self.tail is None:                 # first node
            self.tail = node
        self.size += 1

    def append(self, data):
        """Add at the back — O(1) thanks to the tail pointer."""
        node = DoublyNode(data)
        if self.tail is None:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1

    def insert_at(self, index, data):
        """
        Insert at any position: front (0), middle, or end (size).
        Walking to the position is O(n); the relinking is O(1).
        """
        if index < 0 or index > self.size:
            raise IndexError("insert_at index out of range")
        if index == 0:
            self.prepend(data)
            return
        if index == self.size:
            self.append(data)
            return

        cur = self.head
        for _ in range(index):                # cur becomes the node at 'index'
            cur = cur.next

        node = DoublyNode(data)
        prev = cur.prev
        node.prev = prev                      # new node points back
        node.next = cur                       # new node points forward
        prev.next = node                      # previous points to new node
        cur.prev = node                       # current points back to new node
        self.size += 1

    # =========================================================
    #  REMOVE
    # =========================================================

    def _remove_node(self, node):
        """Unlink a node from the chain. O(1)."""
        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head = node.next             # node was the head
        if node.next is not None:
            node.next.prev = node.prev
        else:
            self.tail = node.prev             # node was the tail
        self.size -= 1
        return node.data

    def delete_at(self, index):
        """Remove the node at a position. O(n) to find."""
        if index < 0 or index >= self.size:
            raise IndexError("delete_at index out of range")
        node = self._node_at(index)
        return self._remove_node(node)

    def delete_value(self, value):
        """Remove the first node holding value. Returns True if removed. O(n)."""
        cur = self.head
        while cur is not None:
            if cur.data == value:
                self._remove_node(cur)
                return True
            cur = cur.next
        return False

    def pop_front(self):
        """Remove and return the front item. O(1)."""
        if self.head is None:
            raise IndexError("pop_front from empty list")
        return self._remove_node(self.head)

    def pop_back(self):
        """Remove and return the back item. O(1)."""
        if self.tail is None:
            raise IndexError("pop_back from empty list")
        return self._remove_node(self.tail)

    # =========================================================
    #  READ / SEARCH
    # =========================================================

    def _node_at(self, index):
        """Return the node at index, walking from the nearer end."""
        if index < self.size // 2:
            cur = self.head
            for _ in range(index):
                cur = cur.next
        else:
            cur = self.tail
            for _ in range(self.size - 1 - index):
                cur = cur.prev
        return cur

    def get(self, index):
        """Read the value at an index. O(n), but walks from the nearer end."""
        if index < 0 or index >= self.size:
            raise IndexError("get index out of range")
        return self._node_at(index).data

    def set_at(self, index, value):
        """Update the value at an index. O(n)."""
        if index < 0 or index >= self.size:
            raise IndexError("set_at index out of range")
        self._node_at(index).data = value

    def search(self, value):
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
        """True if value is in the list. O(n)."""
        return self.search(value) != -1

    # =========================================================
    #  OTHER OPERATIONS
    # =========================================================

    def reverse(self):
        """Reverse in place by swapping each node's next/prev. O(n)."""
        cur = self.head
        while cur is not None:
            cur.next, cur.prev = cur.prev, cur.next   # swap the two links
            cur = cur.prev                            # move forward (was next)
        self.head, self.tail = self.tail, self.head   # swap the ends

    def to_list(self):
        """Forward traversal -> Python list."""
        out = []
        cur = self.head
        while cur is not None:
            out.append(cur.data)
            cur = cur.next
        return out

    def to_list_reverse(self):
        """Backward traversal -> Python list. (A singly list can't do this.)"""
        out = []
        cur = self.tail
        while cur is not None:
            out.append(cur.data)
            cur = cur.prev
        return out

    def clear(self):
        """Empty the list. O(1) (Python reclaims the nodes)."""
        self.head = self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def __repr__(self):
        return " <-> ".join(str(x) for x in self.to_list())


if __name__ == "__main__":
    d = DoublyLinkedList()
    for v in [10, 20, 30]:
        d.append(v)                       # 10 <-> 20 <-> 30
    d.prepend(5)                          # 5 <-> 10 <-> 20 <-> 30
    print("after adds      :", d)

    d.insert_at(0, 1)                     # front
    d.insert_at(2, 7)                     # middle (between 5 and 10)
    d.insert_at(len(d), 99)               # end
    print("after insert_at :", d)

    print("get(3)          :", d.get(3))       # 10
    print("search 20       :", d.search(20))
    print("contains 99     :", d.contains(99))

    d.set_at(0, 100)                      # change front
    print("after set_at    :", d)

    print("pop_front       :", d.pop_front())
    print("pop_back        :", d.pop_back())
    print("after pops      :", d)

    print("delete_at(1)    :", d.delete_at(1))
    print("delete 99?      :", d.delete_value(99))
    print("after deletes   :", d)

    d.reverse()
    print("reversed        :", d)
    print("backward view   :", d.to_list_reverse())
    print("length          :", len(d))

    d.clear()
    print("cleared         :", d, "| len =", len(d))
