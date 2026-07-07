class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge_num=nums1+nums2
        merge_num.sort()
        if len(merge_num)%2 ==1:
            return merge_num[int((len(merge_num)/2)-0.5)]
        else:
            return (merge_num[int((len(merge_num)/2)-1)] + merge_num[int((len(merge_num)/2))])/2