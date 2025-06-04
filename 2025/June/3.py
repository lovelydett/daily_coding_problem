"""
Coloring N houses:
A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.
Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.
"""

from typing import List


def solution(N: int, K: int, costs: List[List[int]]) -> int:
    dp = [[float("inf")] * K, [float("inf")] * K]

    for j in range(K):
        dp[0][j] = costs[0][j]

    i = 0
    for idx in range(1, N):
        i = idx % 2
        for j in range(K):
            dp[i][j] = costs[i][j] + min(
                [v for idx, v in enumerate(dp[1 - idx]) if idx != j]
            )

    return min(dp[i])


if __name__ == "__main__":
    print(solution(1, 1, [[10]]))
    print(solution(2, 2, [[1, 2], [10, 20]]))
