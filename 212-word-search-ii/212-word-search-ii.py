from typing import Any, List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def backtrack(i: int, j: int, t: Any, w: List[str]):
            if 0 <= i < n and 0 <= j < m and board[i][j] in t[0]:
                l = board[i][j]
                w.append(l)
                board[i][j] = '#'
                for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                    backtrack(x, y, t[0][l], w)
                board[i][j] = l
                if t[0][l][1]:
                    ans.add("".join(w[::]))
                    if not t[0][l][0]:
                        del t[0][l]
                w.pop()
        
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
            