class Solution:
    def pivotInteger(self, n: int) -> int:
        total_sum=0
        curr_sum=0
        if n==1:
            return 1
        for i in range(n,1,-1):
            curr_sum=(i*(i+1))//2
            total_sum=total_sum+i
            if curr_sum==total_sum:
                return i
        return -1
