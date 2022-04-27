class UF:
    def __init__(self, nodes: list[int]) -> None:
        self.root = {node: node for node in nodes}
        
    def find(self, node) -> None:
        if self.root[node] != node:
            self.root[node] = self.find(self.root[node])
        return self.root[node]

    def union(self, node1: int, node2: int) -> None:
        root1, root2 = self.find(node1), self.find(node2)
        if root1 != root2:
            self.root[root1] = root2
            
    def groups(self) -> List[List[int]]:
        ans = defaultdict(set)
        for k in self.root:
            ans[self.find(k)].add(k)
        return [sorted(v) for v in ans.values()]
            
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        nodes = set()
        for src, dst in pairs:
            nodes.add(dst)
            nodes.add(src)
        
        uf = UF(nodes)
        for src, dst in pairs:
            uf.union(src, dst)
        groups = uf.groups()
        
        slist = list(s)
        for group in groups:
            cgroup = sorted(slist[i] for i in group)
            for i, idx in enumerate(group):
                slist[idx] = cgroup[i]
        return "".join(slist)