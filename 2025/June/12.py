"""
Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a list of strings which represents each line, fully justified.
More specifically, you should have as many words as possible in each line. There should be at least one space between each word. Pad extra spaces when necessary so that each line has exactly length k. Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.
If you can only fit one word on a line, then you should pad the right-hand side with spaces.
Each word is guaranteed not to be longer than k.
For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16, you should return the following:
["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly
"""


def solution(words: list[str], k: int) -> list[str]:
    # First scatter words into lines
    lines: list[list[str]] = []
    cur_len = -1
    cur_line: list[str] = []

    for word in words:
        if cur_len + 1 + len(word) > k:
            cur_len = -1
            lines.append(cur_line[:])
            cur_line.clear()

        cur_len += 1 + len(word)
        cur_line.append(word)

    if cur_line:
        lines.append(cur_line[:])

    # Then add spaces evenly
    res: list[str] = ["" for _ in lines]
    for i, line in enumerate(lines):
        spaces = k - sum(len(word) for word in line)

        if len(line) == 1:
            res[i] += line[0] + " " * spaces
            continue

        intervals = len(line) - 1
        base = spaces // intervals
        extra = spaces % intervals

        for word in line[:-1]:
            res[i] += word
            res[i] += " " * (base + extra)
            extra -= 1 if extra > 0 else 0

        res[i] += line[-1]

    return res


if __name__ == "__main__":
    # Test case 1: Example from problem description
    words1 = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    k1 = 16
    expected1 = ["the  quick brown", "fox  jumps  over", "the   lazy   dog"]
    assert solution(words1, k1) == expected1

    # Test case 2: Single word
    words2 = ["hello"]
    k2 = 10
    assert solution(words2, k2) == ["hello     "]

    # Test case 3: Words exactly fit line length
    words3 = ["abc", "def", "ghi"]
    k3 = 11  # "abc def ghi" is exactly 11 chars
    assert solution(words3, k3) == ["abc def ghi"]

    # Test case 4: Empty words list
    words4 = []
    k4 = 10
    assert solution(words4, k4) == []

    # Test case 5: Multiple words with varying spacing
    words5 = ["this", "is", "a", "test", "of", "justification"]
    k5 = 13
    expected5 = ["this   is   a", "test       of", "justification"]
    assert solution(words5, k5) == expected5

    print("All test cases passed")
