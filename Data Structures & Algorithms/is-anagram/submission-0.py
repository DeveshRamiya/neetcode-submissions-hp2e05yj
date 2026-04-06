class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s.lower()
        t.lower()
        if len(s) != len(t):
            return False
        arr = [0] * 26
        for i in range(len(s)):
            arr[ord(s[i]) - 97] += 1
            arr[ord(t[i]) - 97] -= 1
        for ele in arr:
            if ele:
                return False
        return True

        