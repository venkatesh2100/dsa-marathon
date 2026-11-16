from collections import deque
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node: return None

        hmap = {}
        hmap[node] = Node(node.val)

        que = deque([node])

        while que:

            cur = que.popleft()

            for nei in cur.neighbors:
                if nei not in hmap:
                    hmap[nei] = Node(nei.val)
                    que.append(nei)
                hmap[cur].neighbors.append(hmap[nei])

        return hmap[node]
