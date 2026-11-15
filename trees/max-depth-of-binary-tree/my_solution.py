from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:return 0 

        que = deque([root])
        ans = 0

        while que:
            for i in range(len(que)):
                node = que.popleft()

                if node.left: que.append(node.left)
                if node.right: que.append(node.right)

            ans+=1
        return ans  
