class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        
        vowels = {"a", "e", "i", "o", "u"}
        hasVowel = False
        hasCons = False
        for c in word:
            if c.isalpha():
                if c.lower() in vowels:
                    hasVowel = True
                else:
                    hasCons = True
            elif not c.isdigit():
                return False
        return hasVowel and hasCons