class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)
        N=n*n
        s_actual=0
        p_actual=0
        for row in grid:
            for val in row:
                s_actual +=val
                p_actual +=val*val

        s_expected =N*(N+1)//2
        p_expected = N*(N+1)*(2*N+1)//6

        d1=s_actual-s_expected
        d2=p_actual-p_expected

        sum_ab=d2//d1

        a=(d1 + sum_ab)//2
        b=a-d1

        return[a,b]