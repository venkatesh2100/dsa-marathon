from collections import deque
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, neighbors: "Optional[list['Node']]" = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: "Optional[Node]") -> "Optional[Node]":
        if not node:
            return None

        # old node -> clone; doubles as the visited set, so cycles can't loop
        clones = {node: Node(node.val)}
        q = deque([node])

        while q:
            cur = q.popleft()
            for nei in cur.neighbors:
                if nei not in clones:  # first sighting: clone it, schedule its edges
                    clones[nei] = Node(nei.val)
                    q.append(nei)
                # wire from the clone side — runs for fresh and already-cloned neighbors alike
                clones[cur].neighbors.append(clones[nei])

        return clones[node]
