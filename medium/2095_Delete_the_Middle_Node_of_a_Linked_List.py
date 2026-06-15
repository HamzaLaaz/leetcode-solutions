from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    L = []
    curr = head
    while curr:
        L.append(curr.val)
        curr = curr.next
    i = len(L) // 2
    L.pop(i)
    new = ListNode(0)
    curr = new
    for val in L:
        curr.next = ListNode(val)
        curr = curr.next

    return new.next
