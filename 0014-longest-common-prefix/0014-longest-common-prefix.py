class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = {}
        for s in strs:
            if not s: return ""
            
            t = trie
            for c in s:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t["#"] = True
        
        prefix = []
        t = trie
        while "#" not in t and len(t) == 1:
            c = next(iter(t))
            prefix.append(c)
            t = t[c]
        return "".join(prefix)
            