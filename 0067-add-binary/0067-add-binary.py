class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a)>len(b):
            b=(len(a)-len(b))*"0"+b
        else:
            a=(len(b)-len(a))*"0"+a
        
        result = []
        carry = 0

        for i in range(len(a)-1,-1,-1):
            total=int(a[i])+int(b[i])+carry
            result.append(str(total%2))
            carry=total//2
        if carry:
            result.append(str(carry))
        return "".join(reversed(result))



        