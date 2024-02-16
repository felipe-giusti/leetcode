#
# @lc app=leetcode id=589 lang=python3
#
# [589] N-ary Tree Preorder Traversal
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from collections import deque

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        stack = deque([(root, False)])
        res = []

        if stack[-1][0] is None:
            return []

        while stack:
            cur, visited = stack.pop()

            if visited or cur.children is None:
                res.append(cur.val)
            else:
                # root, left, right
                for c in reversed(cur.children): # append from right to left
                    stack.append((c, False))
                stack.append((cur, True))
        return res

# @lc code=end

