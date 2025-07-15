class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        def backtrack(pos: int) -> None:
            if len(square) == n:
                res.append(square[::])
            else:
                t = trie
                for w in square:
                    if w[pos] not in t:
                        return
                    t = t[w[pos]]

                for w in t["#"]:
                    square.append(w)
                    backtrack(pos + 1)
                    square.pop()
        
        if not words:
            return []

        n = len(words[0])

        trie = {"#": words}
        for w in words:
            t = trie
            for c in w:
                if c not in t:
                    t[c] = {"#": []}
                t = t[c]
                t["#"].append(w)
        
        square = []
        res = []
        backtrack(0)
        return res