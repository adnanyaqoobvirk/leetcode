class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def helper(i: int, j: int, t: dict) -> None:
            if '#' in t:
                ans.append(t['#'])
                del t['#']
            
            if i < 0 or j < 0 or i >= m or j >= n:
                return
            
            if (i, j) in seen or board[i][j] not in t:
                return
            
            seen.add((i, j))
            for a, b in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                helper(a, b, t[board[i][j]])
            seen.remove((i, j))
            
            if not t[board[i][j]]:
                del t[board[i][j]]
        
        trie = {}
        for word in words:
            t = trie
            for c in word:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t['#'] = word
        
        m, n = len(board), len(board[0])
        ans = []
        for x in range(m):
            for y in range(n):
                seen = set()
                helper(x, y, trie)
        return ans