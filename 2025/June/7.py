"""
You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each False boolean represents a tile you can walk on.
Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.
"""


def solution(
    G: list[list[bool]], start: tuple[int, int], end: tuple[int, int]
) -> int | None:
    q = [(start[0], start[1], 0)]
    M, N = len(G), len(G[0])

    while len(q) > 0:
        x, y, steps = q.pop(0)
        if (x, y) == end:
            return steps

        adjs = [
            (x, y)
            for x, y in [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]
            if 0 <= x < M and 0 <= y < N
        ]

        for x, y in adjs:
            if not G[x][y]:
                continue

            G[x][y] = False
            q.append((x, y, steps + 1))

    return None


if __name__ == "__main__":
    # Test case 1
    grid1 = [[True, True, True], [True, False, True], [True, False, True]]
    assert solution(grid1, (0, 0), (2, 2)) == 4

    grid2 = [[False, True, False], [True, True, True], [False, True, False]]
    assert solution(grid2, (0, 0), (2, 2)) is None

    grid3 = [[True, True, True]]
    assert solution(grid3, (0, 0), (0, 2)) == 2

    print("All test cases passed!")
