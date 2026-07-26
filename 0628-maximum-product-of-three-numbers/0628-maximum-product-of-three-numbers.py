class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # nums.sort()
        m1=-1001
        m2=-1001
        m3=-1001 
        min1=1001
        min2=1001

        for i in range(len(nums)):
            if nums[i]>m1:
                m3=m2
                m2=m1
                m1=nums[i]
            elif nums[i]>m2:
                m3=m2
                m2=nums[i]
            elif nums[i]>m3:
                m3=nums[i]
            
            if nums[i]<min1:
                min2=min1
                min1=nums[i]
            elif nums[i]<min2:
                min2=nums[i]
        return max(m1*m2*m3,min1*min2*m1)
        # return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])