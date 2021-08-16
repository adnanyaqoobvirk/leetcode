class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        output = []
        word_count = 0
        for i in range(len(s)):
            if s[i] == ' ':
                word_count += 1
                if word_count == k:
                    break
            output.append(s[i])
        return "".join(output)