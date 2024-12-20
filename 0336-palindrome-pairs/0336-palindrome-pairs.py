class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def dfs(t1: dict, t2: dict) -> None:
            if "#" in t1 and "#" in t2 and t1["#"] != t2["#"]:
                ans.append([t1["#"], t2["#"]])
            if "#" in t1 and "pp" in t2:
                for i in t2["pp"]:
                    if t1["#"] != i:
                        ans.append([t1["#"], i])
            if "#" in t2 and "pp" in t1:
                for i in t1["pp"]:
                    if t2["#"] != i:
                        ans.append([i, t2["#"]])

            for k in t1:
                if k != "#" and k != "pp" and k in t2:
                    dfs(t1[k], t2[k])
        
        trie1 = {}
        for i, word in enumerate(words):
            t = trie1
            pc = ""
            pt = t
            for c in word:
                if pc != c:
                    pc = c
                    pt = t
                if c not in t:
                    t[c] = {}
                t = t[c]
            t["#"] = i
            if "pp" not in pt:
                pt["pp"] = []
            pt["pp"].append(i)
        
        trie2 = {}
        for i, word in enumerate(words):
            t = trie2
            pc = ""
            pt = t
            for c in reversed(word):
                if pc != c:
                    pc = c
                    pt = t
                if c not in t:
                    t[c] = {}
                t = t[c]
            t["#"] = i
            if "pp" not in pt:
                pt["pp"] = []
            pt["pp"].append(i)
        
        ans = []
        dfs(trie1, trie2)
        return ans