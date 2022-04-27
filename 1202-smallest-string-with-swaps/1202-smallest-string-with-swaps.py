class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        def helper(node: int) -> None:
            for child in graph[node]:
                if child not in seen:
                    seen.add(child)
                    unseen.remove(child)
                    helper(child)
        
        graph, unseen = defaultdict(list), set()
        for src, dst in pairs:
            graph[src].append(dst)
            graph[dst].append(src)
            unseen.add(dst)
            unseen.add(src)
        
        groups = []
        while unseen:
            seen = {unseen.pop()}
            helper(next(iter(seen)))
            groups.append(sorted(seen))
        
        slist = list(s)
        for group in groups:
            cgroup = sorted(slist[i] for i in group)
            for i, idx in enumerate(group):
                slist[idx] = cgroup[i]
        return "".join(slist)
        
        