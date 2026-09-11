class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n=len(digits)
        nums=set()
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i!=j and j!=k and i!=k:
                        h,t,u=digits[i],digits[j],digits[k]
                        if h!=0 and u%2==0:
                            nums.add((h,t,u))
        return len(nums)
        