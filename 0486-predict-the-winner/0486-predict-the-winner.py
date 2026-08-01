class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        # dp[i] will store the maximum net score difference player 1 can achieve
        # for subarray nums[i...j]
        dp = nums.copy()
        
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i] = max(nums[i] - dp[i + 1], nums[j] - dp[i])
                
        return dp[0] >= 0