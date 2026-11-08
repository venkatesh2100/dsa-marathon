from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        # Fast gains one node per round; inside the cycle the "distance
        # from slow to fast" shrinks by exactly 1, so it must hit 0.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:   # identity, not value -- duplicate vals are normal
                return True

        return False
