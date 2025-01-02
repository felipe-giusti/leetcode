#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # DP Problem

        # base case: "" vs word -> len(word) or 0
        # if char1 == char2 -> keep going, no changes: i+1, j+1
        # else Decision:
        # insert: i, j+1
        # delete: i+1, j
        # replace: it changes to the correct one, so i+1, j+1

        # 1d dp -> I only need i-1 and j-1, so I can save it in a prev variable


        m, n = len(word1), len(word2)

        dp = [i for i in range(n+1)]
        
        for i in range(1, m+1):
            # new row
            prev_diagonal = dp[0]
            dp[0] = i

            for j in range(1, n+1):
                temp = dp[j]
                if word1[i-1] == word2[j-1]:
                    dp[j] = prev_diagonal
                else:
                    dp[j] = 1 + min(
                        dp[j],
                        dp[j-1],
                        prev_diagonal
                    )
                prev_diagonal = temp
        return dp[-1]
                

# @lc code=end

