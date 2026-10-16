"""
linked_list/middle_node.py  —  Part 3 problem

Find the middle node of a linked list using the slow/fast pointer trick.
When the fast pointer reaches the end, the slow pointer is at the middle.
O(n) time, O(1) space.
"""

from singly_linked_list import Node


def build(values):
    head = None
    for v in reversed(values):
        node = Node(v)
        node.next = head
        head = node
    return head


def middle_node(head):
    """Return the middle node (second middle if the length is even)."""
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next              # 1 step
        fast = fast.next.next         # 2 steps
    return slow


def middle_value(head):
    node = middle_node(head)
    return node.data if node else None


if __name__ == "__main__":
    print("odd  [1,2,3,4,5]  ->", middle_value(build([1, 2, 3, 4, 5])))   # 3
    print("even [1,2,3,4]    ->", middle_value(build([1, 2, 3, 4])))      # 3
    print("one  [9]          ->", middle_value(build([9])))                # 9
