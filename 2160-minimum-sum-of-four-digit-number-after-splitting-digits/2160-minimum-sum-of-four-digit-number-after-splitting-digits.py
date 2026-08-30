class Solution:
    def minimumSum(self, num: int) -> int:
        digits = sorted(str(num))
        return (int(digits[0]) + int(digits[1])) * 10 + int(digits[2]) + int(digits[3])