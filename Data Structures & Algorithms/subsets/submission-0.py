class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        soln = []
        def dfs(arr, idx):
            if idx >= len(nums):
                soln.append(arr[:])
                return
            arr.append(nums[idx])
            dfs(arr, idx + 1)
            arr.pop()
            dfs(arr, idx + 1)
        dfs([],0)
        return soln