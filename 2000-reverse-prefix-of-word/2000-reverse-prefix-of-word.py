class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        chp = word.find(ch)
        return word[:chp + 1][::-1] + word[chp + 1:]