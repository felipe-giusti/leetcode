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

        # 1. create 2D dp and base case

        m, n = len(word1), len(word2)

        # word2
        dp = [[float("inf")]*(n+1) for _ in range(m+1)]

        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i-1][j],
                        dp[i][j-1],
                        dp[i-1][j-1]
                    )

        return dp[-1][-1]
                

# @lc code=end

