class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        ans = 0
        for ch in s:
            if ch is '(':
                count += 1
            if ch is ')':
                count -= 1
            ans = max(ans, count)
        return ans

        