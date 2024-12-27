#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        START, END = 0, 1

        res = []

        for i, interval in enumerate(intervals):
            # insert before
            if newInterval[END] < interval[START]:
                res.append(newInterval)
                return res + intervals[i:]
            # insert after    
            elif newInterval[START] > interval[END]:
                res.append(interval)
            # merge    
            else:
                newInterval = [
                    min(interval[START], newInterval[START]),
                    max(interval[END], newInterval[END])
                    ]
        res.append(newInterval)
        return res


# @lc code=end

