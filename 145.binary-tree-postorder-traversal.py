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
        stack = deque()
        res = []
        cur = root

        while stack or cur is not None:
            #go left first
            if cur is not None:
                stack.append(cur)
                cur = cur.left
            else:
                # left is None, try right
                tmp = stack[-1].right
                if tmp is not None:
                    # not leaf node, set cur and reloop
                    cur = tmp
                else: # right None -> leaf
                    tmp = stack.pop()
                    res.append(tmp.val)
                    while stack and tmp == stack[-1].right:
                        # 
                        tmp = stack.pop()
                        res.append(tmp.val)
            
        return res
            


# @lc code=end

