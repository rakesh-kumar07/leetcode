class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        e_sum=0
        d_sum2=0
        for i in nums:
            d_sum1=0
            n=i
            while n>0:
                rem=n%10
                d_sum1=d_sum1+rem
                n=n//10
            d_sum2=d_sum2+d_sum1
            e_sum=e_sum+i
        return e_sum-d_sum2
        