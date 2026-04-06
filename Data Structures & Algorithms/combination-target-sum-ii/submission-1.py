class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        soln = []
        candidates.sort()
        
        def dfs(idx,csum, arr):
            if csum == target:
                soln.append(arr[:])
                return
            if idx >= len(candidates) or csum > target:
                return 
            arr.append(candidates[idx])
            dfs(idx + 1, csum + candidates[idx], arr)
            arr.pop()
            
            while idx + 1 < len(candidates) and candidates[idx + 1] == candidates[idx]:
                idx += 1
            dfs(idx + 1, csum , arr)
        dfs(0,0,[])
        return soln
                
            
