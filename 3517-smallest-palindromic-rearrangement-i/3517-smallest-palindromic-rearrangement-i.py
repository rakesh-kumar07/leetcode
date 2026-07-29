class Solution:
    def smallestPalindrome(self, s: str) -> str:
        s=sorted(s)
        n=len(s)
        half=[]
        mid=''
        i=0
        while i<n:
            j=i
            while j<n and s[j]==s[i]:
                j=j+1
            cnt=j-i
            if cnt%2:
                mid=s[i]
            half.append(s[i]*(cnt//2))
            i=j
        half_str=''.join(half)
        return half_str+mid+half_str[::-1]
            
        