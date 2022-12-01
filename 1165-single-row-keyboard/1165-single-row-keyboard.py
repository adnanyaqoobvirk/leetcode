class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        keyboard = {k: i for i, k in enumerate(keyboard)}
        t = curr = 0
        for c in word:
            t += abs(keyboard[c] - curr)
            curr = keyboard[c]
        return t