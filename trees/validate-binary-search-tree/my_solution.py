from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
            
        que = deque([(root, float('-inf'), float('inf'))])
        
        while que:
            node, low, high = que.popleft()
            
            if not (low < node.val < high):
                return False
                
            if node.left:
                que.append((node.left, low, node.val))
            if node.right:
                que.append((node.right, node.val, high))
                
        return True