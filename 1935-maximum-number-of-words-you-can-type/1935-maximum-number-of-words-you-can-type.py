class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        brokenLetters = set(list(brokenLetters))
        valid = True
        ans = 0
        for c in chain(text, " "):
            if c == " ":
                if valid:
                    ans += 1
                valid = True
            elif c in brokenLetters:
                valid = False
        return ans