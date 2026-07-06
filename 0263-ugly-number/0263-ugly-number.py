class Solution:
    def isUgly(self, n: int) -> bool:
        if n<1:
            return False
        f=[2,3,5]
        for i in f:
            while n%i==0:
                n//=i
        return n ==1
        