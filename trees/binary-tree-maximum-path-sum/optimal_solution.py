from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = float("-inf")

        # gain(): the best downward path *starting* at node, never dipping below 0.
        def gain(node):
            nonlocal best
            if not node:
                return 0
            left = gain(node.left)
            right = gain(node.right)
            # A turn through `node` (left -> node -> right) is a candidate answer.
            best = max(best, node.val + left + right)
            # But a parent can only extend ONE side of this subtree.
            return max(0, node.val + max(left, right))

        gain(root)
        return best
