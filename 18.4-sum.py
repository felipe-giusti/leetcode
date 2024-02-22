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
        N = len(nums)

        print(nums)

        nums.sort()
        for i in range(N-3):
            if i > 0 and nums[i] == nums[i-1]: # not sure if this one helps
                continue
            for j in range(i+1, N-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                left = j+1
                right = N-1
                while left < right:
                    # print(f'i{i}: {nums[i]}, j{j}: {nums[j]}, l{left}: {nums[left]}, r{right}: {nums[right]}')
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if s < target:
                        left += 1
                    elif s > target:
                        right -= 1
                    else:
                        res.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1]:
                            # print(f'left{left} skiped')
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            # print(f'right{right} skiped')
                            right -= 1
        return res


# @lc code=end

