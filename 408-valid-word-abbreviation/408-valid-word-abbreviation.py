class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        digits = set(string.digits)
        m, n = len(word), len(abbr)
        
        j = l = 0
        for i in range(n):
            if abbr[i] in digits:
                if abbr[i] == '0' and l == 0:
                    return False
                
                l = l * 10 + int(abbr[i])
                continue
            
            if l > 0:
                j += l
                l = 0
                
            if j >= m or word[j] != abbr[i]:
                return False
            
            j += 1
            
        if l > 0:
            j += l
            
        return j == m