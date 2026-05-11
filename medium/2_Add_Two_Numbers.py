from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode],
                  l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    current = dummy
    ba9i = 0
    while l1 or l2 or ba9i:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        total = v1 + v2 + ba9i
        ba9i = total // 10
        digit = total % 10
        current.next = ListNode(digit)
        current = current.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    return dummy.next
