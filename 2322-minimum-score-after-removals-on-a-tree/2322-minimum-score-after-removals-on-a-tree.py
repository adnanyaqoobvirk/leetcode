class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        def dfs(curr: int) -> int:
            xor = nums[curr]
            for nei in graph[curr]:
                if nei not in seen:
                    seen.add(nei)
                    xor ^= dfs(nei)
            l.append(xor)
            return xor

        graph = defaultdict(list)
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)
        
        res = inf
        for src, dst in edges:
            seen = {src, dst}
            l = []
            sxor = dfs(src)
            slist = l
            seen = {src, dst}
            l = []
            dxor = dfs(dst)
            dlist = l
            for i in range(len(slist) - 1):
                x = slist[i]
                res = min(res, max(x, sxor ^ x, dxor) - min(x, sxor ^ x, dxor))
            for i in range(len(dlist) - 1):
                x = dlist[i]
                res = min(res, max(x, sxor, dxor ^ x) - min(x, sxor, dxor ^ x))
        return res