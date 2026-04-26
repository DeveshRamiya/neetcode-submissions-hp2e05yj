class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for word in strs:
            ans += "$" + str(len(word)) + "$"
            ans += word
        return ans

    def decode(self, s: str) -> List[str]:
        print(s)
        ans = []
        i = 0
        while i < len(s):
            if s[i] == "$":
                wordlen = 0
                for j in range(i+1,len(s)):
                    if s[j] == "$":
                        wordlen = int(s[i+1:j])
                        i = j + wordlen
                        break
                ans.append(s[j+1: j+wordlen + 1])
            i += 1
        return ans