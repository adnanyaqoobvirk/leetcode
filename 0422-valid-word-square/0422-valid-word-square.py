class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for i, word in enumerate(words):
            if len(word) > len(words):
                return False
            
            for j in range(len(word)):
                if i >= len(words[j]) or words[j][i] != word[j]:
                    return False
        return True
                