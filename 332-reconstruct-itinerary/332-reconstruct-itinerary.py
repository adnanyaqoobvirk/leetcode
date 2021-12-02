class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def backtrack(src: str) -> bool:
            if len(ans) == len(tickets) + 1:
                return True
            
            for i, dst in enumerate(graph[src]):
                if not visited[src][i]:
                    visited[src][i] = True
                    ans.append(dst)
                    if backtrack(dst):
                        return True
                    visited[src][i] = False
                    ans.pop()
            return False
        
        visited = defaultdict(list)
        graph = defaultdict(list)
        for src, dst in tickets:
            graph[src].append(dst)
            visited[src].append(False)
            
        for k, v in graph.items():
            v.sort()
        
        ans = ['JFK']
        backtrack('JFK')
        return ans