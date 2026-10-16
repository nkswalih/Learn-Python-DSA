"""
linked_list/detect_cycle.py  —  Part 3 problem (LeetCode 141 / 142)

Detect a cycle with Floyd's "tortoise and hare": a slow pointer (1 step) and
a fast pointer (2 steps). If there is a cycle they must eventually meet.
Also find WHERE the cycle starts. O(n) time, O(1) space.
"""

from singly_linked_list import Node


def build(values):
    head = None
    for v in reversed(values):
        node = Node(v)
        node.next = head
        head = node
    return head


def has_cycle(head):
    """True if the list contains a cycle."""
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


def cycle_start(head):
    """Return the node where the cycle begins, or None if there is no cycle."""
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            # Phase 2: reset one pointer to head; both move 1 step now.
            slow = head
            while slow is not fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None


if __name__ == "__main__":
    # no cycle
    a = build([1, 2, 3, 4])
    print("no cycle      :", has_cycle(a))            # False

    # make a cycle: 1 -> 2 -> 3 -> 4 -> back to node 2
    a = build([1, 2, 3, 4])
    tail = a
    while tail.next is not None:
        tail = tail.next
    tail.next = a.next                                  # 4 -> 2 (cycle)

    print("has cycle     :", has_cycle(a))            # True
    start = cycle_start(a)
    print("cycle starts at:", start.data if start else None)   # 2
