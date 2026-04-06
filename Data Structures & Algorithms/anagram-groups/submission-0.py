class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for word in strs:
            hmap["".join(sorted(word))].append(word)
        ans = []
        for ele in hmap.values():
            ans.append(ele)
        print(ans)
        return ans