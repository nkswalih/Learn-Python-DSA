"""
stack/min_stack.py  —  Part 4 problem (LeetCode 155)

Design a stack that also returns the minimum element in O(1).

Trick: keep a SECOND stack of running minimums. Every push also records
"the smallest value seen so far". All operations stay O(1).
"""


class MinStack:
    def __init__(self):
        self.items = []               # the real stack
        self.mins = []                # running minimum at each level

    def push(self, x):
        self.items.append(x)
        if self.mins:
            self.mins.append(min(x, self.mins[-1]))
        else:
            self.mins.append(x)

    def pop(self):
        if not self.items:
            raise IndexError("pop from empty stack")
        self.mins.pop()
        return self.items.pop()

    def top(self):
        if not self.items:
            raise IndexError("top from empty stack")
        return self.items[-1]

    def get_min(self):
        if not self.mins:
            raise IndexError("min from empty stack")
        return self.mins[-1]

    def is_empty(self):
        return len(self.items) == 0


if __name__ == "__main__":
    s = MinStack()
    s.push(5)
    s.push(3)
    s.push(7)
    print("min   :", s.get_min())   # 3
    s.pop()
    print("top   :", s.top())       # 3
    print("min   :", s.get_min())   # 3
    s.pop()
    print("min   :", s.get_min())   # 5
