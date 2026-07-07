class Solution:
    def reverse(self, x: int) -> int:
        # num=str(x)
        # if num[0]=='-':
        #     # y= num[1:][::-1]
        #     y = int(num[1:][::-1].strip())*(-1)
            
        # else:
        #     y= int(num[::-1])

        sign =-1 if x<0 else 1
        x_abs=abs(x)
        y=int(str(x_abs)[::-1])*sign

        if y<-2**31 or y>2**31-1:
            return 0
        else:
            return y

        # rev=0
        # sign =-1 if x<0 else 1
        # x=abs(x)
        # while x!=0:
        #     pop=x%10
        #     x//=10

        #     if rev>(2**31-1)//10 or (rev==(2**31-1)//10 and pop>7):
        #         return 0
        #     if rev<(-2**31-1)//10 or (rev==(-2**31-1)//10 and pop>8):
        #         return 0
        #     rev=rev*10+pop
        # return rev*sign
