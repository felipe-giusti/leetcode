class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # backtracking / dfs

        res = []

        def backtrack(s, cur_comb, i):
            #goal
            if s == target:
                res.append(cur_comb[:])
                return

            if i > len(candidates) - 1 or s > target:
                return

            # cond
            for j in range(i, len(candidates)):
                if j>i and candidates[j] == candidates[j-1]:
                    continue
                if s + candidates[j] <= target:
                    cur_comb.append(candidates[j])
                    backtrack(s+candidates[j], cur_comb, j+1)
                    cur_comb.pop()
            
        candidates.sort()
        backtrack(0, [], 0)
        return res