# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,node,maxi):
        if node is None:
            return 0
        left=self.solve(node.left,maxi)
        if left<0:
            left=0
        right=self.solve(node.right,maxi)
        if right<0:
            right=0
        maxi[0]=max(maxi[0],node.val+left+right)
        return node.val+max(left,right)
    def maxPathSum(self, root: TreeNode | None) -> int:
        maxi=[float("-inf")]
        self.solve(root,maxi)
        return maxi[0]