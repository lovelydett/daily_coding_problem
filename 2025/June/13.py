"""
Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".
Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.
"""


def encode(s: str) -> str:
    res = ""
    left, right = 0, 1

    while left < len(s):
        while right < len(s) and s[right] == s[left]:
            right += 1

        res += f"{right - left}" + s[left]
        left = right
        right = left + 1

    return res


def decode(s: str) -> str:
    res = ""
    left = 0

    while left < len(s):
        right = left
        while right < len(s) and "0" <= s[right] <= "9":
            right += 1

        res += s[right] * int(s[left:right])

        left = right + 1

    return res


if __name__ == "__main__":
    # Test case 1: Example from problem description
    s1 = "AAAABBBCCDAA"
    encoded1 = "4A3B2C1D2A"

    assert encode(s1) == encoded1
    assert decode(encoded1) == s1

    # Test case 2: Single character
    s2 = "A"
    encoded2 = "1A"
    assert encode(s2) == encoded2
    assert decode(encoded2) == s2

    # Test case 3: Empty string
    s3 = ""
    encoded3 = ""
    assert encode(s3) == encoded3
    assert decode(encoded3) == s3

    # Test case 4: Repeated characters
    s4 = "AAAAA"
    encoded4 = "5A"
    assert encode(s4) == encoded4
    assert decode(encoded4) == s4

    # Test case 5: Mixed characters
    s5 = "ABBBCCCD"
    encoded5 = "1A3B3C1D"
    assert encode(s5) == encoded5
    assert decode(encoded5) == s5

    # Test case 6: Round trip
    s6 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert decode(encode(s6)) == s6

    print("All test cases passed")
