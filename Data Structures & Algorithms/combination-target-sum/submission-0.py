class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        soln = []
        def dfs(arr, csum, idx):
            if csum > target or idx >= len(nums):
                return
            if csum == target:
                soln.append(arr[:])
                return
            
            arr.append(nums[idx])
            dfs(arr, csum + nums[idx], idx)
            arr.pop()
            dfs(arr, csum, idx + 1)
        
        dfs([],0, 0)
        return soln

        