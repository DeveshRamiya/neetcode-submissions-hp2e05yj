class Solution:
    def longestPalindrome(self, s: str) -> str:
        #building the table
        n = len(s)
        dp = [[False] * n for _ in range(n)] 
        
        maxlen = 0
        idx = 0
        for start in range(n-1, -1, -1):
            for end in range(start, n):
                if s[start] == s[end] and ((end - start) <= 2  or dp[start+1][end -1]):
                    dp[start][end] = True
                    if (end - start + 1) > maxlen:
                        maxlen = end - start + 1
                        idx = start
    
        return s[idx: idx + maxlen]



