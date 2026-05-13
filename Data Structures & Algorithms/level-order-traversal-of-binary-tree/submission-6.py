# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #BFS standard method is using a for loop of len(queue)
        #inside the while q so that each level can be done sep
        if not root:
            return []
        res=[]
        q=deque([root])
        while q:
            x=[]
            for i in range(len(q)):
                node=q.popleft()
                x.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(x)
        return res

        