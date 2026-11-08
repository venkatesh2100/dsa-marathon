from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # 1. Weave: insert each clone directly after its original --
        # A -> C -> B becomes A -> A' -> C -> C' -> B -> B'.
        # The weave doubles as the "old -> new" map, saving the O(n) dict.
        # The original's next pointers are (temporarily) destroyed here.
        curr = head
        while curr:
            curr.next = Node(curr.val, curr.next)
            curr = curr.next.next

        # 2. Wire randoms: an original's random is an original, so its clone
        # sits exactly one hop to the right -- orig.random.next. Self-randoms
        # and forward randoms are both covered because originals never move.
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # 3. Split the braid: peel every clone into its own list while
        # rewiring the survivors back into the original chain.
        copy_head = head.next
        curr = head
        while curr:
            clone = curr.next
            curr.next = clone.next   # restore this original's next
            curr = curr.next         # advance (clone's next is still intact)
            if curr:
                clone.next = curr.next  # so this = the NEXT original's clone

        return copy_head
