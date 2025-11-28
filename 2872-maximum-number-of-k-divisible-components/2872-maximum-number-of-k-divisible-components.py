class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        if n < 2:
            return 1
            
        graph = defaultdict(list)
        outdegree = defaultdict(int)
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)
            outdegree[src] += 1
            outdegree[dst] += 1
        
        count = 0
        q = [i for i in range(n) if outdegree[i] == 1]
        while q:
            nq = []
            for node in q:
                m = values[node] % k
                if m == 0:
                    count += 1
                for parent in graph[node]:
                    if outdegree[parent] <= 1:
                        continue
                    outdegree[parent] -= 1
                    values[parent] += m
                    if outdegree[parent] == 1:
                        nq.append(parent)
            q = nq
        return count
