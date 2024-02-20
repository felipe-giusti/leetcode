#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # two pointer
        l, r = 0, len(height) - 1
        max_area = 0
        
        while l < r:
            width = r - l
            min_h = min(height[l], height[r])
            max_area = max(max_area, width*min_h)

            if height[l] < height[r]:
                l += 1
                # saves on area calculation
                while height[l] < min_h:
                    l += 1
            else:
                r -= 1
                while height[r] < min_h:
                    r -= 1
        return max_area

# @lc code=end

