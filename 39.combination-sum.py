class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(cur_target, cur_comb, i):
            
            if cur_target == 0:
                res.append(cur_comb)
                return
            if cur_target < 0 or i >= len(candidates):
                return
            
            
            backtrack(cur_target - candidates[i], cur_comb + [candidates[i]], i)
            # backtrack failed, continue to next candidate
            backtrack(cur_target, cur_comb, i+1)

        backtrack(target, [], 0)
        return res