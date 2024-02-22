#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #pointer approach
        res = set()
        
        nums.sort()
        for i in range(len(nums)-3):
            # if i > 0 and nums[i] == nums[i-1]:
            #     continue
            for j in range(i+1, len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                # print(f'i {i}, j {j} || len {len(nums)}')
                left = j+1
                right = len(nums)-1
                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if s < target:
                        left += 1
                    elif s > target:
                        right -= 1
                    else:
                        res.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1

        return res


# @lc code=end

