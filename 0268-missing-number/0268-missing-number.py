class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        x=sum(nums)
        n=len(nums)
        s=(n*(n+1))/2
        return int(s-x)      