class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        def dfs(pos: int) -> None:
            if len(comb) == 4:
                ans.append(comb[::])
            else:
                t = trie
                for i in range(pos):
                    if comb[i][pos] not in t:
                        return
                    t = t[comb[i][pos]]
                for word in t["#"]:
                    comb.append(word)
                    dfs(pos + 1)
                    comb.pop()

        trie = {"#": []}
        for word in words:
            t = trie
            t["#"].append(word)
            for c in word:
                if c not in t:
                    t[c] = {"#": []}
                t = t[c]
                t["#"].append(word)

        ans = []
        comb = []
        dfs(0)
        return ans