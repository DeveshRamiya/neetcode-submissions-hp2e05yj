class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        soln =[]
        visited = [False] * len(nums)        
        def permute(visited, arr):
            if len(arr) == len(nums):
                soln.append(arr[:])
                return
            for i in range(len(nums)):
                if not visited[i]:
                    arr.append(nums[i])
                    visited[i] = True
                    permute(visited, arr)
                    visited[i] = False
                    arr.pop()
        permute(visited, [])
        return soln
