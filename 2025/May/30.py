"""
Given a stream of elements too large to store in memory, pick k random element from the stream with uniform probability.
"""

from typing import Iterable, List
import random


# Reservoir sampling
def solution(stream: Iterable, k: int):
    res = []
    for i, v in enumerate(stream):
        if i < k:
            res.append(v)
        else:
            j = random.randint(0, i)
            if j < k:
                res[j] = v

    return res


def evaluate(res_list: List[List]):
    m = {}
    for res in res_list:
        for v in res:
            m[v] = m.get(v, 0) + 1

    for v, count in m.items():
        print(f"{v}: {count}")


if __name__ == "__main__":
    res_list = []
    for _ in range(10000):
        res_list.append(solution(range(1, 101), 10))

    evaluate(res_list)
