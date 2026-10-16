"""
stack/postfix_evaluation.py  —  Part 4 problem (LeetCode 150)

Evaluate a Reverse Polish Notation (postfix) expression, e.g. "2 3 +".
In postfix, the operator comes AFTER its two operands.

Stack rule:
    number  -> push it
    operator-> pop two, apply, push the result
O(n) time.
"""


def eval_rpn(tokens):
    stack = []
    ops = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: int(a / b),   # truncate toward zero (LeetCode rule)
    }
    for tok in tokens:
        if tok in ops:
            b = stack.pop()             # second operand
            a = stack.pop()             # first operand
            stack.append(ops[tok](a, b))
        else:
            stack.append(int(tok))
    return stack[0]


if __name__ == "__main__":
    print(eval_rpn(["2", "1", "+", "3", "*"]))            # (2+1)*3 = 9
    print(eval_rpn(["4", "13", "5", "/", "+"]))           # 4 + (13/5) = 6
    print(eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
