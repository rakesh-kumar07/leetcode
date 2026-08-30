class Solution:
    def numberOfMatches(self, n: int) -> int:
        s=0
        while n>1:
            q=n//2
            s=s+q
            n=n-q
        return s