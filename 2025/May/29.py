"""
The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.
"""

import random


def solution(tries: int, thres: int) -> float:

    preds = [0] * thres
    idx = 0
    count, hit = 0, 0
    while True:
        x = random.random()
        y = random.random()
        count += 1
        hit += 1 if x**2 + y**2 <= 1 else 0

        preds[idx] = hit / count * 4
        idx = (idx + 1) % thres

        if count >= tries and all(
            map(lambda pred: int(pred * 1e3) == int(preds[0] * 1e3), preds)
        ):
            return preds[0]


if __name__ == "__main__":
    print(solution(10000, 2))
    print(solution(10000, 4))
    print(solution(10000, 8))
    print(solution(10000, 16))
    print(solution(10000, 32))
    print(solution(10000, 64))
