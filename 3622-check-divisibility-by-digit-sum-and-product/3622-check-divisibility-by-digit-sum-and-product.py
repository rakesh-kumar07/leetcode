class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s=0
        p=1
        n1=n
        while n>0:
            rem=n%10
            s=s+rem
            p=p*rem
            n=n//10
        if n1%(s+p)==0:
            return True
        else:
            return False        