"""
linked_list/remove_nth_from_end.py  —  Part 3 problem (LeetCode 19)

Remove the n-th node from the end of a linked list in ONE pass.

Trick: keep two pointers n+1 apart. When the fast one reaches the end,
the slow one is right before the node to delete. A dummy node handles
deleting the head cleanly. O(n) time, O(1) space.
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


def remove_nth_from_end(head, n):
    dummy = Node(0)
    dummy.next = head
    fast = slow = dummy
    for _ in range(n + 1):            # move fast n+1 ahead of slow
        fast = fast.next
    while fast is not None:           # move both until fast falls off
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next        # slow is just before the target
    return dummy.next


if __name__ == "__main__":
    head = build([1, 2, 3, 4, 5])
    print("before      :", to_list(head))
    print("remove 2nd  :", to_list(remove_nth_from_end(head, 2)))   # [1,2,3,5]
    head = build([1, 2, 3, 4, 5])
    print("remove last :", to_list(remove_nth_from_end(head, 5)))   # [2,3,4,5]
