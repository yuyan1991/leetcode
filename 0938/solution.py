# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.ans = 0
        self.traversal(root, low, high)
        return self.ans
    
    def traversal(self, root, low, high):
        if not root:
            return
        if root.val >= low and root.val <= high:
            self.ans += root.val
        self.traversal(root.left, low, high)
        self.traversal(root.right, low, high)