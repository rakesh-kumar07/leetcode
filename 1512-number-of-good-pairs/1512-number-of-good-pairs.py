from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = Counter(nums)
        pairs = 0        
        for count in counts.values():
            pairs += count * (count - 1) // 2          
        return pairs