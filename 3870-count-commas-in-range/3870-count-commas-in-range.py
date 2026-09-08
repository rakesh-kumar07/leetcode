class Solution:
    def countCommas(self, n: int) -> int:
        return max(n-999,0)
        # return n-1000+1 if n>=1000 else 0