class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        n = len(pattern)
        
        ans = []
        for word in words:
            pchar_map, wchar_map = {}, {}
            for i in range(n):
                if word[i] in wchar_map and wchar_map[word[i]] != pattern[i]:
                    break
                
                if pattern[i] in pchar_map and pchar_map[pattern[i]] != word[i]:
                    break
                    
                wchar_map[word[i]] = pattern[i]
                pchar_map[pattern[i]] = word[i]
            else:
                ans.append(word)
        return ans