class Solution:
    def climbStairs(self, n: int) -> int:
        #n = 2: 0->2, 0->1->2
        #n = 3: 0->2->3, 0->1->3, 0->1->2->3
        dp =[0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-2] + dp[i-1]
        return dp[n]
