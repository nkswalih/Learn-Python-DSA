"""
linked_list/node_basics.py  —  Part 3

Creating and connecting nodes by hand. This is the single best exercise for
understanding linked lists: build a chain manually and walk it.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


if __name__ == "__main__":
    # 1) Create three disconnected nodes.
    a = Node(10)
    b = Node(20)
    c = Node(30)

    # 2) Connect them with next references.
    a.next = b          # 10 -> 20
    b.next = c          # 20 -> 30  (c.next is None, marking the end)

    # 3) Remember the head, then walk the chain.
    head = a
    cur = head
    while cur is not None:
        print(cur.data)          # 10, 20, 30
        cur = cur.next           # move to the next node

    print("---")
    print("head value :", head.data)          # 10
    print("second     :", head.next.data)     # 20
    print("third      :", head.next.next.data)  # 30
