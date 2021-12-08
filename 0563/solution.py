# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.traversal(root)
        return self.ans
    
    def traversal(self, root):
        if root is None:
            return 0
        sumL = self.traversal(root.left)
        sumR = self.traversal(root.right)
        self.ans += abs(sumL - sumR)
        return sumL + sumR + root.val
