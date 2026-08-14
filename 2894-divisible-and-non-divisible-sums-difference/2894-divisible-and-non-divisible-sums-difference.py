class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        tot1=0
        tot2=0
        for i in range(n+1):
            if i%m!=0:
                tot1+=i
            else:
                tot2+=i
        return tot1-tot2
        