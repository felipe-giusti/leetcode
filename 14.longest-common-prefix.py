#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        smallest_prefix = min(strs, key=len)
        
        # for each string, if doesnt start with smallest substring,
        # reduce smallest substring until we find the smallest common
        for s in strs:
            while not s.startswith(smallest_prefix):
                smallest_prefix = smallest_prefix[:-1]
            # if not smallest_prefix:
            #     return ''
        return smallest_prefix

# @lc code=end

