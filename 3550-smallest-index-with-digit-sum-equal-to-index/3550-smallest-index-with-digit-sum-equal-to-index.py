class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range (len(nums)):
            tot = sum(int(digit) for digit in str(nums[i]))
            if tot==i:
                return i
        return -1
                
        