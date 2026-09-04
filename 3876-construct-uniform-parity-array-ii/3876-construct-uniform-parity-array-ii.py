class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        if all(x%2==0 for x in nums1):
            return True
        if all(x%2==1 for x in nums1):
            return True

        odds=[x for x in nums1 if x%2==1]
        evens=[x for x in nums1 if x%2 ==0]

        min_odd=min(odds)
        if all (e>min_odd for e in evens):
            return True
        return False



        # nums2=[]
        # if nums1[0]%2==1:
        #     nums2[0]=nums1[0]
        #     for i in range(1,len(nums1)):
        #         if (nums1[i]%2==0) and ((nums1[i]-nums1[i-1])>0) :
        #             nums2[i]=nums1[i]-nums1[i-1]
        #         else:
        #             nums2[i]=nums1[i]
        # else:
        #     nums2[0]=nums1[0]
        #     for i in range(1,len(nums1)):
        #         if (nums1[i]%2==1) and ((nums1[i]-nums1[i-1])>0) :
        #             nums2[i]=nums1[i]-nums1[i-1]
        #         else:
        #             nums2[i]=nums1[i]
        # return nums2