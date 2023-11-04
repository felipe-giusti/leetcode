#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # trying out sliding window
        left, right = 0, 0  # sliding window range
        char_d = {} # character position
        c = 0
        while left < len(s):

            char_pos = char_d.get(s[right])
            
            if char_pos is None: # char not in dict
                char_d[s[right]] = right
                if right < len(s) -1:
                    right += 1
            else: # char in dict, max lenght reached
                local_max = len(char_d)
                if local_max > c: c = local_max
                # print(f'dict: {char_d}, n_pos: {char_pos+1}, local: {local_max}, right: {right}, left: {left}')
                left = char_pos + 1
                right = left
                char_d = {}

        return c
            
            
        
# @lc code=end

