class Solution:
    def replaceDigits(self, s: str) -> str:
        output = []
        for i in range(1, len(s), 2):
            output.append(s[i - 1])
            output.append(chr(ord(s[i - 1]) + int(s[i])))
        if len(s) % 2 == 1:
            output.append(s[-1])
        return "".join(output)
            