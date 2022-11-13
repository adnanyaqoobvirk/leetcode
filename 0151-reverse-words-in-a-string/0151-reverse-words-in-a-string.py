class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        for word in reversed(s.split(" ")):
            if word:
                ans.append(word)
        return " ".join(ans)