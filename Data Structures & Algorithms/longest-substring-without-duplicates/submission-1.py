class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        i = 0
        maxlength = 0
        for j in range(len(s)):
            if s[j] in seen:
                i = max(seen[s[j]] + 1, i)
            seen[s[j]] = j
            maxlength = max(maxlength, j-i+1)
        return maxlength
            