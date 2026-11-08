from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:   # 0 or 1 node: nothing to reorder
            return

        # 1. Fast starts ONE AHEAD, so slow lands on the FIRST half's last
        # node -- a clean split for both odd and even lengths.
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Cut there, then reverse the tail half (reverse-linked-list).
        second = self._reverse(slow.next)
        slow.next = None

        # 3. Weave second into first: L0,Ln-1,L1,Ln-2... The first half is
        # the longer one (odd lengths), so `while second` needs no leftovers.
        first = head
        while second:
            nxt_first = first.next
            nxt_second = second.next

            first.next = second
            second.next = nxt_first

            first = nxt_first
            second = nxt_second

    def _reverse(self, head):
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev
