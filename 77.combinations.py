#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # backtracking
        res = []

        def backtrack(comb: list, first):
            if len(comb) == k:
                res.append(comb[:])
                return
            
            for i in range(first, n+1):
                comb.append(i)
                backtrack(comb, i+1)
                comb.pop()
            
        backtrack([], 1)
        return res
            



# @lc code=end

