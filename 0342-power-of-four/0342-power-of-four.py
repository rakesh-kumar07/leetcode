class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # return n>0 and 64 % n ==0
        return n>0 and n!=2 and n!=8 and n!=32 and n!=128 and n!=512 and n!=2048 and n!=8192 and n!=32768 and n!=131072 and n!=524288 and n!=2097152 and n!=8388608 and n!=33554432 and n!=134217728 and n!=536870912 and 1073741824 % n ==0