class Solution:
    def mirrorDistance(self, n: int) -> int:
        j=0
        n1=n
        while n>0:
            i=n%10
            j=j*10+i
            n=n//10
        return abs(j-n1)