#
# @lc app=leetcode id=590 lang=python3
#
# [590] N-ary Tree Postorder Traversal
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
    def postorder(self, root: 'Node') -> List[int]:
        # post order -> left, right, root

        stack = deque([(root, False)])
        res = []

        if stack[-1][0] is None:
            return []

        while stack:
            cur, visited = stack.pop()

            if visited or cur.children is None:
                res.append(cur.val)
            else:

                stack.append((cur, True))
                for n in reversed(cur.children):
                    stack.append((n, False))
        return res

# @lc code=end

