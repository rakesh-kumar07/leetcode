class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        my_lst=sorted(list(set(arr)))
        d = {}
        for i,j in enumerate(my_lst, 1):
            d[j]=i
        return [d[num] for num in arr]

