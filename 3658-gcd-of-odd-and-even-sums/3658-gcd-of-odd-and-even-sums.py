class Solution:
    def gcd(a,b):
        while b!=0:
            a,b=b,a%b
        return a
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd=n**2
        sumEven=n*(n+1)
        
        return(gcd(sumOdd,sumEven))
