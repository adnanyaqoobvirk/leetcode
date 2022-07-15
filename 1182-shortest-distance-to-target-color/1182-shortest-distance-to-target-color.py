class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        color_indices = [[] for _ in range(3)]
        for i, color in enumerate(colors):
            color_indices[color - 1].append(i)
        
        ans = []
        for i, c in queries:
            indices = color_indices[c - 1]
            if not indices:
                ans.append(-1)
                continue
            
            idx = bisect_left(indices, i)
            ans.append(
                min(
                    abs(indices[min(idx, len(indices) - 1)] - i),
                    abs(indices[max(idx - 1, 0)] - i)
                )
            )
        return ans