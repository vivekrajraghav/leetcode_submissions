# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,node,low=-float("inf"),high=float("inf")):
        if node is None:
            return True
        if node.val<=low or node.val>=high:
            return False
        return (self.solve(node.left,low,node.val) and self.solve(node.right,node.val,high))
    def isValidBST(self, root: TreeNode | None) -> bool:
        return self.solve(root)