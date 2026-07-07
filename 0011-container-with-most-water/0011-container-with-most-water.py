class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        max_A=0
        while i<j:
            h=min(height[i],height[j])
            b=j-i
            A=h*b
            max_A=max(max_A,A)

            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return max_A



        # area=[]
        # b=0
        # max_A=0
        # for i in range (len(height)-1):
        #     h1=height[i]
        #     for j in range (len(height)-i):
        #         # j=j+i+1               
        #         h2=height[j+i]
        #         h=min(h1,h2)
        #         b=(j+i)-i
        #         A=h*b
        #         if A>max_A:
        #             max_A=A
        #     area.append(max_A)
        # return max(area)



        