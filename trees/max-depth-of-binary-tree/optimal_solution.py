from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # The depth of a tree is 1 (this node) + the deeper of its two subtrees.
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
