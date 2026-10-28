class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s      # "neet" -> "4#neet"
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":                   # read digits up to the '#'
                j += 1
            length = int(s[i:j])                 # the word's length
            result.append(s[j + 1 : j + 1 + length])  # take exactly that many chars
            i = j + 1 + length                   # jump to the next length
        return result