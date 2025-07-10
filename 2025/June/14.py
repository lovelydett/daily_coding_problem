"""
You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.
Compute how many units of water remain trapped on the map in O(N) time and O(1) space.
For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.
Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.
"""


def solution(walls: list[int]) -> int:
    left, right = 0, len(walls) - 1

    lm, rm = walls[0], walls[-1]

    res = 0

    while left <= right:
        if lm < rm:
            res += max(0, lm - walls[left])
            lm = max(lm, walls[left])
            left += 1
        else:
            res += max(0, rm - walls[right])
            rm = max(rm, walls[right])
            right -= 1

    return res


if __name__ == "__main__":
    # Test case 1: Example from problem description
    walls1 = [2, 1, 2]
    assert solution(walls1) == 1

    # Test case 2: Second example from problem description
    walls2 = [3, 0, 1, 3, 0, 5]
    assert solution(walls2) == 8

    # Test case 3: Single wall (no trapping possible)
    walls3 = [5]
    assert solution(walls3) == 0

    # Test case 5: Increasing walls (no trapping)
    walls5 = [1, 2, 3, 4, 5]
    assert solution(walls5) == 0

    # Test case 6: Decreasing walls (no trapping)
    walls6 = [5, 4, 3, 2, 1]
    assert solution(walls6) == 0

    # Test case 7: Valley shape
    walls7 = [5, 1, 1, 1, 5]
    assert solution(walls7) == 12

    # Test case 8: Complex multi-peak
    walls8 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    assert solution(walls8) == 6

    print("All test cases passed")
