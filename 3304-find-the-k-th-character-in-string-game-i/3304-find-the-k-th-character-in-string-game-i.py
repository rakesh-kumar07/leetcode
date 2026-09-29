class Solution:
    def kthCharacter(self, k: int) -> str:
        shift = (k - 1).bit_count()
        return chr(ord('a') + shift)