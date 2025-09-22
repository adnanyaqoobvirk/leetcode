class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        n = len(username)
        visits = sorted((timestamp[i], username[i], website[i]) for i in range(n))

        umap = defaultdict(list)
        for t, u, w in visits:
            umap[u].append(w)
        
        counts = defaultdict(int)
        max_count = 0
        for u, ws in umap.items():
            m = len(ws)
            for i in range(m):
                for j in range(i + 1, m):
                    for k in range(j + 1, m):
                        pattern = (ws[i], ws[j], ws[k])
                        counts[pattern] += 1
                        max_count = max(max_count, counts[pattern])
        
        top_patterns = []
        for pattern, cnt in counts.items():
            if cnt == max_count:
                top_patterns.append(pattern)
        return sorted(top_patterns)[0]
            