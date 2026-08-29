class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            mini = min(nums)
            indx = nums.index(mini)
            nums[indx] *= multiplier
        return nums
        # for i in range (k):
        #     min_val,min_idx=min((val,idx) for idx,val in enumerate(nums))
        #     nums[min_idx]=min_val*multiplier
        # return nums
        