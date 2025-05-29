"""
This problem was asked by Amazon.
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""


def solution(s: str, k: int) -> int:
    m = {s[0]: 1}
    l, r = 0, 0
    res = 1
    while r < len(s):
        while r < len(s) and len(m) <= k:
            res = max(res, r - l + 1)
            r += 1
            if r < len(s):
                m[s[r]] = m.get(s[r], 0) + 1

        while l < len(s) and r < len(s) and l <= r and len(m) > k:
            m[s[l]] -= 1
            if m[s[l]] == 0:
                del m[s[l]]
            l += 1

    return res


if __name__ == "__main__":
    # Test cases
    print(solution("abcba", 2))  # Expected: 3 ("bcb")
    print(solution("a", 1))  # Expected: 1 ("a")
    print(solution("aaabbb", 1))  # Expected: 3 ("aaa" or "bbb")
    print(solution("eceba", 2))  # Expected: 3 ("ece")
    print(solution("abcdef", 3))  # Expected: 3 ("abc", "bcd", etc.)
    print(solution("aabacbebebe", 3))  # Expected: 7 ("cbebebe")
    print(solution("aaaaa", 2))  # Expected: 5 ("aaaaa")
    print(solution("ababababab", 2))  # Expected: 10 ("ababababab")
