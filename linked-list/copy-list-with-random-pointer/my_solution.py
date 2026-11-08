# Definition for a Node. (commented out on LeetCode, embedded in the docstring —
# needed here because this code constructs the copies at runtime)
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Map each original node to its copy; None maps to None
        old_to_new = {None: None}

        # Step 1: Create all new nodes without wiring connections
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

    

        # Step 2: Assign next and random pointers using the map
        curr = head
        while curr:
            copy = old_to_new[curr]
            copy.next = old_to_new[curr.next]
            copy.random = old_to_new[curr.random]
            curr = curr.next

        # print(old_to_new[head])
        return old_to_new[head] 
