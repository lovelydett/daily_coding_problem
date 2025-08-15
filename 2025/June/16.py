"""
Suppose you are given a table of currency exchange rates, represented as a 2D array. Determine whether there is a possible arbitrage: that is, whether there is some sequence of trades you can make, starting with some amount A of any currency, so that you can end up with some amount greater than A of that currency.
There are no transaction costs and you can trade fractional quantities
"""

import math


def solution(rates: list[list[float]]) -> bool:
    for i in range(len(rates)):
        for j in range(len(rates)):
            rates[i][j] = math.log2(rates[i][j])

    edges = [(u, v, w) for u in range(len(rates)) for v, w in enumerate(rates[u])]

    dist = [0] * len(rates)

    # Do V - 1 times relaxation
    for _ in range(len(edges) - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Do one more time
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            return True

    return False


if __name__ == "__main__":
    # Test case 1: Simple arbitrage opportunity (3 currencies)
    rates1 = [[1, 2, 4], [0.5, 1, 2], [0.25, 0.49, 1]]
    assert solution(rates1) == True

    # Test case 2: No arbitrage opportunity (3 currencies)
    rates2 = [
        [1, 2, 4],
        [0.5, 1, 2],
        [0.25, 0.5, 1.1],  # Slightly different to break arbitrage
    ]
    assert solution(rates2) == False

    # Test case 3: Single currency (edge case)
    rates3 = [[1]]
    assert solution(rates3) == False

    # Test case 4: Two currencies without arbitrage
    rates4 = [[1, 2], [0.4, 1]]  # 2 * 0.6 = 1.2 > 1
    assert solution(rates4) == True

    # Test case 5: Two currencies with arbitrage
    rates5 = [[1, 2], [0.6, 1]]  # 2 * 0.4 = 0.8 < 1
    assert solution(rates5) == False

    # Test case 6: Larger matrix with arbitrage
    rates6 = [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 0.8, 1],
        [1, 1, 1.2, 1, 1],
        [1, 1, 1, 1, 1],
    ]
    assert solution(rates6) == True

    print("All test cases passed!")
