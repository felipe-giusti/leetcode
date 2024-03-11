class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(cur_target, cur_comb, i):
            
            if cur_target == 0:
                res.append(cur_comb)
                return
            if cur_target < 0:
                return
            
            for j in range(i, len(candidates)):
                backtrack(cur_target - candidates[j], cur_comb + [candidates[j]], j)
            
        backtrack(target, [], 0)
        return res