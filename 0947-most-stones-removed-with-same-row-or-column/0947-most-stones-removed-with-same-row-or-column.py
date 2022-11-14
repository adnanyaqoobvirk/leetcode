class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        
        graph = defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    graph[i].append(j)
                    graph[j].append(i)
        
        subgraphs = 0
        unseen = set(range(n))
        while unseen:
            stack = [unseen.pop()]
            while stack:
                node = stack.pop()
                for neighbor in graph[node]:
                    if neighbor in unseen:
                        stack.append(neighbor)
                        unseen.remove(neighbor)
            subgraphs += 1
        return n - subgraphs