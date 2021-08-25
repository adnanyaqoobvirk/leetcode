class Solution:
    def freqAlphabets(self, s: str) -> str:
        output = []
        start = ord('a') - 1
        for i in range(len(s)):
            if s[i] == '#':
                output.pop()
                output.pop()
                output.append(chr(start + int(s[i - 1]) + int(s[i - 2]) * 10))
            else:
                output.append(chr(start + int(s[i])))
        return "".join(output)