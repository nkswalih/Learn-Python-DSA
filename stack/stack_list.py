"""
stack/stack_list.py  —  Part 4

A stack (LIFO) built on a Python list.
Rule: only ever touch the END of the list (append / pop), else operations
become O(n).
"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)                 # add to the end — O(1)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()              # remove from the end — O(1)

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]                # look at the top — O(1)

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


def is_valid_parentheses(s):
    """The classic stack problem (LeetCode 20)."""
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        else:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return len(stack) == 0


if __name__ == "__main__":
    s = Stack()
    s.push("a")
    s.push("b")
    s.push("c")
    print("peek    :", s.peek())     # c
    print("pop     :", s.pop())      # c
    print("pop     :", s.pop())      # b
    print("size    :", s.size())     # 1
    print("empty?  :", s.is_empty()) # False

    print()
    print("valid parens '( [ { } ] )':", is_valid_parentheses("([{}])"))
    print("valid parens '( [ ) ]'    :", is_valid_parentheses("([)]"))
