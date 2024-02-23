#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #backtracking
        res = []

        def backtrack(open_conter, closed_counter, s):
            #goal
            if closed_counter == n:
               res.append(s)
               return

            if open_conter < n:
                backtrack(open_conter+1, closed_counter, s+"(")
            if closed_counter < open_conter:
                backtrack(open_conter, closed_counter+1, s+')')
        
        backtrack(0, 0, "")
        return res

# @lc code=end

