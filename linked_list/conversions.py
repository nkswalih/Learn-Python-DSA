"""
linked_list/conversions.py  —  Part 3

Convert between a singly linked list and a doubly linked list.
Both conversions are a single forward walk that fixes up references.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None          # used only once converted to doubly


def build_singly(values):
    """Helper: build a singly linked chain from a list of values."""
    head = None
    for v in reversed(values):
        node = Node(v)
        node.next = head
        head = node
    return head


def to_doubly(head):
    """Singly -> Doubly: set each node's prev to the node before it."""
    prev = None
    cur = head
    while cur is not None:
        cur.prev = prev
        prev = cur
        cur = cur.next
    return head


def to_singly(head):
    """Doubly -> Singly: drop all backward links."""
    cur = head
    while cur is not None:
        cur.prev = None
        cur = cur.next
    return head


def walk_forward(head):
    out = []
    cur = head
    while cur is not None:
        out.append(cur.data)
        cur = cur.next
    return out


def walk_backward(tail):
    out = []
    cur = tail
    while cur is not None:
        out.append(cur.data)
        cur = cur.prev
    return out


if __name__ == "__main__":
    head = build_singly([10, 20, 30])
    print("singly forward :", walk_forward(head))

    head = to_doubly(head)
    last = None
    cur = head
    while cur is not None:
        last = cur
        cur = cur.next
    print("as doubly back :", walk_backward(last))   # [30, 20, 10]

    head = to_singly(head)
    print("back to singly :", walk_forward(head))    # [10, 20, 30]
