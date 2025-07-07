"""
Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).
For example, given the string "([])[]({})", you should return true.
Given the string "([)]" or "((()", you should return false.
"""


def solution(s: str) -> bool:
    stk = []

    pairs = {
        "(": ")",
        "[": "]",
        "{": "}",
    }
    for ch in s:
        if ch in pairs:
            stk.append(ch)
        elif len(stk) == 0 or ch != pairs[stk[-1]]:
            return False
        else:
            stk.pop()

    return len(stk) == 0


if __name__ == "__main__":
    # Test case 1: Example from problem description (balanced)
    assert solution("([])[]({})") == True

    # Test case 2: Example from problem description (unbalanced)
    assert solution("([)]") == False
    assert solution("((()") == False

    # Test case 3: Empty string
    assert solution("") == True

    # Test case 4: Single bracket
    assert solution("(") == False
    assert solution(")") == False
    assert solution("[") == False
    assert solution("]") == False

    # Test case 5: Nested brackets
    assert solution("([{}])") == True
    assert solution("([{])") == False

    # Test case 6: Mixed bracket types
    assert solution("({[]})") == True
    assert solution("({[})") == False

    # Test case 7: Long balanced sequence
    assert solution("(([[{{}}]]))") == True
    assert solution("(([[{{}}]])") == False

    print("All test cases passed!")
