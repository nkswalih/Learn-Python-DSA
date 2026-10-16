"""
recursion/tower_of_hanoi.py  —  Part 7 problem

Move n disks from peg A to peg C using peg B, one disk at a time, never
placing a larger disk on a smaller one.

The recursive insight: to move n disks to the target, first move n-1 out of
the way, move the biggest, then move the n-1 back on top.
Minimum moves = 2^n - 1, so O(2^n) time.
"""


def tower_of_hanoi(n, source, target, auxiliary, moves):
    if n == 1:
        moves.append((source, target))     # base case: one disk, just move it
        return
    tower_of_hanoi(n - 1, source, auxiliary, target, moves)
    moves.append((source, target))         # move the largest disk
    tower_of_hanoi(n - 1, auxiliary, target, source, moves)


if __name__ == "__main__":
    moves = []
    tower_of_hanoi(3, "A", "C", "B", moves)
    print("Move count:", len(moves), "(2^3 - 1 = 7)")
    for i, (src, dst) in enumerate(moves, 1):
        print(f"{i}. {src} -> {dst}")
