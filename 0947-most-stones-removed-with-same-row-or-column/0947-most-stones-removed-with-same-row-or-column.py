class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rmap = defaultdict(list)
        cmap = defaultdict(list)
        for i, (r, c) in enumerate(stones):
            rmap[r].append(i)
            cmap[c].append(i)
        
        nodes = set(tuple(e) for e in stones)
        ans = 0
        while nodes:
            q = [nodes.pop()]
            count = 0
            while q:
                nq = []
                for node in q:
                    for i in rmap[node[0]]:
                        stone = tuple(stones[i])
                        if node != stone and stone in nodes:
                            nq.append(stone)
                            nodes.remove(stone)
                    for i in cmap[node[1]]:
                        stone = tuple(stones[i])
                        if node != stone and stone in nodes:
                            nq.append(stone)
                            nodes.remove(stone)
                    count += 1
                q = nq
            ans += count - 1
        return ans
        