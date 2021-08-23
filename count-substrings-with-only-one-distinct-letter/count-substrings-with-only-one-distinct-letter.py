class Solution:
    def countLetters(self, s: str) -> int:
        c = s[0]
        n = 1
        count = 0
        for i in range(1, len(s)):
            if c == s[i]:
                n += 1
            else:
                count += (n * (n + 1) // 2)
                n = 1
                c = s[i]
        return count + (n * (n + 1) // 2)