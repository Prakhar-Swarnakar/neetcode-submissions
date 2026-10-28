class Solution:
    def isPalindrome(self, s: str) -> bool:
        last = len(s)-1
        i=0
        while(i<last):
            if not s[i].isalnum():
                i += 1
            elif not s[last].isalnum():
                last -= 1
            elif s[i].lower() == s[last].lower():
                i += 1
                last -= 1
            else:
                return False
        return True