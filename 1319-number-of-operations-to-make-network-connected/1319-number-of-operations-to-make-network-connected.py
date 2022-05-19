class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return - 1
        
        graph = defaultdict(list)
        for src, dst in connections:
            graph[src].append(dst)
            graph[dst].append(src)
            
        computers, ans = {i for i in range(n)}, 0
        while computers:
            stack = [computers.pop()]
            while stack:
                src = stack.pop()
                for dst in graph[src]:
                    if dst in computers:
                        stack.append(dst)
                        computers.remove(dst)
            ans += 1
        return ans - 1