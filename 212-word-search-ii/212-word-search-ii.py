from typing import Any, List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def backtrack(i: int, j: int, t: Any, w: List[str]):
            if 0 <= i < n and 0 <= j < m and board[i][j] in t[0]:
                w.append(board[i][j])
                nt = t[0][board[i][j]]
                if nt[1]:
                    ans.add("".join(w[::]))
                board[i][j] = '#'
                for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                    backtrack(x, y, nt, w)
                board[i][j] = w.pop()
        
        trie = [{}, False]
        for word in words:
            curr = trie
            for c in word:
                if c not in curr[0]:
                    curr[0][c] = [{}, False]
                curr = curr[0][c]
            curr[1] = True
        
        n, m = len(board), len(board[0])
        ans = set()
        for i in range(n):
            for j in range(m):
                backtrack(i, j, trie, [])
        return list(ans)
            