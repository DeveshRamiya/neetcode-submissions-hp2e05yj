class Solution:
    def partition(self, s: str) -> List[List[str]]:
        soln = []
        def dfs(idx, arr):
            if idx >= len(s):
                soln.append(arr[:])
                return
            for i in range(idx, len(s)):
                if isPalindrome(idx, i):
                    arr.append(s[idx: i + 1])
                    dfs(i + 1, arr)
                    arr.pop()
        def isPalindrome(idx, i):
            while idx <= i:
                if s[idx] != s[i]:
                    return False
                idx += 1
                i -= 1
            return True
        dfs(0,[])
        return soln