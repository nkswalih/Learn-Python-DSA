"""
linked_list/merge_two_lists.py  —  Part 3 problem (LeetCode 21)

Merge two sorted linked lists into one sorted list.
Uses a dummy node so we never special-case an empty result.
O(n + m) time, O(1) extra space.
"""

from singly_linked_list import Node


def build(values):
    head = None
    for v in reversed(values):
        node = Node(v)
        node.next = head
        head = node
    return head


def to_list(head):
    out = []
    while head is not None:
        out.append(head.data)
        head = head.next
    return out


def merge_two_lists(l1, l2):
    dummy = Node(0)              # sentinel: avoids "empty list?" branches
    tail = dummy
    while l1 is not None and l2 is not None:
        if l1.data <= l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 if l1 is not None else l2   # attach the leftovers
    return dummy.next


if __name__ == "__main__":
    a = build([1, 3, 5, 7])
    b = build([2, 4, 6, 8])
    print("a     :", to_list(a))
    print("b     :", to_list(b))
    print("merged:", to_list(merge_two_lists(a, b)))   # [1..8]
