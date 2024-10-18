class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        char_map = {}
        for i, c in enumerate(order):
            char_map[c] = i
        
        for i in range(1, len(words)):
            j = 0
            n = min(len(words[i]), len(words[i - 1]))
            while j < n:
                c1, c2 = words[i - 1][j], words[i][j]
                if c1 == c2:
                    j += 1
                elif char_map[c1] > char_map[c2]:
                    return False
                else:
                    break
            else:
                if len(words[i - 1]) > len(words[i]):
                    return False
        return True
            

            