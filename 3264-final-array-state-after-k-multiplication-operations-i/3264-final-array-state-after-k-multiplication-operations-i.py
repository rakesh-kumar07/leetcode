class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            mini = min(nums)
            indx = nums.index(mini)
            nums[indx] *= multiplier
        return nums
        