from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    new = []
    for head in lists:
        while head:
            new.append(head.val)
            head = head.next
    new.sort()
    result = ListNode()
    current = result
    for n in new:
        current.next = ListNode(n)
        current = current.next
    return result.next
