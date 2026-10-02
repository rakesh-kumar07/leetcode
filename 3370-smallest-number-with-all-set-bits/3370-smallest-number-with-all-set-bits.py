class Solution:
    def smallestNumber(self, n: int) -> int:
        binary= bin(n)
        length=len(binary)
        new_binary="1"*(length-2)
        return int(new_binary,2)