class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def backtrack(a: int, b: int, t: dict) -> None:
            if "#" in t:
                ans.append(t["#"])
                del t["#"]
            
            for x, y in [(a + 1, b), (a - 1, b), (a, b + 1), (a, b - 1)]:
                if 0 <= x < m and 0 <= y < n and board[x][y] in t and (x, y) not in seen:
                    seen.add((x, y))
                    backtrack(x, y, t[board[x][y]])
                    if not t[board[x][y]]:
                        del t[board[x][y]]
                    seen.remove((x, y))

        trie = {}
        for word in words:
            t = trie
            for c in word:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t["#"] = word
        
        ans = []
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    seen = {(i, j)}
                    backtrack(i, j, trie[board[i][j]])
        return ans