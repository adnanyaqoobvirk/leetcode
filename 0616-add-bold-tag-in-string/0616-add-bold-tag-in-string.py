class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        trie = {}
        for word in words:
            t = trie
            for c in word:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t["#"] = {}
        
        n, intervals = len(s), []
        for i in range(n):
            t = trie
            for j in range(i, n):
                if s[j] not in t:
                    break
                    
                t = t[s[j]]
                
                if '#' in t:
                    if intervals and i - 1 <= intervals[-1][1]:
                        intervals[-1][1] = max(j, intervals[-1][1])
                    else:
                        intervals.append([i, j])
                        
        ans, prev = [], 0
        for start, end in intervals:
            ans.append(s[prev:start])
            ans.append("<b>")
            ans.append(s[start:end + 1])
            ans.append("</b>")
            prev = end + 1
            
        if prev < n:
            ans.append(s[prev:])
            
        return "".join(ans)