from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def pairSum(head: Optional[ListNode]) -> int:
    curt = head
    arr = []
    while curt:
        arr.append(curt.val)
        curt = curt.next
    result = 0
    for nb in arr:
        total = nb + arr[-1]
        if total > result:
            result = total
        arr.pop()
    return result
