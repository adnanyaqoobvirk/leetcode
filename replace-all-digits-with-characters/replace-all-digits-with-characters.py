class Solution:
    def replaceDigits(self, s: str) -> str:
        output = list(s)
        for i in range(1, len(s), 2):
            output[i] = chr(ord(s[i - 1]) + int(s[i]))
        return "".join(output)