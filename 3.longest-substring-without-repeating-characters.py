#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # trying out sliding window
        left = 0  # sliding window range
        char_pos = {} # character position
        length = 0
        for right in range(len(s)):
            char = s[right]
            
            if char in char_pos and char_pos[char] >= left: # repeating and in current substring (left forward)
                left = char_pos[char] + 1
            else:
                length = max(length, right-left + 1)
            char_pos[char] = right

        return length       
            
            
        
# @lc code=end

