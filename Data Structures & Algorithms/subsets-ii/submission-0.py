class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        soln = []
        nums.sort()
        def dfs(idx, arr):
            if idx == len(nums):
                soln.append(arr[:])
                return 
            arr.append(nums[idx])
            dfs(idx+1, arr)
            arr.pop()
            while idx + 1 < len(nums) and nums[idx + 1] == nums[idx]:
                idx += 1
            dfs(idx + 1, arr)
        dfs(0,[])
        return soln