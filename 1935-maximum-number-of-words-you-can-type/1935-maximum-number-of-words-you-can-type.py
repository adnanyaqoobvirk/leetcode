class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        ans = 0
        for word in map(set, text.split(" ")):
            for bl in brokenLetters:
                if bl in word:
                    break
            else:
                ans += 1
        return ans
            