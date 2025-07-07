'''
Word Break
Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.
For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].
Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
'''

from functools import cache

def solution(s: str, words: list[str]) -> list[str]:
    dic = set(words)

    res = []

    @cache
    def dfs(i: int) -> bool:
        if i == len(s):
            return True
        for j in range(i + 1, len(s) + 1):
            if s[i:j] in dic:
                res.append(s[i:j])
                if dfs(j):
                    return True
                res.pop()
        return False
    
    return res if dfs(0) else []

if __name__ == "__main__":
    # Test case 1: Example from problem description
    words1 = ['quick', 'brown', 'the', 'fox']
    s1 = "thequickbrownfox"
    assert solution(s1, words1) == ['the', 'quick', 'brown', 'fox']

    # Test case 2: Multiple solutions
    words2 = ['bed', 'bath', 'bedbath', 'and', 'beyond']
    s2 = "bedbathandbeyond"
    result = solution(s2, words2)
    assert result in [['bed', 'bath', 'and', 'beyond'], ['bedbath', 'and', 'beyond']]

    # Test case 3: No solution
    words3 = ['cat', 'dog', 'mouse']
    s3 = "catdogelephant"
    assert solution(s3, words3) == []

    # Test case 4: Empty string
    words4 = ['a', 'b', 'c']
    s4 = ""
    assert solution(s4, words4) == []

    # Test case 5: Empty dictionary
    words5 = []
    s5 = "abc"
    assert solution(s5, words5) == []

    # Test case 6: Single word
    words6 = ['hello']
    s6 = "hello"
    assert solution(s6, words6) == ['hello']

    print("All test cases passed")
