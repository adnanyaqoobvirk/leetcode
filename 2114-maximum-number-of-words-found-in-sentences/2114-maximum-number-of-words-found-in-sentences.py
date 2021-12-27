class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = 0
        for s in sentences:
            wcount = 1
            for c in s:
                if c == " ":
                    wcount += 1
            ans = max(ans, wcount)
        return ans