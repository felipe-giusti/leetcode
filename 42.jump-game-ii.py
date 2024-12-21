class Solution:
    def jump(self, nums: List[int]) -> int:

        res, max_dist, i_end = 0, 0, 0

        # because we are already getting max dist every time, we don't need to worry about going back indexes
        for i in range(len(nums)-1):
            max_dist = max(max_dist, i + nums[i])

            if max_dist >= len(nums)-1:
                return res + 1

            if i == i_end:
                res += 1
                i_end = max_dist
        return res
