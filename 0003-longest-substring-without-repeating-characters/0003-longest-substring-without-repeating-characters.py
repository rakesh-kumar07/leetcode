class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start =0
        seen = {}
        max_len=0
        max_sub=""
        for end,char in enumerate(s):
            if char in seen and seen[char]>=start:
                start = seen[char]+1
            seen[char]=end

            if end-start+1>max_len:
                max_len=end-start+1
                max_sub=s[start:end+1]
        return max_len