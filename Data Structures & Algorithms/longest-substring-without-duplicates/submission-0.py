class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        i = 0
        maxlength = 0

        for j in range(len(s)):
            while s[j] in seen:      # shrink until s[j] is no longer a duplicate
                seen.remove(s[i])
                i += 1
            seen.add(s[j])
            maxlength = max(maxlength, j - i + 1)

        return maxlength