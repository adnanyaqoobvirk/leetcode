class Solution:
    def hasSameDigits(self, s: str) -> bool:
        chars = list(s)
        while len(chars) > 2:
            nchars = []
            for i in range(1, len(chars)):
                nchars.append(str((int(chars[i]) + int(chars[i - 1])) % 10))
            chars = nchars
        return chars[0] == chars[1]