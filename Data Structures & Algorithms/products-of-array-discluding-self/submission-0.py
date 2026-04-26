class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prev = [1] * len(nums) 
        adv = [1] * len(nums)
        ans = [0] * len(nums) 
        for i in range(1,len(nums)):
            prev[i] = prev[i-1] * nums[i-1]
        for i in range(len(nums) - 2, -1, -1):
            adv[i] = adv[i+1] * nums[i+1]
        for i in range(len(nums)):
            ans[i] = prev[i] * adv[i]
        return ans