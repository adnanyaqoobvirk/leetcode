class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def helper(pos: int) -> None:
            if pos == n:
                ans.append(path[::])
            else:
                for i in graph[pos]:
                    path.append(i)
                    helper(i)
                    path.pop()
        n, ans, path = len(graph) - 1, [], [0]
        helper(0)
        return ans