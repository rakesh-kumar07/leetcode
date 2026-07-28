class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        x=sorted(nums)
        return (x[-1]-1)*(x[-2]-1)