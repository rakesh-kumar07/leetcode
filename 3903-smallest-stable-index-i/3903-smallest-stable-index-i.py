class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        if n==0:
            return -1
        max_num=[0]*n
        curr_max=nums[0]
        for i in range (n):
            curr_max=max(curr_max,nums[i])
            max_num[i]=curr_max
        min_num=[0]*n
        curr_min=nums[-1]
        for i in range (n-1,-1,-1):
            curr_min=min(curr_min,nums[i])
            min_num[i]=curr_min
        for i in range(n):
            if max_num[i]-min_num[i]<=k:
                return i

        return -1