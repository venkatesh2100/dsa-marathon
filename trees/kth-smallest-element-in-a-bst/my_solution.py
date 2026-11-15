from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        

        que = deque([root])
        arr = []
        while que:

            for i in range(len(que)):

                node = que.popleft()

                if node.val or node.val == 0: arr.append(node.val)

                if node.left: que.append(node.left)
                if node.right: que.append(node.right)


        arr.sort()
        
        return arr[k-1]