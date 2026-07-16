import math

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefixGcd = []
        mx = nums[0]
        for i in nums:
            mx = max(mx, i)
            prefixGcd.append(math.gcd(i, mx))
        
        prefixGcd.sort()

        total_sum = 0
        left = 0
        right = len(prefixGcd) - 1
        
        while left < right:
            total_sum += math.gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1
            
        return total_sum


