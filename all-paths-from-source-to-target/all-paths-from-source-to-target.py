class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def recurse(pos: int, path: List[int]) -> None:
            if pos == len(graph) - 1:
                paths.append(path[::])
            else:
                for node in graph[pos]:
                    path.append(node)
                    recurse(node, path)
                    path.pop()
        paths = []
        recurse(0, [0])
        return paths