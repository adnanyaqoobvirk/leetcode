from typing import Any, List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def backtrack(i: int, j: int, t: Any, w: List[str]):
            if 0 <= i < n and 0 <= j < m and board[i][j] in t:
                l = board[i][j]
                w.append(l)
                board[i][j] = '#'
                for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                    backtrack(x, y, t[l], w)
                board[i][j] = l
                if t[l].get('$', False):
                    ans.add("".join(w[::]))
                    if len(t[l]) == 1:
                        t.pop(l)
                w.pop()
        
        trie = {}
        for word in words:
            curr = trie
            for c in word:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            curr['$'] = True
        
        n, m = len(board), len(board[0])
        ans = set()
        for i in range(n):
            for j in range(m):
                backtrack(i, j, trie, [])
        return list(ans)
            