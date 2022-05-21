class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for src, dst in edges:
            graph[src].append(dst)
            
        nodes, ans = {node for node in range(n)}, set()
        while nodes:
            stack = [nodes.pop()]
            ans.add(stack[-1])
            while stack:
                src = stack.pop()
                for dst in graph[src]:
                    if dst not in nodes:
                        ans.discard(dst)
                    else:
                        nodes.remove(dst)
                        stack.append(dst)
        return ans