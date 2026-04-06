class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hmap = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        soln = []
        def dfs(idx, ans):
            if idx >= len(digits):
                if ans != "":
                    soln.append(ans)
                return
            for ch in hmap[digits[idx]]:
                dfs(idx + 1, ans + ch)
        dfs(0,"")
        return soln