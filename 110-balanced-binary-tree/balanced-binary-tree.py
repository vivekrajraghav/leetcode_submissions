# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,node):
        if node is None:
            return 0
        left=self.solve(node.left)
        if left==-1:
            return -1
        right=self.solve(node.right)
        if right==-1:
            return -1
        if abs(left-right)>1:
            return -1
        return 1+max(left,right)
    def isBalanced(self, root: TreeNode | None) -> bool:
        ans=self.solve(root)
        if ans==-1:
            return False
        else:
            return True