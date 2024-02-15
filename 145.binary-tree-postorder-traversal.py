#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = deque([(root, False)])
        res = []

        while stack:
            cur, visited = stack.pop()
            if cur is None:
                continue

            if visited:
              res.append(cur.val)
            else:
                # Post -> left, right, root
                stack.append((cur, True))
                stack.append((cur.right, False))
                stack.append((cur.left, False))  
        return res
            




# @lc code=end

