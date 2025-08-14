"""
G = (V, E)
V = |V|, E = |E|
Do relaxation V - 1 times, each time check all E edges to update dist[v] in each (u, v).
Imagine tightening the paths with a rope: each relaxation is like gently pulling on all paths.
After V - 1 pulls, all paths are tightened, if still can pull, means there are negative weight cycle.
"""


def solution(G: list[list[int]], src: int) -> bool:
    edges = [
        (u, v, w) for u in range(len(G)) for v, w in enumerate(G[u]) if w is not None
    ]

    dist = [float("inf")] * len(G)
    dist[src] = 0

    count = 0
    while True:
        flag = True
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                flag = False

        count += 1

        if flag:
            return False
        if count == len(G) + 1:
            return True


if __name__ == "__main__":
    # Test case 1: Graph with no negative cycles
    graph1 = [
        [None, 4, None, None],
        [None, None, 6, None],
        [None, None, None, 2],
        [None, None, None, None],
    ]
    assert solution(graph1, 0) == False

    # Test case 2: Graph with negative cycle
    graph2 = [
        [None, 1, None, None],
        [None, None, -2, None],
        [None, None, None, -1],
        [1, None, None, None],
    ]
    assert solution(graph2, 0) == True

    # Test case 3: Single node graph
    graph3 = [[None]]
    assert solution(graph3, 0) == False

    # Test case 4: Disconnected graph with no negative cycles
    graph4 = [
        [None, 1, None, None],
        [None, None, 2, None],
        [None, None, None, None],
        [None, None, None, None],
    ]
    assert solution(graph4, 0) == False

    # Test case 5: Graph with negative weights but no cycles
    graph5 = [
        [None, -1, None, None],
        [None, None, -2, None],
        [None, None, None, 3],
        [None, None, None, None],
    ]
    assert solution(graph5, 0) == False

    print("All test cases passed!")
