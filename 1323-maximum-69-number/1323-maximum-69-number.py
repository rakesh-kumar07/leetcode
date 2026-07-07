class Solution:
    def maximum69Number (self, num: int) -> int:
        # x =[]
        # temp_num=num
        # while temp_num > 0:
        #     y= temp_num %10
        #     x.append(y)
        #     temp_num=temp_num//10
        # x.reverse()
        # max_num=0
        # for i in range(len(x)):
        #     if x[i] == 6: 
        #         x[i] =9
        #         break
        # for j in x:
        #     max_num=max_num*10+j


        # # for i in range(0,len(x)):
        # #     new_num =0
        # #     for j in range(0,len(x)):
        # #         if x[i] == 6: 
        # #             x[j] =9
        # #         new_num= new_num+x[j]*10*(len(x)-j-1)
        # #     if new_num[i]>num: 
        # #         max_num=new_num
        # #     else:
        # #         max_num=num
        # return max_num
        result=0
        num_str=str(num)
        for i in range(len(num_str)):
            if num_str[i]=='6':
                new_num=num_str[:i]+'9'+num_str[i+1:]
                num_val=int(new_num)
                if num_val > result:
                    result = num_val
        return result if result!=0 else num




        


             
