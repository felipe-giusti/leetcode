#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # approach 1: sort, and compare, return extra list
        # approach 2: do it inplace

        intervals = sorted(intervals, key=lambda interval: interval[0])
        
        merged = []
        prev = intervals[0]

        for interval in intervals[1:]:
            # if overlap, merge
            if prev[1] >= interval[0]:
                prev = [prev[0], max(prev[1], interval[1])]
            # doesn't overlap, append previous
            else:
                merged.append(prev)
                prev = interval

        # last item
        merged.append(prev)
        
        return merged

# @lc code=end

