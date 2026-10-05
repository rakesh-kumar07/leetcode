class Solution:

    def canAliceWin(self, nums: list[int]) -> bool:
        single_digit_sum = sum(x for x in nums if x < 10)
        double_digit_sum = sum(x for x in nums if x >= 10)

        # Alice wins if either single-digit or double-digit sum is strictly greater than the other
        return single_digit_sum != double_digit_sum