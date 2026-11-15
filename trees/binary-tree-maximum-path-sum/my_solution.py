from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.res = -float('inf')
        self.getMax(root)
        return self.res
        # dfs(root)
        

    def getMax(self, root):
        if not root: return 0 

        left = self.getMax(root.left)
        right = self.getMax(root.right)

        self.res = max(self.res, root.val + left + right)
        path = root.val + max(left , right)
        return max(0 , path)