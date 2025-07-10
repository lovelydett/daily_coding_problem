"""
The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.
Given two strings, compute the edit distance between them.
"""

from functools import cache


def solution(s1: str, s2: str) -> int:
    @cache
    def get_distance_from(i: int, j: int) -> int:
        if i == len(s1):
            return len(s2) - j
        if j == len(s2):
            return len(s1) - i

        if s1[i] == s2[j]:
            return get_distance_from(i + 1, j + 1)

        return 1 + min(
            get_distance_from(i + 1, j),
            get_distance_from(i, j + 1),
            get_distance_from(i + 1, j + 1),
        )

    return get_distance_from(0, 0)


if __name__ == "__main__":
    # Test case 1: Example from problem description
    assert solution("kitten", "sitting") == 3

    # Test case 2: Empty strings
    assert solution("", "") == 0
    assert solution("abc", "") == 3
    assert solution("", "xyz") == 3

    # Test case 3: Identical strings
    assert solution("hello", "hello") == 0

    # Test case 4: Single character difference
    assert solution("abc", "axc") == 1
    assert solution("abc", "abcd") == 1
    assert solution("abc", "bc") == 1

    # Test case 5: Complete mismatch
    assert solution("abc", "xyz") == 3

    # Test case 6: Prefix/suffix differences
    assert solution("abcdef", "bcdefg") == 2
    assert solution("abcdef", "xbcdef") == 1
    assert solution("abcdef", "abcxyz") == 3

    print("All test cases passed")
