class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        n = len(folder)
        trie = {"#": []}
        for i in range(n):
            t = trie
            for f in folder[i].split("/"):
                if not f:
                    continue
                if f not in t:
                    t[f] = {"#": []}
                t = t[f]
                t["#"].append(i)
        
        res = set(list(range(n)))
        for i in range(n):
            t = trie
            for c in folder[i].split("/"):
                if not c:
                    continue
                t = t[c]
            for j in t["#"]:
                if i != j:
                    res.discard(j)
        
        return [folder[i] for i in res]