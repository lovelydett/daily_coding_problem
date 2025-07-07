"""
Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.
The list is very long, so making more than one pass is prohibitively expensive.
Do this in constant space and in one pass.
"""

from dataclasses import dataclass


@dataclass
class Node:
    val: int
    nxt: "Node"


def solution(head: Node, k: int) -> Node:
    dummy = Node(None, head)

    fast, slow = dummy, dummy

    while fast.nxt:
        fast = fast.nxt
        k -= 1
        slow = slow.nxt if k < 0 else slow

    slow.nxt = slow.nxt.nxt

    return dummy.nxt


if __name__ == "__main__":

    def list_to_linked_list(lst):
        head = None
        for val in reversed(lst):
            head = Node(val, head)
        return head

    def linked_list_to_list(head):
        lst = []
        while head:
            lst.append(head.val)
            head = head.nxt
        return lst

    # Test case 1: Remove last element (k=1)
    lst1 = [1, 2, 3, 4, 5]
    head1 = list_to_linked_list(lst1)
    result1 = solution(head1, 1)
    assert linked_list_to_list(result1) == [1, 2, 3, 4]

    # Test case 2: Remove first element (k=length)
    lst2 = [1, 2, 3, 4, 5]
    head2 = list_to_linked_list(lst2)
    result2 = solution(head2, 5)
    assert linked_list_to_list(result2) == [2, 3, 4, 5]

    # Test case 3: Remove middle element (k=3)
    lst3 = [1, 2, 3, 4, 5]
    head3 = list_to_linked_list(lst3)
    result3 = solution(head3, 3)
    assert linked_list_to_list(result3) == [1, 2, 4, 5]

    # Test case 4: Single element list (k=1)
    lst4 = [1]
    head4 = list_to_linked_list(lst4)
    result4 = solution(head4, 1)
    assert linked_list_to_list(result4) == []

    # Test case 5: Remove second last element (k=2)
    lst5 = [1, 2, 3, 4, 5]
    head5 = list_to_linked_list(lst5)
    result5 = solution(head5, 2)
    assert linked_list_to_list(result5) == [1, 2, 3, 5]

    print("All test cases passed")
