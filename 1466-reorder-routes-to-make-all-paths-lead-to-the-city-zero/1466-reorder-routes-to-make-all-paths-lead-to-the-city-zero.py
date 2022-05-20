class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        for src, dst in connections:
            graph[src].append((dst, True))
            graph[dst].append((src, False))
        
        stack, seen, ans = [0], set(), 0
        while stack:
            src = stack.pop()
            seen.add(src)
            for dst, forward in graph[src]:
                if dst not in seen:
                    if forward:
                        ans += 1
                    stack.append(dst)
        return ans