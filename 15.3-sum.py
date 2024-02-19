#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # idea 1: find all combinations where sum = 0
        # start i at 0 -> find 2 sum with rest of...
        # if conditions -> add to final set
        # repeat with indexes forward

        triplets = set()
        two_sum = set()

        for i, ni in enumerate(nums):
            #two sum
            for num in nums[i+1:]:
                target = -(num + ni)
                if target in two_sum:
                    t = tuple(sorted((ni, num, target)))
                    triplets.add(t)
                two_sum.add(num)
            two_sum.clear()
        return [list(t) for t in triplets]
# @lc code=end

