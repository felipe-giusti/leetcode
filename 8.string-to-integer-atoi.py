#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        #IDEAS: for with isdigit
        # or Regex
        
        s = s.lstrip()
        if not s:
            return 0
        
        start_index = 0
        
        if s[0] == '-':
            mult = -1
            s = s[1:]
        elif s[0] == '+':
            mult = 1
            s = s[1:]
        else:
            mult = 1
        
        for i in range(start_index, len(s)):
            if not s[i].isdigit(): # first non digit
                s = s[:i]
                break
        if not s:
            return 0
        
        integer = int(s) * mult
        
        MAX_INT = 2**31 -1
        MIN_INT = -2**31
        if integer > MAX_INT:
            return MAX_INT
        elif integer < MIN_INT:
            return MIN_INT
        return integer
        
# @lc code=end

