from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        if not root: return []
        rval = root.val
        que = deque([(root , rval)])
        c = 0
        

        while que:


            for i in range(len(que)):

                node , rval = que.popleft()

                if node.val >= rval:
                    c+=1
                rval = max(node.val , rval)

                if node.left: que.append((node.left , rval))
                if node.right: que.append((node.right , rval))

        return c