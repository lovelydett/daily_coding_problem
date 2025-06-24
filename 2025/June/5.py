'''
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.
For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
'''

def solution(lectures: list[tuple[int, int]]) -> int:
    times: list[tuple[int, bool]] = []
    for s, e in lectures:
        times.append((s, True))
        times.append((e, False))

    times.sort()
    res = 0
    tmp = 0

    for _, is_start in times:
        tmp += 1 if is_start else -1
        res = max(res, tmp)

    return res

if __name__ == "__main__":
    # Test case 1: Example from problem
    assert solution([(30, 75), (0, 50), (60, 150)]) == 2
    
    # Test case 2: No overlapping intervals
    assert solution([(0, 10), (20, 30), (40, 50)]) == 1
    
    # Test case 3: All intervals overlap
    assert solution([(0, 100), (10, 90), (20, 80)]) == 3
    
    # Test case 4: Single interval
    assert solution([(0, 50)]) == 1
    
    # Test case 5: Empty list
    assert solution([]) == 0
    
    # Test case 6: Multiple overlaps
    assert solution([(0, 30), (5, 10), (15, 20), (25, 35)]) == 2
    
    print("All test cases passed!")
