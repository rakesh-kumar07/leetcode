class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr1=sorted(arr)
        if len(arr1)==2:
            return True
        diff=abs(arr1[0]-arr1[1])
        for i in range(len(arr1)-1):
            if abs(arr1[i]-(arr1[i+1])) != diff:
                return False
            
        return True
        