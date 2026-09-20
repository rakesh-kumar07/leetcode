class Solution:
    def reverseDegree(self, s: str) -> int:
        total_sum = 0
        for i, ch in enumerate(s, start=1):
            # 'a' -> 26, 'b' -> 25, ..., 'z' -> 1
            reversed_alphabet_idx = 26 - (ord(ch) - ord('a'))
            total_sum += reversed_alphabet_idx * i
        return total_sum