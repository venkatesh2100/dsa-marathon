from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Dummy in front of head: even deleting the FIRST node collapses to a
        # slow.next re-link, and the return becomes dummy.next instead of head.
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy

        # Open an n-wide gap: fast lands on the nth node from the start.
        # Relies on 1 <= n <= size (LeetCode's constraint).
        for _ in range(n):
            fast = fast.next

        # March the gap to the end; slow ends on the node BEFORE the target.
        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next
