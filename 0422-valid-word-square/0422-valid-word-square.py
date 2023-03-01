class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        n = len(words)
        for i in range(n):
            if len(words[i]) > n:
                return False
            for j in range(len(words[i])):
                if i >= len(words[j]) or words[i][j] != words[j][i]:
                    return False
        return True