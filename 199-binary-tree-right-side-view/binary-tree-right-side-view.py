# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverse_post_order(self,node,level,ans):
        if node is None:
            return
        if len(ans)==level:
            ans.append(node.val)
        if node.right:
            self.reverse_post_order(node.right,level+1,ans)
        if node.left:
            self.reverse_post_order(node.left,level+1,ans)
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        # if not root:
        #     return []
        # result=[]
        # queue=deque([root])
        # while len(queue)!=0:
        #     level_size=len(queue)
        #     for i in range(level_size):
        #         node=queue.popleft()
        #         if i==level_size-1:
        #             result.append(node.val)
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        # return result
        ans=[]
        self.reverse_post_order(root,0,ans)
        return ans