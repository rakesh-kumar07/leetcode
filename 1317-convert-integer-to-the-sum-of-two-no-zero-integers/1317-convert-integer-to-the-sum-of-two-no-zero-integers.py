class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def zero_fun(x):
            return '0' in str(x)
        for a in range(1,n):
            b=n-a
            if not zero_fun(a) and not zero_fun(b):
                return a,b


