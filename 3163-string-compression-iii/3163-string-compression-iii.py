class Solution:
    def compressedString(self, word: str) -> str:
        ans = []
        count = 0
        char = word[0]
        for c in word:
            if c == char and count < 9:
                count += 1
                continue
            ans.append(str(count))
            ans.append(char)
            count = 1
            char = c
        ans.append(str(count))
        ans.append(char)
        return "".join(ans)