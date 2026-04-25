class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = []
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        for key,val in freq.items():    
            buckets.append([val,key])
        buckets.sort(reverse = True)
        ans = []
        for i in range(k):
            ans.append(buckets[i][1])
        return ans

