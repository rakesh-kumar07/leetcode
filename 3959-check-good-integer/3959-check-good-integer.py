class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        diff = 0
        while n > 0:
            d = n % 10
            diff += d * d - d
            n //= 10
        return diff >= 50