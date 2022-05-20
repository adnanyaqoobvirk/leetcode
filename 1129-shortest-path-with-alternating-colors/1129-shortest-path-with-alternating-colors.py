class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        RED, BLUE = 0, 1
        graph, q = defaultdict(lambda: [[],[]]), []
        for src, dst in redEdges:
            graph[src][0].append(dst)
            if len(q) < 1 and src == 0:
                q.append((src, BLUE))
        for src, dst in blueEdges:
            graph[src][1].append(dst)
            if len(q) < 2 and src == 0:
                q.append((src, RED))
        
        ans, seen = [-1] * n, set()
        ans[0] = level = 0
        while q:
            nq = []
            for src, color in q:
                if ans[src] == -1:
                    ans[src] = level
                if color == BLUE:
                    for dst in graph[src][RED]:
                        if (src, dst, RED) not in seen:
                            seen.add((src, dst, RED))
                            nq.append((dst, RED))
                else: 
                    for dst in graph[src][BLUE]:
                        if (src, dst, BLUE) not in seen:
                            seen.add((src, dst, BLUE))
                            nq.append((dst, BLUE))
            level += 1
            q = nq
        return ans
                