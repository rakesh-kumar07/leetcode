class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        op=[]
        for i in range(len(nums)):
            if nums[i]==target:
                op.append(i)
        return op
        