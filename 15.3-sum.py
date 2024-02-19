#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # idea 2 -> sort + check sum

        triplets = set()
        nums = sorted(nums)

        for i in range(len(nums) - 2):
            target = -nums[i]
            #two sum
            l = i+1
            r = len(nums) - 1

            while l < r:
                # print(f'i: {i}, l" {l}, r:{r}  || len: {len(nums)}')
                if nums[l] + nums[r] == target:
                    triplets.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return triplets
                    

# @lc code=end

