from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        que = deque([root])
        arr = []

        while que:
            val = 0

            for i in range(len(que)):
                node = que.popleft()
                # print(node.val , i )
                if node: val = node.val
                if node.left: que.append(node.left)
                if node.right: que.append(node.right)
            arr.append(val)
        return arr