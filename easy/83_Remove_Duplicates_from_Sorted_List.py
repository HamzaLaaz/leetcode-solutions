from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    check = head
    while check and check.next:
        if check.val == check.next.val:
            check.next = check.next.next
        else:
            check = check.next
    return head
