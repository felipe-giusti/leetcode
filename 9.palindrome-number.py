#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # two pointer
        x = str(x)

        left, right = 0, len(x)-1
        while left < right:
            if x[left] != x[right]:
                return False
            left += 1
            right -= 1
        return True
        
# @lc code=end

