#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        # idea: binary search until we find the number

        left, right = 1, x

        while left <= right:
            mid = (left + right) // 2

            if mid*mid == x:
                return mid
            elif mid*mid < x:
                # pow < x -> need to make left bigger
                left = mid + 1
            else:
                right = mid - 1
        # right <= left, so we return right
        return right

        
# @lc code=end

