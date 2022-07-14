class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        char_map = {c: i for i, c in enumerate(order)}
        for i in range(1, len(words)):
            for j in range(min(len(words[i]), len(words[i - 1]))):
                if words[i][j] == words[i - 1][j]:
                    continue
                
                if char_map[words[i - 1][j]] > char_map[words[i][j]]:
                    return False
                else:
                    break
            else:
                if len(words[i]) < len(words[i - 1]):
                    return False
        return True
                    