"""
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
"""

from typing import List
from functools import cache


def solution(steps: List[int], N: int) -> int:

    @cache
    def dfs(remain: int) -> int:
        if remain == 0:
            return 1
        if remain < 0:
            return 0
        return sum(dfs(remain - step) for step in steps)

    return dfs(N)


if __name__ == "__main__":
    print(solution([1], 2))
    print(solution([1, 2], 4))
    print(solution([1, 2], 5))
    print(solution([1, 3, 5], 5))
