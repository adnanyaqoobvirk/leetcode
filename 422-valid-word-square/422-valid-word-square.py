class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for i, word in enumerate(words):
            for j, c in enumerate(word):
                if j >= len(words) or i >= len(words[j]) or words[j][i] != c:
                    return False
        return True