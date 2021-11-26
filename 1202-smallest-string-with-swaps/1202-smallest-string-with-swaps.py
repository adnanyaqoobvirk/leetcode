class DisjointSet:
    def __init__(self: 'DisjointSet', n: int) -> None:
        self.nodes = [-1 for _ in range(n)]
    
    def find(self: 'DisjoinSet', x: int) -> int:
        if self.nodes[x] >= 0:
            self.nodes[x] = self.find(self.nodes[x])
            return self.nodes[x]
        else:
            return x

    def union(self: 'DisjoinSet', x: int, y: int) -> None:
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.nodes[px] < self.nodes[py]:
                self.nodes[py] = px
            elif self.nodes[px] > self.nodes[py]:
                self.nodes[px] = py
            else:
                self.nodes[px] = py
                self.nodes[py] -= 1
                
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        ds = DisjointSet(len(s))
        for i, j in pairs:
            ds.union(i, j)
        
        imap = defaultdict(list)
        for i in range(len(s)):
            imap[ds.find(i)].append(s[i])
        for k in imap:
            imap[k].sort(reverse=True)
        
        ans = []
        for i in range(len(s)):
            ans.append(imap[ds.find(i)].pop())
        return "".join(ans)