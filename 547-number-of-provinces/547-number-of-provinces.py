class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n, graph = len(isConnected), defaultdict(list)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    graph[i].append(j)

        nodes, ans = {i for i in range(n)}, 0
        while nodes:
            stack = [nodes.pop()]
            while stack:
                src = stack.pop()
                for dst in graph[src]:
                    if dst in nodes:
                        stack.append(dst)
                        nodes.remove(dst)
            ans += 1
        return ans