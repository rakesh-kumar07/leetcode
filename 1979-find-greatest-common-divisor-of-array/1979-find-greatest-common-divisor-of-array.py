class Solution:
    def findGCD(self, nums: List[int]) -> int:
        x,y=min(nums),max(nums)
        while y != 0:
            x,y = y, x % y
        return abs(x)
        