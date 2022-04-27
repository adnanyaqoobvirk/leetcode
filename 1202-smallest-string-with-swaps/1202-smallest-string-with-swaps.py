class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        graph, unseen = defaultdict(list), set()
        for src, dst in pairs:
            graph[src].append(dst)
            graph[dst].append(src)
            unseen.add(dst)
            unseen.add(src)
        
        groups = []
        while unseen:
            group = [unseen.pop()]
            q = [group[0]]
            while q:
                nq = []
                for node in q:
                    for child in graph[node]:
                        if child in unseen:
                            group.append(child)
                            unseen.remove(child)
                            nq.append(child)
                q = nq
            groups.append(sorted(group))
        
        slist = list(s)
        for group in groups:
            cgroup = sorted(slist[i] for i in group)
            for i, idx in enumerate(group):
                slist[idx] = cgroup[i]
        return "".join(slist)
        
        