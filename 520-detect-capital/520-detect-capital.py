class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        
        if ord(word[0]) < 97:
            if ord(word[1]) < 97:
                for i in range(2, len(word)):
                    if ord(word[i]) >= 97:
                        return False
                return True
            else:
                for i in range(2, len(word)):
                    if ord(word[i]) < 97:
                        return False
                return True
        else:
            for i in range(len(word)):
                if ord(word[i]) < 97:
                    return False
            return True