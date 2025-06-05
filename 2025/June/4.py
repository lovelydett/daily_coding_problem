"""
Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.
For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.
"""


class ListNode:
    def __init__(self, *, val: int, nxt: "ListNode" = None):
        self.val = val
        self.nxt = nxt


def solution(list1: ListNode, list2: ListNode) -> ListNode | None:
    n1, n2 = list1, list2
    while n1 or n2:
        if n1 and n2 and n1.val == n2.val:
            return n1
        n1 = n1.nxt if n1 else list2
        n2 = n2.nxt if n2 else list1

    return None


if __name__ == "__main__":
    n4 = ListNode(val=4, nxt=None)
    n3 = ListNode(val=3, nxt=n4)
    n99 = ListNode(val=99, nxt=n3)
    n2 = ListNode(val=2, nxt=n99)
    n1 = ListNode(val=1, nxt=n99)
    n0 = ListNode(val=0, nxt=n1)

    print(solution(n1, n2).val)
    print(solution(n0, n2).val)
