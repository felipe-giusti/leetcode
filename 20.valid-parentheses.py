#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start

from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
       
        d = {'(': ')', '[':']', '{':'}'}
        stack = deque()

        for c in s:
            if c in d: #open brackets
               stack.append(c)
            elif len(stack)==0 or d[stack.pop()] != c: # if last appended not type of bracket
                return False
        return len(stack) == 0 # if entire stack popped, OK
        
                  
# @lc code=end