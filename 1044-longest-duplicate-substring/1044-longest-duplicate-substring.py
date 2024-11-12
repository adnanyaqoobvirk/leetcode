class Solution:
    def longestDupSubstring(self, s: str) -> str:
        def suffixArray(indices: List[int], order: int) -> List[int]:
            buckets = defaultdict(list)
            for i in indices:
                buckets[s[i:i + order]].append(i)
            
            res = []
            for b in buckets.keys():
                if len(buckets[b]) > 1:
                    res.extend(suffixArray(buckets[b], order * 2))
                else:
                    res.append(buckets[b][0])
            return res

        n = len(s)
        sa = suffixArray(list(range(n)), 1)
        
        ranks = [0] * n
        for i in range(n):
            ranks[sa[i]] = i

        idx = None
        max_k = k = 0
        for i in range(n):
            if ranks[i] == n - 1:
                k = 0
                continue
            
            j = sa[ranks[i] + 1]
            while i + k < n and j + k < n and s[i + k] == s[j + k]:
                k += 1
            
            if max_k < k:
                max_k = k
                idx = i
            
            k = max(0, k - 1)
        
        return "" if max_k == 0 else s[idx:idx + max_k]