"""
Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.
Recall that the median of an even-numbered list is the average of the two middle numbers.
For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:
2
1.5
2
3.5
2
2
2
"""

from heapq import heappush, heappop


def solution(sequence: list[int]) -> list[int]:
    min_heap = []  # Big-end heap for the smaller numbers
    max_heap = []  # Small-end heap for the bigger numbers

    def compute(num: int) -> float:
        nonlocal min_heap, max_heap

        if not min_heap and not max_heap:
            max_heap.append(num)
            return num

        min_of_max = max_heap[0] if max_heap else float("inf")

        if num < min_of_max:
            heappush(min_heap, -1 * num)
        else:
            heappush(max_heap, num)

        if len(max_heap) - len(min_heap) > 1:
            heappush(min_heap, -1 * heappop(max_heap))

        if len(min_heap) - len(max_heap) > 0:
            heappush(max_heap, -1 * heappop(min_heap))

        return (
            max_heap[0]
            if len(max_heap) == len(min_heap) + 1
            else (max_heap[0] + -1 * min_heap[0]) / 2
        )

    return list(map(compute, sequence))


if __name__ == "__main__":
    # Test case 1: Example from problem description
    result1 = solution([2, 1, 5, 7, 2, 0, 5])
    expected1 = [2, 1.5, 2, 3.5, 2, 2, 2]
    assert result1 == expected1, f"Expected {expected1}, but got {result1}"

    # Test case 2: Single element
    result2 = solution([5])
    expected2 = [5]
    assert result2 == expected2, f"Expected {expected2}, but got {result2}"

    # Test case 3: Two elements
    result3 = solution([3, 7])
    expected3 = [3, 5.0]
    assert result3 == expected3, f"Expected {expected3}, but got {result3}"

    # Test case 4: Three elements (odd count)
    result4 = solution([1, 3, 5])
    expected4 = [1, 2.0, 3]
    assert result4 == expected4, f"Expected {expected4}, but got {result4}"

    # Test case 5: Four elements (even count)
    result5 = solution([1, 2, 3, 4])
    expected5 = [1, 1.5, 2, 2.5]
    assert result5 == expected5, f"Expected {expected5}, but got {result5}"

    # Test case 6: All same numbers
    result6 = solution([5, 5, 5, 5])
    expected6 = [5, 5.0, 5, 5.0]
    assert result6 == expected6, f"Expected {expected6}, but got {result6}"

    # Test case 7: Descending order
    result7 = solution([5, 4, 3, 2, 1])
    expected7 = [5, 4.5, 4, 3.5, 3]
    assert result7 == expected7, f"Expected {expected7}, but got {result7}"

    # Test case 8: Ascending order
    result8 = solution([1, 2, 3, 4, 5])
    expected8 = [1, 1.5, 2, 2.5, 3]
    assert result8 == expected8, f"Expected {expected8}, but got {result8}"

    # Test case 9: Empty sequence
    result9 = solution([])
    expected9 = []
    assert result9 == expected9, f"Expected {expected9}, but got {result9}"

    print("All test cases passed!")
