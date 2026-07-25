class Solution:
    def maxProduct(self, n: int) -> int:
        m1 = 0
        m2 = 0
        while n>0 :
            rem = n%10
            if rem>m1 : 
                m2 = m1
                m1 = rem
            elif rem>m2 :
                m2 = rem
            n = n//10
        return m1*m2
        