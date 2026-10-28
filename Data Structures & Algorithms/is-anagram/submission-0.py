class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        alphabetCounter = [0]*26
        for i in range(len(s)):
            alphabetCounter[ord(s[i]) - ord('a')] += 1
            alphabetCounter[ord(t[i]) - ord('a')] -= 1

        for val in alphabetCounter:
            if val != 0:
                return False
        return True


        