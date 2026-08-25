class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        num_set=set(nums)
        mul=k
        while mul in num_set:
            mul=mul+k
        return mul