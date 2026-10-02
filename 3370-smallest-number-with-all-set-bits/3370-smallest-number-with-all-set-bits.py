class Solution:
    def smallestNumber(self, n: int) -> int:
        length=n.bit_length()
        return (1<<length)-1