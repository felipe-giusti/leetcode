#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        START, END = 0, 1
        i = 0

        while i < len(intervals):
            # Insert before the current interval
            if newInterval[END] < intervals[i][START]:
                intervals.insert(i, newInterval)
                return intervals

            # Skip intervals that end before the newInterval starts
            elif newInterval[START] > intervals[i][END]:
                i += 1

            # Merge overlapping intervals
            else:
                newInterval = [
                    min(intervals[i][START], newInterval[START]),
                    max(intervals[i][END], newInterval[END]),
                ]
                intervals.pop(i)  # Remove the current interval since it is merged

        # If we reach here, the new interval goes at the end
        intervals.append(newInterval)
        return intervals



# @lc code=end

