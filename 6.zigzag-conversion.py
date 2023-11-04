#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Idea 1: go through string, add to dict / list, at the end of numRows go back. Concatenate all
        if numRows == 1:
            return s
        
        rows = [ '' for _ in range(numRows)]
        curr_row = 0
        direction = 1
        for char in s:
            if curr_row == numRows-1 and direction == 1: # go back
                direction = -1
            elif curr_row == 0 and direction == -1: # go forward
                    direction = 1
            
            rows[curr_row] += char
            curr_row += direction
        
        return ''.join(rows)

            
                
            
                                     
# @lc code=end