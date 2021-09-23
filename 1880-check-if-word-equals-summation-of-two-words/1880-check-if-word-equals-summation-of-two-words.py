class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def toInt(word: str) -> int:
            ans = 0
            for i, c in enumerate(reversed(word)):
                ans += (ord(c) - letterStart) * (10 ** i)
            return ans
        
        letterStart = ord('a')
        return toInt(firstWord) + toInt(secondWord) == toInt(targetWord)