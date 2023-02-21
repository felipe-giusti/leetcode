#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Idea: dict [char] = num  -->> external count
        char_counter = {}
        length = 0
        curr_length = 0
        i = 0
        i_follow = 0
        while i < len(s):
            if char_counter.get(s[i]) is not None: # has repeating char
                if curr_length > length:
                    length = curr_length

                i_follow += 1
                i = i_follow + 1
                char_counter = {s[i_follow]: 1}
                curr_length = 1
            else:
                char_counter[s[i]] = 1
                curr_length += 1
                i +=1
                if curr_length > length:
                    length = curr_length 
        
        return length
        
# @lc code=end

